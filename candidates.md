# Candidates — One-Line Roast: The Gadget You Use Every Day

Competition: u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610. Pot $5, top 3 paid ($2/$2/$1). Judge: z-ai/glm-5.3-flash, pairwise, criteria IN ORDER: (1) roasts a daily gadget/app (gate), (2) actually funny, (3) fresh, (4) neatly worded, (5) specific concrete behaviour. 370 submissions already — the line must be genuinely funny and fresh. The RULES.txt examples (phone dies at 4pm, app asks for a rating, smart kettle firmware update) are the clichés to avoid.

Internal scoring: gate pass/weak/fail on criterion 1, then funny x4 + fresh x3 + neat x2 + specific x1 (max 100). Scored hard.

## All 15 candidates

| ID | Line (chars) | Gate | Funny | Fresh | Neat | Specific | Weighted |
|----|--------------|------|-------|-------|------|----------|----------|
| C1 | My AirPods die mid-sentence, so every call ends like my relationships do: suddenly, mid-apology. | pass | 8 | 7 | 7 | 9 | 76 |
| C2 | Autocorrect fixed 'teh' to 'the', then let 'I love you' go to my landlord. | pass | 7 | 6 | 9 | 9 | 73 |
| C3 | My smartwatch applauds me for standing up, as if reaching for snacks were a summit. | pass | 8 | 8 | 9 | 8 | 82 |
| C4 | My printer needs a pep talk, a restart and a firmware update before it will print a single page. | weak | 6 | 4 | 7 | 7 | 57 |
| C5 | My phone hits 1% the moment I leave the house, like it was waiting for me to need it. | pass | 5 | 3 | 8 | 6 | 51 |
| C6 | My microwave beeps at me until I open the door, like it's the one who did the cooking. | pass | 8 | 8 | 8 | 9 | 81 |
| C7 | My robot vacuum mapped my flat to the centimetre, then got stuck on the same rug again. | pass | 7 | 7 | 9 | 9 | 76 |
| C8 | My smart TV takes longer to open Netflix than the film takes to disappoint me. | pass | 6 | 5 | 8 | 6 | 61 |
| C9 | Face ID knows me in every light except first thing in the morning, when I apparently don't exist. | pass | 8 | 7 | 8 | 8 | 77 |
| C10 | My earbuds pair with my neighbour's TV faster than they pair with my phone. | pass | 7 | 8 | 9 | 8 | 78 |
| C11 | My laptop fan roars like a jet engine whenever I open a spreadsheet, as if the numbers were heavy. | pass | 8 | 8 | 8 | 8 | 80 |
| C12 | My smart speaker hears me whisper from the kitchen, but goes deaf when I ask it to play music from the sofa. | pass | 7 | 7 | 6 | 9 | 70 |
| C13 | My phone is full, and the 4 GB labelled 'Other' is a mystery it refuses to explain. | pass | 7 | 8 | 8 | 9 | 77 |
| C14 | My phone's snooze button is bigger than its stop button, because it knows exactly who I am. | pass | 8 | 7 | 9 | 7 | 78 |
| C15 | My washing machine plays a fanfare when it finishes, as if spinning my socks deserved applause. | WEAK | 8 | 9 | 9 | 8 | 85 |

## Scoring notes (why the low ones lost)

- C5 is the RULES.txt example angle (phone dies) in different clothes — the most obvious complaint in the field; fresh 3.
- C4 printer-woes is a decade-old trope, and a printer is not a daily gadget for most people; fresh 4, gate weak.
- C8 is two mild grumbles stapled together; no sting of recognition, specific 6.
- C12 lands the behaviour but is wordy (116 chars, two clauses doing the same job); neat 6.
- C2 autocorrect jokes are ancient; the landlord twist saves it from worse, but fresh 6.
- C15 tops the weighted score but carries a criterion-1 risk: a washing machine is not an every-day gadget for most people, so it may lose the gate to any line that clearly targets a daily gadget. Flagged for the panel to weigh explicitly.
- C3 vs C6: both daily gadgets, both concrete behaviours (stand-ring applause; the beep that won't stop). C3 edges C6 on neatness; C6 edges C3 on specificity.

## Internal top 3 (to the panel)

1. **C15 (85)** — "My washing machine plays a fanfare when it finishes, as if spinning my socks deserved applause."
2. **C3 (82)** — "My smartwatch applauds me for standing up, as if reaching for snacks were a summit."
3. **C6 (81)** — "My microwave beeps at me until I open the door, like it's the one who did the cooking."

Next best: C11 (80) — held as reserve if the panel finds a concrete flaw in a top-3 line.

## Independent judge panel (CrowLLM, 3 models)

Panel letters: A = C15, B = C3, C = C6. Each judge scores each line 0–10 on the brief's criteria IN ORDER (on-subject, funny, fresh, neat, specific) plus "would this make a cold reader actually laugh — yes/no, why". Weighted per judge = funny x4 + fresh x3 + neat x2 + specific x1 (on-subject recorded separately as the gate). Raw replies: panel-results.json.

Panel letters: A = C15, B = C3, C = C6. Weighted = funny x4 + fresh x3 + neat x2 + specific x1 per judge.

**gemma-4-31b-it:free** (substitute — qwen4-max:free failed 503)
- A: on_subject 0, funny 4, fresh 5, neat 8, specific 7 — laugh: no — "fails primary brief; washing machines are not daily gadgets." (weighted 54)
- B: on_subject 10, funny 8, fresh 7, neat 9, specific 9 — laugh: yes — "highly relatable contrast between the device's praise and the user's laziness." (weighted 80)
- C: on_subject 10, funny 6, fresh 4, neat 8, specific 6 — laugh: no — "a common observation that feels more like a grumble than a roast." (weighted 58)

**glm-4.7-flash:free** (substitute — llama-3.3-70b-instruct:free failed 429/500, minimax-m3.1-flash:free failed 429, deepseek-v4-flash:free failed 429)
- A: on_subject 0, funny 4, fresh 5, neat 7, specific 6 — laugh: no — "it's a mild grumble, not a punchline" (weighted 51)
- B: on_subject 10, funny 9, fresh 8, neat 9, specific 10 — laugh: yes — "the 'snack summit' comparison is relatable and sharp" (weighted 88)
- C: on_subject 10, funny 7, fresh 5, neat 8, specific 8 — laugh: yes — "the entitlement of the microwave is a classic gag" (weighted 67)

**grok-4.7-fast:free** (substitute — ernie-5.5-flash-preview:free failed 429/503)
- A: on_subject 2, funny 4, fresh 3, neat 8, specific 6 — laugh: no — "not every-day gadget, common complaint" (weighted 47)
- B: on_subject 9, funny 6, fresh 7, neat 8, specific 7 — laugh: yes — "clever snack summit twist lands well" (weighted 68)
- C: on_subject 10, funny 7, fresh 6, neat 9, specific 8 — laugh: yes — "fun microwave self-roast with recognition" (weighted 72)

**Combined panel weighted totals: A (C15) 152 · B (C3) 236 · C (C6) 197.** Laugh test: A 0/3 yes, B 3/3 yes, C 2/3 yes. On-subject (gate): A 0/0/2, B 10/10/9, C 10/10/10.

Panel mechanics note: the first-choice judges qwen4-max:free, llama-3.3-70b-instruct:free and minimax-m3.1-flash:free all failed repeatedly (HTTP 429/500/503 across 3 attempts each after waits); deepseek-v4-flash:free also 429 twice; ernie-5.5-flash-preview:free 429/503. Substitutes gemma-4-31b-it:free, glm-4.7-flash:free and grok-4.7-fast:free answered and are recorded as the three judges, per the substitution rule. The CrowLLM key was sourced from crowllm.env in the shell only — never printed, logged, or committed.

### The disagreement, and the call
The internal scoring picked **C15** (85). The panel overruled it unanimously and decisively: all three judges scored C15 on_subject 0/0/2 — a washing machine is not a gadget people use every day, so it fails criterion 1, the gate, exactly the risk flagged in the scoring notes before the panel ran. No concrete flaw can be named in that reasoning; it is the brief's own first criterion, and the panel converged on it independently. **The panel's pick stands: C3 is the entry.** C3 also won the panel weighted totals outright (236 vs C6's 197) and was the only line all three judges said makes a cold reader actually laugh (3/3). C3 was the internal #2 (82), not a weak candidate. main.ts implements exactly this: internal weighted scorer over all 15 candidates, then the recorded panel verdict (gate + totals) applied to the internal top 3, C3 wins.

## WINNER
**"My smartwatch applauds me for standing up, as if reaching for snacks were a summit."** (83 characters)
