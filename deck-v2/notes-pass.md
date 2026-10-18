# Deck v2: speaker-notes rigour pass

Proposals only. Nothing here has been applied to `deck.md`.

**Rebased against `deck.md` as of 17 Oct 2026 19:33** (md5 `046c6d7c70b3ca8b5b316e28c9d18e75`) — the 17-slide version with the rewritten Hypothesis/Method/Measure ask slide and the "typical jobs" line moved off slide 5 into its notes. Slide numbers count the title slide as 1: main talk 1–12, appendix 13–17.

Every OLD string below was machine-checked to appear **exactly once** in that version of `deck.md`. All 26 are inside speaker-note comments; none touch a slide body, a directive comment or the front matter. Note that `deck.md` moved twice while this pass was being written — if it has moved again, re-run the uniqueness check before applying (the script at the end does it).

**Standard applied:** every number carries its status (*measured* · *reported by GitHub* · *self-reported* · *this deck's interpretation*); every note runs plain-English line → technical detail → numbers and sources → questions → transition; nothing merely repeats the slide; every claim cross-checked against `sources.md`. No new facts. Slide 4's story and slide 12's decision rule stay TODO.

---

## HIGH — correctness, epistemic status, and broken note order

### H1. Slide 8: the note claims more than the docs do about the API proxy
`sources.md` mismatch 1 is the only ledger row still marked **changed**, and this note is where the rejected claim survives. "No credential to exfiltrate" is an absolute the architecture page contradicts in its own words: it says the proxy "may hold endpoint-specific credentials", and warns that an in-container identifier should be treated "as leaked by design". The SVG has already been corrected to "Keeps the engine token out of the container"; the note has not. In a security-minded room this is the single most challengeable sentence in the deck.

**OLD**
```
The API proxy matters for a different reason: it keeps the engine's auth token out of the agent's container, so a prompt-injected agent has no credential to exfiltrate.
```
**NEW**
```
The API proxy does a different job: it keeps the engine's auth token out of the agent's container. The docs' own name for this is "agent auth-token isolation".
Careful wording: do not say there is nothing in there to steal. The same page says an in-container identifier should be treated "as leaked by design". The claim is that the engine token is held somewhere else, not that the container holds no secrets.
```

### H2. Slide 12: `staged: true` is on the slide as the safety step, and the docs say staging is not a sandbox
The method slide promises "runs it for real and writes nothing" — which is exactly right about outputs, and exactly the sentence a listener will round up to "so it can't do anything". The staged-mode page says in as many words that "staging is not a sandbox": custom jobs, scripts, external MCP servers and custom credentials are not skipped (`sources.md`, slide 8 row). The second half of the same patch fixes a command that would not do what he says it does: `gh aw new` scaffolds a template, it does not fetch the agentics file.

**OLD**
```
Commands for engineers, if asked: gh extension install github/gh-aw; gh aw init, then gh aw new update-docs; gh aw trial, then staged: true; approve the first PR. The first two take minutes.
```
**NEW**
```
Commands for engineers, if asked: gh extension install github/gh-aw; gh aw init; gh aw new <name> to scaffold a workflow; gh aw trial, then staged: true; approve the first pull request. The first two take minutes.
Precision: gh aw new creates a template in .github/workflows, it does not fetch the agentics file. That comes from gh aw add-wizard githubnext/agentics/<name>, and I have not confirmed the exact path for update-docs, so don't recite it as a known command.
Careful wording on staging: it writes nothing to our repository, but the docs say plainly that "staging is not a sandbox" — custom jobs, scripts, external MCP servers and custom credentials still run. Say "it writes nothing to our repo", never "it can't do anything".
```

### H3. Slide 12: the note attributes the 57/59 to "GitHub's repos", which the source does not say
This one contradicts slide 10's own note three slides earlier ("the post doesn't say which repos"), and `sources.md` mismatch 4 exists specifically to stop this claim. Two notes disagreeing about the same number is worse than either wording alone.

**OLD**
```
The ask: TODO (pilot repo, owner, budget, and the decision rule). Do not present the 96% as a target we expect to hit; it is GitHub's figure for GitHub's repos, reported by them, on a small sample.
```
**NEW**
```
The ask: TODO (pilot repo, owner, budget, and the decision rule).
Do not present the 96% as a target we expect to hit. It is GitHub's own figure, reported by GitHub, from 59 pull requests, and the post does not say which repositories produced it. Our number is unknown, which is the whole reason to run the month.
```

### H4. Slide 9: the transition sits in the middle of the note, and the note has no plain-English line
Required order is plain line → technical → numbers and sources → questions → transition. Here the transition is third of four, with a question after it. The patch reorders, adds the opening line for the non-technical half, and adds the prepared answer to the question this slide invites — "is that really the whole file?" — using the trimmed-fields list already recorded in `sources.md`, including the honest one: the real file can also be started by hand.

**OLD**
```
This is a real file, trimmed: update-docs.md from githubnext/agentics. Not a made-up example.
Walk it against the teammate pairs from slide 5: shift = every push to main; badge = read-all plus network: defaults (the firewall); outbox = one draft pull request.
Transition: that is the entire job description. Now, what does a run like this actually produce?
Expect the question "bash: true?" Yes, tools are broad, but the agent job is read-only and its network goes through the firewall. Writes happen later, in a separate job (the "never holds a write token" slide).
```
**NEW**
```
Plain line for the non-technical half: do not read the syntax to them. Four blocks, four questions — when it runs, what it may read, where it may call out, and what it may send.
This is a real file, trimmed: workflows/update-docs.md from githubnext/agentics, checked against the raw file on 17 Oct 2026. Not a made-up example.
Walk it against the teammate pairs from the teammate slide: shift = every push to main; badge = read-all plus network: defaults; outbox = one draft pull request.
If asked what was cut: workflow_dispatch, protected-files, labels, timeout-minutes: 15, and a commented-out smaller model. The one worth mentioning is workflow_dispatch — the real file can also be started by hand.
Q: "bash: true?" Yes, the tools are broad, but the agent job is read-only and its network goes through the firewall. Writes happen later, in the separate job from the write-token slide.
Q: "Only one pull request?" One per run is the default maximum for create-pull-request, not a limit I invented.
Transition: that is the entire job description. So what does a run like this actually produce?
```

### H5. Slide 7: "a detected threat blocks the writes" is contradicted by the next line, and the "four jobs" warning is now stale
Two problems in one block. First, the note asserts the block and then takes it back, so under pressure he could say either half; stating the docs' sentence and its default in one breath is both shorter and safer. Second, the slide now carries "four of its six jobs shown" in its own muted line, so a note telling him not to say "four jobs" argues with the slide — the live instruction is to say it the way the slide does. The patch also adds the question this slide reliably draws ("an AI checks the AI?") and upgrades "usual default" to the docs' "Copilot CLI is the default".

**OLD**
```
Detection looks for prompt injection, secret leaks and malicious patches. A detected threat blocks the writes.
Careful wording: don't say it "always blocks". By default, continue-on-error is true, so a detection warning or failure becomes a caution notice rather than a block.
Q: "Which AI does the work?" Engine choice is a setting: GitHub Copilot, Claude Code, Codex, Antigravity (experimental) and Pi; Copilot is the usual default. Gemini is listed but deprecated in favour of Antigravity.
Careful wording: the docs list six jobs (adding pre-activation and conclusion); the diagram simplifies, so don't say "four jobs".
Q: "Is it GA?" No: public preview since 11 Jun 2026 (GitHub changelog).
```
**NEW**
```
Detection is itself an agent, in its own job with no write permissions, looking for prompt injection, secret leaks and malicious patches. It turns on automatically as soon as safe outputs are configured.
Careful wording, and this is the one to get right: the docs say that if a threat is detected "the workflow fails and safe outputs are blocked" — but continue-on-error defaults to true, so in the default configuration a detection failure arrives as a caution notice, not a hard block. Never say detection "always blocks".
Careful wording: the slide says "four of its six jobs" for a reason. Pre-activation and conclusion are the two not drawn, so say "four of six" out loud, the way the slide does.
Q: "So an AI checks the AI?" Yes. Detection is a second agent job and it holds no write permissions either. It is a layer, not a guarantee — and whatever gets past it still lands as a draft that a person reads.
Q: "Which AI does the work?" Engine choice is a setting: GitHub Copilot, Claude Code, Codex, Antigravity (experimental) and Pi. The docs say Copilot CLI is the default. Gemini is listed too, but deprecated in favour of Antigravity.
Q: "Is it GA?" No: public preview since 11 Jun 2026 (GitHub changelog).
```

### H6. Slide 2: the note repeats the slide, and the deck's biggest number has no status
The slide already says "56.5% of 12,374 developers ... outdated information". The note's second line says it again in different words and adds nothing — the rules forbid that. What the note should carry is the raw count, the survey's own question, and the status: *measured, but self-reported perception*, not an audit of anyone's documentation. The careful-wording line matters because the survey option is "information is outdated", not "documentation is outdated" — reading it as a docs problem is this deck's move, and a sharp listener will spot the gap before he admits it.

**OLD**
```
56.5% of 12,374 developers name outdated information as a blocker.
```
**NEW**
```
Precision, in case the number is challenged: 6,989 of 12,374 developers picked "information is outdated" when asked what gets in the way of getting the context they need for work. Measured, but self-reported — it is what developers say gets in their way, not an audit of anyone's docs.
Careful wording: the survey says outdated information, not documentation. Hearing it as a docs problem is this deck's interpretation, so say "information" and let the room make the jump.
```

### H7. Slide 2: the fallback citation is vague where it could be exact, and the note has no transition
"About two-thirds of 45 developers" is the kind of rounding that invites "which two-thirds?". The ledger has the exact split and the exact statement, and it records that the copy read was course-hosted rather than the publisher's page — disclosing that is cheap and it is precisely the register being asked for. The last line also becomes the transition into the volume slide, which the note currently lacks.

**OLD**
```
Older backup if challenged: about two-thirds of 45 developers agreed docs are "always outdated" (Lethbridge et al., IEEE Software, 2003). The problem is old; what's new is the speed.
```
**NEW**
```
Older backup if challenged: 68% of 45 developers agreed that "documentation is always outdated relative to the current state of a software system" — 24% strongly, 44% somewhat (Lethbridge, Singer and Forward, IEEE Software, 2003). Tiny sample, twenty-three years old, and the copy I read is a course-hosted PDF rather than the publisher's page.
Transition: so the problem is old. What is new is how fast the code underneath the page changes.
```

### H8. Slide 3: the L1–L5 numbering is presented as the paper's, and the 43.2 million needs one more word
`sources.md` is explicit: the five names and their order were verified from the abstract, the L1-to-L5 numbering was not checked in the full text. Saying "the ladder runs L1 to L5 (Feng et al.)" attributes a label he has not verified — the cheapest possible correction, and exactly the kind of thing an academic room catches. Second: 43.2 million is a *monthly average* that rose from 35 million, not a monthly peak, and the Octoverse window (1 Sep 2024 – 31 Aug 2025) is in the ledger as coming from secondary coverage, which is worth saying out loud if asked.

**OLD**
```
Technical: the ladder runs L1 Operator to L5 Observer (Feng et al.). L4 Approver is my reading of gh-aw: the agent does the work, a human approves the consequential step, the PR. It is not the paper's classification of gh-aw.
Numbers: only the Octoverse figures are measured: 43.2M PRs merged per month (+23%), nearly 1 billion commits in 2025 (+25.1%). Don't claim a measured docs gap; slide 2's survey is the docs evidence. The link from more code to staler docs is this deck's interpretation.
Q: "Is AI really behind the growth?" Octoverse reports the growth; don't attribute all of it to AI.
```
**NEW**
```
Technical: the five rungs and their order — Operator, Collaborator, Consultant, Approver, Observer — are Feng et al.'s. The L1-to-L5 numbering is my labelling: I verified the names and the order from the abstract, not the numbering from the body. Putting gh-aw at Approver is my reading too — the agent does the work, a human approves the consequential step, the pull request. The paper does not mention gh-aw at all.
Numbers, and only these two are measured: 43.2 million pull requests merged per month, which is a monthly average up from 35 million the year before, and nearly 1 billion commits pushed in 2025, up 25.1%. Octoverse 2025. Say "pushed", because that is the word Octoverse uses.
If asked whether that means calendar 2025: the Octoverse window is reported as 1 September 2024 to 31 August 2025, and I have that from coverage of the report rather than from the report itself.
Careful wording: there is no measured docs gap on this slide. The survey slide is the docs evidence, and the link from more code to staler docs is this deck's interpretation.
Q: "Is AI really behind the growth?" Octoverse reports the growth. It does not attribute all of it to AI, and neither should I.
```

### H9. Slide 15: the note's first line is now the slide's title, and the staged caveat is missing here too
After the title was shortened to "a repo event, a clock, a button, or a comment", the note's opening line says the same four things in the same order — a repeat, and a wasted first line. What is worth adding is the thing the diagram shows and nobody says: all four routes end in the same run, with the same permissions and the same outbox. The patch also lands the "staging is not a sandbox" caveat on the slide that introduces `staged: true`, names the trial repo default and the two comment triggers, and fixes the sentence that currently starts mid-stream after a question mark.

**OLD**
```
Four ways to start a shift: something happens in the repo, a clock, a button, or someone asks in a comment.
Schedules can be fuzzy ("daily") rather than exact cron times.
Two safety nets before it can touch our repo: gh aw trial uses a throwaway private repo (marked experimental in the docs); staged: true runs for real but only previews what it would write, in the run summary.
Q: "Can anyone trigger it with a comment?" by default only users with admin, maintainer or write role can trigger it; the pre-activation job checks this (gh-aw triggers and architecture docs).
Appendix slide: pull it up if someone asks how a run gets started.
```
**NEW**
```
The title lists the four. The point worth adding is the one the diagram makes: all four end in the same run, with the same permissions and the same outbox. The trigger only decides who starts the shift.
Detail: schedules can be written fuzzy — "daily", "weekly" — instead of exact cron, so a fleet of workflows doesn't all fire on the same minute. The comment routes are slash_command and label_command.
Two safety nets before it touches our repository: gh aw trial runs the workflow in a temporary private repo, gh-aw-trial by default, and the TrialOps page marks the feature experimental; staged: true runs for real and prints every output it would have made into the Actions step summary instead of making it.
Careful wording: the staged-mode page says "staging is not a sandbox" — custom jobs, scripts, external MCP servers and custom credentials are not skipped. Staging stops the outputs, not the run.
Q: "Can anyone trigger it with a comment?" By default only users with admin, maintainer or write role; the pre-activation job runs that check (gh-aw triggers and architecture docs).
Appendix slide: pull it up if someone asks how a run gets started, or when staging comes up on the pilot slide.
```

### H10. Slide 5: the note's first line is the title, reworded
"It is still a GitHub Action; the difference is that you brief it instead of scripting it" is the title — "a GitHub Action you brief instead of script" — said twice. That line was written when the title was "A classic Action is a recipe; an agentic workflow is a brief", and the title has since absorbed it. The replacement keeps the delivery instruction and adds the concrete contrast that is *not* on the slide.

**OLD**
```
The title is the whole idea. Say it, pause, then: it is still a GitHub Action; the difference is that you brief it instead of scripting it.
```
**NEW**
```
The title is the whole idea: say it, pause, and let the diagram carry it.
The line to add, which is not on the slide: you already have Actions that run a script somebody wrote. This one runs a paragraph somebody wrote, and it works out the steps itself.
```

### H11. Slide 12: the supporting quote cuts against the pilot, and the obvious objection has no answer
The GitHub Blog line says to start with low-risk outputs "before enabling pull request creation" — and the method on this slide goes to draft pull requests. Quoted as support, an attentive listener can turn it into an objection in one sentence. The note should pre-empt that rather than hand him the quote unguarded. The added question is the one a manager asks about any pilot, and it is answerable entirely from what is already on the slide.

**OLD**
```
Supporting guidance: "Start with low-risk outputs such as comments, drafts, or reports before enabling pull request creation." (GitHub Blog)
```
**NEW**
```
Supporting guidance: "Start with low-risk outputs such as comments, drafts, or reports before enabling pull request creation." (GitHub Blog.) Use it to justify staging first and reviewing everything — not as GitHub endorsing this pilot. Read closely it says low-risk outputs before enabling pull requests, and our method ends at draft pull requests, so don't present it as a blessing.
Q: "What if it just wastes reviewer time?" Staged mode shows us what it would have written before any pull request exists, and the measure is the share we merge without edits. A month of bad drafts is a cheap no, not an expensive one.
```

### H12. Slide 17: the only note in the deck that isn't a note
"Render with: marp deck.md" is a build command, and a stale one — without `--allow-local-files` the diagrams don't load (the correct command is in `deck-v2/CLAUDE.md`). The slide's real job is to be the page he turns to when a number is challenged, so the note should be the two answers he'd need there, which are the two facts the deck deliberately omits.

**OLD**
```
Backup slide; don't present it. Render with: marp deck.md
```
**NEW**
```
Never presented. This is the slide to turn to if a number is challenged: it carries the check date and the two facts left off the deck on purpose.
If pushed on the daily credit cap: the cost-management page says 5,000 AI Credits per workflow per day by default, the frontmatter page says max-daily-ai-credits is disabled when omitted. Two official pages, one contradiction, so it is on no slide.
If pushed on detection: continue-on-error defaults to true, so a failed check is a caution notice by default. That is why nothing in this deck says detection blocks.
Everything was re-checked on 17 Oct 2026, claim by claim, in deck-v2/sources.md — offer that to anyone who wants the receipts afterwards.
```

---

## MEDIUM — precision, order and delivery

### M1. Slide 1: the spoken agenda doesn't match the talk, and "stay safe" is the one register to avoid
The deck's arc is problem → what it is → how it's checked → what happened when GitHub ran one → the library → the ask, but the agenda line promises three of those. "How they stay safe" is also the exact claim the rest of the deck spends four slides refusing to make; "kept in check" is the deck's own framing (slide 6: "checked, not trusted").

**OLD**
```
"Today: what GitHub Agentic Workflows are, how they stay safe, and a one-month pilot I'd like us to try."
```
**NEW**
```
"Today: what GitHub Agentic Workflows are, how they are kept in check, what happened when GitHub ran one on its own docs, and a one-month pilot I'd like us to try."
```

### M2. Slide 1: no transition
Every other main-talk note ends with one. This is also the highest-risk moment for drifting into product explanation before the problem has landed.

**OLD**
```
Mixed room: plain-English version first on every slide; the technical detail is there for those who want it.
```
**NEW**
```
Mixed room: plain-English version first on every slide; the technical detail is there for those who want it.
Transition: don't name the product again yet. Go straight to the page that is wrong.
```

### M3. Slide 4: keep the TODO, add the delivery discipline and a placeholder transition
The story stays his to write. What can be added without inventing anything is the shape (under a minute, three beats, no architecture detour) and an explicit reminder that the hand-off line into the next slide needs writing rather than improvising. The current second line is transition guidance but names nothing.

**OLD**
```
TODO: tell the story of the earlier project in three beats: what I built, what worked, what was missing.
End on the gap, because the next part of the talk answers it.
```
**NEW**
```
TODO: tell the story of the earlier project in three beats: what I built, what worked, what was missing.
Under a minute. Three beats, no detour into how it was built — the room doesn't need the architecture, it needs the gap.
End on the gap and name it in one sentence, because the next slide is the answer to it.
Transition: TODO — write the one line that hands off from my gap to what gh-aw is, and write it before the day rather than improvising it.
```

### M4. Slide 5: the typical-jobs line is one 60-word sentence, and it undersells how well sourced it is
Now that the list has moved off the slide and into the notes it has to be spoken from memory, so it needs to be two sentences, not one. And the sourcing is better than the note admits: the three groups are the gh-aw home page's own headings (the third is "Report and plan", which the deck shortens), while filing each gallery task under a group is the deck's work. Saying exactly which half is his is stronger than "the grouping is mine".

**OLD**
```
Say the typical jobs out loud rather than listing them on the slide: maintain the repo (docs, triage, dependencies), improve code (reviews, security), report (metrics). Those three groups are from the gh-aw home page and the tasks are from the gallery, but the grouping is mine — say so. Then point at docs: that's this talk's job and the lowest-risk place to start.
```
**NEW**
```
Say the typical jobs out loud rather than listing them on the slide: maintain the repo — docs, triage, dependencies; improve code — reviews, security; report — metrics.
Sourcing, and say it: the three groups are the gh-aw home page's own headings, and the tasks are from its gallery. What's mine is which task I filed under which group, plus shortening their "Report and plan" to report.
Then point at docs: that's this talk's job, and the lowest-risk place to start.
```

### M5. Slide 6: name the experimental merge output instead of alluding to it
"Since an experimental merge output exists" is the weakest sentence in an otherwise exact note — it is the reason the caveat exists, so it should be nameable. `sources.md` has the detail: `merge-pull-request`, gated by policy, and merges to the default branch are always refused. That last clause is also reassuring, so there is no cost to saying it.

**OLD**
```
Wrong edits: PRs open as drafts; the docs call draft "a policy, not a default", so the agent can't override it. "Never merged automatically" is GitHub Blog guidance, not a hard limit, since an experimental merge output exists.
```
**NEW**
```
Wrong edits: pull requests open as drafts; the docs call draft "a policy, not a default", so the agent cannot override it at runtime.
Careful wording: "pull requests are never merged automatically" is GitHub Blog guidance, not a hard limit. An experimental merge-pull-request output does exist — it is gated by policy, and merges to the default branch are always refused.
```

### M6. Slide 6: the quote sits after the Q&A, and two source details are one word short of exact
Required order puts quotes with the numbers and sources, before the questions; here the May Walter quote is last but one. The same patch names the setting (`max-ai-credits`), uses the docs' own "best-effort" phrasing, and replaces "two docs pages disagree" with which two pages — he will be asked about cost, and naming the pages is the difference between a hedge and a read source.

**OLD**
```
Cost: a per-run budget is on by default, 1,000 AI Credits; 1 AIC = $0.01, so about $10. The docs call AIC best-effort, so it may not match the bill exactly.
If asked about a daily cap: two docs pages disagree on its default, so I've left it out.
Q: "Could it replace our CI or release pipeline?" No: it's not for build, test or release pipelines; it's for work that needs interpretation. Say the limit out loud as well as showing it; naming it early buys trust.
Say the quote out loud rather than putting it on the slide: "Getting an agent to open a pull request was never the hard part. Trusting it enough to merge is." (May Walter, CTO, Hud.io, GitHub changelog, 11 Jun 2026.)
```
**NEW**
```
Cost: the per-run budget is max-ai-credits, on by default at 1,000 AI Credits. 1 credit is $0.01, so about $10 a run. The docs say credits are computed on a best-effort basis, so it won't match the bill exactly.
If asked about a daily cap: the cost-management page and the frontmatter page give different defaults, so I've left it off the slides. Both versions are on the status and sources slide at the end.
Say the quote out loud rather than putting it on the slide: "Getting an agent to open a pull request was never the hard part. Trusting it enough to merge is." (May Walter, CTO, Hud.io, GitHub changelog, 11 Jun 2026.)
Q: "Could it replace our CI or release pipeline?" No, and the blog says so in as many words: these do not replace build, test or release pipelines. This is for work that needs interpretation. Say that limit out loud as well as showing it; naming it early buys trust.
```

### M7. Slide 7: attribute the architecture claim, and don't point at "a job" when a real file is coming
"The model never runs in a job that has write scopes" is his sentence standing in front of the docs' sentence. Quoting first and concluding second is the same length and shifts the burden onto GitHub's page. The forward reference to the frontmatter slide also makes the abstract claim checkable three slides later.

**OLD**
```
Technical version: least privilege by job boundary. "The agent job runs with minimal read-only permissions, while write operations are deferred to separate jobs" (gh-aw architecture docs). The model never runs in a job that has write scopes.
```
**NEW**
```
Technical version: least privilege by job boundary. Quote it exactly, because it's the architecture's claim rather than mine: "The agent job runs with minimal read-only permissions, while write operations are deferred to separate jobs" (gh-aw architecture docs).
So the model never runs in the job that holds the write token — and the frontmatter slide shows what that looks like in a real file: permissions: read-all.
```

### M8. Slide 10: the room's first objection is "merged by whom?", and there is no prepared answer
He already says the post doesn't name the repos. The step he is missing is turning that admission into the reason for the pilot, which is the same move the ask slide makes. Nothing new is claimed — the answer is "the post doesn't say".

**OLD**
```
Caveat out loud: reported by GitHub, small samples; the post doesn't say which repos. Merged is not the same as correct.
```
**NEW**
```
Caveat out loud: reported by GitHub, small samples, and the post doesn't say which repositories. Merged is not the same as correct.
Q: "Merged by whom, though?" Fair, and the honest answer is that the post doesn't say who reviewed them or where they ran. That gap is exactly what a month of our own runs would fill.
```

### M9. Slide 10: give the CNCF quote its title and its status
`sources.md` has the exact title — CTO, Cloud Native Computing Foundation — and it costs four words. The status line matters more: it is a customer quote inside a vendor blog post, which is colour, not evidence, and saying so is cheaper than being told.

**OLD**
```
Outside evidence if asked: "Inside of CNCF, we are benefiting from improved documentation automation along with improving team reporting across the organization." Chris Aniszczyk, CNCF, GitHub Blog, 13 Feb 2026.
```
**NEW**
```
Outside evidence if asked: "Inside of CNCF, we are benefiting from improved documentation automation along with improving team reporting across the organization." Chris Aniszczyk, CTO of the Cloud Native Computing Foundation, GitHub Blog, 13 Feb 2026. A customer quote in a vendor post — use it as colour, not as proof.
```

### M10. Slide 11: the answer that rescues the slide rests on a self-report, and doesn't say so
The careful-wording line above it is exemplary. But the answer to "so none of this actually works?" asserts that the frontmatter and safe outputs are valid, on the strength of a compile result from the repository's own `agents.md`, with no lock files committed to show anyone. Marking it in six words keeps the answer and removes the only line on this slide that outruns its evidence.

**OLD**
```
Q: "So none of this actually works?" Four compile cleanly against the pinned gh-aw version, so the frontmatter and safe-outputs are valid. Runtime behaviour is unproven, and that is exactly what a month of real runs would prove.
```
**NEW**
```
Q: "So none of this actually works?" Four compile cleanly against the pinned gh-aw version, so their frontmatter and safe outputs are valid — self-reported, and with no lock files committed, I can't show you the artefact. Runtime behaviour is unproven, and that is exactly what a month of real runs would settle.
```

### M11. Slide 11: the version pin is the one number on this slide with no stated source
Everything else in the note is labelled (GitHub API, or the repo's `agents.md`). `v0.83.4` is read from the repository and has never been exercised by a run, so it belongs in the same convention.

**OLD**
```
Technical detail: 98 markdown briefs in workflows/, each with a docs page in docs/workflows/ carrying the same required-fields table. Six shared modules under workflows/shared/ are imported rather than copy-pasted, so a safety change lands in one place. aw.yml pins min-version v0.83.4.
```
**NEW**
```
Technical detail: 98 markdown briefs in workflows/, each with a docs page in docs/workflows/ carrying the same required-fields table. Six shared modules under workflows/shared/ are imported rather than copy-pasted, so a safety change lands in one place. Its aw.yml pins gh-aw min-version v0.83.4 — read from the repository, never exercised by a run.
```

### M12. Slide 13: date the quote and give the appendix note a hand-off
The slide credits "GitHub Blog" with no date; the note should carry the date and post title so a question about it is answerable without the slide. Appendix notes also need the equivalent of a transition — slide 15's note has one ("pull it up if…"), this one doesn't.

**OLD**
```
For managers: there's a receipt for every run.
```
**NEW**
```
For managers: there's a receipt for every run, and it's the same receipt any other Action leaves.
The quote is from the GitHub Blog post of 13 Feb 2026, "Automate repository tasks with GitHub Agentic Workflows".
Appendix slide: pull it up when someone asks how we'd know what it did.
```

### M13. Slide 14: the plain-English line is third, and two pieces of advice are presented as documentation
Order first: the line that unlocks the slide for the non-technical half is currently buried under two technical ones. Then two attributions. The quick start does say to commit both files — "and both get reviewed" is his advice. And the docs tell you to regenerate with `gh aw compile`; they don't actually forbid hand-editing the lock file, so "the lock file is generated" is a rule he's imposing, which is a better thing to say than a rule he's inventing.

**OLD**
```
Below the frontmatter is the job description, in plain English. The real body is a page of style rules — it names the Diataxis framework and forbids pushing to the default branch; this one line is a paraphrase.
gh aw compile turns the markdown into a .lock.yml, ordinary GitHub Actions YAML. You commit both, and both get reviewed.
For non-technical listeners: the settings are the rules, the body is the request, and compile turns them into something GitHub already knows how to run.
Q: "Do I need to edit the YAML?" No: edit the markdown and recompile; the lock file is generated.
```
**NEW**
```
Plain line first: the settings are the rules, the body is the request, and compiling turns the pair into something GitHub Actions already knows how to run.
Below the frontmatter is the job description, in plain English. The real body is a page of style rules — it names the Diátaxis documentation framework and forbids pushing to the default branch. The line on the slide is my paraphrase, not a quote.
gh aw compile turns the markdown into a .lock.yml, ordinary GitHub Actions YAML. The quick start says to commit both files; that both then get reviewed is my advice, not theirs.
Q: "Do I need to edit the YAML?" Treat it as generated: edit the markdown and recompile. The docs tell you to regenerate with gh aw compile — they don't actually forbid hand-editing it, so that rule is mine.
```

### M14. Slide 16: three lines, one of which repeats the slide, and no hand-off
"The agentics repo is where today's update-docs.md came from" is already the third bullet on the slide. Replace it with what the note should carry: the check date, what the gallery is for someone who wants to try it tonight, a decision about the TODO bullet, and the hand-off past the sources slide behind it.

**OLD**
```
Leave this up during questions.
The agentics repo is where today's update-docs.md came from.
TODO: my own examples and URLs.
```
**NEW**
```
Leave this up during questions. Don't read it out; point at it.
The three live links were checked on 17 Oct 2026. The gallery is GitHub's own set of ready-made workflows, which is the fastest route for anyone who wants to try one after this.
TODO: my own examples and URLs. Decide whether that bullet survives — an empty promise on the links slide is worse than one fewer link.
Transition: this is the last slide I mean to show. The one behind it is my source ledger, for a number that gets challenged.
```

---

## SKIP — considered and rejected

- **Writing slide 4's story or slide 12's decision rule.** Deliberately his. Both TODOs are left verbatim; M3 and H3 only add shape and caution around them.
- **Reinstating the 72.6% trustworthiness figure on slide 2.** `sources.md` records it as could-not-verify. The TODO line stays exactly as written.
- **Changing every "slide N" callback to a name-based reference.** The deck reordered twice today, so numbered callbacks are a standing hazard — but all four surviving ones (slide 2 from slides 3 and 12, slide 5 from slide 9, slide 9 from the links slide) are correct in this version, and rewriting notes purely for future-proofing adds diff risk for no delivery gain. Where a patch already touched the line, I switched to a name ("the survey slide", "the teammate slide", "the frontmatter slide").
- **Slide 5's transition, "before I show you the file".** The file is four slides later, not next. It still reads correctly as framing for the safety block that intervenes, and it is the best sentence in that note.
- **Shortening slide 11's note.** It's the longest in the deck and the most question-dense. It's also the slide where his credibility is decided, and every line is doing work. M10 and M11 touch two sentences and leave the length alone.
- **Adding percentages to "88 of 103, 10 of 10" on slide 10.** 85% and 100% are in `sources.md`, but the raw counts are the honest form for samples this small, and the percentages invite a comparison the post doesn't support.
- **Adding `GH_AW_DEFAULT_MAX_AI_CREDITS` to slide 6.** Verified and real, but it's a spoken note about cost for a mixed room; an environment-variable name is where precision tips into noise.
- **Pushing the daily-cap conflict onto a slide.** Root `CLAUDE.md` forbids it when official sources conflict. It stays in slide 6's note and on the status slide, which H12 now makes explicit.
- **Trimming slide 8's "sealed room / phone numbers" plain line.** It's the best non-technical image in the deck.
- **Flagging slide 9's note for "the firewall" gloss on `network: defaults`.** H4 drops the parenthetical because the previous slide now owns the firewall, but the gloss itself was accurate.

---

## NOT APPLIED — slide body observations

1. **Slide 11's title overclaims against its own table.** "Running it is the one step left" sits directly above a row saying 4 of 98 compiled and 94 are still briefs. Compiling the other 94 is also a step left, and it's the second thing a technical reader will notice after the 98. The note's careful-wording block is scrupulous about this; the title isn't. Something like "written and documented; running it is the step I haven't taken" keeps the claim and the honesty.
2. **Slide 16 bullet 3 hard-codes "slide 9's `update-docs.md`".** Correct today, and it's visible to the audience alongside page numbers — but this deck has reordered twice in one day, and that bullet is the one place a reorder silently produces a wrong slide. "the frontmatter slide shown earlier" costs nothing.
3. **Slide 6's cost line still shows `~$10` with no status.** The slide says "1,000 AI Credits (~$10) by default". The docs call credits best-effort, so the dollar figure is an approximation of an approximation. The muted source line already covers the page; a two-word "approximate" would cover the number.
4. **Slide 13 credits the quote to "GitHub Blog" with no date,** while every other source line in the deck carries one. M12 puts the date in the note; the slide could carry it too.
5. **Slide 15's bullet says `gh aw trial` is "(experimental)".** Precisely, the TrialOps *page* marks TrialOps experimental; the CLI page doesn't label `trial` itself. The slide's shorthand is defensible and errs toward caution, so I'd leave it — noting it only because it's the kind of thing `sources.md` flags.

---

## Claims in the notes that `sources.md` does not cover

Not errors — gaps in the ledger. Each is a factual product claim he would say out loud, with no row behind it. Worth either verifying before the talk or dropping.

- **Slide 8: "`network: {}` is no access at all."** The ledger verifies `network: defaults` (basic infrastructure, and the default when omitted) but has no row for `network: {}`. I did not change the line, since weakening a caveat is worse than flagging it.
- **Slide 8: "`bash: ["gh issue comment"]` limits bash to that one command."** No ledger row. It's the most concrete example in that note and the one most likely to be repeated back.
- **Slide 11: `aw.yml` pins `v0.83.4`.** From his own repository, so it can't be checked against GitHub's docs — M11 labels it rather than removing it.
- **Slide 14: "Diataxis"** is spelled without the accent in the note (Diátaxis). Fixed in M13 in passing.

---

## How to apply and verify

Every OLD string above is verbatim from `deck.md` at md5 `046c6d7c70b3ca8b5b316e28c9d18e75` and was checked to occur exactly once. To re-check after any further edit:

```
python3 - <<'PY'
import re, pathlib
deck = pathlib.Path('deck-v2/deck.md').read_text()
blocks = re.findall(r'\*\*OLD\*\*\n```\n(.*?)\n```\n\*\*NEW\*\*', pathlib.Path('deck-v2/notes-pass.md').read_text(), re.S)
for i, old in enumerate(blocks, 1):
    print(i, deck.count(old), repr(old[:60]))
PY
```

Every line must print a count of `1`. Then render and check nothing changed visually (notes don't affect layout, so this is a formality):

```
marp deck-v2/deck.md --allow-local-files --images png -o <scratchpad>/slide.png
marp deck-v2/deck.md --notes -o <scratchpad>/notes.txt
python3 deck-v2/check_deck.py
```
