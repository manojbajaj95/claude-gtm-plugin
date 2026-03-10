# Copywriting - Validations

## Passive Voice Usage

### **Id**
copy-passive-voice
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \b(?:is|are|was|were|been|be|being)\s+(?:\w+ed|gone|done|taken|made|given|shown|seen|written)\b
  - \b(?:is|are|was|were)\s+being\s+\w+ed\b
### **Message**
Passive voice detected - weakens copy impact and clarity
### **Fix Action**
Rewrite in active voice to make the subject perform the action (e.g., 'We built' instead of 'It was built')
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Weak or Generic Verbs

### **Id**
copy-weak-verbs
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \b(?:is|are|was|were|has|have|had|does|do|did|make|makes|get|gets|got)\s+
  - \b(?:utilize|implement|leverage|execute)\b
### **Message**
Weak or unnecessarily complex verbs detected - reduces copy power
### **Fix Action**
Replace with strong, specific action verbs (e.g., 'use' instead of 'utilize', 'build' instead of 'implement')
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Jargon and Buzzwords

### **Id**
copy-jargon-overload
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \b(?i)(?:synergy|paradigm|leverage|disrupt|revolutionary|game-changer|cutting-edge|best-in-class|world-class|innovative|next-generation|turnkey|holistic|robust)\b
### **Message**
Business jargon or buzzwords detected - may alienate or confuse readers
### **Fix Action**
Replace jargon with clear, concrete language that describes actual benefits and features
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Overly Long Sentences

### **Id**
copy-long-sentences
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - [^.!?]{150,}[.!?]
### **Message**
Sentence exceeds 150 characters - may reduce readability and comprehension
### **Fix Action**
Break into shorter sentences (aim for 15-20 words) or use bullet points for complex ideas
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Feature-Focused Without Benefits

### **Id**
copy-missing-benefits
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - (?i)\b(?:feature|function|capability|specification)\b(?!.*\b(?:benefit|advantage|help|enable|allow|improve|save|increase|reduce)\b)
### **Message**
Features mentioned without connecting to customer benefits
### **Fix Action**
For every feature, explain the benefit: 'This feature helps you [benefit]' or 'So you can [outcome]'
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Excessive Adverb Usage

### **Id**
copy-adverb-overuse
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \b\w+ly\s+(?:very|really|extremely|absolutely|completely|totally)\b
  - (?:\b\w+ly\b.*){3,}
### **Message**
Excessive adverb usage detected - weakens copy strength
### **Fix Action**
Remove adverbs and use stronger, more specific verbs or adjectives instead
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Filler Words and Phrases

### **Id**
copy-filler-words
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \b(?i)(?:very|really|just|actually|basically|literally|quite|rather|somewhat|perhaps|maybe)\b
  - \b(?i)(?:in order to|due to the fact that|at this point in time|for the purpose of)\b
### **Message**
Filler words detected that add no value and dilute message impact
### **Fix Action**
Remove filler words or replace wordy phrases with concise alternatives (e.g., 'to' instead of 'in order to')
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Missing Social Proof

### **Id**
copy-no-social-proof
### **Severity**
info
### **Type**
regex
### **Pattern**
  - ^(?!.*(?i)(?:customer|client|user|review|testimonial|rating|case study|trusted by|used by|\d+\+?\s+(?:companies|users|customers))).*$
### **Message**
No social proof elements detected - missing trust-building opportunity
### **Fix Action**
Add testimonials, customer counts, ratings, or case studies to build credibility
### **Applies To**
  - *.md
  - *.html

## Unclear Value Proposition

### **Id**
copy-unclear-value-prop
### **Severity**
error
### **Type**
regex
### **Pattern**
  - ^(?!.*(?i)(?:save|increase|reduce|improve|faster|easier|better|more|help you|enable you|get|achieve)).*$
### **Message**
Value proposition unclear - no clear benefit or outcome stated
### **Fix Action**
Lead with a clear value statement: 'Save X time/money' or 'Achieve Y result' in the first paragraph
### **Applies To**
  - *.md
  - *.html

## Complex or Academic Language

### **Id**
copy-complex-language
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \b\w{15,}\b
  - \b(?i)(?:aforementioned|heretofore|notwithstanding|subsequently|aforementioned|utilize|endeavor|facilitate)\b
### **Message**
Complex or overly formal language detected - may reduce accessibility
### **Fix Action**
Simplify language to 8th-grade reading level - use short, common words that everyone understands
### **Applies To**
  - *.md
  - *.html
  - *.txt

## Missing Urgency or Scarcity

### **Id**
copy-missing-urgency
### **Severity**
info
### **Type**
regex
### **Pattern**
  - ^(?!.*(?i)(?:now|today|limited|deadline|expires|only|last chance|while supplies|hurry|don't miss|ends soon)).*$
### **Message**
No urgency or scarcity elements detected - may reduce conversion motivation
### **Fix Action**
Add time-bound or quantity-limited language to create appropriate urgency (e.g., 'Limited spots available')
### **Applies To**
  - *.md
  - *.html

## Company-Centric Language (We/Our vs You/Your)

### **Id**
copy-you-vs-we
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - (?:\b(?i)(?:we|our|us)\b.*){3,}(?!.*\b(?i)(?:you|your)\b)
### **Message**
Copy is too company-centric - lacks customer focus
### **Fix Action**
Shift focus to the customer by using 'you' and 'your' more than 'we' and 'our'
### **Applies To**
  - *.md
  - *.html
  - *.txt