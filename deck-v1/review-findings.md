# Deck v1: in-depth review findings (18 Oct 2026)

Raw reports from three read-only reviewers (story and notes, accuracy, visual design). Source-read plus screenshots; nothing here was applied unless deck-v1/todo.md says so. Re-check each item against the current deck before acting.

---

## Lens: story

# deck-v1 story, narration and speaker notes review (read-only)

Slide numbers are deck order (1-28). Main talk is 1-18; 19-28 are appendix. Reviewed `deck-v1/deck.md` against the root CLAUDE.md note order. Spot-checked PNGs 02 and 13.

## Overall read
The spine works: hook (1) -> payoff stat (2) -> blank personal story (3) -> mechanism (4) -> ask up front (5) -> role shift (6) -> why an agent (7) -> real PR (8) -> evidence (9) -> risk (10) -> limits (11-13) -> cost (14) -> pilot/decision rule/bounds (15-17) -> decision (18). The close echoes the hook well. What is still weak: the middle hole (slide 3), the ask stated four times, risk/limits told three times, notes that point at things that are not on the slide, and several lines a presenter cannot say.

Timing (main talk, 18 slides, roughly 20-24 min at a steady pace): slides over ~90 s as written are 6 (five Q&A, role shift plus who-does-what), 10 (four cards, each narrated), 11 (plain paragraph plus a four-part code walk), 13 (diagram, Saltzer, detection caveat, four Qs) and 14 (four-box equation plus AIC units). Slides that must stay under 45 s: 3, 5, 17.

## Top 12 findings, ranked by impact

### 1. Slide 3 (and the hook payoff): the story the hook promises is blank, and slide 2 hands off to it conditionally
Problem: slide 1 asks "When did a page of documentation last mislead you?"; the personal answer (slide 3) is all TODO, and slide 18's close has a TODO to name its gap. If Donal has no story ready, the talk goes hook -> stat -> two empty cards. Slide 2's Transition contains a bracketed `[TODO: ...]` plus an either/or, which cannot be spoken.
Fix (no invented facts): keep slide 3 as a TODO until supplied, but make slide 2's transition sayable in both cases. Replace slide 2 Transition with:
> "Numbers like that are easy to nod at. Here is how it showed up for me." (If the story is not confirmed, skip slide 3 in presenter view and say instead: "If that is the cost, here is how the debt builds up.")
Keep the TODO about the story in the Detail line of slide 3, not in a spoken line.

### 2. Slide 2: Say does not cash in the hook; two notes point at a chart that is not there
Problem: the hook ends "Was that just you?"; slide 2 opens "In that survey..." (the survey is only named in slide 1's transition). Also slide 2 Detail says "The right-hand bar redraws the same figure", but the slide shows a 100-square grid, not a bar. Slide 9 Say/Detail also says "the bars use the reported rates", but slide 9 is a square strip.
Fix, slide 2 Say:
> "Was that just you? In Stack Overflow's 2026 survey, 56.5 percent of developers named outdated information as something that makes context hard to get. I will call the accumulated cost documentation debt, borrowing Ward Cunningham's technical-debt metaphor."
Slide 2 Detail: change "right-hand bar" to "right-hand grid of 100 squares". Slide 9: change "The bars use the reported rates" to "Each square is one pull request; the strip length is the sample size."

### 3. Slide 13: the first spoken line is a 1975 citation, and the note describes a different diagram
Problem: Say opens "least privilege... Saltzer and Schroeder in 1975" before stating the claim. For a mixed room the claim ("agent cannot write; a separate job does") is never said plainly in Say. Detail says "the diagram groups five stages into three readable phases", but the slide shows four jobs ("4 of 6 documented jobs shown"; Prepare, Agent, Detection, Safe outputs). Careful-wording paragraph is ~200 words, contains a stray lowercase sentence ("the failure case is deliberately not stated as a rule.") and a Saltzer-versus-separation warning that bloats the slide. Notes are out of order (analogy before the claim).
Fix, Say:
> "The part that thinks is not the part that writes. The agent can read and draft, but it cannot change the repository. A separate job, after a check, is the only one that can write."
Detail first sentence: "The diagram shows four of the six documented jobs: Prepare, Agent, Detection, then a separate Safe outputs job that holds the only write permission." Move the Saltzer and Schroeder attribution to a one-line Evidence item ("least privilege, Saltzer and Schroeder 1975"), and split the Careful wording into 3 short lines (detection is a layer; continue-on-error defaults to true; four-eyes is an analogy for the job split, not a second human).

### 4. Slide 10 Q&A overclaims: "closed in the same second it is read"
Problem: the answer to "Isn't confidently wrong documentation worse than stale documentation?" says a wrong draft "is closed in the same second it is read". That contradicts the slide's own premise (confidently wrong is the failure a reviewer might not catch) and the note's careful-wording line ("Do not promise that a reviewer always catches confidently wrong prose"). Also it is the strongest objection in the deck and is answered with rhetoric.
Fix:
> Q: Isn't confidently wrong documentation worse than stale documentation? A: It is the sharpest objection to this proposal, and why the output is a draft pull request, not a commit. A wrong draft that a reviewer catches costs one close. One they miss is the residual risk, and sizing it is what week one is for.

### 5. Slides 5, 15, 17, 18: the ask and its bounds are stated four times
Problem: "four weeks, one repository, docs only, draft PR, human merges" is on slide 5 (tiles), slide 15 (four weeks plus staged), slide 17 (nested limits) and slide 18 ("The ask, in full and for the last time"). Slide 5's Say, slide 17's Say and slide 18's Say overlap word for word in places. Root rule: say each fact once.
Fix: keep slide 5 as a 30-second shape-only preview and keep 18 as the full ask; on slide 17 drop the restatement. Replace slide 17 Say with:
> "Here is why the downside is small. Each ring limits a different kind of failure: time, money, place, scope and output."
and slide 18 Say opening "The ask, in full and for the last time:" with "Now the ask I previewed at the start:" (accurate, and it keeps the callback to slide 5).

### 6. Slides 10, 13, 17: risk and limits are told three times
Problem: slide 10 gives four failure modes each with a limit, slide 13 explains the main limit (write split), slide 17 re-draws all limits as rings. Slides 16 -> 17 hand off as "upside -> downside", but the audience has already had the downside twice, so slide 17 lands as a recap, not a turn.
Fix (wording, no restructure): change slide 16 Transition to "That is what the upside has to look like. The limits you have just seen add up to one picture of the downside." and keep 17 under 45 seconds. If a cut is allowed later, merge 17 into 10's takeaway, but that is a structural call for Donal.

### 7. Slide 6: a second talk is hiding in the notes (duplicated with slide 26)
Problem: slide 6's note carries a full "Who does what" paragraph and three Q&As (replace writers, approve whatever it writes, accountable for bad merge) that are word-for-word the Q&As and Detail on appendix slide 26. It is the longest note in the deck (5 questions), it breaks the root note order (the paragraph sits between Evidence and Careful wording), and it invites a 2-minute detour on a slide whose job is one sentence.
Fix: delete the "Who does what" paragraph and the three duplicated Q&As from slide 6, leaving two Q&As (Copilot Chat difference; which model), and add at the end of Detail: "If asked exactly who does what, jump to Appendix 8 (slide 26)." Slide 26 already holds the full version.

### 8. Slides 6 and 7 and 9 and 10: repeated stock phrases the presenter will say back to back
Problem: slide 6 Transition says "I want to meet it head on"; slide 7 Say opens "I want to meet it head on" (verbatim, consecutive). Slide 9 Transition "Now the honest part" and slide 10 Say "Now the honest part" (verbatim, consecutive); slide 18 then says "the honest limit". Slides 15 and 16 both use the "pre-registered trial" analogy.
Fix:
- Slide 6 Transition: "Fair question: why hand this to an agent at all, when we already automate with scripts?"
- Slide 7 Say: "We already automate things. Why hand this to an agent instead of writing a script?" (drop the repeated lead-in)
- Slide 9 Transition: "Those are good numbers, from someone else's repositories. The question to ask next is what happens when it is wrong."
- Slide 10 Say: "I have shown you a good result. This will sometimes be wrong, and a pilot that cannot survive being wrong is not worth running. Here are four ways it fails."
- Slide 15: delete the "pre-registered" Analogy line; keep it on slide 16 only.

### 9. Slide 4 -> 5 hand-off asks a question the next slide does not answer
Problem: slide 4's Transition ends "So the question is who repays it", but slide 5 is the ask, and "who repays it" is not answered until slide 6. The audience gets a question, then a detour, then (3 slides later) the answer.
Fix, slide 4 Transition:
> "Repaying it by hand is the step that gets skipped when shipping is busy. Before I show the alternative, here is exactly what I will ask you for, so you can judge everything that follows against it."
Slide 5 Transition stays; it already leads into slide 6.

### 10. Slide 12 title is too long to say, and its job (the turn) is unclear
Problem: "The same file also grants bash, web fetch and a network allowlist, so the other limits matter" is 17 words and "the other limits" is vague. It is the deck's best tension beat (tidy file -> it can run shell commands -> so the write split matters), but the title buries the beat.
Fix:
> "The same file also lets the agent run commands and fetch pages, so the write limit has to hold"
(Every term is on the slide: bash, web fetch, allowlist, write limit. No new claims.) Keep the Say as is.

### 11. Slides 19-25 and 28: appendix notes have no Transition (root rule: exactly one); 26-27 use an ambiguous one
Problem: slides 19, 20, 21, 22, 23, 24, 25 and 28 end with Questions or Sources and no Transition. Slides 26 and 27 end "Back to the question you were asked." which a presenter cannot resolve under pressure (which question?).
Fix: add to each appendix note a one-line Transition "Back to the decision slide (18)." (or "Back to the slide you came from.") and replace 26/27's line with the same sentence. Slide 27 is also duplicated by slide 14's "Algebra" paragraph; delete the Algebra line from slide 14's note and keep it only on slide 27.

### 12. Appendix 2, 4 and 5 (slides 20, 22, 23) restate or empty out the main talk
Problem: slide 22 ("Use agents where interpretation adds value") repeats slide 7's script-versus-agent point and its Q&A; slide 20 repeats slide 7's "third pillar" source and the same Q&A ("Why not just script the docs update?"). Slide 23 is a TODO shell with a template command (`gh aw add-wizard owner/repo/workflow`) and is labelled "Template, not runnable". In a mixed room, appendix slides that say little can read as unfinished work.
Fix: no new content; mark slides 22 and 23 in the notes as "Do not present unless asked" and add a TODO in slide 22's note to merge it into slide 7's Q&A. Slide 7 note: change "Why not just script it" Q to point to slide 20 instead of re-answering. Slide 23 stays a TODO until the real workflow reference is supplied; do not show an install line as runnable.

## Smaller items (not ranked)
- Slide 14 Detail says the agentic step "defaults to a 20-minute timeout"; slide 12 shows `timeout-minutes: 15`. Add one clause to avoid a presenter mix-up: "the file sets 15; the default is 20".
- Slide 15 Say says "look, try, tune, decide" while the diagram says "review, try, measure, decide". Use the diagram's words.
- Slide 7 carries a visible TODO about whether CI runs on the agent's own PRs; the same unknown reappears in the slide 13 Q&A as "see the TODO on the script-versus-agent slide". It is a verifiable gh-aw docs check; resolve it once and delete both.
- Slide 1 Say roadmap says "end with a small proposal", but the ask appears on slide 5. Change to: "I will tell you what I am going to ask for early, then show the evidence, the controls and the cost."
- Slide 9 Evidence contains a third-person recount (4,034 / 2,688 merged, bot-authored). It is fine as a presenter-only note, but it is the only figure that points the other way and it is not on the slide; consider saying it aloud when asked "Will we get 96%?" so the answer is not just "not a forecast".
- Slide 2 caption on the PNG sits under the nav overlay in the screenshot only; not a content issue.

## What is working (leave alone)
- Hook echo: slide 18's closing line ties back to slide 1's question and its title-slide line. Keep it.
- Slide 8 -> 9 -> 10 handoffs (one PR is not evidence; here is volume; now what if it is wrong) are the best tension, turn, payoff run in the deck.
- Slide 11 to 12 to 13 (tidy file, the rest of the file, the write split) is the strongest honest-disclosure sequence.
- TODOs are kept visible and not invented; keep that.

---

## Lens: facts

# deck-v1 accuracy and credibility review (read-only; checked 18 Oct 2026)

Method: read all 28 slides of deck-v1/deck.md (main 1-17 incl. 09b, appendix 1-10) and the speaker notes; pulled the cited pages with curl/gh (gh-aw threat-detection, architecture, cost-management, safe-outputs-pull-requests, engines, blog 2026-01-13, update-docs.md from githubnext/agentics, PR github/gh-aw#68654, Stack Overflow 2026 survey data page, GitHub changelog 2026-06-11). Copies are in scratchpad/final/src/.

## Verified as correct (no action)
- Survey: "Information is outdated" 56.5%, 6,989 of n = 12,374, multi-select, question wording matches (survey.stackoverflow.co/2026/knowledge/data). 5,385 = derived, labelled in notes.
- Blog (13 Jan 2026): Daily Documentation Updater 57/59 (96%), Documentation Unbloat 88/103 (85%), Glossary Maintainer 10/10 (100%). The same post lists Noob Tester at 43% merge rate, so "most were merged, but not all" is fair.
- PR #68654: title "[docs] Update glossary - daily scan", +8 -0, 1 file, merged 2026-10-14, author app/github-actions; the two entries match the diff text. (Of the 8 added lines, 2 are blank and 2 are headings.)
- update-docs.md: matches the trimmed frontmatter; `timeout-minutes: 15`, `protected-files: fallback-to-issue`, bash comment quoted correctly. Note the real file also has `workflow_dispatch`, `labels`, a commented `engine: model: small` hint.
- Changelog 11 Jun 2026 public preview; Copilot CLI is the default engine; `draft` is "a policy, not a default, so the agent cannot override it at runtime" (safe-outputs-pull-requests).
- 1 AIC = $0.01; per-run default 1000 AIC; 20-minute agentic-step timeout.
- docs home: "A third pillar beside CI and CD", CI "Builds it", CD "Ships it", "Improving your repo, around the clock".

## Top 12 findings, ranked by impact

### 1. Slide 8 (risk), card 3 "Planted instructions - Limit: No write access" overclaims
Problem: A skeptical security engineer will say prompt injection is not bounded by "no write access". The same file grants `bash: true`, `web-fetch`, `toolsets: [all]` (slide 09b) so injected text can still influence what is read, fetched and exfiltrated within the network allowlist, and it can shape the draft PR text a tired reviewer approves. The slide also says "Each has a limit we set, not trust in the model", which is stronger than the notes' own "bound them, not prevent them".
Evidence: threat-detection page "a threat detection job ... identify prompt injection attempts, secret leaks, and malicious code patches" (a layer); architecture: "even a fully compromised agent cannot directly modify repos" (writes only, not reads/egress). Deck's own notes: "Detection is a layer, not a guarantee".
Replace card limit with: "Limit: the agent job cannot write to the repository directly; its output is checked and a person reads the diff." Replace takeaway with: "Each has a limit we set; none is a guarantee, so a person still reads the diff."

### 2. Slide 15/Appendix 10 and slide 11 notes: "official sources disagree on the daily AI-credit cap" is stale or unsourced
Problem: the cost-management page now states a default plainly: "1000 AI Credits per workflow run, and 5000 AI Credits per workflow per day (24-hour window)" and "When omitted, the guardrail inherits the default daily limit (5000 AI Credits unless overridden)". The deck claims a conflict exists, but never names the conflicting source. Either the conflict is real and the second source must be cited, or the fact can go back on the page with its date.
Evidence: https://github.github.com/gh-aw/reference/cost-management/ (fetched 18 Oct 2026).
Replace (Appendix 10 todo): "Unresolved conflict: whether a failed detection run blocks safe outputs. Daily AI-credit cap: 5000 AIC per workflow per day per the cost-management page (18 Oct 2026); re-check before presenting." Or, if you can name the contradicting page, cite it by URL on the slide.

### 3. Slide 10 (run pipeline): "Stages 1 to 3 hold no write permission" and title "The agent job has no write access" go beyond the source
Problem: the architecture page says the agent job "runs with minimal read-only permissions" and that the detection job "has no access to write permissions". It says nothing about the prepare/activation job's permissions (in real compiled workflows activation can post reactions/comments). The diagram makes a flat claim for stages 1-3 and the title adds an absolute. Also the diagram says "Role + permissions", and a skeptic will ask about the safe-outputs job's token scope, which is "minimal scoped" but not specified.
Evidence: architecture: "The agent job runs with minimal read-only permissions, while write operations are deferred to separate jobs that execute only after the agent completes."
Replace title: "The agent job is read-only; repository writes happen in a separate, scoped job". Replace the diagram label with: "The agent and detection jobs are read-only". Drop the "Stages 1 to 3" statement unless the compiled `.lock.yml` is inspected (none exists for deck's own workflow).

### 4. Slide 9 / 09b / 14: "docs only" and `protected-files` are described as "unconfirmed", but the docs do define it, and the real meaning undermines "docs only"
Problem: the notes and slides say what `protected-files` enforces is unconfirmed (TODO). The safe-outputs-pull-requests page defines it: values include `request-review` (default), `fallback-to-issue` ("push branch, create review issue if protected files modified"), and protected files are "the standard manifest and protected-directory set" (e.g. package manifests, AGENTS.md, hidden config directories). It is a supply-chain guard on sensitive files, not a docs-only path restriction. Also unmentioned: `max-patch-files` default 100 and `max: 1` PR per run default, which are the real mechanical bounds on the "too wide a diff" risk (slide 8 card 2). A skeptic asks: "can it edit .github/workflows or source?" Nothing in this file restricts paths (`allowed-files` exists but is not used).
Evidence: https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/ (Policy Options; Patch limits).
Replace slide 09b annotation 3: "A guard that routes changes to sensitive files (manifests, config) to a review issue; it does not restrict the PR to docs." Replace todo: "TODO: add `allowed-files: docs/**` (or equivalent) to the pilot copy if 'docs only' is to be enforced; confirm in a trial." Slide 8 card 2 limit: "Draft PR; patch-size limits; docs-only by instruction (not enforced)".

### 5. Slide 6: "a reviewer can judge it in minutes" and "real pull request" as proof of review size; the PR does not demonstrate drift repair
Problem: the claim "unit of review is one small diff" is generalised from n = 1, and the diff adds two dense glossary entries describing a new feature; it is documentation of new code, not correction of stale docs, which is the deck's headline problem (slides 2-3). Also "eight added lines" counts two blank lines and two headings. The notes say this, but the slide takeaway does not carry it.
Evidence: gh pr diff 68654 (2 headings, 2 paragraphs, 2 blank lines, 1 trailing blank).
Replace title: "One example of a documentation agent's pull request: two glossary entries in one file". Replace takeaway: "One example, not a rate: it adds new text; it does not show the agent repairing drift."

### 6. Slide 7 (evidence): bar sample is cherry-picked, and the kept caveat is thin
Problem: the post lists many documentation workflows; the slide shows the three best (96, 85, 100%) and the post's Noob Tester is 43%, Multi-device 100% on 2. Slide says "Selected samples" which is good, but the notes' claim "same post includes others with lower merge rates" is not on the slide. Also notes say "4,034 PRs, 2,688 merged" bot-authored recount: that is a derived number (66.6%) presented beside source numbers and is not on the slide; keep it out or label "our recount". The post does not identify the repository, which the slide hides.
Evidence: blog 2026-01-13, "Documentation Noob Tester ... 9 merged PRs (43% merge rate)".
Replace takeaway: "Three of the better-performing workflows in GitHub's own report (others in the same post are lower, e.g. 43%); a forecast for nothing of ours." Add to caption: "reported by GitHub, repository not stated, not independently verified".

### 7. Slide 1 and Slide 4: "AI that suggests" vs "AI that does", and "Agents shift the human role from execution to review" are framing claims with no source
Problem: kicker "FROM AI THAT SUGGESTS TO AI THAT DOES" is a slogan implying capability the pilot (draft PRs, human merge) does not exercise, and "the work moves from writing to judging" is this deck's thesis stated as fact in the title. Fig. 2 is labelled "Illustrative, this deck's framing", which is good; the title is not.
Replace kicker: "FROM AI THAT SUGGESTS TO AI THAT PROPOSES, WITH A PERSON DECIDING". Replace slide 4 title: "An agentic workflow hands the human a prepared change to review".

### 8. Slide 3 / Appendix 2 / notes: "Documentation debt" and "Fig 1" presented as mechanism
Problem: the chart is flagged illustrative (good) but the title "Documentation debt accrues between doc passes" is a causal claim with no data (the survey measures perceived barriers, not accrual). Cunningham's 1992 OOPSLA experience report is about technical debt, not docs; the extension is the deck's own.
Replace title: "Documentation can fall behind code between doc passes (illustrative)". Keep caption.

### 9. Slide 5 TODO is a visible unverified claim that is a real security question: does CI run on the agent's PRs?
Problem: the slide carries "TODO ... whether CI runs on the agent's own pull requests (the default GITHUB_TOKEN usually does not trigger workflows)". The safe-outputs-pull-requests page has an option (`github-token-for-extra-empty-commit: ${{ secrets.CI_TOKEN }}`, "push empty commit triggering CI") that answers exactly this; so the TODO is answerable from the docs now. The security-engineer challenge is "so the PR is merged without CI?"
Evidence: https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/ (frontmatter reference: "optional token to push empty commit triggering CI").
Replace todo: "By default PRs created with the workflow token do not trigger CI; gh-aw documents an optional token to push an empty commit that triggers it. Decide before week one."

### 10. Slide 12/13/14/15 consistency: "Draft PR" vs "person decides" vs "never merged automatically"
Problem: slides 4, 9, 14, 15 state "a person decides what merges" as a limit. Notes correctly say it is our pilot policy, not a product guarantee; but slide 14 draws it as the centre ring of "bounded risk" and slide 8 "Limit: A person reads the diff". Nothing technical (branch protection, CODEOWNERS, required reviewers) is named as enforcing it. Skeptic: "what stops someone merging unread?" Also there is a `merge-pull-request` safe output in the docs, so "no auto-merge" is a configuration choice.
Replace slide 14 centre label: "Merge is a human decision under our pilot policy (enforce with branch protection / required review)" and add a TODO "branch protection setting".

### 11. Slide 11 / 12 notes vs slide: stale/contradictory cost statements
Problem: slide 11 notes say "Careful wording: do not quote a default for the daily AI-credit cap ... The 1,000 AIC per-run default (about $10 estimated) is not on the slide", but the Detail/Evidence paragraphs of the same notes quote the 1,000 AIC / ~$10 default; they contradict their own warning. Also "1 AIC ≈ $0.01 estimated": the source states "One AIC equals $0.01 USD" and says AIC "maps to provider billing"; "best-effort" wording comes from elsewhere. Also the 20-minute default is the agentic step, while the shown file sets 15 minutes: say which applies. The detection job has its own default cap of 400 AIC (threat-detection page), not stated.
Replace note: delete "Do not quote a default for the daily AI-credit cap" or update it to "Cost page (18 Oct 2026) states 1000 AIC per run and 5000 per workflow per day defaults; we set our own". On slide caption keep "1 AIC = $0.01 (GitHub's unit; billing may differ)".

### 12. Appendix 5/6 and slide 15: command and starting point presented near-runnable
Problem: Appendix 5 takeaway `gh aw add-wizard owner/repo/workflow` is a template; ok, labelled. But slide 15 proposes `githubnext/agentics workflows/update-docs.md` "Candidate, a public third-party template" and the file triggers on every push to main, with `bash: true` and `toolsets: [all]`, i.e. higher privilege than a docs pilot needs. Skeptic: "you propose adopting an upstream file with broad tools into our repo". The deck acknowledges "adapt and narrow" only in notes. Also slide 15 status "Public preview ... features and defaults can change" is right and should stay.
Replace slide 15 left text: "Candidate starting point (public template, not our repository): githubnext/agentics workflows/update-docs.md, narrowed before use: fewer tools, narrower trigger, path-limited outputs."

## Other checks and smaller flags
- Slide 1 title page: the loop shows "OPEN PR - Writes checked before they land" (diagram step text): "checked" is detection-as-layer; fine with the existing "layers, not a guarantee" caption, but the slide itself carries no caveat. Notes handle it.
- Slide 9 notes: "Can the agent change its own permissions or turn off draft? A: Not at runtime." Supported for `draft` (source). For permissions it rests on compilation; reasonable but not directly sourced; add "(draft: per PR policy page)".
- Slide 9 notes: "It runs on every push to main; ... week one's staged preview shows the volume". Staged mode still costs (stated). Good.
- Slide 10 Fig 5 caption "Detection defaults to a caution, not a block": correct per `continue-on-error` "When true (default), detection warnings/failures produce a caution notice instead of blocking safe outputs", while "If the detection process itself fails ... safe outputs are not applied" is also on the page. The deck's "disputed" framing is accurate; it should say "the page says both" on the slide, not "disputed in the docs" (reads as an accusation).
- Appendix 7/staged: matches docs; nothing to change.
- Appendix 10 "re-checked 18 Oct 2026" while most slides' notes say "checked 17 Oct 2026". Mixed dates are fine but be consistent in what was re-verified; the cost page changed (finding 2).
- Notes call `gh aw trial` default "temporary private repository"; project CLAUDE.md says it retains a host repo `gh-aw-trial`. Appendix 6 notes say "Confirm cleanup rather than promising..." which is correct; the slide text "Temporary private repo by default" may read as auto-deleted. Replace with "Private host repo (kept unless deleted)".
- Un-sourced: Saltzer and Schroeder (1975) "least privilege", Bezos 2015 letter, Cunningham 1992: accurate attributions, appear in notes/captions only; fine.
- Title-slide hook "When did a page of documentation last mislead you?" is a question, no claim.
- Nothing in the deck links the private example repo; no invented repo/workflow names found (update-docs.md, glossary PR are real).
- Placeholders: "tool name / what it did" (slide 2b), thresholds, budget, repo, owner are all marked TODO with dashed `.gap` chips; no placeholder reads as a real workflow or result.

## What a skeptical security engineer would ask, by slide
- S4: "Where does the agent's token come from, what scopes?" (not shown; Copilot auth). S8: "Show me the injection test." (none). S9: "`permissions: read-all` is broad: it reads every repo secret-free but also private content, and `web-fetch` can leak it." S10: "Prove stage permissions from a `.lock.yml`." (none exists; deck never says so). S13/14: "What is the kill switch and who holds it?" (owner TODO). S15: "What is approved: the template or our adapted file?"

---

## Lens: visual

# deck-v1 visual design review (read-only, all 28 slides viewed)

Slide numbers are the Marp page numbers (page 11 = "09 / The workflow", page 16 = "13 / Decision rule", page 18 = the dark decision slide). Fixes use tokens and existing classes only. Nothing was edited.

## Overall verdict
The deck is clean, consistent and accessible, and it has real craft in places: the waffle strips (p9), the annotated file (p11), the nested-limits diagram (p17) and the title slide. The weakness is sameness. About 15 of 28 slides are "kicker, title, one gradient card row, blue callout bar, grey source line", and the callout bar fires on nearly every slide, so nothing is the loudest thing. Diagram labels also run under the 18px rule, and the right margin drifts between slides.

## Top 12 findings, ranked by impact

1. **Cards and callout bar are used on almost every slide (pp 3, 5, 7, 10, 14, 19, 22, 23, 24, 28; callout on 4-9, 13-17, 25).**
   Problem: the same top-border gradient card plus the same left-bar gradient callout appear on slide after slide, so the deck reads as a template and no slide has a focal point. The appendix slides 19, 22, 23, 24 and 28 are the worst: a title, a card row, a callout, then 200px of dead space.
   Fix: make the callout a rationed device, at most one per slide and only on claim slides. On slides 19, 22, 23, 24 and 28 drop the callout and turn the card row into a real diagram (see 9). Drop the gradient on non-hero cards: use a flat `--surface` fill and keep the top-border and gradient treatment for the one card carrying the slide's idea. Vary the scale: one slide per section should be a single big object (a stat, a diagram or a file) rather than cards.

2. **Diagram labels sit under the 18px floor at slide scale (pp 4, 6, 13, 15, 17, 20, 21, 26).**
   Problem: measured by eye against the 1280px render, these are about 13-16px: the chart labels on p4 ("doc pass", "cumulative changes", "time (no scale)", "documentation debt"), "replaced by" and the row captions on p6, "Prepare", "Agent", "4 of 6 documented jobs shown" and "if permitted" on p13, "PROPOSED FOUR-WEEK PILOT" on p15, "default: continue-on-error: true" on p21, and the "agent holds no merge decision" captions on p26. On a projector they vanish.
   Fix: in each `img/*.svg` raise `.t` and `.tm` to at least 18px (caption/tm tier) and keep the 22-24px tier for box titles. Where text no longer fits, cut the caption rather than shrink it. The p13 mono labels ("Prepare", "Agent") are the first to cut, since the box title already says it.

3. **Right edge and left edge drift (pp 9, 16, 17, 20, 26, 27, 6).**
   Problem: content ends at x=1212 on card slides but at ~1190 on p9, ~1187 on p16, ~1197 on p27, and ~1099 on p17 (a 110px dead strip on the right). SVG diagrams start at x=80 while titles start at 68 (pp 6, 20, 21, 26). Charts on p4 and p15 float centred under left-aligned titles. The eye reads this as unsteadiness.
   Fix: give every diagram the same viewBox width as the text column (1144px) and zero internal side padding, so its leftmost box edge lands on x=68 and its rightmost on x=1212. Make `.gates` (p16) and `.strips` (p9) fill the full column. Re-centre or widen the p17 rings to 1144 and let the labels follow.

4. **The decision slide (p18) is dark but not yet custom.**
   Problem: it has the right bookend colour, but the layout is a plain two-column text block with a lot of thin grey uppercase labels ("PROPOSED STARTING POINT", "TO DECIDE BEFORE WEEK ONE") that are low contrast at about 24px weight 300. The right-hand third and bottom are empty, the title is the only large element, and nothing echoes the title slide's glow or loop. The ask from p5 (4 weeks, 1 repo, docs only, draft PR) is not restated as the visual.
   Fix: put the four ask values as a horizontal strip of dark cards (the p5 stats, in `--accent` purple numerals) between the title and the lists, so the slide closes the loop the title slide opened. Make the two list labels 20px, weight 600, full-contrast `--muted` on dark. Give the checklist boxes a larger 28px hit and align TODO chips in a single right column. Add the same soft radial glow behind the title that the Octocat has on p1, but still none on rules or boxes, per the rule.

5. **Title slide (p1): strong image, weak left column.**
   Problem: there are two stacked rules (the short bar at y=453, then a second dash in front of the purple kicker), the hook question is 24px weight 300 and orphans "you?", and the gap between the title and the rule is larger than the gap between rule and kicker, so the three lines at the bottom read as an afterthought. The loop is purple-only, which is right, but the six labels are about 16px.
   Fix: delete the standalone bar and keep only the kicker dash (or the reverse). Pull the title down 24px so title, kicker, hook form one group. Set the hook in 28px with `text-wrap: balance`, or shorten it ("When did documentation last mislead you?") so it breaks cleanly. Raise the loop labels to 18px.

6. **Caption, source and TODO lines stack into a grey wall (pp 5, 6, 7, 9, 10, 13, 14, 15, 16).**
   Problem: up to four layers sit under the content: callout, "Fig. N" caption, TODO line (with its own rule), source footer, then the page number. They are all the same grey at nearly the same size, so the one that matters (the caveat) is not distinguishable. On p7 the TODO paragraph is long and wraps to two lines at 20px. On p6, p9 and p13 the Fig line crowds the footer (about 30px apart). Figure numbering also skips (Fig 1, 2, 4, 5, 6a, 6, 7...).
   Fix: one caption tier only: merge "Fig. N" into the footer source line on the left, and keep a single TODO line, never both a Fig line and a TODO line above the footer. Shorten the p7 TODO to one line and move the rest to notes. Renumber figures, or drop "Fig." numbers on slides that reference nothing by number.

7. **Same idea, two visual treatments for the annotated file (pp 11 vs 12).**
   Problem: p11 uses numbered circle badges inside the code and a matching badge list, which is the best slide in the deck. p12 uses `# 1`, `# 2` comments in the code and plain "1 ·" text on the right, with no badges and no highlight bands. The code card on p25 sits lower than its list (code top 293 vs list top 258). They look like they were made by different people.
   Fix: reuse the p11 `.mark` badge and highlight-band classes on p12 and p25 (remove the `# 1` comments). Top-align the code and the annotation column using the same `align-items:start` as p11. Also p11's footer ("Real file, trimmed (…) · githubnext/agentics update-docs.md · PR policy") runs into the page number; shorten it to "Trimmed from githubnext/agentics update-docs.md".

8. **Chart p4 and the nested boxes p17 have low-contrast structure.**
   Problem: p4 plots a good idea at small scale: the hatched "documentation debt" area is a faint tan, its label is brown at about 13px, and the chart occupies only 60% of the width. On p17 the five ring fills are nearly the same pale grey, so the nesting is carried by hairlines alone. Both use the caution/brown tone or hairlines for important information.
   Fix: p4: widen the plot to the full column, make the debt area a stronger `--accent` hatch at 18% and the label `--accent` text at 20px, and move the "ILLUSTRATIVE · NO DATA" tag into the corner of the plot. p17: step the ring fills in clear tonal increments (white, then four steps of `--surface`, then accent-tinted core) and set ring labels in 20px `--text` at weight 600.

9. **Sequences without arrows (pp 19, 24, 5) and weak visual metaphors (pp 7, 22, 28).**
   Problem: p19 (Author, Compile, Publish) and p24 (Select, Trial, Inspect) are sequential but laid out as plain cards with no connectors, while p16 uses arrows for the same job. p7, p22 and p28 are two text cards each with no visual: a non-technical viewer gets no "at a glance" read.
   Fix: use the p16 gate pattern (numbered badge, arrow between cards) for p19 and p24. For p7 make the two cards a decision fork: one question at the top and two result branches, reusing the p21 connector style. For p22 merge into a single two-column "keep in CI / hand to agent" table with the p20 lane look. For p28 use a plain list of sources with dates, because cards promise structure that is not there.

10. **Caution colour is overused on p21 and the TODO chips fight the content on p14 and p27.**
    Problem: p21 shows two tan dashed boxes plus a tan "default" label, which breaks "reserved caution token at most once per slide". On p14 the "NOT MEASURED" chips are 24px bold and heavier than the card titles above them, so the eye lands on the absence of data. p27 repeats six chips in the table.
    Fix: p21: keep tan only on the "Warning / failed check" box and make "Threat detected" a plain dashed neutral box with a ? marker. p14 and p27: shrink chip text to 18px weight 600 and use outline-only (no fill) so the labels above stay dominant; on p14 collapse the four identical "NOT MEASURED" chips into one line below the equation row ("Nothing measured yet") and let the equation breathe.

11. **Fine spacing and vertical rhythm (pp 6, 10, 15, 16, 25).**
    Problem: p6 and p10 stack diagram or cards, callout, Fig line and footer with 10-12px gaps, while p14, p19, p22, p23 and p24 leave 150-200px empty at the bottom. The p6 diagram starts 20px below a two-line-title-height gap, so the title and diagram feel pasted together. p15 draws a connector line that runs into circle 4 and ends in an arrowhead, and p13's arrow between boxes 2 and 3 is short enough that the head overlaps box 3.
    Fix: add a `--gap-block` token (28-32px) used above and below every callout. Vertically distribute short slides with `justify-content: space-between` on the content region (not centring) so empty space sits between groups. Lengthen the p13 connector by 12px, and stop the p15 line 8px short of circle 4.

12. **Kicker numbering and footer text are inconsistent (pp 3, 11, 12, 18).**
    Problem: kickers read 01, 01B, 02 ... 09, 09B, 10 ... 15, and the dark slide's "15 / THE DECISION" sits at page 18, so kicker number and page number never match and appendix kickers have a third scheme. Footer text length varies from nothing (p3, p15, p16) to a sentence that nearly collides with the page number (p11).
    Fix: either drop the numbers from kickers and keep section names (THE PROBLEM, THE ASK...) or number sequentially without "B". Cap the footer source at about 60 characters with ellipsis and move the full source to notes. Keep the footer on every slide for consistency.

## Slide-by-slide notes (one line each)
- 1: strong; see 5. 2: waffle plus stat works, but the grey caption line sits under the toolbar zone and 56.5% is the only slide-2 hierarchy; good.
- 3: placeholder, bottom half empty; acceptable as a TODO but it should not ship. 4: see 8. 5: four stat cards good, but "Draft PR" card has a three-line description, so row heights look uneven.
- 6: best diagram concept; labels too small (2). 7: text only (9). 8: diff block is all pale blue like a callout, with no +/- colouring, so it reads as a quote; give added lines `--good`-tinted rows or at least a gutter.
- 9: best evidence slide; right edge short (3). 10: good risk cards; limit text in link blue reads like hyperlinks, so use `--text` with the accent only on the "LIMIT" label.
- 11, 12: see 7. 13: good mechanism; tiny labels (2) and the duplicated "no write permission" header plus bracket, so keep just the bracket.
- 14: see 10. 15: see 11, and the circles read "1-4" not "Week 1-4", so add the word. 16: gates good, but the three top-right icons (tick, triangle, arrow-to-line) carry no clear meaning; drop them or use tick, minus, coin.
- 17: see 8 and 3. 18: see 4. 19-28: appendix is the most template-like part (1, 9); 20 and 26 duplicate the "who decides" message of 6 and 17; p26 could be cut or merged into p6.
