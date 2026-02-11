# OGP & Social Sharing Templates

## Open Graph (Facebook/LinkedIn)

```html
<meta property="og:title" content="Page Title" />
<meta property="og:description" content="Description" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta property="og:url" content="https://example.com/page" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Site Name" />
```

Image requirements: 1200x630px, < 8MB

## Twitter Cards

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Page Title" />
<meta name="twitter:description" content="Description" />
<meta name="twitter:image" content="https://example.com/image.jpg" />
```

## Next.js Metadata API

```typescript
export const metadata: Metadata = {
  title: 'Page Title',
  description: 'Description',
  openGraph: {
    title: 'Page Title',
    description: 'Description',
    images: [{ url: '/og-image.jpg', width: 1200, height: 630 }],
  },
  twitter: { card: 'summary_large_image' },
};
```
