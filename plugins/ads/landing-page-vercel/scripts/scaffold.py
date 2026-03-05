#!/usr/bin/env python3
"""
Landing Page Vercel - Static landing page scaffold with Formspree integration.

Generates a production-ready landing page with:
- Dark theme responsive design
- Email capture form (Formspree)
- Features and FAQ sections
- Vercel deployment config
- Accessibility features (skip link, ARIA, reduced motion)

Usage:
    python3 scaffold.py --out ./my-landing --name "ProductName" --tagline "Value prop here"
    python3 scaffold.py --out ./my-landing --formspree "your-form-id"
"""
import argparse
import json
import os
import textwrap
from typing import List, Optional


def create_default_data(
    name: str = "Your Product",
    tagline: str = "A clear, short value proposition that explains what you do.",
    features: Optional[List[str]] = None,
    formspree_id: Optional[str] = None,
) -> dict:
    """Create default data.json content with optional customization."""
    default_features = [
        {"title": "Fast setup", "body": "Go from zero to live in minutes."},
        {"title": "Simple pricing", "body": "Transparent plans with no surprises."},
        {"title": "Real results", "body": "Focused features that drive outcomes."},
    ]

    # Parse features from CLI if provided (format: "Title:Description,Title2:Desc2")
    if features:
        parsed_features = []
        for f in features:
            if ":" in f:
                title, body = f.split(":", 1)
                parsed_features.append({"title": title.strip(), "body": body.strip()})
            else:
                parsed_features.append({"title": f.strip(), "body": ""})
        default_features = parsed_features if parsed_features else default_features

    return {
        "title": name,
        "tagline": tagline,
        "cta": {"label": "Get Started", "href": "#signup"},
        "features": default_features,
        "faq": [
            {"q": "Who is this for?", "a": f"Anyone who wants to use {name}."},
            {"q": "How do I get started?", "a": "Sign up for the waitlist and we'll reach out."},
            {"q": "Is there a free trial?", "a": "Yes, we offer a free trial period."},
        ],
        "formspree": formspree_id or "",
    }

INDEX_HTML = """\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" id="meta-description" content="A product landing page" />
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <main id="main-content" class="page">
      <section class="hero" aria-labelledby="title">
        <div class="hero-copy">
          <p class="eyebrow">Launch fast</p>
          <h1 id="title"></h1>
          <p id="tagline" class="tagline"></p>
          <div class="cta-row">
            <a id="cta" class="cta" href="#signup"></a>
            <a class="cta secondary" href="#features-section">See features</a>
          </div>
          <p class="note">No credit card required. Ship in a day.</p>
        </div>
        <div class="hero-card">
          <p class="hero-label">Starter kit</p>
          <ul class="hero-list" role="list">
            <li>Static bundle, no backend</li>
            <li>Editable content in data.json</li>
            <li>Vercel config included</li>
          </ul>
        </div>
      </section>

      <section id="features-section" class="features" aria-labelledby="features-title">
        <h2 id="features-title" class="section-title">Features</h2>
        <div id="features" class="grid" role="list"></div>
      </section>

      <section class="faq" aria-labelledby="faq-title">
        <h2 id="faq-title" class="section-title">FAQ</h2>
        <div id="faq" class="stack"></div>
      </section>

      <section id="signup" class="signup" aria-labelledby="signup-title">
        <h2 id="signup-title" class="section-title">Get started</h2>
        <p id="signup-description">Join the waitlist to get early access.</p>
        <form id="signup-form" class="signup-form" action="" method="POST">
          <div class="form-group">
            <label for="email" class="sr-only">Email address</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="you@example.com"
              required
              autocomplete="email"
              aria-describedby="signup-description"
            />
            <button type="submit" class="cta">Join Waitlist</button>
          </div>
          <p id="form-status" class="form-status" role="status" aria-live="polite"></p>
        </form>
      </section>
    </main>

    <footer class="footer">
      <p>&copy; <span id="year"></span> <span id="footer-name"></span>. All rights reserved.</p>
    </footer>

    <script src="script.js" defer></script>
  </body>
</html>
"""

STYLES = """\
:root {
  --bg: #0f0f10;
  --ink: #f5f5f7;
  --accent: #10b981;
  --accent-2: #f59e0b;
  --muted: #9ca3af;
  --card: #18181b;
  --stroke: #27272a;
  --shadow: rgba(0, 0, 0, 0.4);
  --error: #ef4444;
  --success: #22c55e;
  --font-display: "SF Pro Display", "Inter", "Segoe UI", sans-serif;
  --font-body: "SF Pro Text", "Inter", "Segoe UI", sans-serif;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: var(--font-body);
  background:
    radial-gradient(900px 500px at 12% -10%, rgba(16, 185, 129, 0.12), transparent 60%),
    radial-gradient(700px 480px at 88% 5%, rgba(245, 158, 11, 0.08), transparent 65%),
    linear-gradient(180deg, #0f0f10 0%, #18181b 100%);
  color: var(--ink);
  min-height: 100vh;
}

/* Skip link for accessibility */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--accent);
  color: #000;
  padding: 8px 16px;
  z-index: 100;
  text-decoration: none;
  font-weight: 600;
}
.skip-link:focus {
  top: 0;
}

/* Screen reader only */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

a { color: inherit; }

.page {
  max-width: 1040px;
  margin: 0 auto;
  padding: 72px 24px 96px;
}

.page > section {
  opacity: 0;
  transform: translateY(12px);
  animation: fadeUp 0.7s ease forwards;
}
.page > section:nth-of-type(1) { animation-delay: 0.05s; }
.page > section:nth-of-type(2) { animation-delay: 0.15s; }
.page > section:nth-of-type(3) { animation-delay: 0.25s; }
.page > section:nth-of-type(4) { animation-delay: 0.35s; }

.hero {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  gap: 28px;
  padding: 36px;
  background: var(--card);
  border-radius: 22px;
  border: 1px solid var(--stroke);
  box-shadow: 0 18px 40px var(--shadow);
  overflow: hidden;
}

.hero::before {
  content: "";
  position: absolute;
  top: -120px;
  right: -120px;
  width: 280px;
  height: 280px;
  background: radial-gradient(circle, rgba(15, 94, 75, 0.18), transparent 70%);
  pointer-events: none;
}

.hero-copy h1 {
  font-family: var(--font-display);
  font-size: clamp(2.4rem, 4vw, 3.6rem);
  margin: 0 0 12px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 12px;
  color: var(--muted);
  margin: 0 0 16px;
}

.tagline {
  font-size: 18px;
  color: var(--muted);
  max-width: 520px;
  margin: 0 0 16px;
}

.cta-row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 20px;
  background: var(--accent);
  color: #fff;
  text-decoration: none;
  border-radius: 999px;
  font-weight: 600;
  font-family: var(--font-display);
  border: none;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 10px 24px rgba(15, 94, 75, 0.25);
}

.cta:hover {
  transform: translateY(-1px);
}

.cta.secondary {
  background: transparent;
  color: var(--accent);
  border: 1px solid var(--accent);
  box-shadow: none;
}

.note {
  margin: 16px 0 0;
  color: var(--muted);
  font-size: 14px;
}

.hero-card {
  background: var(--card);
  border-radius: 16px;
  padding: 24px;
  border: 1px solid var(--stroke);
  box-shadow: 0 12px 24px var(--shadow);
}

.hero-label {
  font-family: var(--font-display);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 12px;
  color: var(--muted);
  margin: 0 0 12px;
}

.hero-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 10px;
}

.hero-list li {
  position: relative;
  padding-left: 18px;
}

.hero-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: var(--accent-2);
}

.section-title {
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 2.6vw, 2.1rem);
  margin: 0 0 16px;
}

.features,
.faq,
.signup {
  margin-top: 56px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.card {
  background: var(--card);
  padding: 20px;
  border-radius: 14px;
  border: 1px solid var(--stroke);
  box-shadow: 0 10px 24px var(--shadow);
}

.card h3 {
  font-family: var(--font-display);
  margin-top: 0;
}

.stack {
  display: grid;
  gap: 12px;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .page > section {
    animation: none;
    opacity: 1;
    transform: none;
  }
  .cta { transition: none; }
}

@media (max-width: 840px) {
  .hero {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .page { padding: 48px 18px 72px; }
  .hero { padding: 28px; }
  .signup-form .form-group { flex-direction: column; }
  .signup-form input { width: 100%; }
}

/* Signup form */
.signup-form {
  max-width: 480px;
}

.signup-form .form-group {
  display: flex;
  gap: 12px;
  margin-top: 16px;
}

.signup-form input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid var(--stroke);
  border-radius: 999px;
  background: var(--card);
  color: var(--ink);
  font-size: 16px;
  font-family: var(--font-body);
}

.signup-form input::placeholder {
  color: var(--muted);
}

.signup-form input:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
}

.form-status {
  margin-top: 12px;
  font-size: 14px;
}

.form-status.success {
  color: var(--success);
}

.form-status.error {
  color: var(--error);
}

/* Footer */
.footer {
  text-align: center;
  padding: 32px 24px;
  color: var(--muted);
  font-size: 14px;
  border-top: 1px solid var(--stroke);
  margin-top: 64px;
}
"""

SCRIPT = """\
async function loadData() {
  const res = await fetch("./data.json");
  if (!res.ok) return null;
  return await res.json();
}

function renderFeatures(features) {
  const container = document.getElementById("features");
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
  features.forEach((item) => {
    const card = document.createElement("div");
    card.className = "card";
    const title = document.createElement("h3");
    title.textContent = item.title;
    const body = document.createElement("p");
    body.textContent = item.body;
    card.appendChild(title);
    card.appendChild(body);
    container.appendChild(card);
  });
}

function renderFaq(items) {
  const container = document.getElementById("faq");
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
  items.forEach((item) => {
    const card = document.createElement("div");
    card.className = "card";
    const question = document.createElement("strong");
    question.textContent = item.q;
    const answer = document.createElement("p");
    answer.textContent = item.a;
    card.appendChild(question);
    card.appendChild(answer);
    container.appendChild(card);
  });
}

function setupForm(formspreeId) {
  const form = document.getElementById("signup-form");
  const status = document.getElementById("form-status");

  if (formspreeId) {
    form.action = "https://formspree.io/f/" + formspreeId;
  }

  form.addEventListener("submit", async (e) => {
    if (!formspreeId) {
      e.preventDefault();
      status.textContent = "Form not configured. Add formspree ID to data.json";
      status.className = "form-status error";
      return;
    }

    e.preventDefault();
    const formData = new FormData(form);

    try {
      const response = await fetch(form.action, {
        method: "POST",
        body: formData,
        headers: { Accept: "application/json" }
      });

      if (response.ok) {
        status.textContent = "Thanks! We will be in touch soon.";
        status.className = "form-status success";
        form.reset();
      } else {
        throw new Error("Form submission failed");
      }
    } catch (error) {
      status.textContent = "Oops! Something went wrong. Please try again.";
      status.className = "form-status error";
    }
  });
}

async function init() {
  const data = await loadData();
  if (!data) return;

  document.title = data.title;
  const metaDesc = document.getElementById("meta-description");
  if (metaDesc) metaDesc.content = data.tagline;

  document.getElementById("title").textContent = data.title;
  document.getElementById("tagline").textContent = data.tagline;

  const cta = document.getElementById("cta");
  cta.textContent = data.cta.label;
  cta.href = data.cta.href;

  renderFeatures(data.features || []);
  renderFaq(data.faq || []);

  // Setup form with Formspree
  setupForm(data.formspree || "");

  // Footer
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
  const footerName = document.getElementById("footer-name");
  if (footerName) footerName.textContent = data.title;
}

init();
"""

VERCEL = """\
{
  "cleanUrls": true,
  "trailingSlash": false
}
"""


def write_file(path, content, force):
    if os.path.exists(path) and not force:
        print(f"skip: {path}")
        return
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)
        if not content.endswith("\n"):
            handle.write("\n")


README_TEMPLATE = """\
# {name}

{tagline}

## Development

Open `index.html` in your browser or use a local server:

```bash
npx serve .
```

## Deployment

This project is configured for Vercel deployment:

1. Push to GitHub
2. Import in Vercel
3. Deploy

Or deploy directly:

```bash
npx vercel
```

## Configuration

Edit `data.json` to customize:

- **title**: Product name
- **tagline**: Value proposition
- **features**: Feature cards
- **faq**: FAQ items
- **formspree**: Your Formspree form ID (get one at https://formspree.io)

## Email Capture

To enable email capture:

1. Create a free form at [Formspree](https://formspree.io)
2. Copy your form ID (e.g., `xyzabcde`)
3. Add it to `data.json`: `"formspree": "xyzabcde"`

## Files

- `index.html` - Main page
- `styles.css` - Dark theme styles
- `script.js` - Dynamic content loading
- `data.json` - Editable content
- `vercel.json` - Deployment config
"""


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a static landing page with dark theme and email capture."
    )
    parser.add_argument("--out", default=".", help="Output directory")
    parser.add_argument("--name", default="Your Product", help="Product name")
    parser.add_argument("--tagline", default=None, help="Value proposition tagline")
    parser.add_argument(
        "--features",
        nargs="*",
        help="Features in 'Title:Description' format (can specify multiple)",
    )
    parser.add_argument("--formspree", default=None, help="Formspree form ID for email capture")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    # Generate data.json with CLI arguments
    tagline = args.tagline or f"A clear, short value proposition for {args.name}."
    data = create_default_data(
        name=args.name,
        tagline=tagline,
        features=args.features,
        formspree_id=args.formspree,
    )

    # Generate README
    readme = README_TEMPLATE.format(name=args.name, tagline=tagline)

    write_file(os.path.join(args.out, "data.json"), json.dumps(data, indent=2), args.force)
    write_file(os.path.join(args.out, "index.html"), textwrap.dedent(INDEX_HTML), args.force)
    write_file(os.path.join(args.out, "styles.css"), textwrap.dedent(STYLES), args.force)
    write_file(os.path.join(args.out, "script.js"), textwrap.dedent(SCRIPT), args.force)
    write_file(os.path.join(args.out, "vercel.json"), textwrap.dedent(VERCEL), args.force)
    write_file(os.path.join(args.out, "README.md"), readme, args.force)

    print(f"Landing page created in {args.out}/")
    print(f"  - Product: {args.name}")
    print(f"  - Formspree: {'configured' if args.formspree else 'not configured'}")
    print("\nNext steps:")
    print("  1. Edit data.json to customize content")
    if not args.formspree:
        print("  2. Add formspree ID to enable email capture")
    print("  3. Deploy with: npx vercel")


if __name__ == "__main__":
    main()
