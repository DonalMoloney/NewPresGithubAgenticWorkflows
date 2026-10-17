# Deck v2: language sharpening pass

Proposals only. Nothing here has been applied to `deck.md`.

**Rebased against `deck.md` as of 17 Oct 2026 18:56** — the 16-slide version that includes the new blast-radius slide ("Even a misled agent can only reach what we put on the list") at position 8. Slide numbers below count the title slide as 1. Main talk 1–11, appendix 12–16.

Every OLD string was machine-checked to appear **exactly once** in that version of `deck.md`. All 15 edits were applied to a scratchpad copy and rendered with `marp --images png`; every affected slide was inspected. Nothing overflows, nothing shrinks below the 20px/18px floors, no title gained a line.

**Goal:** sound expert by being more precise and less hedged, not by adding vocabulary. No new facts; nothing here is unsupported by `deck.md` or `sources.md`.

---

## HIGH — clear wins

### H1. Slide 5: promote the recipe/brief line out of the notes and into the title
The best line in the deck is currently invisible to the audience. The title is 20 words and 3 clauses; this one is 11 words and sticks. The body keeps everything the title drops ("GitHub Action", "AI agent", "plain English" → "describe the goal").

**OLD** (title + the line under it, one block)
```
## An agentic workflow is a GitHub Action whose job is written in plain English and done by an AI agent

**Classic Action:** you script every step. **Agentic workflow:** you describe the goal, and the agent plans the steps.
```
**NEW**
```
## A classic Action is a recipe; an agentic workflow is a brief

It is still a GitHub Action. Instead of scripting every step, **you describe the goal and an AI agent plans the steps.**
```
Verified: title now fits on **one line** at 40px (was two). Body is two lines. Slide has the same height as before.

### H2. Slide 5 note: stop repeating what is now on the slide
Required if H1 lands — `CLAUDE.md` says notes must not merely repeat the slide.

**OLD**
```
Plain line: a classic Action is a recipe; an agentic workflow is a brief.
```
**NEW**
```
The title is the whole idea. Say it, pause, then: it is still a GitHub Action; the difference is you brief it instead of scripting it.
```

### H3. Slide 8 note: "fifteen lines" is wrong — the slide shows thirteen
He says this out loud immediately before a slide the audience can count. The YAML block on slide 9 is exactly 13 lines (the "fifteen" is a leftover from the longer draft in `slide-additions.md`). Nothing costs authority faster than a number the room can check.

**OLD**
```
Transition: that is the cage. Here is the whole job, in fifteen lines.
```
**NEW**
```
Transition: that is the cage. Here is the whole job description, in thirteen lines.
```

### H4. Slide 9 title: count the lines instead of saying "the settings"
"The settings say" is a limp subject. The number is concrete, verifiable on the slide, and pre-empts "this must be complicated". Keeps the memorable "the one thing it can send".

**OLD**
```
## The settings say when it runs, what it can read, and the one thing it can send
```
**NEW**
```
## Thirteen lines say when it runs, what it can read, and the one thing it can send
```
Verified: wraps to two lines, exactly as the current title does. No regression. Depends on H3 for consistency.

### H5. Slide 11 (the ask): name the mechanism instead of promising safety
"nothing is written to our repo until we choose" is the vaguest line on the most important slide — it asks for trust at exactly the moment he should be showing a setting. `deck-v2/CLAUDE.md` explicitly permits `staged: true` on this slide and the ways-to-run slide.

**OLD**
```
2. **Try it safely:** nothing is written to our repo until we choose.
```
**NEW**
```
2. **Try it staged:** `staged: true` runs it for real and writes nothing to our repo.
```
Verified: one line, slide still has ~150px of clear space below.

### H6. Slide 10: cut the title/body repetition and put the caveat the room is thinking about on the slide
"pull requests ... merged" is in the title and again in the body. And "merged is not the same as correct" is the first objection a sharp listener forms — saying it before they do is worth more than any added word. It is already in the speaker notes, so nothing new is being claimed.

**OLD**
```
Daily Documentation Updater pull requests merged (96%). <span class="muted">gh-aw blog, 13 Jan 2026; reported by GitHub, small sample.</span>
```
**NEW**
```
A 96% merge rate for its Daily Documentation Updater. <span class="muted">gh-aw blog, 13 Jan 2026; reported by GitHub, small sample. Merged is not the same as correct.</span>
```
Verified: muted line wraps to two lines; the TODO line and the slide still fit with room to spare. Both existing source qualifications are retained verbatim.

### H7. Slide 3: Octoverse says "pushed", so say "pushed"
One word, and it is the word in the source. `sources.md` flags this ("Octoverse says 'pushed'"). Commits made and commits pushed are not the same measure, and someone in a technical room knows that.

**OLD**
```
- **Nearly 1 billion** commits in 2025, up 25.1%.
```
**NEW**
```
- **Nearly 1 billion** commits pushed in 2025, up 25.1%.
```

### H8. Slide 6: use the docs' own phrase, "a policy, not a default"
This is the single best "I read the primary source" detail in the deck, and the slide currently paraphrases it away. The docs say verbatim: "`draft` is a **policy**, not a default, so the agent cannot override it at runtime" (`sources.md`, safe-outputs-pull-requests). "Policy, not a default" is also instantly meaningful to a non-technical listener — it means nobody can turn it off at runtime.

**OLD**
```
`draft: true` is a policy the agent cannot override.
```
**NEW**
```
`draft: true` is a policy, not a default: the agent cannot override it.
```
Verified: the "Wrong edits" paragraph still wraps to two lines; the slide gains no height.

---

## MEDIUM — judgement calls

### M1. Slide 7: name the setting behind the caution-notice caveat
The caveat is already honest; naming the flag turns it from a hedge into a demonstration that he read the threat-detection page. Verified in `sources.md`: `continue-on-error` defaults to `true`.

**OLD**
```
<span class="muted">A failed check defaults to a caution notice, not a hard block.</span>
```
**NEW**
```
<span class="muted">A failed check defaults to a caution notice, not a hard block (`continue-on-error` is `true`).</span>
```
Verified: fits on the same two lines. **Caveat:** the two code chips render brighter than the muted grey around them, so the eye is pulled to a footnote. If that bothers you, drop the backticks — `(continue-on-error is true)` — and the whole line stays quiet. Judgement call, not a correctness one.

### M2. Slide 7: say the diagram is a simplification
The notes already warn "don't say four jobs". Saying "four of its six" on the slide pre-empts the one question a gh-aw reader in the room would ask, and costs five words.

**OLD**
```
<span class="muted">gh-aw architecture documentation. Status: public preview since 11 Jun 2026 (GitHub changelog).</span>
```
**NEW**
```
<span class="muted">gh-aw architecture documentation; four of its six jobs shown. Status: public preview since 11 Jun 2026 (GitHub changelog).</span>
```
Verified: still one line.

### M3. Slide 6: "by default" twice in one sentence
Repetition inside a single line reads as padding. "On automatically" is accurate — the docs say threat detection is "automatically enabled when safe outputs are configured". Shorter by 18 characters.

**OLD**
```
**Prompt injection →** read-only by default, every write checked, threat detection on by default.
```
**NEW**
```
**Prompt injection →** read-only by default, every write checked, threat detection on automatically.
```

### M4. Slide 14 (appendix): a 101-character title
Longest title in the deck. The notes already have the punchier parallel ("something happens in the repo, a clock, a button, or someone asks in a comment"). 79 characters, still a full-sentence claim, and the diagram underneath already labels each route.

**OLD**
```
## You can start a workflow four ways: on a repo event, on a schedule, by hand, or by asking in a comment
```
**NEW**
```
## You start a workflow four ways: a repo event, a clock, a button, or a comment
```
Verified: still two lines, but balanced rather than running almost to a third.

### M5. Slide 7 title: active verb instead of "writes happen"
"Writes happen" is an agentless construction on a slide whose whole point is *which job holds the token*. Same length, same claim.

**OLD**
```
## The agent never holds a write token: writes happen in a separate, checked job
```
**NEW**
```
## The agent never holds a write token: a separate, checked job does the writing
```

### M6. Slide 9: trim the Tools bullet now that slide 8 owns the firewall
With the new blast-radius slide in front of it, "firewalled" and "the outbox above" are being explained twice. This keeps the `bash: true` pre-empt (which the notes say to expect) but stops re-arguing the previous slide.

**OLD**
```
- **Tools:** broad **reads** — `bash` and the GitHub toolsets stay inside the read-only, firewalled job. The outbox above is still the only way out.
```
**NEW**
```
- **Tools:** broad **reads** — `bash` included, all inside the read-only, firewalled job. The outbox is still the only way out.
```
Verified: drops from four rendered lines to three.

### M7. Slide 2: mirror the survey's own question
The Stack Overflow question is "What gets in the way of you getting the context you need for work?" (`sources.md`). Quoting the instrument's wording is what makes a statistic quotable back. Marginal — include only if you like the rhythm.

**OLD**
```
of 12,374 developers say **outdated information** makes it hard to get the context they need.
```
**NEW**
```
of 12,374 developers say **outdated information** gets in the way of the context they need at work.
```

### M8. Slide 13 note (appendix): the real body names Diátaxis
Notes only — this is a Q&A asset, not slide content. `sources.md` records that the real `update-docs.md` body is "a long technical-writer prompt (Diátaxis, never push to the default branch)". If someone asks "how long is the real prompt?", naming the framework it follows answers it in four words. Keep it off the slide: it is jargon for a mixed room.

**OLD**
```
Below the frontmatter is the job description, in plain English. The real body is longer (style rules, what to check); this one line is a paraphrase.
```
**NEW**
```
Below the frontmatter is the job description, in plain English. The real body is a page of style rules — it names the Diátaxis framework and forbids pushing to the default branch; this one line is a paraphrase.
```

---

## FLAG — not a language fix, but found while reading (worth a decision)

### F1. The new blast-radius diagram re-states a claim `sources.md` marked "changed"
`deck-v2/img/agent-blast-radius.svg` renders the API proxy box as:

```
API proxy
Holds the engine token
Agent never sees it
```

`sources.md` mismatch 1 flags exactly this: the architecture page says the proxy "may hold endpoint-specific credentials" and labels the feature "Agent auth-token isolation", and it warns that an in-container identifier should be treated "as leaked by design". The ledger's status for "API proxy holds the tokens; agent never sees them" is **changed**, with suggested wording *"keeps the engine's auth token out of the agent's container"* — which is what the previous slide-7 bullet said, and what this SVG's own `aria-label` still says ("an API proxy that keeps the engine token out of the container").

So the slide text now says something the deck's own ledger rejected, while the alt text says the correct thing. In a security-minded room this is the claim most likely to be challenged.

Suggested SVG text edits (two lines, same width):
- `Holds the engine token` → `Keeps the engine token`
- `Agent never sees it` → `out of the container`

Also worth a look while in there: the Agent box reads `Sandboxed, no token`. "No token" is doing the same absolute work; `Sandboxed, read-only` is verified by the architecture page and says enough.

I did not edit the SVG — flagging for whoever owns the diagram.

---

## SKIP — considered and rejected

- **The daily AI-credit cap conflict, onto slide 6.** It is genuinely the best "I read both pages" detail in the deck, but the root `CLAUDE.md` is explicit: when official sources conflict, leave the fact off the slide and record it on the status and sources slide. It is already on slide 16 and already in slide 6's notes as a prepared answer ("two docs pages disagree on its default, so I've left it out"). Said in response to a question it sounds like mastery; printed on a slide it sounds like a footnote fight, and it spends attention on the one slide that is already carrying four ideas.
- **The GitHub Blog "start with low-risk outputs" quote, onto slide 11.** Tempting — it makes the pilot look like it follows GitHub's published advice rather than the speaker's preference. But the quote says to start with low-risk outputs "before enabling pull request creation", and the pilot's step 3 reviews pull requests. An attentive listener would catch the mismatch and the quote would cost more than it earns. It stays in the notes as support if challenged.
- **Slide 13 title, "one command locks them into a GitHub Action".** Looks like a weak verb until you notice the compile output is a `.lock.yml` file. It is a deliberate pun that happens to be technically exact. Leave it.
- **"read-only" appearing on slides 6, 7 and 9.** Looks like a repetition violation but is not: slide 6 is the one-word answer to an objection, slide 7 is the mechanism, slide 9 is the evidence in the file (`permissions: read-all`). Three different jobs for the same fact.
- **Slide 15 title ("Try it yourself: my examples and the official docs") is not a full-sentence claim.** True, but it is a links slide left up during Q&A. Forcing a claim onto it would add words to the one slide whose job is to be scanned.
- **Upgrading vocabulary — "least privilege by job boundary", "egress allowlist", "containerised".** All present in the speaker notes, where they belong. On the slides they would break "plain English first, technical second" and, in a mixed room, read as someone reaching. Precision already does the work.
- **Slide 6 cost line ("capped per run: 1,000 AI Credits (~$10) by default, and you choose the model").** Could be tightened by a word or two; not worth the diff.
- **Adding "(the default maximum)" to slide 9's "Outbox: one draft pull request".** Accurate (`create-pull-request` defaults to max 1 per run) but the whole point of the line is that the outbox holds one thing. The parenthesis weakens it.
- **Slide 11's "Would we get 96%? Unknown; that is what the pilot measures."** Checked as a hedge candidate — it is the opposite. Confident about an unknown is exactly the register the speaker wants. Leave it alone.

---

## How to apply

Each OLD string above is verbatim and unique in the 18:56 version of `deck.md`. If `deck.md` has moved again, re-check uniqueness before applying — slide 5's title block and slide 7's muted lines are the two most likely to have been touched.

After applying: `marp deck-v2/deck.md --allow-local-files --images png` and look at slides 5, 6, 7, 9, 10, 11 and 14, then run `python3 deck-v2/check_deck.py`.
