---
name: webconsulting-branding
description: >-
  Enforces webconsulting.at design system, color palettes, typography, and MDX component
  structures for frontend development. Use when working with frontend, design, branding,
  ui, components, styling.
compatibility: TYPO3 13.0 - 14.x
metadata:
  version: "2.0.0"
---

# webconsulting Design System

## 1. Brand Identity & Voice

**Persona**: Innovative, Technical, Professional ("Senior Solutions Architect")

**Tone**: Clear, concise, authoritative. Avoid marketing fluff.

**Language**: German (Primary) / English (Technical documentation)

## 2. Visual Design Tokens (Strict Adherence)

### Brand Color Palette

| Token | Light Mode | Dark Mode | Tailwind Class | Usage |
|-------|------------|-----------|----------------|-------|
| Primary | `#1b7a95` | `#66c4e1` | `text-webcon-primary` | Links, primary buttons, active states |
| Primary Light | `#66c4e1` | `#9dd8eb` | `text-webcon-primary-light` | Hover states, accents |
| Primary 50 | `#e8f4f8` | `#0f3d4a` | `bg-webcon-primary-50` | Light backgrounds |
| Primary 100 | `#c5e4ed` | `#155d73` | `bg-webcon-primary-100` | Subtle backgrounds |
| Primary 200 | `#9dd2e2` | `#1b7a95` | `bg-webcon-primary-200` | Borders, highlights |
| Primary 700 | `#1b7a95` | `#66c4e1` | `text-webcon-primary-700` | Primary text |
| Primary 800 | `#155d73` | `#9dd8eb` | `text-webcon-primary-800` | Strong emphasis |
| Primary 900 | `#0f4555` | `#c5e8f2` | `text-webcon-primary-900` | Maximum contrast |

### Semantic State Colors

| State | Color | Light BG | Border | Tailwind Prefix |
|-------|-------|----------|--------|-----------------|
| Success | `#16a34a` / `#4ade80` | `#dcfce7` / `#14532d` | `#86efac` / `#22c55e` | `webcon-success` |
| Error | `#dc2626` / `#f87171` | `#fee2e2` / `#450a0a` | `#fca5a5` / `#ef4444` | `webcon-error` |
| Warning | `#d97706` / `#fbbf24` | `#fef3c7` / `#451a03` | `#fcd34d` / `#f59e0b` | `webcon-warning` |
| Info | `#1b7a95` / `#66c4e1` | `#e8f4f8` / `#0f3d4a` | `#66c4e1` / `#1b7a95` | `webcon-info` |

### Using Brand Colors

```jsx
// Primary button
<button className="bg-webcon-primary text-white hover:bg-webcon-primary-800">
  Action
</button>

// Info callout
<div className="bg-webcon-info-light border border-webcon-info-border text-webcon-info">
  Information message
</div>

// Success state
<div className="bg-webcon-success-light border border-webcon-success-border">
  <CheckIcon className="text-webcon-success" />
</div>
```

### Typography

| Element | Font Family | Weight | Usage |
|---------|-------------|--------|-------|
| All Text | Hanken Grotesk | 400-700 | Body, headings, UI |
| Display | Hanken Grotesk (wide) | 600, 700 | Hero titles, emphasis |
| Code | System monospace | 400 | Code blocks, inline code |

**Font Configuration** (Next.js):

```typescript
import { Hanken_Grotesk } from 'next/font/google'

const hankenGrotesk = Hanken_Grotesk({
  subsets: ['latin'],
  variable: '--font-hanken-grotesk',
  display: 'swap',
})
```

**CSS Variables**:

```css
--font-sans: var(--font-hanken-grotesk), ui-sans-serif, system-ui, sans-serif;
--font-display: var(--font-hanken-grotesk), ui-sans-serif, system-ui, sans-serif;
--font-display--font-variation-settings: 'wdth' 125;
```

## 3. MDX Component Architecture

When generating content or frontend components, use the following structure. **Do NOT use raw HTML**.

### Interactive Tabs

Use for version comparisons (e.g., TYPO3 v11 vs v12 vs v13 vs v14):

```jsx
<Tabs defaultValue="v14">
  <TabsList>
    <TabsTrigger value="v13">TYPO3 v13</TabsTrigger>
    <TabsTrigger value="v14">TYPO3 v14</TabsTrigger>
  </TabsList>
  <TabsContent value="v13">
    Content for v13...
  </TabsContent>
  <TabsContent value="v14">
    Content for v14 (preferred)...
  </TabsContent>
</Tabs>
```

### Data & Comparison Tables

Use `ComparisonTable` for feature matrices. Supports boolean checkmarks:

```jsx
<ComparisonTable 
  headers={['Feature', 'v13', 'v14']}
  rows={[
    { label: 'Content Blocks', values: [true, true] },
    { label: 'Symfony 7', values: [false, true] },
    { label: 'PHP 8.2+', values: [true, true] }
  ]} 
/>
```

### Code Blocks with Syntax Highlighting

```jsx
<CodeBlock 
  language="php" 
  filename="Classes/Controller/PageController.php"
  highlightLines={[3, 7]}
>
{`<?php
declare(strict_types=1);

namespace Vendor\\Extension\\Controller;

use Psr\\Http\\Message\\ResponseInterface;
use TYPO3\\CMS\\Extbase\\Mvc\\Controller\\ActionController;

final class PageController extends ActionController
{
    public function indexAction(): ResponseInterface
    {
        return $this->htmlResponse();
    }
}`}
</CodeBlock>
```

### Callout Boxes

```jsx
<Callout type="info" title="Best Practice">
  Always use `declare(strict_types=1);` in PHP files.
</Callout>

<Callout type="warning" title="Breaking Change">
  This API changed in TYPO3 v14.
</Callout>

<Callout type="danger" title="Security">
  Never expose sensitive configuration files.
</Callout>
```

### MDX Images

```jsx
<MDXImage 
  src="/images/architecture-diagram.png" 
  alt="TYPO3 Extension Architecture"
  caption="Figure 1: Domain-Driven Design in TYPO3 Extensions"
/>
```

## 4. Mermaid Diagrams (Theming)

All diagrams must explicitly override the theme to match the webconsulting palette:

```markdown
%%{init: {'theme': 'base', 'themeVariables': { 
  'primaryColor': '#1b7a95', 
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#155d73',
  'lineColor': '#404040',
  'secondaryColor': '#d97706',
  'tertiaryColor': '#fef3c7',
  'edgeLabelBackground': '#ffffff'
}}}%%
graph TD
    A[Client Request] -->|HTTP| B(Load Balancer)
    B --> C{TYPO3 Backend}
    C -->|Cache Hit| D[Response]
    C -->|Cache Miss| E[Database]
    E --> D
```

**CSS enhancements** (automatically applied via base.css):
- Nodes have 10px border-radius for modern look
- 2px stroke width for better definition
- White text with shadow on mindmap nodes
- Cluster/subgraph backgrounds use light gray (`#f0f0f0`)

## 5. Accessibility Guidelines (WCAG 2.1 AA)

### Contrast Requirements

- Ensure **4.5:1** contrast ratio for all text
- Large text (18px+ bold, 24px+ regular): **3:1** minimum

### Interactive Elements

- All interactive elements must have visible **focus states**
- Use ring: `focus:ring-2 focus:ring-webcon-primary focus:ring-offset-2`
- Outline for scrollable regions: `outline: 2px solid #1B7A95`

### Images and Media

- All images MUST include `alt` text
- Use `caption` prop in MDXImage component
- Decorative images: use `alt=""`

### Keyboard Navigation

- All interactive elements must be keyboard accessible
- Logical tab order (no positive tabindex)
- Skip links for main content (styled with dark background, white text)

## 6. Responsive Breakpoints

| Breakpoint | Width | Tailwind Prefix |
|------------|-------|-----------------|
| Mobile | < 640px | (default) |
| Tablet | ≥ 640px | `sm:` |
| Desktop | ≥ 1024px | `lg:` |
| Wide | ≥ 1280px | `xl:` |

## 7. Component Spacing Scale

Use consistent spacing based on 4px grid:

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | 4px | Icon gaps |
| `space-2` | 8px | Inline elements |
| `space-4` | 16px | Component padding |
| `space-6` | 24px | Section gaps |
| `space-8` | 32px | Major sections |
| `space-12` | 48px | Page sections |

## 8. Button Styles

### Primary Button

```html
<button class="bg-webcon-primary hover:bg-webcon-primary-800 text-white font-medium px-6 py-3 rounded-lg transition-colors focus:ring-2 focus:ring-webcon-primary focus:ring-offset-2">
  Primary Action
</button>
```

### Secondary Button

```html
<button class="border-2 border-webcon-primary text-webcon-primary hover:bg-webcon-primary-50 font-medium px-6 py-3 rounded-lg transition-colors">
  Secondary Action
</button>
```

### Ghost Button

```html
<button class="text-muted-foreground hover:text-webcon-primary hover:bg-muted px-4 py-2 rounded transition-colors">
  Ghost Action
</button>
```

## 9. Dark Mode Support

The design system supports automatic dark mode via the `.dark` class. All `webcon-*` colors automatically invert:

| Token | Light | Dark |
|-------|-------|------|
| `--webcon-primary` | `#1b7a95` | `#66c4e1` |
| `--webcon-success` | `#16a34a` | `#4ade80` |
| `--webcon-error` | `#dc2626` | `#f87171` |
| `--webcon-warning` | `#d97706` | `#fbbf24` |

**Usage**: Apply `dark` class to a parent element (usually `<html>`) to enable dark mode.

## 10. shadcn/ui Integration

The design system is compatible with shadcn/ui components. Semantic tokens map to shadcn conventions:

| shadcn Token | webconsulting Equivalent |
|--------------|--------------------------|
| `--background` | Light: white, Dark: neutral-950 |
| `--foreground` | Light: neutral-950, Dark: white |
| `--primary` | `--webcon-primary` |
| `--destructive` | `--webcon-error` |
| `--muted` | Neutral grays |
| `--accent` | Light backgrounds |
| `--ring` | Focus ring color |

