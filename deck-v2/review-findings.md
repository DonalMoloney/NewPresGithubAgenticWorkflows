# Deck v2: in-depth review findings (18 Oct 2026)

Raw reports from three read-only reviewers (story and notes, accuracy, visual design). Source-read plus screenshots; nothing here was applied unless deck-v2/todo.md says so. Re-check each item against the current deck before acting.

---

## Lens: story

# deck-v2 story, narration and notes review (read-only, 21 slides)

Slide numbers: 1 title, 2 stat, 3 nobody's job, 4 volume, 5 ladder, 6 earlier attempt, 7 what it is, 8 works, 9 risks, 10 write token, 11 blast radius, 12 thirteen lines, 13 the 98, 14 cost, 15 ask, 16 close, 17 audit, 18 compile, 19 triggers, 20 links, 21 status.

Overall: the spine is sound (stale page -> nobody's job -> pressure -> tool -> proof -> safety -> cost -> ask -> echo). Remaining weakness is in the last third (slides 12-16 carry the decision but are the most overloaded and most TODO-laden) and in note hygiene. The close does echo the opening, but loosens its wording and leaves the ask off the screen.

## Top 12 findings, ranked by impact

### 1. Slide 15 (the ask): two ideas, a 17-word title, and the ask itself is only TODOs
Problem: the decision slide holds the ask (3 yeses) AND the method (3 steps) AND baseline/measure/keep-or-stop. That is well over 90 seconds and the audience cannot tell which part to say yes to. The title cannot be said smoothly. Every field the presenter must speak is a TODO. The note also hard-codes "Callback to slide 2".
Fix: split into two slides. 15a "the ask", 15b "how we would judge it".
- 15a title: `## We need three yeses today: a repository, a reviewer and a budget`
  Body: the existing `.need` box enlarged, plus one lede: `One page, one repository, one month. Draft pull requests only; a person decides what merges.`
- 15b title: `## We decide keep or stop by a rule we set before the first run`
  Body: the existing steps row (Staged -> Draft PRs -> Reviewed) and the Baseline / Measure / Keep-or-stop cards.
- In the note replace "Callback to slide 2:" with "Callback to the stale-page slide:" (slide numbers shift).

### 2. Slides 15 note, 16: the close overclaims relative to the opening, and the ask is not on screen
Problem: slide 2 says "a page is **probably** one of those"; slide 16 says a page "is wrong right now" (and the slide 15 note says the same). The deck has no evidence of a wrong page; its own baseline is TODO. The deck's rule is never overclaim. Also the note says "restate the three asks in one breath" but the slide shows only a TODO page name, so the last thing the room reads is not the decision.
Replace slide 16 title with:
`## Somewhere in our docs, a page is probably wrong. In a month we can know whether an agent keeps it right.`
Replace the lede with:
`<p class="lede">The ask: a repository, a reviewer for every pull request, and a budget. The page: <span class="todo">TODO: name the real page or repo once chosen</span></p>`
Slide 15 note: replace `"a page is wrong right now"` with `"a page is probably wrong"`.

### 3. Slide 5 (and the 5 -> 7 gap): product named before it is defined; ladder not tied to the title's promise
Problem: slide 1's note says "don't name the product again yet", but slide 5's muted line says "gh-aw (GitHub Agentic Workflows) sits at L4" before slide 7 explains what it is. The room gets a code name and a research ladder (L1-L5) with no docs link. The subtitle's "from AI that suggests to AI that does" never reappears on screen. Also five slides (2-6) pass before the product is defined; with slide 6 likely cut, that is still four, about five to six minutes of setup for a mixed room.
Fix, slide 5 muted line, replace with:
`The tool in this talk sits at L4 in this deck's reading: the agent works, a person approves.`
Fix, slide 5 lede, replace with:
`The step this talk is about is the one from AI that suggests to AI that does. Low rungs: a person drives and the AI helps. High rungs: the AI drives and a person approves or watches.`
Optional pacing fix: slide 4 is the weakest link (its docs connection is explicitly "this deck's interpretation"). If time is tight, fold its two numbers into the slide 5 note and keep one slide for volume plus autonomy.

### 4. Slide 6 (earlier attempt): "similar" is undefined, and the slide is all TODO in the middle of the arc
Problem: "I built something similar before" arrives before the audience knows what the tool is, so "similar" has no referent. It is also the only slide with no plain-English line, numbers section or Q&A. Slide 5's note carries two transitions (the main one plus a conditional one).
Replace title with: `## I tried to fix this by hand before, and it showed me what was missing`
Slide 5 note: keep one `Transition:` line and move the cut-case into a line labelled `If slide 6 is cut:` so the note has exactly one Transition.
Slide 6 note: begin with `Plain line: this is not my first attempt at the stale-page problem.` Keep the day-of cut rule; it is correct and should be decided a week out, not on the day.

### 5. Slide 12 (thirteen lines): the most important sentence is in the smallest box
Problem: "Worst case: a poisoned page steers a draft a tired reviewer approves" is the honest payoff of the whole safety section, and it sits at 20px in a callout that also carries the "a lot of access" admission and the pilot changes (three ideas). It also quietly callbacks slide 3's tired reviewer without saying so.
Replace the `.turn` content with:
`A lot of access, but it all runs <em>inside the read-only, firewalled job</em>. The worst case is a plausible draft that a tired reviewer approves.`
Move "A pilot would add a bash allowlist and a schedule" to the slide 14 note (it is what makes the run count a number we control). In the slide 12 note add: `This is the same tired reviewer from the nobody's-job slide; the design does not remove them, it gives them a draft to read.`

### 6. Slide 14 (cost): the point is said three times and the title carries two ideas
Problem: title (ceiling set by us, run count is a line in a file), lede (what a month costs is a decision about frequency) and the `.turn` ("Both numbers are settings in the workflow file, reviewed like code") restate one idea. The title is 17 words.
Replace title with: `## A month's cost has a ceiling, and we set both numbers behind it`
Delete the `.turn` div (its sentence moves into the note as "Both numbers are settings in the workflow file, reviewed like code"). Keep the lede as is. The $300 arithmetic and the "ceiling, not a forecast" caveat are good; leave them.

### 7. Slide 8 (works): over 90 seconds, and the screenshot argues against the claim
Problem: stat, 59 squares, GitHub's caveat, then a screenshot of a different workflow with its own disclaimer, plus the "80 links left alone" aside in the note. Non-technical listeners hear 57/59, then are told the picture is not that workflow. The note also places "Outside evidence" between the Q&A and the transition, breaking the required order.
Fix: keep the stat and squares as the claim. Make the screenshot caption carry its job: replace the bold caption with
`A different workflow in the same repo, shown to see what a reviewable pull request looks like.`
Cap this slide at about 75 seconds: say the 57/59 and the caveat, point at the screenshot once, and move the "fixed 2, left 80 alone" story to a deliberate "if asked" line. Move the CNCF quote to just above the Q lines or delete it (a vendor-post quote is colour only).

### 8. Slide 9 (risks): two ideas, a wrong count, and risk 1 and 3 have no stated payoff
Problem: three risks plus a "Limit · Not a fit" card (a scope idea with a TODO). Risk 2 says "the next two slides show how" but slides 10, 11 and 12 all do (three). Risk 1's answer (draft: true) is not seen until slide 12; Risk 3's until slide 14. The room is told three worries and answered on one.
Fix risk 2 text: `...The agent is read-only and fenced in; the next three slides show how.`
Fix risk 1 text, add at end: `The file on slide 12 sets it.` (so the room knows when the answer arrives; shorter: `Shown in the file on slide 12.` but avoid slide numbers on screen, so use: `We look at the real file later.`)
Move the "Not a fit" card to the slide 7 note or a final-slide Q (the note already has the answer); that leaves three risks, which is the number the title implies.

### 9. Notes hygiene across the deck: missing plain-English lines, hard-coded slide numbers
Problem against the required order (plain line, technical, numbers+sources, questions, one Transition):
- No "Plain line" first on slides 1, 2, 6, 7, 9, 15, 17, 18, 19, 20 and 21. Several open with stage directions ("Pause after the title", "Be honest first", "The title is the whole idea"). Slide 2's note also buries the claim under a long TODO and a 2003 backup stat.
- Hard-coded slide numbers in notes will go stale as soon as slide 15 is split: slide 12 note "two slides back"; slide 15 note "Callback to slide 2", "slide 2's problem".
Fix: start each note with a single `Plain line:` sentence (slide 2: `Plain line: more than half of developers say old information gets in their way, and you have probably met one such page.`; slide 9: `Plain line: it will sometimes be wrong, so the design assumes someone checks.`; slide 7: `Plain line: an agentic workflow is a job your repo runs, written as a paragraph instead of a script.`). Replace numbered back-references with names ("the write-token slide", "the stale-page slide").

### 10. Slide 10 (write token): mixed metaphor and an absolute title
Problem: the teammate model uses "outbox", but the lede introduces a postbox and a key ("the teammate drafts the letter; someone else holds the key to the postbox"), so the room learns a second metaphor for the same thing. The title says "never holds"; the deck's own rule is never to overclaim safety.
Replace the lede with:
`The teammate drafts into an outbox. A separate, checked job, not the teammate, holds the key that sends it. The key is the write token: permission to change things.`
Replace title with: `## The agent job holds no write token: a separate, checked job does the writing`

### 11. Slide 11 (blast radius): an open security question on screen, and too much for one beat
Problem: three layers, three proxies, a dashed gateway, a code excerpt and a visible TODO ("can an allowlisted domain still receive data?"). A security-minded person will read the TODO as the answer being "yes". It is also a "sealed room" analogy that is new, not the access badge from slide 7. Likely 100+ seconds.
Fix: resolve the allowlist question before the day. If it cannot be resolved, move the TODO to the note and say it aloud as a limitation (the note already phrases it carefully). Replace the note's plain line with:
`Plain line: the access badge also limits where the teammate can reach: only the addresses on a list we write, and someone else holds the keys.`
On screen keep the code excerpt and the diagram; drop the `.todo` paragraph once it is a spoken caveat.

### 12. Slide 13 (the 98): the library is disconnected from the one-page ask
Problem: 98 gets the loudest number in the "What I've built" section, then the ask is for one page. The note's answer to "Why 98 not 4?" is weak and the slide's two TODOs (time taken, public yes/no) are the questions the room will ask. The "6 shared modules" line is said again in the note (say each fact once).
Fix: replace the muted line (remove the modules sentence) with:
`The ask on the next slides is one workflow, not 98.`
Keep the six-module detail in the note only. Decide the "how long did this take" sentence before the day; unanswered it makes 98 read as padding.

## Hand-offs (tension -> turn -> payoff), one line each
1 -> 2 good (promise, then the page). 2 -> 3 good. 3 -> 4 fine but 4 is the least necessary. 4 -> 5 abrupt (volume then a research ladder; see 3). 5 -> 6 weak, depends on a TODO. 6 -> 7 depends on a TODO transition. 7 -> 8 good. 8 -> 9 good. 9 -> 10 -> 11 -> 12 good, the best run in the deck. 12 -> 13 good ("I have already written ninety-eight"). 13 -> 14 good (cost before ask is deliberate and paid off). 14 -> 15 fine. 15 -> 16 good echo, see 2. 16 -> 17 fine.

## Timing for a mixed room (flagged slides over ~90 seconds)
- Over 90 s: 8 (stat + squares + screenshot), 11 (three layers + TODO), 12 (code + four annotations + worst case), 15 (ask + method + measures; split it).
- Borderline: 13 (funnel plus two TODO answers), 9 (four cards).
- Under 45 s each: 2, 3 (but pause), 4, 5, 10, 14, 16.
- Rough total of the main talk (slides 1-16, with 6 cut and 15 split): 18-22 minutes.

## Items I checked and found fine
- Titles are full-sentence claims throughout; notes exist on all 21 slides; each ends with one Transition except slides 5 and 6 (see 3, 4) and 21 ("none", correct).
- Careful-wording warnings (continue-on-error, staged is not a sandbox, merged is not correct, draft: true per workflow) are all present in the right notes.
- No invented numbers found; the remaining TODOs are the real open ones.

---

## Lens: facts

# deck-v2 accuracy and credibility review (read-only, checked 18 Oct 2026)

Method: read deck.md (all 21 slides + notes), sources.md; re-fetched gh-aw architecture, threat-detection, network, tools, safe-outputs-pull-requests, cost-management pages, the 13 Jan 2026 gh-aw blog, the 13 Feb 2026 GitHub Blog post, the Octoverse post; read update-docs.md (githubnext/agentics), link-checker.lock.yml (agentics) and daily-doc-updater.md (github/gh-aw) via `gh`.
Confirmed OK (no action): 43.2M PRs/month +23%, ~1B commits +25.1% (Octoverse text matches); 57/59 and 10/10 (blog text matches); "never merged automatically", "low-risk outputs" and "Treat the workflow Markdown as code" quotes; "do not replace build, test, or release pipelines"; `draft` is "a policy, not a default"; 1000 AI Credits/run; `continue-on-error` default true; "leaked by design"; MCP gateway "not a strong security boundary"; update-docs.md frontmatter matches the trimmed slide-10 listing. Not re-checked this pass: the 56.5% survey figure (survey page did not return text to curl; ledger says verified 17 Oct).

## Top 12 findings, ranked by impact

### 1. Slide 12 (and 16 note) - the 57/59 source workflow now auto-merges; the deck frames it as human-reviewed drafts
Problem: Slide says "people reviewed what it proposed and merged almost all of it" and pairs the stat with "draft PR / never merged automatically" framing. The Daily Documentation Updater lives in github/gh-aw (`.github/workflows/daily-doc-updater.md`). Its current frontmatter has `create-pull-request: auto-merge: true, draft: false, expires: 1d, reviewers: [copilot]`. Commit "Add auto-merge support for safe-outputs.create-pull-request (#10890)" landed 2026-01-20, one week after the 13 Jan blog. The blog post does not say who merged, and the workflow has since been configured to merge without a human. A skeptic who opens the file will say the headline evidence for "reviewed drafts" is a workflow that does the opposite. (`auto-merge` is not documented on the safe-outputs-pull-requests page; it exists only in the repo file/commit.)
Evidence: https://github.com/github/gh-aw/blob/main/.github/workflows/daily-doc-updater.md ; blog https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/ ("57 merged PRs out of 59 proposed (96% merge rate)").
Replacement (slide 12 lede): "A 96% merge rate for GitHub's own Daily Documentation Updater, as reported in Jan 2026. GitHub measured <em>merged</em>, not <em>accurate</em>, and the post does not say who reviewed them." Replacement (muted, slide 12): "gh-aw blog, 13 Jan 2026; reported by GitHub, small sample. That workflow's current file in github/gh-aw sets auto-merge: true, so today's merges may involve no human review." Replace the slide-12 speaker-note line "people reviewed what it proposed" with "the post reports they were merged; it does not say by whom." Add to note Q: "Is that the safe setup you are proposing?" -> "No. That is GitHub's own repo and config; our pilot stays draft-only with a named reviewer."

### 2. Slides 9/10 and run-jobs.svg - "Detection: permissions none" and "agent has no write" are contradicted by a real lock file
Problem: Slide 10 shows `detection: permissions: none` and `agent: permissions: read`, labelled paraphrased. The real compiled agentics file (link-checker.lock.yml) gives the agent job `contents: read, copilot-requests: write, issues: read, pull-requests: read` and the detection job `contents: read, copilot-requests: write`. The docs' own wording is "no write permissions" for detection, which is also loose. Title "The agent never holds a write token" is defensible for repo writes only; a security engineer will point at `copilot-requests: write` and call the snippet invented. Also the `conclusion` job (not drawn) holds `contents/issues/pull-requests: write`.
Evidence: https://raw.githubusercontent.com/githubnext/agentics/main/.github/workflows/link-checker.lock.yml (lines ~370-378 agent, ~1465-1474 detection, ~1724-1734 safe_outputs, ~1172-1188 conclusion). Architecture page: "agent execution never has direct write access to external state."
Replacement title: "The agent never holds a repository write token: a separate, checked job does the writing". Replace the paraphrased block with the verbatim excerpt (the TODO can now be closed): agent `permissions: contents: read, copilot-requests: write, issues: read, pull-requests: read`; detection `contents: read, copilot-requests: write`; safe_outputs `contents: write, issues: write, pull-requests: write`; caption "Verbatim excerpt, trimmed: link-checker.lock.yml, githubnext/agentics. copilot-requests lets the engine call the model; it does not write to the repo." Update run-jobs.svg's "no write token" row to "no repo write token".

### 3. Slide 9 snippet - `bash: ["gh issue comment"]` is a made-up-looking key, not shown in docs
Problem: The paraphrased block and the slide-11 note present `bash: ["gh issue comment"]` as how to limit bash to one command. The tools page confirms `bash:` accepts true/false/[] and "defaults to safe commands (echo, printf, ls, ...)"; I could not find a documented allowlist-entry example of that form in the fetched page text. It is labelled paraphrased, but it is also reused as the pilot's promise on slide 11 and 17 notes ("a bash allowlist"). If the form is wrong the pilot proposal is unbuildable as described.
Evidence: https://github.github.com/gh-aw/reference/tools/ ("Bash Tool (bash:) ... Defaults to safe commands").
Replacement: use a verbatim form from the Bash Tool section (confirm before use) or write `bash: [echo, ls]  # allowlist of command names` only after checking. Interim text: "Basic network only; bash restricted to a short allowlist (see the tools reference for the syntax)." Notes: change "`bash: ["gh issue comment"]` limits bash to that one command" to "bash accepts an allowlist of commands; confirm syntax in the tools reference before demoing."

### 4. Slide 11 - "A lot of access, but it all runs inside the read-only, firewalled job" overstates containment
Problem: `network: defaults` plus `web-fetch` and `bash: true` is a data-exfil and prompt-injection surface; the docs say the firewall limits egress to allowlisted domains, and sanitization only redacts URLs in outputs. "Read-only" is true for the repo token but the agent job still has `copilot-requests: write` (finding 2). The open TODO on slide 9 ("can an allowlisted domain still receive data?") is exactly what a security engineer asks, and the answer is yes in principle: the allowlist includes GitHub domains by default (the docs say the allowed list "includes GitHub domains by default"), so data can leave via an allowed domain.
Evidence: architecture: Squid "controls the agent's egress traffic via a configurable domain allowlist to prevent data exfiltration and restrict compromised agents to permitted domains"; network page "Content Sanitization ... to reduce exfiltration risk".
Replacement (slide 11 turn box): "A lot of access, held inside a repo-read-only job behind an egress allowlist. The outbox is the only write path; the allowlist narrows where data can go, it does not make exfiltration impossible. Worst case: a poisoned page steers a draft a tired reviewer approves." Close the slide-9 TODO with: "Possible in principle through any allowlisted domain; the docs describe the firewall as limiting, not eliminating, egress."

### 5. Slide 8 - "boxed in by layers" claim and the API-proxy line: align to the architecture page
Problem: Already corrected from the home-page "never sees them", good. Remaining: the svg alt text still reads "an API proxy that keeps the engine's auth token out of the agent's container" while the same page says the agent identifier is "leaked by design" and "rely on substrate isolation, network policy, and staged permission separation". Fine as-is on the slide, but the slide title "A misled agent is boxed in" over-promises given three layers each described by the docs as partial.
Evidence: https://github.github.com/gh-aw/introduction/architecture/ ("Treat this identifier as leaked by design").
Replacement title: "A misled agent is limited by layers, not stopped by any single wall". (Keeps the existing note.)

### 6. Slide 17 - $300 ceiling is not a ceiling
Problem: Title says "A month costs at most what we allow". The equation 30 x $10 = $300 omits: (a) `workflow_dispatch` and retries, (b) the detection job has its own credit budget (docs: detection budget defaults to 400 AI Credits, separate from the agent's 1,000), so per-run spend can reach ~1,400 AIC = ~$14, (c) AIC is "best-effort" and may not match the bill, (d) Actions minutes, (e) the daily cap is unresolved. Calling $300 a ceiling is a derived number presented as bound.
Evidence: https://github.github.com/gh-aw/reference/threat-detection/ ("Defaults to 400 when unset ... independent of the main agent budget"); cost-management: "1000 AI Credits per workflow run".
Replacement title: "A month's cost is bounded by two settings we choose: how often it runs and the per-run cap". Replacement term text: "Illustrative arithmetic, not a forecast: 30 runs x about $10 agent budget = about $300, plus the separate threat-detection budget (default 400 AIC, about $4 a run) and Actions minutes. AIC is best-effort." Mark "ceiling" -> "planning figure".

### 7. Slides 12 / 16 - "GitHub's own repos" / "small sample, merged is not correct" fine, but "GitHub measured merged" lacks a denominator window
Problem: 57/59 has no date window, no repo, no review info (ledger mismatch 4 recorded but slide still says "reported by GitHub, small sample"). Add the window gap and that the figure is from a vendor-authored post. Also the slide 16 note says "Do not present the 96% as a target we expect to hit" - good - but the slide-12 lede "our pilot will measure accurate" is a promise; the pilot slide's measure #1 is merge rate, which is the same flawed metric.
Replacement muted: "gh-aw blog, 13 Jan 2026; reported by GitHub (vendor post), no date window or repo given, small sample - merged is not the same as correct."

### 8. Slide 12 screenshot - real PR 394 is correctly labelled, but verify the "agent leaves 80 links alone" claim
Problem: The note presents "the agent reports about 80 other 'broken' links... changes none of them" as an observed fact in a captured PR. Not re-verified here; if the PR body differs, the best detail in the deck becomes a misquote. Also note: that PR is `githubnext/agentics` link-checker with `draft: false` (per the deck's own slide-9 note), so the slide shows a non-draft PR next to the "drafts" story.
Evidence: https://github.com/githubnext/agentics/pull/394 (open and confirm the "~80" and "fixed 2" wording before the talk).
Replacement: add to the on-slide label: "Not the docs updater; a link-checker run configured with draft: false." and in the note: "Re-read PR 394 before presenting; quote only what is in its body."

### 9. Slide 13 - "98 ... plain-English instruction files ... Checked for errors: 4" mixes self-report with a measurement
Problem: Slide column is titled "Checked for errors" and shows "4 compiled locally"; no `.lock.yml` is committed, so the only evidence is the repo's own agents.md. The source line does say self-reported, but the large "4" and "Checked" heading read as verified. The funnel "98 -> 4 -> 0" is a deck-drawn funnel; "0 ran" is "per the repo's own agents.md", not provable.
Evidence: project CLAUDE.md: "No .lock.yml is committed anywhere, so 'compiled' is a self-report".
Replacement column label: "Compiled (self-reported)"; text "4 compiled by me, no lock files committed to show it; the other 94 are briefs".

### 10. Slide 15 vs slide 9/10 - "never merged automatically" appears as Blog guidance on slide 9 but the experimental merge output and auto-merge key are not mentioned together
Problem: The deck correctly says "Blog guidance, not a hard limit", citing the experimental `merge-pull-request`. It omits the undocumented-in-docs `auto-merge:` key on `create-pull-request` (finding 1), which is a stronger counterexample. A skeptic will find it.
Replacement note line (slide 9): "Counterexamples exist: an experimental merge-pull-request output, and GitHub's own Daily Documentation Updater sets auto-merge: true. Our pilot would not enable either."

### 11. Slide 2 note / sources.md - unverifiable stat and survey framing
Problem: Slide 2 headline "More than half of developers say outdated information gets in the way..." fine (6,989/12,374 = 56.5%). But "Somewhere in our docs, a page is probably one of those" is an inference, flagged in notes. Keep. The note's 72.6% (n=12,996) is flagged TODO; ensure it is deleted from the note before the talk since it is in the repo's notes text, not just a TODO. Also the Lethbridge backup uses a course-hosted PDF.
Replacement: delete the 72.6% sentence from the note; keep only "TODO".

### 12. Slides 3/4 - "We ship more code than ever" and L4 placement
Problem: Slide 3 title uses "We" for GitHub-wide Octoverse totals; the slide never says it is platform-wide, and Octoverse reports "pull requests merged ... on average each month" platform-wide, not ours. Lede "each one can change what the docs should say" is interpretation (labelled in note, not on slide). Slide 4 "gh-aw sits at L4" is labelled interpretation: fine.
Replacement title (slide 3): "Developers on GitHub now merge 43.2 million pull requests a month". Add to lede end: "(platform-wide, not our repo; the link to stale docs is this deck's interpretation)".

## Other checks (lower priority)
- Slide 8 and 14 "four of six jobs": consistent with the architecture page; keep. The real lock also has `activation`, `conclusion`, `safe_outputs`, `update_cache_memory`: say "four of its jobs".
- Slide 6 "Is it safe?" cards: "Reported by GitHub: 'never merged automatically' is Blog guidance" good wording.
- Slide 18 pilot: "Merge rate measures agreement, not freshness" good; consider adding "reviewer minutes per merged PR" on-slide, not just in notes.
- Staged mode: "writes nothing" appears on slide 8-appendix and pilot; docs say "Staging is not a sandbox"; the slide 18 source line carries it. Fine.
- sources.md: ledger row for slide 9 "Detection job has no write access" is marked verified; add caveat "docs say no write permissions; real lock file shows copilot-requests: write and contents: read (see finding 2)".
- Placeholders: all TODOs are visible (amber). Slide 5 (earlier attempt) is an all-TODO slide; note already says cut if empty. Recommend cutting for the final deck if no content, since a skeptical room reads empty cards as unfinished.
- Date staleness: slide 15 / status slide says checked 17-18 Oct 2026; today 18 Oct; fine.

---

## Lens: visual

# deck-v2 visual design review (read-only; 21 PNGs viewed, toolbar pill ignored)

Overall: the system is coherent (section label, bold claim title, grey lede, cards, light-blue callout, amber TODO). Weak spots: diagrams are narrower than the text column on several slides, three slides are mostly empty, slides 2/16 break the left-aligned grid, and diagram text on 10/11/18/19 is small and uses a different weight/radius language than the HTML cards.

## Top 12 by impact

1. Slide 7 (what it is, the deck's core idea): the teammate map stops at x~940 of a 1136 column, leaving ~200px dead on the right, and the "Classic Action vs Agentic workflow" strip sits ~45px above the footer (tightest slide). Row labels (sub text ~16px) are under 18px. Fix: widen the SVG to the full column (viewBox width to ~1136, `width:100%`), move the two-line classic/agentic strip out of the SVG into a `.callout` under it or drop it into the lede; raise sub-labels to 18px+ and give each arrow a larger gap so the pairing reads left-to-right as "plain English -> file setting". Alternative balance: keep the SVG at ~62% width and put the 4-row legend (`--text`, mono keys) in a right-hand card, same pattern as slides 10-12.

2. Slide 5 (autonomy ladder): ladder is ~1000px wide and ends at x~1070 while the title/text run to ~1136; the dotted trend line peaks above the "MORE AGENT AUTONOMY" label and touches the lede area; the gloss line below it crowds the footer and the source line is 2 lines of 18px grey. L1-L3 and L5 are mostly empty boxes with 16px text. Fix: stretch the SVG to full width, give the trend line 24px clear of the lede (move label to the right end, not left), shrink step-box height differences so the bottom gloss has 32px air, and move the "gh-aw sits here" amber text to a pill/flag above L4 so the box body stays plain. Cut the gloss line (it repeats the claim and the source line already carries "this deck's interpretation").

3. Slides 6, 16, 20: 40-60% of the canvas is blank, which reads unfinished rather than intentional. 6 is TODO cards then a void; 16 (the ask) is a centred title floating with a small TODO; 20 has ~230px empty. Fix: 6 and 20 `align-content:start` is fine but add a fixed min card height or a single large `.stat`-style empty-state frame (dashed `--line-soft` border, 3 columns stretched to fill, `min-height:340px`) so the TODOs look like deliberate placeholders; 16 is the closing beat, so make it a true lead slide: title at ~56px, a big blue rule beneath it (reuse slide 1's `.rule` but blue only), the TODO page name set as a pill under it, and a faint large blue radial in the corner using the slide-1 glow token, so it echoes the title slide.

4. Slides 1 vs 2+: the title slide is dark navy neon, every other slide is flat white. The handover is abrupt and slide 1 is the only "custom" slide. Fix: add one echo on the white slides: a 2px `--accent` top rule across the full width (or the 28px section dash extended) and use the same Inter 800 title weight; on 2 and 16 add the glowing short rule from slide 1 in `--accent` under the title. Also slide 1's TODO pill is hard against the author name; add 16px gap and drop the pill below the name.

5. Slide 2 (hook number): centred title and lede break the left-aligned grid used by 3-21, and the 56.5% stat (~170px) overpowers the claim title; the lede is 3 centred lines at ~26px. Fix: left-align title, put the stat at left (~40% width) and the lede and sentence "Somewhere in our docs..." at right as a `.callout`, or keep centred but cap the stat at ~120px and set the lede to `max-width:30ch` so it is 2 lines. Consistent alignment with slide 3 matters because 2->3 is one continuous argument.

6. Slides 10 and 11 (safety diagrams): diagram text is 14-16px (sub-labels "no write token", "bash limited to", "token stays here") which fails the 18px floor at slide scale; slide 10's four rows have almost no vertical gap (row 2 dashed amber butts against row 1), and the lock icons are small. Slide 11 packs 3 nested frames, 7 boxes, a "?" badge and a dashed-dashed-solid border mix; the outer frame label "3 ONLY WHAT WE LIST" is the hardest to find. Fix 10: row pitch +12px, drop the "JOB / WRITE TOKEN" column headings into the SVG at 18px bold, bump sub-labels to 18px, shorten them. Fix 11: split into 2 slides if possible; otherwise remove the "?" badge (the amber TODO card on the right already carries the unknown), make the three layer labels the same size and number badges the same blue, and drop the MCP gateway amber fill to outline-only so amber stays reserved for TODO/caution consistently.

7. Slide 9 (four risk cards): all four cards are identical weight, so "Limit: not a fit" reads equal to "Risk 2: prompt injection". Card 2 has big empty space; card 3 is half empty; heights are forced equal. Fix: give risk cards a leading icon-less numeral token (`1`,`2`,`3` in blue circle like the diagram badges) and make the limit card a different style (`--surface` with dashed `--line-soft` border) so the 3+1 structure shows; trim card 1's second paragraph into the source line to equalise heights.

8. Slide 14 (cost equation): the x and = signs are 28px grey and float; the third card is highlighted but its TODO is jammed into the bottom (a 12px gap under "plus Actions minutes"). Cards in row are equal height with large dead space in cards 1-2. Fix: make operators 40px `--accent`, vertical-centre them to the card, add 12px margin above the TODO pill, and make the "30 x $10 = $300" the card's headline number (`.stat`-sized) so the sum is visible at a glance, not buried in sentence 3.

9. Slide 15 (the pilot): densest slide. Two rows of three cards plus a callout holding three TODO pills that wrap unevenly (gap between the first two pills, third pill squeezed) and a method label that floats between callout and cards. Rows are not labelled as rows, so "1 Staged -> 2 Draft PRs -> 3 Reviewed" then "Baseline / Measure / Keep or stop" read as one 6-card grid. Fix: add a thin `--line-soft` divider and row labels at left ("Run" / "Judge"), make the top arrows span only the top row, move the TODO pills in the callout to a flex row with equal `flex:1` and consistent gap, and set the callout's "What I need from you today" at 24px bold since it is the ask.

10. Slides 12 and 13 balance: 12's code card is ~570px wide with a right column of bullet markers (the only slide with default bullets, and the `# 1..4` comments sit far right inside the card); the callout is 5 lines. Fix: replace bullets with numbered blue circles matching the `# 1..4` markers (same badge style as slide 7/11), pull the `# n` comments in to column ~34ch, and cut the callout to 3 lines. On 13, the three big numbers are strong, but the amber TODO paragraph wraps across two lines as two orphan pills; render each TODO as its own pill on its own line, and add a bottom border under the card row so the TODOs do not look part of the grid.

11. Slide 8 (proof): good composition (waffle + screenshot), but the waffle is 11x5 with 2 empty cells that are easy to miss; the screenshot is cropped mid-table, border-radius ~6px vs card radius ~12px; two captions below the screenshot are separate paragraphs at the same grey as the source. Fix: label the 2 outlined cells with a small amber-free "not merged" tag in the SVG (18px), match screenshot `border-radius` to the card token, join the two captions into a single `.muted` pair separated by 8px, and align the stat's baseline with the screenshot top.

12. Appendix slides 17-21 (consistency): 17 has a code block plus a pull quote with a grey bar (the only quote style in the deck, and a different bar colour from the blue callouts); 18's diagram is small (~1000px wide, 18px mono) with a bracket and caption that is 14px; 19's diagram is 1000px wide of 1136 and the bottom third of the slide is empty; 20's URLs overflow the card (`...changelog/2026-06-11-githu` hard-wraps mid-word); 21 uses `--line` cards of unequal text fill. Fix: use the blue-bar `.callout` for the quote on 17; widen the 18/19 SVGs to full column and set captions to 18px; on 20 set URLs to `word-break:break-all` with 18px mono (or shorten display text to `github.blog/changelog/2026-06-11-...` with the full link in notes) so no hyphen-in-the-middle wrap; on 21 set all four cards to equal heights with `grid-auto-rows:1fr`.

## Cross-deck consistency findings (apply once, globally)
- Corner radii: cards ~12px, code ~10px, SVG boxes ~8-10px, screenshot ~6px, pills ~8px. Pick two (card 12px, inner 8px) and use tokens.
- Diagram stroke: boxes 1.5-2px, arrows 1.5px, dashed amber 2px. Normalise to 1.5px `--line`, 2px `--accent` for active.
- SVG label sizes: titles ~22px, sublabels ~15-16px, mono ~15px. Floor of 18px for subs, 20px for titles; where space does not allow, remove words rather than shrink.
- Blue is used for: section label, card `.k` label, stats, badges, rule, callout bar, code keys. That is fine, but the tinted callout and the highlighted card (slides 5, 7, 14, 18) use the same light-blue fill for "important", "mapped" and "generated"; give "emphasis" fill one meaning (the answer/the ask) and use white with blue border for the rest.
- Amber appears for TODO pills, caution (slide 10 dashed Check row, slide 11 gateway) and the "gh-aw sits here" label on slide 5. Per the rules amber is for unresolved/caution, but a viewer cannot tell a real caution from a TODO. Differentiate: TODO = dashed amber pill with the word TODO; caution = solid amber left bar with a text label "Caution".
- Footer/source line: sits at ~685px with 18px grey, wraps to two lines on 4/5/8/13/14/15, and collides with content on 7. Reserve a 72px footer zone (`section{padding-bottom:88px}`) and trim source text to one line where possible; move the qualifications into the notes.
- Right-hand dead space: lede and SVG widths on 3, 5, 7, 12, 14 stop at ~1050px while cards run to 1208px. Use one content width (`max-width:none` on lede) for cards and SVGs.
- Slides 6/9/13/20/21 are "four boxes" layouts; combined with 3/4/14/15 that makes ~9 of 21 slides card grids, which is what reads template-like. Break the rhythm by converting 9 (risks) to a left numbered list plus one large right-hand "limit" panel, and 21 to a plain two-column text slide without cards (it is an appendix reference).

## What already works (leave alone)
- Slide 1 (custom, glow, loop diagram); slide 8 (stat + real evidence); slide 12 (code + annotations); slide 13 (98 -> 4 -> 0 progression, the strongest at-a-glance slide in the deck).
- Slide 19's icon cards are the cleanest diagram style; use it as the reference for 10/11.
