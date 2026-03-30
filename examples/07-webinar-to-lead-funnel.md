# The Webinar-to-Lead Funnel

Convert your most recent webinar into a lead-generating asset — a downloadable cheat sheet with a tracked landing page that shows exactly which channel drives the most downloads.

## Workflow

### Step 1 — Extract the top audience questions

```
Review the recording or transcript of our most recent webinar.
Identify the top 3 questions asked by the audience (highest engagement or most upvoted).
For each question return:
  - The question as asked
  - A thorough answer (3–5 sentences) that could stand alone without the webinar context
```

### Step 2 — Create the cheat sheet

```
Using the 3 questions and answers from Step 1, write a 1-page "Cheat Sheet" PDF outline.
Structure:
  - Title: "[Webinar Topic]: 3 Questions Answered"
  - Brief intro (2 sentences max)
  - Q&A section: each question as a bold header, answer below
  - Footer: our website URL and logo placeholder
The content should read as self-contained value, not a webinar recap.
```

### Step 3 — Build tracked links

```
Generate UTM-tagged URLs for the cheat sheet landing page.
Base URL: [Cheat Sheet Landing Page URL]
Create 3 tagged links:
  1. Source: webinar-followup-email, medium: email, campaign: webinar-cheatsheet
  2. Source: linkedin, medium: social, campaign: webinar-cheatsheet
  3. Source: twitter, medium: social, campaign: webinar-cheatsheet
```

### Step 4 — Write the landing page

```
Write a lead generation landing page for the cheat sheet.
Page structure:
  - Headline: benefit-driven, references the webinar topic
  - 3-bullet value prop (what they'll learn from the cheat sheet)
  - Email capture form (first name + email only)
  - Privacy reassurance line
Include a note on where to embed each UTM link from Step 3 (email vs social).
```

## Output

- `content/assets/drafts/YYYY-MM-DD_cheatsheet-<webinar-slug>.md` — cheat sheet copy
- `content/landing-pages/drafts/YYYY-MM-DD_lp-<webinar-slug>.md` — landing page copy with UTM placement notes

