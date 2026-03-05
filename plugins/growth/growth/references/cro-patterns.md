# CRO (Conversion Rate Optimization) Patterns

## CTA Best Practices

| Element | Best Practice | Example |
|---------|--------------|---------|
| Copy | Action-oriented verb | "Start free trial" not "Submit" |
| Color | High contrast to background | Primary brand color |
| Size | Large enough to tap (44x44px min) | Full-width on mobile |
| Position | Above the fold, after value prop | Hero section |
| Urgency | Time/scarcity when genuine | "3 spots left" |

## Form Optimization

1. Reduce fields to minimum required
2. Use inline validation (not on submit)
3. Show progress for multi-step forms
4. Auto-focus first field
5. Use appropriate input types (email, tel, etc.)

## Exit Intent Detection

```typescript
document.addEventListener('mouseout', (e) => {
  if (e.clientY < 0) {
    showRetentionOverlay();
  }
});
```

## Social Proof Patterns
- Customer count: "Join 10,000+ teams"
- Logos: Trusted by [Company logos]
- Testimonials: Quote with photo and name
- Rating: "4.8/5 from 500+ reviews"
