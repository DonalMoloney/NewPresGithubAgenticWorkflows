# Deck v3: in-depth review findings (18 Oct 2026)

Raw reports from three read-only reviewers (story and notes, accuracy, visual design). Source-read plus screenshots; nothing here was applied unless deck-v3/todo.md says so. Re-check each item against the current deck before acting.

---

## Lens: story

# deck-v3 story, narration and notes review (read-only; 22 slides)

Method: read deck.md in full (did not open PNGs; no visual claims here). Slide numbers = order in deck.md. Ranked by impact.

Spine as it stands: 1 title | 2-3 stale docs + more code | 4 ladder | 5 earlier attempt (empty) | 6 turn | 7-11 what it is | 12-15 safety (4 in a row) | 16 evidence | 17-18 library | 19 ask | 20-22 appendix.
Opening/close echo: the opening ("a page is probably wrong, nobody knows which") is echoed only in the slide 19 NOTE, not on the slide. Fix #5.

## Top 12

### 1. Slide 14 (and its note): title says "three limits" but the diagram and note list four
Title: "...three limits narrow what they can do". Note and diagram: no write token, domain allowlist, opt-in tools, `max` cap per output = four. A technical listener will count.
Replace title: `Hidden instructions can reach the agent, and four limits narrow what they can do`
Replace note line 1 phrase "three limits narrow what it can do" with "four limits narrow what it can do".

### 2. Slides 14 + 15 repeat each other and the same amber TODO shows twice; four safety slides in a row (12-15)
Both slides list the limits, both show the open allowlist question, and the room sits through four consecutive safety slides with no proof between them (the v2 CLAUDE.md reordered precisely to avoid this). Fix, smallest first: (a) drop the TODO from slide 15's footer (keep it on 14 only, say it once); (b) move slide 16 (57/59 evidence) to sit between 12 and 13 so the order is: wrong+draft -> "does it work?" -> how the walls are built; or (c) merge 14 into 15 as a one-line lede ("Prompt injection means someone tricks the AI with hidden instructions in text it reads") and drop the separate path diagram.
Slide 15 footer replacement: `Documented: gh-aw architecture and network reference; the MCP gateway caveat is the docs' own wording.`
If (b): slide 12 transition becomes `Transition: so it is wrong sometimes and a person reviews it. Before the walls, the fair question: does it produce anything worth reviewing?` and slide 16's becomes `Transition: that is GitHub's number on GitHub's repos. Here is what keeps a misled agent from doing damage, starting with the token.`

### 3. Slide 4 (autonomy ladder) pre-empts the turn on slide 6 and its link to slide 3 is a non-sequitur
Slide 3 is about code volume; slide 4 introduces a second framing (L1-L5), and slide 6 then makes the same point again ("suggests" versus "does"). Two framings of one idea, and the ladder asks the room to learn five levels before they know what gh-aw is. The note claims "L4 is where the previous slide's volume argument lands"; volume does not imply autonomy, so that is an unsupported leap said aloud.
Best fix: move slide 4 to the appendix or after slide 6 (as "where this sits"). If it stays, replace the note sentence with: `The more code there is, the more tempting it is to hand the agent more of the work. This ladder is one published way to name how much, and L4 is the level this talk is about.` and change the slide 3 transition to: `Transition: so the question is how much of that work we hand over, and to whom.`

### 4. Slide 6 note contradicts itself in its first line
Plain line says "every AI tool we use today waits for a human to ask", then two paragraphs later "Do NOT say 'every AI tool waits to be asked' - it is false". The plain line is what gets said aloud.
Replace: `Plain line: the assistants we type at wait for us. You ask, it answers, and if you are not there nothing happens. This one has a trigger instead of a prompt, so the work happens whether or not anyone is at the keyboard, and your job changes from asking to reviewing.`

### 5. Slide 19 (the ask): the close does not visibly echo the opening, and the slide is over-dense
The callback to slide 2 lives only in the note. On the slide: five TODO boxes, a four-step timeline, an OPEN DECISION line, a source line. Likely 2+ minutes and it is the last thing the room sees.
Add the echo as the slide's first line (replace the `.k` label "What I need from you today: five answers I will not invent" or put above it as a lede): `Somewhere in our docs a page is wrong right now. Pick one, and find out.`
Keep the five blanks but cut the OPEN DECISION line on-slide to: `OPEN DECISION: pilot workflow, update-docs or readme-auto-updater.` (move the cost-per-run detail to the note, where it already is).

### 6. Slide 5 (earlier attempt) is an empty hinge and its hidden contract is fragile
All content is TODO and the note itself says the whole turn depends on beat 3 reading "it only ran when a person remembered to run it". Decide before the talk: either write it (3 sentences) or delete the slide and change slide 6's opening to `Transition (from slide 3/4): the old way needed someone to start it. What changed is not that the AI got smarter; it stopped waiting to be asked.`
Do not ship the strip empty; it is the only human moment, so writing it beats cutting it.

### 7. Slide 8 states the ask early and the slides after it forget it
"We are asking for one job, in the first box" is said on slide 8, then re-stated on slide 19 and in the status slide ("say each fact once"). Slide 8 should only make the "documentation is the safe corner" argument.
Replace the bold line: `**Documentation is the safest corner to start in.** A wrong answer there costs a review comment, not an outage.`
Note: delete the sentence "The ask is one job in the first box." Replace with "I will return to this at the end."

### 8. Slide 8 note names the wrong neighbours
It says "the two slides either side are a compiler and a trigger table". Either side of slide 8 are the teammate-model diagram (7) and the compile slide (9); the trigger table is slide 10.
Replace: `The slide before is a diagram and the slide after is a compiler, so slow down here and let the non-technical half of the room back in.`

### 9. Slide 11 title overclaims "the whole job"; slide 10 + 11 are the longest talking slides
Title "Thirteen lines say when it runs..." is accurate about the lines shown, but slide 10's transition says "Here is the whole job" and the slide is trimmed. Also slide 10 (four triggers, role gate, fork rule, schedule exception) and slide 11 (four annotated blocks, bash question) each run well over 90 seconds, and slide 10 interrupts the flow from "brief" (9) to "the file" (11). Fixes: swap order so the file (11) comes straight after compile (9) and triggers (10) follows it; or keep the order and trim slide 10's spoken part to: title, one sentence on the gate, stop (everything in the note stays as Q&A only).
Slide 10 transition replacement: `Transition: that is when it runs and who can start it. Now the file itself: the settings, trimmed, in thirteen lines.`
Slide 11 title replacement: `Thirteen lines of settings say when it runs, what it can read, and the one thing it can send`

### 10. Notes on slides 9, 11, 10 skip the required first item (plain-English line)
Slide 9 opens on a technical detail ("Below the frontmatter..."); slide 11 opens "This is a real file, trimmed"; slide 10 opens on the title. Required order is plain line first.
Slide 9 insert as the first line: `Plain line: you describe the job in a paragraph, and one command turns it into the format GitHub already runs.`
Slide 11 insert as the first line: `Plain line: this is the whole job description - when it starts, what it can read, and the one thing it is allowed to send.`
Slide 10 insert as the first line: `Plain line: four ways to start it; if a person starts it, their access is checked first.`

### 11. Slide 16 and the pilot repeat the "merged is not accurate" point three times
It is on slide 16 (card pair), slide 19's timeline, and the status slide. Keep the contrast only where it earns its keep (slide 16, the pilot slide); drop it from the status slide's bullet to a single reference. Also "A person clicked merge." asserts something the source does not state; GitHub counted pull requests merged.
Replace card text: `**Merged.** GitHub counted pull requests that were merged.`
Status slide bullet replacement: `This deck's choice of measure: the pilot counts accepted as accurate, not merged (see the evidence slide).`

### 12. Slide 17 opens oddly and the library takes two slides before the ask
Plain line "I didn't come here with a slide deck" reads strange aloud, and slides 17 and 18 both spend time on the library's maturity label (stated twice: "not one has run" and "Experimental, all 98"). Also slide 17's note ends "That last part is the ask", but the ask is one page for a month, not running 98.
Replace plain line: `Plain line: I have already written ninety-eight of these. Not one has ever run, and I would rather you hear that from me. What I am asking for is much smaller: one.`
Slide 18 note: delete the Q "Experimental means what, exactly?" answer's repeat ("Same honest line as the previous slide") and fold it into slide 17's Q&A.

## Other checks
- Exactly one Transition per note: yes on slides 1-21; slide 22 has none (backup, fine).
- Titles carry claims: yes throughout; slide 21 ("Try it yourself") is a label by design (appendix).
- Over ~90 s for a mixed room: 5 (if written), 10, 11, 14+15, 19. Under: 2, 3, 6, 8, 12.
- Mixed-room jargon aloud: "safe-outputs", "toolsets", "Squid proxy", "MCP gateway" are all in notes, not on titles; good. Keep "web filter" and "tool connector" on-slide as the note says.
- Title slide note says "Shape of the hour"; the arc omits the library slides (17-18). Add: `...what I have already built, and the one decision I want at the end.`

---

## Lens: facts

# deck-v3 accuracy and credibility review (read-only; checked 18 Oct 2026)

Slide numbers: 1 title, 2 stale stat, 3 volume, 4 ladder, 5 earlier project, 6 turn, 7 what it is, 8 three kinds, 9 compile, 10 triggers, 11 thirteen lines, 12 will be wrong, 13 write token (run-jobs), 14 injection, 15 blast radius, 16 evidence, 17 library 98, 18 spec, 19 ask, 20 debug, 21 try it, 22 status.

Sources opened: gh-aw docs (architecture, triggers, threat-detection, safe-outputs, safe-outputs-pull-requests, network, tools, cost-management, staged-mode, permissions, blog 2026-01-13), GitHub changelog 2026-06-11, GitHub Blog 2026-02-13, Octoverse 2025, arXiv 2506.12469 abstract, github/gh-aw source and compiled lock files via `gh api`, githubnext/agentics update-docs.md, DonalMoloney/Agentic-Workflows-Lib via `gh api`. Not re-checked: Stack Overflow 2026 (JS site), Lethbridge 2003.

## Top 12, ranked by impact

### 1. Slide 13 (run-jobs diagram + caption): "No write key in any of these three" is false for Activation
- Problem: the diagram strikes through the key on Activation, Agent and Detection and says only Safe outputs holds a key. In a real compiled gh-aw workflow the activation job holds `issues: write`, and the conclusion job (not drawn) holds `contents/issues/pull-requests: write`.
- Evidence: github/gh-aw `.github/workflows/daily-doc-updater.lock.yml`: `activation` permissions `actions: read, contents: read, issues: write` (line 96-99); `conclusion` `contents: write, issues: write, pull-requests: write` (1386-1390); `agent` read-only; `safe_outputs` `contents/issues/pull-requests: write`. Triggers docs: "the activation job posts a comment on workflow start and updates it on completion"; `reaction:` and `status-comment:` default ON for `slash_command` and `label_command`. Architecture page lists six jobs (Pre-Activation, Activation, Agent, Detection, Safe Output Jobs, Conclusion).
- Also: stage 1 label "Opens the shift / Checks inputs. Runs first." is wrong. The role check is in the separate Pre-Activation job, which runs first; Activation does context prep, event-text sanitization and lock-file validation.
- Replace the diagram claim and caption with: "**The agent job holds no write token; the jobs that write are separate and scoped.** The activation and conclusion jobs can post status comments; the safe-outputs job holds the write token for the draft pull request." Relabel stage 1 "Activation: Cleans the incoming text. Posts a status comment." and mention pre-activation (role check) as the step before it, or draw it. Replace the sub-label "No write key in any of these three" with "The agent and detection jobs hold no write key".

### 2. Slide 16 (evidence): "Merged. A person clicked merge." is unsupported, and the 57/59 came from a non-draft workflow
- Problem: the blog says only "57 merged PRs out of 59 proposed (96% merge rate)". It does not say who merged or how, and does not name the repository. The workflow's own config at that time said `draft: false`, which contradicts the deck's story ("every change arrives as a draft") and the pilot design. Its current config has `auto-merge: true` (feature added 20 Jan 2026, after the post). Also, the same blog table lists weaker rows (Documentation Noob Tester 43%, Slide Deck Maintainer 2 of 5, 40%); the deck cites only the 96%, 85% and 100% rows.
- Evidence: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/ ("57 merged PRs out of 59 proposed"; "Documentation Noob Tester ... 9 merged PRs (43% merge rate)"; "Slide Deck Maintainer ... 2 merged PRs out of 5 proposed (40% merge rate)"). github/gh-aw `.github/workflows/daily-doc-updater.md` at commit c93b63d (27 Dec 2025): `create-pull-request: ... draft: false`; current file: `draft: false`, `auto-merge: true`; commit 2026-01-20 "Add auto-merge support for safe-outputs.create-pull-request (#10890)". Inference that this is the gh-aw repo is mine (the workflow lives there; the post does not say).
- Replace the card: "GitHub measured: **Merged.** The post does not say who merged or how." Add to the muted source: "That workflow opened non-draft PRs (`draft: false`); it is not the configuration this pilot would use. Other docs workflows in the same post merged 40-43%." Cut the notes' "people reviewed what it proposed and merged almost all of it" to "almost all were merged".

### 3. Slide 14 (injection): title says three limits, diagram and notes list four; "opt-in tools" contradicts slide 11
- Problem: title "three limits" vs diagram "limited by four things" (no write token, allowlist, opt-in tools, cap) and the SVG desc says four; notes say "three limits" then name four. And "Only tools we turn on" sits two slides after a file with `toolsets: [all]` and `bash: true` (docs: `bash: [":*"]` "All commands (use with caution)").
- Replace title: "Hidden instructions can reach the agent, and four limits narrow what they can do". Replace limit 3 text with "Only the tools listed in the file (this example lists a lot)" or drop it. Add one documented limit the deck omits: content sanitization before the agent sees the text (activation stage: @mentions, bot-trigger phrases, XML/HTML tags, non-HTTPS URLs, 0.5 MB / 65k-line limit) and protected-file checks (dependency manifests, CI config, agent instruction files fail or go to review by default).
- Evidence: architecture page "Content Sanitization" section; threat-detection page "Default Remediation" ("Protected file protection is enabled by default for create-pull-request ..."); tools reference.

### 4. Slides 14-15 open question is partly answerable from the docs, and the answer is not comforting
- Problem: the deck says "no documented answer yet". The network page says: "GitHub domains (github.com, githubusercontent.com, etc.) are always allowed by default," and the sanitization allowlist "includes GitHub domains by default". So an injected agent with `bash`/`web-fetch` can reach GitHub hosts regardless of `network: defaults`; the allowlist narrows destinations but is not a no-exfiltration guarantee. The docs describe the Squid allowlist as intended "to prevent data exfiltration and restrict compromised agents to permitted domains", not as a guarantee.
- Evidence: https://github.github.com/gh-aw/reference/network/ (Content Sanitization section); architecture "Agent Workflow Firewall (AWF)".
- Replace the slide-14 TODO with: "Open question, partly answered: the allowlist always includes GitHub domains, so it limits where the agent can reach, not whether data can leave. We have not tested exfiltration." Remove "Squid... only listed domains out" absolutism on the diagram ("Only listed domains out" -> "Listed domains, plus GitHub's").

### 5. Slides 11-12: "one draft pull request, and nothing else" / "can only open a draft" overclaims
- Problem: (a) the real file you excerpt sets `protected-files: fallback-to-issue` and `labels:`; trimmed out, they mean a patch touching protected files produces an issue instead. `create-pull-request` also "Falls back to opening an issue if PR creation is blocked" by default (`fallback-as-issue`). So the outbox is not "one draft PR and nothing else". (b) Draft is set by the workflow author; GitHub's own docs workflow uses `draft: false` (see 2). "Cannot override" refers to the agent, which is correct, but "this one cannot skip that step" (lede) reads as a product guarantee. `auto-merge` and an experimental `merge-pull-request` output exist.
- Evidence: update-docs.md (raw githubnext/agentics main) lines `protected-files: fallback-to-issue`, `labels: [automation, documentation]`; https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/ ("Falls back to opening an issue ... set fallback-as-issue: false to disable"; "`draft` is a policy, not a default, so the agent cannot override it at runtime").
- Replace slide 11 annotation 3: "**Outbox:** one draft pull request per run (or a review issue if the PR is blocked)". Replace slide 12 lede: "You would review a new teammate's first pull request. In this configuration, so do you." Add to muted line: "Draft is a setting the workflow author chooses."

### 6. Slide 15 (blast radius): "no engine token" / "no credential to exfiltrate" is stronger than the docs
- Problem: the SVG says the container has "No token" and its description says "a prompt-injected agent has no credential to exfiltrate". Docs: the API proxy "may hold endpoint-specific credentials or routing configuration for supported engines" and the page labels it "Agent auth-token isolation"; separately the MCP gateway agent ID is to be "treated as leaked by design". MCP servers get secrets "via environment variables". The notes already caution, but the diagram text contradicts them.
- Evidence: https://github.github.com/gh-aw/introduction/architecture/ (substrate paragraph; "Treat this identifier as leaked by design and rely on substrate isolation, network policy, and staged permission separation"; "Secret Injection: Secrets are passed via environment variables").
- Replace "No token" with "Engine token kept in the API proxy" and the desc sentence with "the API proxy holds the engine credential outside the container; the docs still treat some in-container identifiers as leaked by design". Also note it is the MCP gateway agent ID that is "leaked by design", not "an in-container identifier" generally (slide-15 note wording is loose).

### 7. Slide 13 title: "The agent never holds a write token"
- Problem: documented as the design ("the agent never requires write permissions"; "agent job runs with minimal read-only permissions") but the permissions reference lets authors grant write scopes, and the deck cites nothing that enforces it for every config. I did not confirm that strict mode (which I believe rejects write on the agent job) is on by default; GitHub's own lock files show `strict: true` set explicitly.
- Replace title with: "In this setup the agent holds no write token: a separate, checked job does the writing". Keep the architecture quote.

### 8. Slide 10 (triggers): role-check claims partly rest on source code, not the docs; "four things" is the deck's grouping
- Problem: docs say only "Workflows with unsafe triggers (push, issues, pull_request) automatically enforce permission checks. Failed checks cancel the workflow with a warning." The diagram extends that to Manual (`workflow_dispatch`) and Comment (`slash_command`) and states schedule is exempt. The source supports this: `check_membership.cjs` skips only `["schedule", "merge_group"]`, and `role_checks.go` treats `slash_command` as unsafe. But the docs do not say it, and the roles list is configurable (`roles: all`, `skip-roles`, `bots`). The docs list many more triggers (workflow_run, pull_request_target, label_command, deployment_status, repository_dispatch).
- Replace headline: "Many things can start it; people-started runs are permission-checked by default, a schedule has no person to check". Caption: "Source: gh-aw triggers docs (default roles `[admin, maintainer, write]`, configurable) and the compiler source for dispatch, comments and schedules." Add "by default" to the diagram's "admin, maintainer or write role".

### 9. Slide 19 (ask): "cap about $10 a run" understates the per-run ceiling
- Problem: the detection job has its own separate budget. Docs: detection `max-ai-credits` "Defaults to 400 when unset ... independent of the main agent budget". Worst case is 1,000 + 400 = 1,400 AIC, about $14, before Actions minutes and any Copilot licence cost. The deck correctly omits the conflicting daily cap but should not call $10 the ceiling.
- Evidence: https://github.github.com/gh-aw/reference/threat-detection/ (detection `max-ai-credits`); https://github.github.com/gh-aw/reference/cost-management/ ("1000 AI Credits per workflow run", "One AIC equals $0.01 USD").
- Replace: "per-run cap: 1,000 AI Credits for the agent (about $10) plus a separate 400 for detection (about $4); best-effort estimates, excluding Actions minutes".

### 10. Slide 18 (spec): "Outbox: one pull request" ignores inherited safe outputs
- Problem: `readme-auto-updater` imports `shared/policy/baseline-safety.md`, which declares `safe-outputs: add-comment (max 1), add-labels (allowed: bug, enhancement, question, needs-info)` and `network: allowed: [defaults, github]`; the library says every installable workflow imports it. Imports merge into the compiled workflow. The slide says the frontmatter backs "one pull request". Also note the engine is `copilot` with a `COPILOT_GITHUB_TOKEN` secret.
- Evidence: DonalMoloney/Agentic-Workflows-Lib `workflows/readme-auto-updater.md` (imports) and `workflows/shared/policy/baseline-safety.md`. Not run through `gh aw compile` here, so the merge behaviour is from the docs' "All tools declared in imported components are merged", not an observed lock file.
- Replace the Outbox row: "**one** pull request (`create-pull-request`, `max: 1`), plus one comment and a fixed label set inherited from `baseline-safety`". Add `network: defaults + github (inherited)` to the Access badge row.

### 11. Slide 11 headline and slide 22 status line: "Thirteen lines" and "fact-checked 18 Oct 2026" overstate
- Problem: (a) "Thirteen lines say when it runs..." counts only the trimmed excerpt; the real frontmatter also has `workflow_dispatch` (a second, person-started trigger), `protected-files`, `labels`, `timeout-minutes: 15` and a ~100-line body of instructions. Caption says trimmed; headline implies the whole job. (b) Slide 22 says fact-checked 18 Oct 2026 "against the sources cited on each slide", yet `sources.md` itself records the Chris Aniszczyk (CNCF) quote as "could not verify" and the slide-16 note still attributes it to "GitHub Blog, 13 Feb 2026". I could not find it on that post either (no "Aniszczyk" or "CNCF" on the fetched page). Also the "72.6%" line is correctly parked as TODO.
- Replace slide 11 headline: "Thirteen trimmed lines show when it runs, what it can read, and what it can send". Remove the Aniszczyk quote from the slide-16 note, or mark it "TODO: source not found". Add to slide 22: "Not verified: Aniszczyk quote; Stack Overflow, Octoverse and Feng et al. last checked 17 Oct".

### 12. sources.md is stale for v3
- Problem: the ledger header says "Deck v2" and its slide numbers (9 = architecture, 15 = status) match v2, not this 22-slide deck. It cannot back the per-slide claims, and it records slide-8 role-check "verified" while the 18 Oct re-check says the diagram needed redrawing. Readers auditing from it will mis-map claims (for example "Slide 12 57 of 59").
- Fix: renumber against the table above, add rows for the new slides 13 (activation write finding), 14, 17, 18 and for the run-jobs plain labels, and change the slide-8 row to point at slide 10.

## Other checks (no change needed unless noted)
- Slide 2: 56.5% / 12,374 / 6,989 as per ledger; the deck sensibly says "information", not documentation. Not re-fetched today (Stack Overflow site is JS-rendered).
- Slide 3: Octoverse text matches: "merged 43.2 million pull requests on average each month (+23% YoY), and pushed nearly 1 billion commits in 2025 (+25.1% YoY)". Data is 2025; fine for Oct 2026 but say "2025".
- Slide 4: Feng et al. five levels and names match the abstract. L4 placement is labelled as the deck's. Mild challenge: a scheduled run with no human before the PR is arguably closer to L5 until the PR; the deck already says "interpretation".
- Slide 6 note: "Do NOT say every AI tool waits" good. Slide 7: "paragraph" framing is fine.
- Slide 11: `permissions: read-all` is broad read (all scopes), not "contents: read"; a skeptic will note it, and `web-fetch` plus `bash: true` in the same job. The note handles bash well; add one sentence on `read-all`.
- Slide 12 / 19 quotes: May Walter quote matches the changelog verbatim; "never merged automatically" and "Start with low-risk outputs" match the Blog; "They do not replace build, test, or release pipelines" matches.
- Slide 13: detection is "a prompted AI agent" (architecture page), so the checker is an LLM reviewing an LLM; a security engineer will ask. Say so on the slide ("an AI check, not a rule engine"). `continue-on-error: true` default is stated correctly and the diagram shows it.
- Slide 17: counts verified today via `gh api`: 98 workflows, 98 docs pages, 6 shared modules, 0 `.lock.yml` in the tree, private, last push 2026-09-23; `agents.md` supports "4 compiled, 0 errors, sandbox repo does not exist, no release". Nothing overclaims; the "98 dots / 4 filled / 0 run" framing is sound. One challenge: "four filled dots compiled locally" is self-reported with no lock file, which the caption already says.
- Slide 18: `acme-org` placeholder is flagged on the slide; fine.
- Slide 19: staged/trial caveats ("not a sandbox", trial experimental) match the docs. "Week one writes nothing at all" is slightly strong given the docs' list of things staging does not skip; the slide-19 notes already say "writes nothing to our repo". Keep that phrasing on the slide too.
- Slide 20: "four of the six" jobs matches the architecture page.

---

## Lens: visual

# deck-v3 visual design review (read-only, all 22 PNGs viewed)

Overall: the editorial feel holds (serif titles, paper canvas, indigo rule/kicker, caution brown used for gaps). Strongest: 13 (write-token flow), 15 (layers), 4 (ladder), 17 (dot grid). Weakest: 5, 12, 20, 21 (empty/template), 7 and 9 (crowding into footer), 3/16 (stat slides inconsistent).

## Top 12 by impact

1. Slides 6, 7, 9, 11: content collides with the footer/source line (source sits under the toolbar pill zone; on 7 the "Classic Action / Agentic workflow" bar and the source line are touching, on 9 the "Commit both files" row nearly touches the source, on 11 the code card 4 runs to y~655 against the source). Fix: these four slides are 15-25% over budget. Drop the `.lede` line on 7 and 9 (title already says it), or shrink diagram heights via scoped `margin-top` on the `<img>`/svg and set a consistent `--gap-footer` reserve (padding-bottom on `section` equal to source block height). On 11, shorten the code to the 4 lines that matter or put annotations beside without the number badges repeating.

2. Slide 12: bottom 40% of the slide is empty and three cards are short-text with the middle card taller content; reads as a template. Fix: make the cards fill the vertical space (`align-items: stretch`, min-height ~ 55% of body, larger 28px body text) or replace with one claim card + two supporting. Alternatively merge with 13's opening. Remove the serif lede-vs-card double statement.

3. Slides 20 and 21: half empty, flat list/cards; appendix feels unfinished compared with the main arc. Fix: 20 - convert to three numbered steps with larger type (28px) and a single mono command per step, vertically centred via `_class: lead` or scoped `place-content: start` plus `margin-top`. 21 - give links a two-column "label / URL" table with the URL in `.muted` mono, and drop the 4th bullet's smaller font (inconsistent size, looks like an overflow fix). Keep the amber TODO as the first row.

4. Slide 5: three amber TODO cards plus an amber dashed box plus an amber line = a wall of brown; the caution colour (meant for gaps) stops signalling anything and the slide has no hierarchy. Fix: one dashed TODO frame holding the three cards in ink/muted (cards neutral, with only the TODO word amber), and put the "confirm landing line" under it in `.muted` small. Cards 1-3 should read as a left-to-right sequence: add the same arrow connector used on 14.

5. Slide 19: the ask is the climax but is the busiest slide: five dashed TODO pills, a four-step row, two more TODO blocks, an open-decision paragraph, a source. Pills use 20px bold-brown text at near-equal weight so nothing leads. Fix: make the four steps the hero (bigger step headings, 32px); collapse the five pills into a single "Needs from you" strip with ink labels and only a small amber glyph; move the OPEN DECISION into a card in step 2's column or into notes. The top full-width indigo bar is unique to this slide: good as a signal, but the cream panel background also changes; keep one of the two.

6. Slides 2 and 3 (stat slides): 56.5% is a great hook, but the sentence under it, the "somewhere in our docs..." line, and a two-line source create three text weights stacked. On 3 the stats are in the same font size as the hook on 2, so the deck's biggest-number moment is diluted twice, and the "Nearly 1 billion" wraps its descriptor awkwardly vs 43.2 million. Fix: on 2 put the stat left (50% width) with the claim sentence beside it vertically centred; on 3 reduce both stats to ~72px so 2 stays the one big hook (`.stat` max one per deck per CLAUDE.md), and align the two descriptors on one baseline with fixed 2-line height.

7. Slide 16: stat `57 / 59` plus a serif paragraph beside it plus two cards plus a TODO strip. The serif paragraph repeats the title. Fix: delete the paragraph, put the small-sample caveat as a muted caption directly under the stat, and size the two cards as a true compare pair (arrow or "vs" between, "GitHub measured" vs "Our pilot will measure", the second in indigo outline to show it is the thing we do).

8. Slide 4 (ladder): good concept but staircase offsets make L4 label tab clash with the dotted divider, the legend and caption sit at 18px-ish and the bar meter is small; source line is repeated twice (caption inside SVG and footer). Fix: remove the in-SVG "Illustrative ladder..." caption (footer already says it), raise rung labels and "Human signs off" text to >=20px, make L4 box taller than neighbours rather than shifted, and extend the dotted line to full height. Bars are fine.

9. Slide 15 (layers): reads well, but the nested boxes' inner text (Squid proxy, MCP gateway, bottom captions "network: {} = no access") is ~14-15px at slide scale, and the dashed amber connector exits the container at the bottom with no label. The diagram fills only ~85% width, leaving a dead strip right of 1090px. Fix: widen SVG viewBox usage to the full 1136px column, raise all secondary labels to >=18px, delete the bottom-right "network: {}" note or move to notes, and keep the legend glyph for "not a strong boundary".

10. Slide 13: best slide in the deck, but the sub-labels inside boxes (Activation, Agent, Detection, Safe outputs) and the icons are small (~16-18px); the "Caution by default, not a block" amber text is bold and competes with the green "Opens draft PR". Fix: use ink for the amber box body and keep amber only for the border/glyph; bring "READ AND PREPARE / PERMITTED WRITES" labels to the same weight as slide kickers. Keep as the template for 14 and 15.

11. Slides 8 and 12 (cards) vs 14 and 15 (diagram cards): three different card styles. Cards on 8/12/20 have a top 3px border that is tan or indigo, 14 uses a full outline with a numbered badge, 19 uses dashed. Radius and padding differ. Fix: define two card variants only: `.card` (neutral, tan top rule) and `.card.hi` (indigo tint + indigo top rule); on diagram cards use the same radius (currently 8 vs 12) and the same label style (small caps letterspaced kicker, as on 8). Dashed is reserved for gaps/weak boundary only.

12. Slide 18 and 22 (tables/lists): table header row empty with a single code-chip column title looks like a layout bug, and slide 22 is a wall of bullets at 20px with bold-indigo highlights on 6+ phrases, contradicting the "spend accent sparingly" rule. Fix: 18 - move "readme-auto-updater" into the title row as a caption ("Illustrative spec: readme-auto-updater") and drop the header row; 22 - keep bold in ink not indigo, group into two columns ("How to read a source" / "Left off on purpose") using `.cards`.

## Cross-deck notes
- Consistency of header/kicker, title position and footer is good. Page number sits fine; the source line height varies (1 to 3 lines) so footers float: pin `.source` to the bottom with a fixed bottom offset.
- Diagram line weights: slides 6, 7 use ~1.5px, 13-15 ~2px; radius 8 on 6/7/13, 12 on 14/15. Normalise via the shared SVG prelude.
- Colour contrast: indigo `#3f3fb0`-ish on paper and brown amber on paper both pass AA for text; the muted tan-grey source text (~#6b6252 on #f9f5ee) is borderline at 18px; darken the `--muted` token slightly.
- Slide 1: strong; the TODO line under the byline is the only clutter (the loop diagram's 12px captions are small but decorative).
- Slide 10 (triggers): clear, but the left "no person starts it" arrow label and the Pre-activation box leave the Schedule card visually orphaned; align Workflow run's arrow target so both paths visibly merge, and drop one of the two 20px lines above (lede) to give the diagram space.
