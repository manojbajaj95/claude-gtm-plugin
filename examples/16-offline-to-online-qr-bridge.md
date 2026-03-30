# The Offline-to-Online QR Bridge

Turn physical event flyers into tracked digital touchpoints — generate a QR code, optimize the landing page it hits, and wire up UTM tracking so you know exactly how many offline scans become real sign-ups.

## Workflow

### Step 1 — Generate the tracked QR code

```
Generate a dynamic QR code for our upcoming physical event flyers.
Destination: [Event Registration or Landing Page URL]
QR code requirements:
  - Dynamic (URL can be updated after printing)
  - Include a UTM-tagged URL as the destination:
      source: flyer, medium: print, campaign: [event-slug]
  - Export formats needed: PNG (high resolution for print) and SVG
  - Add a short caption below the QR code for the flyer: "Scan to register free"
Return the tagged URL and the QR code files.
```

### Step 2 — Optimize the landing page for mobile

```
Apply landing page optimization principles to the registration page that the QR
code points to.
URL: [Event Registration or Landing Page URL]

The page will be accessed primarily on mobile via a flyer scan. Audit and optimize:
  - Above the fold on mobile (first screen, no scroll):
      - Headline: what the event is and why attend — under 8 words
      - Date, time, and format (in-person / virtual) visible immediately
      - Single CTA button: large tap target, high contrast, action verb
  - Form friction: reduce to name + email only (no phone, company, etc.)
  - Page load speed: flag any elements likely to slow mobile load
  - Trust signal: one social proof element visible before the fold

Return: specific copy rewrites for the headline, CTA button, and form labels,
plus a mobile layout recommendation.
```

### Step 3 — Build the UTM tracking framework

```
Set up a UTM builder framework to track all offline-to-online conversion paths for
this event across all physical and digital placements.

Create tagged URLs for:
  1. Flyer (print): source=flyer, medium=print, campaign=[event-slug]
  2. Poster (venue): source=poster, medium=print, campaign=[event-slug]
  3. Table tent / handout: source=handout, medium=print, campaign=[event-slug]
  4. QR in follow-up SMS (if applicable): source=sms, medium=text, campaign=[event-slug]
  5. QR in post-event thank you email: source=email, medium=email, campaign=[event-slug]

For each URL also provide:
  - The QR code destination (same page, different UTM)
  - Which analytics view or goal in GA4 / your analytics tool to check
  - How to distinguish offline scan conversions from direct or organic traffic

Return as a tracking framework table: placement | UTM URL | analytics goal | notes
```

## Output

- `content/events/drafts/YYYY-MM-DD_qr-tracking-framework-<event-slug>.md` — UTM framework table and QR spec
- `content/landing-pages/drafts/YYYY-MM-DD_mobile-lp-audit-<event-slug>.md` — mobile landing page copy and layout recommendations

