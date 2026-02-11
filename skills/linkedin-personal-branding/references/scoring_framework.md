# LinkedIn Profile Scoring Framework

## Table of Contents
1. [Visual Identity Scoring](#visual-identity-scoring)
2. [Headline Scoring](#headline-scoring)
3. [About Section Scoring](#about-section-scoring)
4. [Experience Scoring](#experience-scoring)
5. [Skills & Endorsements Scoring](#skills--endorsements-scoring)
6. [Recommendations Scoring](#recommendations-scoring)
7. [Activity & Content Scoring](#activity--content-scoring)
8. [Overall Score Calculation](#overall-score-calculation)

---

## Visual Identity Scoring (15% of total)

### Profile Photo (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Professional headshot, excellent lighting, face fills 60-70% of frame, warm expression, clean background, industry-appropriate attire |
| 7-8 | Good quality photo, professional appearance, decent lighting, appropriate background |
| 5-6 | Acceptable photo, some issues with lighting/background/cropping, face visible |
| 3-4 | Low quality, unprofessional, distracting background, or poorly cropped |
| 1-2 | Very low quality, inappropriate, or barely visible |
| 0 | No photo or default avatar |

**Photo Scoring Checklist (start at 10, subtract for issues):**
- [ ] Face not clearly visible (-3)
- [ ] Sunglasses/hat obscuring face (-2)
- [ ] Cropped from group photo (-2)
- [ ] Distracting or cluttered background (-1)
- [ ] Photo appears outdated (>5 years) (-1)
- [ ] Poor lighting (too dark/bright/harsh shadows) (-1)
- [ ] Low resolution/blurry (-1)
- [ ] Unprofessional attire for industry (-1)
- [ ] Not smiling/unapproachable expression (-0.5)
- [ ] Face doesn't fill 60-70% of frame (-0.5)

**Bonus Points:**
- [ ] Verified badge visible (+0.5)
- [ ] Premium quality/studio lighting (+0.5)
- [ ] Perfect industry alignment (+0.5)

**Red Flags (automatic deductions):**
- Sunglasses or face partially hidden
- Group photo or cropped image
- Outdated photo (5+ years old)
- Unprofessional attire or setting
- Low resolution or blurry
- Logo or avatar instead of face

### Banner Image (0-10)

| Score | Criteria |
|-------|----------|
| 9-10 | Custom branded banner, clear value proposition, professional design, relevant to industry, includes tagline or key message |
| 7-8 | Custom banner, industry-relevant, professional appearance |
| 5-6 | Basic custom banner or relevant stock image |
| 3-4 | Low-quality banner or unrelated imagery |
| 1-2 | Distracting or unprofessional banner |
| 0 | Default LinkedIn banner |

---

## Headline Scoring (15% of total)

| Score | Criteria |
|-------|----------|
| 9-10 | Clear value proposition, includes target audience, specific results/benefits, relevant keywords, memorable, uses full 220 characters effectively |
| 7-8 | Good value proposition, includes role and expertise, some keywords |
| 5-6 | Describes role clearly, missing value proposition or target audience |
| 3-4 | Just job title and company, no differentiation |
| 1-2 | Vague or unclear, no useful information |
| 0 | Empty or default text |

**Headline Formula Check:**
- [ ] States who they are/what they do
- [ ] Identifies who they help (target audience)
- [ ] Explains value/benefit they provide
- [ ] Contains relevant keywords
- [ ] Differentiates from competitors

**Example Scoring by Industry:**

| Industry | Low Score (2-3) | Medium Score (5-6) | High Score (8-9) |
|----------|-----------------|--------------------|--------------------|
| **Tech** | "Software Engineer" | "Software Engineer at Google" | "Senior Software Engineer | Building ML Systems That Scale | Python, TensorFlow, AWS" |
| **Finance** | "Financial Analyst" | "Financial Analyst | Investment Banking" | "Financial Analyst | Helping PE Firms Value Targets | CFA, 50+ Deals Closed" |
| **Healthcare** | "Nurse" | "Registered Nurse | ICU" | "ICU Nurse | 10+ Years Critical Care | Improving Patient Outcomes Through Evidence-Based Practice" |
| **Legal** | "Lawyer" | "Attorney | Corporate Law" | "M&A Attorney | Helping Founders Navigate Exits | 100+ Transactions, $2B+ Deal Value" |
| **Marketing** | "Marketing Manager" | "Digital Marketing Manager | B2B SaaS" | "Growth Marketing Leader | 3x Pipeline for B2B SaaS | Demand Gen, ABM, Content Strategy" |
| **HR** | "Recruiter" | "Technical Recruiter | Startups" | "Tech Recruiter | Hired 200+ Engineers for YC Startups | Building Teams That Ship" |
| **Sales** | "Sales Representative" | "Account Executive | Enterprise Software" | "Enterprise AE | Helping CIOs Modernize Infrastructure | $3M Quota, President's Club" |
| **Consulting** | "Consultant" | "Management Consultant | Strategy" | "Strategy Consultant | Helping Retailers Grow 25%+ | Ex-BCG, Now Independent" |

---

## About Section Scoring (15% of total)

| Score | Criteria |
|-------|----------|
| 9-10 | Compelling hook in first 3 lines, clear story/journey, specific achievements with metrics, relevant keywords, strong CTA, proper formatting, uses most of 2,600 characters |
| 7-8 | Good structure, includes achievements, some metrics, clear offering |
| 5-6 | Describes role and experience, missing story or metrics, no CTA |
| 3-4 | Basic description, generic content, poor formatting |
| 1-2 | Minimal content, unclear value |
| 0 | Empty |

**Structure Checklist:**
- [ ] Hook (first 3 lines compelling)
- [ ] Personal story/journey
- [ ] What they do and who they help
- [ ] Specific achievements with numbers
- [ ] Skills and expertise areas
- [ ] Call-to-action (contact info, link, invitation)

**Formatting Check:**
- [ ] Short paragraphs (2-3 sentences)
- [ ] Strategic use of line breaks
- [ ] Emojis used sparingly and professionally
- [ ] Easy to scan

---

## Experience Scoring (20% of total)

### Completeness (0-5)

| Score | Criteria |
|-------|----------|
| 5 | All relevant positions listed, complete date ranges, company logos linked |
| 4 | Most positions listed, minor gaps |
| 3 | Key positions only, some gaps |
| 2 | Incomplete history, missing key roles |
| 1 | Only current/recent position |
| 0 | Empty |

### Quality of Descriptions (0-5)

| Score | Criteria |
|-------|----------|
| 5 | Quantified achievements (%, $, #), specific outcomes, keyword-rich, media attached |
| 4 | Clear achievements with some metrics, good descriptions |
| 3 | Descriptions present but generic, few metrics |
| 2 | Basic descriptions, job duties only |
| 1 | Minimal or no descriptions |
| 0 | Empty |

**Achievement Checklist per Role:**
- [ ] Quantified results (revenue, growth %, team size, etc.)
- [ ] Scope of responsibility clear
- [ ] Key projects mentioned
- [ ] Skills demonstrated
- [ ] Media attachments (if applicable)

---

## Skills & Endorsements Scoring (10% of total)

| Score | Criteria |
|-------|----------|
| 9-10 | 50+ skills listed, top 3 pinned strategically, 99+ endorsements on key skills, skills align with target role keywords |
| 7-8 | 30-50 skills, good endorsement counts, relevant skills pinned |
| 5-6 | 15-30 skills, some endorsements, mostly relevant |
| 3-4 | 5-15 skills, few endorsements |
| 1-2 | Under 5 skills, minimal endorsements |
| 0 | No skills listed |

**Skills Checklist:**
- [ ] At least 5 skills listed (minimum for "All-Star" profile)
- [ ] Top 3 skills are most relevant to target role
- [ ] Skills include industry keywords
- [ ] Endorsements from credible connections

---

## Recommendations Scoring (10% of total)

| Score | Criteria |
|-------|----------|
| 9-10 | 10+ recommendations, diverse sources (managers, peers, clients), recent (within 2 years), specific and detailed |
| 7-8 | 5-10 recommendations, good variety, mostly recent |
| 5-6 | 3-5 recommendations, some variety |
| 3-4 | 1-2 recommendations, limited scope |
| 1-2 | Single old or generic recommendation |
| 0 | No recommendations |

**Quality Factors:**
- Specificity (mentions projects, skills, outcomes)
- Relevance to current career goals
- Credibility of recommender
- Recency (within last 2 years preferred)
- Variety (different relationship types)

---

## Activity & Content Scoring (15% of total)

### Posting Frequency (0-5)

| Score | Criteria |
|-------|----------|
| 5 | Posts 3+ times per week consistently |
| 4 | Posts 1-2 times per week |
| 3 | Posts 2-4 times per month |
| 2 | Posts occasionally (monthly or less) |
| 1 | Rarely posts (every few months) |
| 0 | No posting activity |

### Engagement Quality (0-5)

| Score | Criteria |
|-------|----------|
| 5 | High engagement rate (5%+), active comments, meaningful discussions |
| 4 | Good engagement (2-5%), some comments and shares |
| 3 | Average engagement (1-2%), occasional interaction |
| 2 | Low engagement (<1%), few reactions |
| 1 | Minimal engagement |
| 0 | No engagement or activity |

### Engagement Rate Calculation

**Formula:**
```
Engagement Rate = (Reactions + Comments + Shares) / Impressions × 100
```

**Calculation Example:**
```
Post with: 1,376 impressions, 15 reactions, 1 comment, 0 shares
Engagement Rate = (15 + 1 + 0) / 1,376 × 100 = 1.16%
→ This is "Average" (1-2%) - needs improvement
```

**Benchmarks by Follower Count:**
| Followers | Expected Rate | Notes |
|-----------|---------------|-------|
| <1,000 | 4-8% | Small but engaged audience |
| 1,000-5,000 | 3-5% | Growth phase |
| 5,000-10,000 | 2-4% | Scaling |
| 10,000+ | 1.5-3% | Broad reach, lower rates normal |

**Content Checklist:**
- [ ] Regular posting schedule
- [ ] Variety of formats (text, images, carousels, video, polls)
- [ ] Original thought leadership content
- [ ] Engagement with others' posts
- [ ] Responds to comments on own posts

---

## Services Section Scoring (Bonus for Consultants/Freelancers)

| Score | Criteria |
|-------|----------|
| 9-10 | 3-5 well-defined services, keyword-rich titles, aligned with headline positioning, clear value propositions |
| 7-8 | Services listed with good descriptions, relevant to expertise |
| 5-6 | Basic services listed, generic descriptions |
| 3-4 | 1-2 services, poorly defined |
| 1-2 | Services enabled but empty or irrelevant |
| 0 | Not using Services section (may be appropriate for non-consultants) |

**Services Checklist:**
- [ ] Services section enabled (if consultant/freelancer)
- [ ] 3-5 services listed
- [ ] Service titles include target keywords
- [ ] Descriptions explain value/outcomes
- [ ] Aligned with headline and About section
- [ ] Pricing indication (optional but helpful)

**Note:** Services section is weighted as bonus points for consultants/freelancers. Not applicable for employees in corporate roles.

---

## Featured Section Scoring (Bonus)

| Score | Criteria |
|-------|----------|
| 9-10 | 4-6 high-quality items, portfolio pieces, case studies, best content, lead magnets |
| 7-8 | 3-4 relevant items, good variety |
| 5-6 | 1-2 items, relevant but limited |
| 3-4 | Items present but outdated or irrelevant |
| 1-2 | Default items (profile sections) only |
| 0 | Featured section empty or not used |

**Ideal Featured Items:**
- Best-performing posts or articles
- Portfolio pieces or case studies
- Media appearances or interviews
- Lead magnets or free resources
- "Work with me" or services page
- Publications or research

---

## Overall Score Calculation

### Weighted Score Formula

```
Overall Score = (Visual × 0.15) + (Headline × 0.15) + (About × 0.15) + 
                (Experience × 0.20) + (Skills × 0.10) + 
                (Recommendations × 0.10) + (Activity × 0.15)
```

### Score Interpretation

| Score Range | Rating | Description |
|-------------|--------|-------------|
| 90-100 | Elite | Top 1% profile, exceptional personal brand, thought leader status |
| 80-89 | Excellent | Strong professional presence, well-optimized, attracting opportunities |
| 70-79 | Good | Solid foundation, some gaps to address, above average |
| 60-69 | Average | Functional profile, missing key optimizations, room for improvement |
| 50-59 | Below Average | Significant gaps, not leveraging LinkedIn effectively |
| Below 50 | Needs Work | Major improvements required across multiple areas |

### Priority Improvement Matrix

Based on score gaps, prioritize improvements:

1. **Immediate fixes** (if score < 5):
   - Profile photo
   - Headline
   - About section hook

2. **High-priority** (if score < 7):
   - Experience descriptions
   - Featured section
   - Skills pinning

3. **Growth focus** (if score 7-8):
   - Content strategy
   - Recommendations
   - Engagement tactics

4. **Excellence** (if score 8+):
   - Thought leadership content
   - Newsletter launch
   - Speaking opportunities

---

## LinkedIn Features Assessment

### Creator Mode Evaluation

| Criteria | Enable If | Keep Off If |
|----------|-----------|-------------|
| Posting frequency | 3+ posts/week | Less than weekly |
| Content focus | Thought leadership | Job seeking primarily |
| Follower goal | Growing audience | Quality connections |
| Newsletter interest | Yes | No |

### Open to Work Assessment

| Scenario | Recommendation |
|----------|----------------|
| Active job search | Enable (recruiters only) |
| Passive but open | Enable (recruiters only) |
| Not job seeking | Disable |
| Freelancer/Consultant | Use "Providing Services" instead |

### Providing Services Assessment

| Criteria | Enable If |
|----------|-----------|
| Freelancer/Consultant | Yes |
| Accepting new clients | Yes |
| Have clear service offerings | Yes |
| Want inbound leads | Yes |

### Newsletter Evaluation

| Criteria | Recommendation |
|----------|----------------|
| Followers 1,000+ | Consider launching |
| Consistent content creator | Good candidate |
| Unique expertise to share | Strong candidate |
| Time to write weekly/biweekly | Required |

---

## Profile Completeness Scoring

LinkedIn "All-Star" profile requires:

| Element | Required | Points |
|---------|----------|--------|
| Profile photo | ✅ | 10 |
| Location | ✅ | 5 |
| Industry | ✅ | 5 |
| Current position (with description) | ✅ | 15 |
| Two past positions | ✅ | 10 |
| Education | ✅ | 10 |
| Skills (5+) | ✅ | 10 |
| Summary/About | ✅ | 15 |
| Connections (50+) | ✅ | 10 |
| **Custom additions (bonus):** | | |
| Custom URL | Recommended | +5 |
| Banner image | Recommended | +5 |
| Featured section | Recommended | +5 |
| Recommendations (3+) | Recommended | +10 |

---

## Keyword Optimization Scoring

### Keyword Density Check

For each target keyword, check presence in:

| Location | SEO Weight | Target |
|----------|------------|--------|
| Headline | High | 1-2 keywords |
| About section | High | 3-5 keywords |
| Experience titles | Medium | Natural inclusion |
| Experience descriptions | Medium | 2-3 per role |
| Skills section | High | All relevant |

### Keyword Research Process

1. Identify 5-10 keywords for target role/industry
2. Check current presence in profile
3. Analyze competitor profiles for keyword ideas
4. Map keywords to profile sections
5. Add naturally without keyword stuffing
