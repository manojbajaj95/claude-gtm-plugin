# Close CRM Deep Dive

Your daily driver — power features, query language, and automation patterns.

## Close Query Language

Close uses a powerful query language for searching and filtering. Master this for Smart Views.

### Basic Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `:` | `company:Coperniq` | Contains |
| `=` | `status="Potential"` | Exact match |
| `>` `<` `>=` `<=` | `opportunities.value>10000` | Numeric comparison |
| `is:` | `is:contacted` | Boolean states |
| `has:` | `has:email` | Field exists |
| `not:` | `not:contacted` | Negation |

### Field References

```
# Lead fields
lead_id, display_name, status_label, created_by
date_created, date_updated, description

# Contact fields
contact.name, contact.email, contact.phone, contact.title

# Opportunity fields
opportunities.status_label, opportunities.value
opportunities.confidence, opportunities.date_won

# Activity fields
activities.date_created, activities.note
calls.duration, emails.status

# Custom fields
custom.cf_xxxxxx
```

### Power Queries

```python
# Leads with no activity in 30 days
'sort:date_updated asc date_updated < "30 days ago"'

# High-value opportunities in pipeline
'opportunities.value >= 50000 opportunities.status_type:active'

# Leads with email but no calls
'has:email not:call'

# Specific custom field value
'custom.cf_industry = "MEP Contractor"'

# Multiple trade types (your ICP)
'custom.cf_trades:HVAC OR custom.cf_trades:Electrical OR custom.cf_trades:Plumbing'

# Leads created this month with opportunities
'created >= "first day of this month" has:opportunity'

# Stalled deals (no activity in 14 days, still active)
'opportunities.status_type:active sort:activities.date desc activities.date < "14 days ago"'
```

---

## Smart Views (Saved Searches)

### Sales Process Views

```yaml
# New This Week
query: 'created >= "7 days ago" sort:date_created desc'

# My Active Pipeline
query: 'opportunities.status_type:active opportunities.user_id:me sort:opportunities.value desc'

# Needs Follow-Up (No activity 7+ days)
query: 'opportunities.status_type:active activities.date < "7 days ago" sort:activities.date asc'

# Closing This Month
query: 'opportunities.expected_close_date >= "first day of this month" opportunities.expected_close_date <= "last day of this month"'

# Lost Recently (Win-back candidates)
query: 'opportunities.status_type:lost opportunities.date_lost >= "30 days ago" sort:opportunities.date_lost desc'
```

### Lead Quality Views

```yaml
# Gold Tier (Multi-trade, has website)
query: 'custom.cf_tier = "Gold" sort:date_created desc'

# Missing Info (No email or phone)
query: 'not:email not:phone sort:date_created desc'

# Recently Enriched
query: 'custom.cf_enriched_date >= "7 days ago" sort:custom.cf_enriched_date desc'
```

---

## API Power Features

### Bulk Lead Update

```python
async def bulk_update_leads(
    client: CloseClient,
    query: str,
    updates: dict,
    dry_run: bool = True
) -> dict:
    """Bulk update leads matching a query."""
    
    # Search for matching leads
    results = client.search_leads(query, limit=1000)
    
    if dry_run:
        return {"would_update": len(results), "leads": [r["id"] for r in results]}
    
    updated = []
    failed = []
    
    for lead in results:
        try:
            client._request("PUT", f"/lead/{lead['id']}/", json=updates)
            updated.append(lead["id"])
        except Exception as e:
            failed.append({"id": lead["id"], "error": str(e)})
        
        await asyncio.sleep(0.1)  # Rate limiting
    
    return {"updated": len(updated), "failed": failed}

# Usage: Update all leads from a specific source
await bulk_update_leads(
    client,
    query='custom.cf_source = "dealer-scraper"',
    updates={"custom.cf_tier": "Bronze"},
    dry_run=False
)
```

### Activity Timeline Builder

```python
def get_lead_timeline(client: CloseClient, lead_id: str) -> list:
    """Get complete activity timeline for a lead."""
    
    activities = []
    
    # Get all activity types
    for activity_type in ["note", "call", "email", "sms", "meeting"]:
        endpoint = f"/activity/{activity_type}/"
        params = {"lead_id": lead_id, "_limit": 100}
        
        result = client._request("GET", endpoint, params=params)
        for item in result["data"]:
            activities.append({
                "type": activity_type,
                "date": item.get("date_created"),
                "user": item.get("user_name"),
                "content": item.get("note") or item.get("subject") or item.get("body_text"),
                "direction": item.get("direction"),
                "duration": item.get("duration"),
            })
    
    # Sort by date
    activities.sort(key=lambda x: x["date"], reverse=True)
    return activities
```

### Opportunity Pipeline Stats

```python
def get_pipeline_stats(client: CloseClient) -> dict:
    """Get current pipeline statistics."""
    
    # Get all opportunity statuses
    statuses = client._request("GET", "/status/opportunity/")["data"]
    
    stats = {}
    total_value = 0
    weighted_value = 0
    
    for status in statuses:
        if status["type"] == "active":
            # Query opportunities in this status
            opps = client._request(
                "GET", "/opportunity/",
                params={"status_id": status["id"], "_limit": 1000}
            )["data"]
            
            count = len(opps)
            value = sum(o.get("value", 0) or 0 for o in opps)
            
            # Weighted by confidence
            weighted = sum(
                (o.get("value", 0) or 0) * (o.get("confidence", 50) / 100)
                for o in opps
            )
            
            stats[status["label"]] = {
                "count": count,
                "value": value,
                "weighted": weighted,
                "avg_value": value / count if count else 0
            }
            
            total_value += value
            weighted_value += weighted
    
    stats["_totals"] = {
        "total_value": total_value,
        "weighted_value": weighted_value
    }
    
    return stats
```

---

## Sequences & Workflows

### Email Sequence via API

```python
def enroll_in_sequence(
    client: CloseClient,
    lead_id: str,
    sequence_id: str,
    contact_id: str
) -> dict:
    """Enroll a contact in an email sequence."""
    
    return client._request(
        "POST", "/sequence_subscription/",
        json={
            "sequence_id": sequence_id,
            "lead_id": lead_id,
            "contact_id": contact_id,
            "sender_account_id": "emailacct_xxx",  # Your sending account
            "sender_email": "tim@coperniq.ai",
            "sender_name": "Tim Kipper"
        }
    )

def pause_sequence(client: CloseClient, subscription_id: str) -> dict:
    """Pause a sequence subscription."""
    return client._request(
        "PUT", f"/sequence_subscription/{subscription_id}/",
        json={"status": "paused"}
    )
```

### Workflow Triggers (Webhooks)

```python
# Create webhook subscription
def create_webhook(client: CloseClient, url: str, events: list) -> dict:
    """Subscribe to Close webhooks."""
    return client._request(
        "POST", "/webhook/",
        json={
            "url": url,
            "events": events
        }
    )

# Common events to subscribe to:
WEBHOOK_EVENTS = [
    "lead.created",
    "lead.updated",
    "lead.deleted",
    "lead.status_changed",
    "contact.created",
    "contact.updated",
    "opportunity.created",
    "opportunity.updated",
    "opportunity.status_changed",
    "activity.note.created",
    "activity.call.created",
    "activity.email.created",
]
```

---

## Reporting Queries

### Daily Sales Report

```python
def daily_sales_report(client: CloseClient, date: str = None) -> dict:
    """Generate daily sales activity report."""
    
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    report = {
        "date": date,
        "calls": 0,
        "call_duration_minutes": 0,
        "emails_sent": 0,
        "leads_created": 0,
        "opportunities_created": 0,
        "opportunities_won": 0,
        "revenue_won": 0,
    }
    
    # Calls today
    calls = client._request(
        "GET", "/activity/call/",
        params={"date_created__gte": f"{date}T00:00:00", "_limit": 1000}
    )["data"]
    report["calls"] = len(calls)
    report["call_duration_minutes"] = sum(c.get("duration", 0) for c in calls) / 60
    
    # Emails sent today
    emails = client._request(
        "GET", "/activity/email/",
        params={"date_created__gte": f"{date}T00:00:00", "direction": "outgoing", "_limit": 1000}
    )["data"]
    report["emails_sent"] = len(emails)
    
    # Leads created today
    leads = client.search_leads(f'created >= "{date}"', limit=1000)
    report["leads_created"] = len(leads)
    
    # Opportunities won today
    won_opps = client._request(
        "GET", "/opportunity/",
        params={"date_won__gte": f"{date}T00:00:00", "status_type": "won", "_limit": 1000}
    )["data"]
    report["opportunities_won"] = len(won_opps)
    report["revenue_won"] = sum(o.get("value", 0) or 0 for o in won_opps)
    
    return report
```

### Pipeline Velocity

```python
def calculate_velocity(client: CloseClient, days: int = 90) -> dict:
    """Calculate pipeline velocity over a period."""
    
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    
    # Get won opportunities in period
    won = client._request(
        "GET", "/opportunity/",
        params={"date_won__gte": cutoff, "status_type": "won", "_limit": 1000}
    )["data"]
    
    # Get lost opportunities in period
    lost = client._request(
        "GET", "/opportunity/",
        params={"date_lost__gte": cutoff, "status_type": "lost", "_limit": 1000}
    )["data"]
    
    total_closed = len(won) + len(lost)
    win_rate = len(won) / total_closed if total_closed else 0
    avg_deal_size = sum(o.get("value", 0) or 0 for o in won) / len(won) if won else 0
    
    # Calculate average cycle time
    cycle_times = []
    for opp in won:
        created = datetime.fromisoformat(opp["date_created"].replace("Z", "+00:00"))
        won_date = datetime.fromisoformat(opp["date_won"].replace("Z", "+00:00"))
        cycle_times.append((won_date - created).days)
    
    avg_cycle = sum(cycle_times) / len(cycle_times) if cycle_times else 0
    
    # Get current pipeline
    active = client._request(
        "GET", "/opportunity/",
        params={"status_type": "active", "_limit": 1000}
    )["data"]
    pipeline_count = len(active)
    
    # Velocity = (# Opps × Win Rate × Avg Deal) / Cycle Days
    velocity = (pipeline_count * win_rate * avg_deal_size) / avg_cycle if avg_cycle else 0
    
    return {
        "period_days": days,
        "win_rate": round(win_rate * 100, 1),
        "avg_deal_size": round(avg_deal_size, 2),
        "avg_cycle_days": round(avg_cycle, 1),
        "pipeline_count": pipeline_count,
        "monthly_velocity": round(velocity * 30, 2),  # Monthly projection
    }
```

---

## Integration with sales-agent

```python
# After enrichment, push to Close
async def push_enriched_lead_to_close(
    close_client: CloseClient,
    enriched_data: dict
) -> str:
    """Push an enriched lead from sales-agent to Close."""
    
    lead_data = {
        "name": enriched_data["company_name"],
        "url": enriched_data.get("website"),
        "custom.cf_tier": enriched_data["tier"],
        "custom.cf_source": "sales-agent",
        "custom.cf_enriched_date": datetime.now().isoformat(),
        "custom.cf_trades": enriched_data.get("trades", []),
        "custom.cf_employee_count": enriched_data.get("employee_count"),
        "custom.cf_annual_revenue": enriched_data.get("revenue_estimate"),
    }
    
    # Add contacts
    contacts = []
    for contact in enriched_data.get("contacts", []):
        contacts.append({
            "name": contact["name"],
            "title": contact.get("title"),
            "emails": [{"email": contact["email"], "type": "office"}] if contact.get("email") else [],
            "phones": [{"phone": contact["phone"], "type": "office"}] if contact.get("phone") else [],
        })
    
    if contacts:
        lead_data["contacts"] = contacts
    
    result = close_client.create_lead(lead_data)
    return result["id"]
```

---

## Custom Field Setup for Coperniq

Recommended custom fields for your MEP contractor ICP:

```python
COPERNIQ_CUSTOM_FIELDS = [
    {"name": "Tier", "type": "choices", "choices": ["Gold", "Silver", "Bronze"]},
    {"name": "Trades", "type": "choices", "choices": ["HVAC", "Electrical", "Plumbing", "Fire Protection", "Solar"]},
    {"name": "Employee Count", "type": "number"},
    {"name": "Annual Revenue", "type": "number"},
    {"name": "Tech Stack", "type": "text"},
    {"name": "Source", "type": "choices", "choices": ["dealer-scraper", "sales-agent", "inbound", "referral", "trade-show"]},
    {"name": "Enriched Date", "type": "date"},
    {"name": "ICP Score", "type": "number"},  # 0-100 from sales-agent
    {"name": "Current PM Software", "type": "text"},
    {"name": "Pain Points", "type": "text"},
]
```
