# GitHub Agentic Workflows — Presentation Spine

**Story in one line:** We ship faster than our docs can keep up. AI agents can now do the work, not just suggest it. GitHub Agentic Workflows let them propose the fix as a draft pull request, with a person deciding what merges. Here's how, and here's what I'm asking for.

## Style — GitHub dark theme (Primer colours)
| Use | Colour | Hex |
|---|---|---|
| Background | Canvas dark | `#0d1117` |
| Panels / cards | Canvas subtle | `#161b22` |
| Borders | Border | `#30363d` |
| Main text | Foreground | `#e6edf3` |
| Secondary text | Muted | `#7d8590` |
| Accent / links / headings | Blue | `#2f81f7` |
| Agent / AI highlights | Purple | `#a371f7` |
| Success / "it works" | Green | `#3fb950` |
| Code font | Monospace | `SFMono-Regular, Consolas, monospace` |

## Title slide
- **Title:** GitHub Agentic Workflows
- **Subtitle:** From AI that suggests to AI that does
- **Shows:** dark `#0d1117` background, title in `#e6edf3`, subtitle in `#7d8590`, a thin blue-to-purple (`#2f81f7` → `#a371f7`) accent line, a small terminal-style snippet in monospace, e.g. `gh aw run update-docs`
- **Hook (visible on slide):** "When did a page of documentation last mislead you?"
- **Footer:** my name · date

## Audience
Mixed: technical and non-technical. Titles and pictures are plain language for everyone; technical detail sits in a short "For the technical" line per slide.

## Presentation sequence

Main talk: title plus 15 slides. Ten appendix slides hold technical depth and supporting evidence.

### Slide 1 — Outdated documentation already costs developers time
- **Shows:** 56.5% of 12,374 developers name outdated information as a context blocker (Stack Overflow 2026), with the caveat that it is a multi-select survey about context in general, not our repositories.

### Slide 1b — My earlier attempt solved part of the problem, and left a gap
- **Shows:** the presenter's own earlier tool and the gap it left. Tool, what it solved and the remaining gap are TODO placeholders until supplied.

### Slide 2 — Documentation debt accrues between doc passes
- **Shows:** illustrative chart (no data): code steps up with each change; each doc pass closes only part of the gap. Cites Cunningham (1992) for the debt metaphor.

### Slide 3 — The ask is four weeks, one repository, and docs only
- **Shows:** the ask stated up front so the audience can weigh the evidence against it: four weeks, one repository, docs only, every change a draft pull request a person decides on. Repository, owner, budget and week-four thresholds TODO.

### Slide 4 — Agents shift the human role from execution to review
- **Shows:** two-row diagram: assistance (person carries the change by hand) versus workflow (agent proposes a draft PR, person reviews; review highlighted). Also carries who does what: the agent drafts, a person decides what merges; this moves work from writing to judging rather than removing it; reviewer minutes TODO. The full who-does-what diagram is Appendix 8.

### Slide 5 — Scripts check fixed rules; an agent is for the part that needs reading
- **Shows:** a fixed rule (broken links, missing API entries, formatting, doctests, API diffs) belongs in a deterministic tool; deciding whether prose still describes the code is judgement-heavy and only partly checkable. TODO: whether CI runs on agent-opened PRs is unverified.

### Slide 6 — The unit of review is one small diff
- **Shows:** real public PR github/gh-aw#68654 ([docs] Update glossary - daily scan, +8/-0 in 1 file, merged 14 Oct 2026): a documentation agent's output at its real size. GitHub's repository, not our pilot.

### Slide 7 — In three of GitHub's documentation workflows, most pull requests were merged, but not all
- **Shows:** reported merge counts (57/59, 88/103, 10/10) with denominators, labelled selected samples from other repositories, not a forecast.

### Slide 8 — It will be wrong sometimes, and that has to be survivable
- **Shows:** the four ways this fails — wrong prose, an over-wide diff, poisoned input, spend with nothing merged — and that each is bounded by a limit we set rather than by trusting the model. Our own error rate is unmeasured; week one's staged preview is the first measurement.

### Slide 9 — The limits live in a file you can read, not in the model
- **Shows:** the real Update Docs frontmatter, trimmed, including bash, web-fetch, network defaults and protected-files (semantics unconfirmed, TODO), with the teammate model.

### Slide 10 — The agent job has no write access; writes happen in a separate job
- **Shows:** prepare → agent → detection → safe-output pipeline with the write boundary; cites least privilege (Saltzer & Schroeder, 1975). Detection is a layer, not a guarantee.

### Slide 11 — A cheap run nobody merges is still expensive
- **Shows:** plain visual: (AI credits + compute + reviewer time) ÷ changes accepted, each term marked NOT MEASURED; pilot limits TODO. Plain sentence first (cost per accepted change); the equation and 7-row symbol table are Appendix 9.

### Slide 12 — Each week of the pilot has one job
- **Shows:** four-week timeline; week 1 previews outputs with `staged: true`; proposed measurements.

### Slide 13 — Week four ends in a decision we agreed in advance
- **Shows:** three gates in a row - useful fixes a reviewer agreed were real, less total effort than the agreed manual baseline, spend within the caps - all must pass; agreed before week one so the result can say stop. Thresholds and baseline TODO.

### Slide 14 — The downside is bounded by five proposed limits
- **Shows:** nested proposed bounds: four weeks, spend limit (TODO), one repo and owner (TODO), docs only by instruction and reviewed in the diff, draft PRs only; a person decides what merges. Proposals, not enforced yet.

### Slide 15 — Approve a four-week, docs-only pilot
- **Shows:** hero ask; public preview since 11 Jun 2026; candidate workflow, "switch off at any time"; checklist "to decide before week one": repo + owner, budget, thresholds + baseline (all TODO).

### Appendix 16 — Compilation turns that file into an Actions workflow
- **Shows:** compile-and-publish details for technical questions.

### Appendix 17 — Agents add a third lane beside CI and CD
- **Shows:** CI "Builds it", CD "Ships it", Continuous AI "Improving your repo, around the clock" (gh-aw docs).

### Appendix 18 — Detection adds a review gate, not a safety guarantee
- **Shows:** threat, warning and permitted-output branches; failure behaviour qualified.

### Appendix 19 — Use agents where interpretation adds value
- **Shows:** task-fit guidance and autonomy TODO.

### Appendix 20 — Start with one workflow from the example collection
- **Shows:** the user’s example collection (repo/file TODO) and installation.

### Appendix 21 — A trial can run in a temporary private repository
- **Shows:** experimental trial in a temporary private repository.

### Appendix 22 — Staged mode previews safe outputs before they are applied
- **Shows:** staged-mode configuration and steps for technical questions.

### Appendix 8 — The agent drafts; a person decides what merges
- **Shows:** full who-does-what diagram: the agent reads, drafts and opens a draft PR; a person owns the workflow file, reviews, decides, and merge or close are both correct.

### Appendix 9 — Cost per accepted change is a formula the pilot fills in, not a number we have
- **Shows:** the equation and a 7-row symbol table (A, p_a, M, p_m, R, w, N_acc); every value TODO or not measured except the estimated 0.01 per AI credit.

### Appendix 25 — The technical claims are grounded in GitHub’s documentation
- **Shows:** official status, sources and unresolved documentation conflicts.

## Deck v2 spine (`deck-v2/deck.md`, 17 Oct 2026)
The sections above describe deck v1 and `draft-overview.html`. Deck v2 follows its own arc: why now → what it is → proof → the ask, then an appendix.

The main talk is ten slides and runs as an objection ledger, not a feature tour: it is a teammate (5), **but** it can be wrong (6), **therefore** the writes are separated and checked (7), here is the whole job (8), here is what it produced (9), here is the ask (10). Reference material — compile, trigger routes, debugging — sits in the appendix.

| # | Section | Title | Shows |
|---|---|---|---|
| 1 | — | Repos that keep themselves up to date | Title and promise; presenter and date TODO |
| 2 | Why now | Somewhere in our docs, a page is wrong right now, and nobody knows which one | 56.5% stat (Stack Overflow 2026) |
| 3 | Why now | As AI climbs the autonomy ladder, we ship more code than ever | Ladder diagram, Octoverse numbers; our level TODO |
| 4 | Why now | I built something similar before, and it showed me what was missing | TODO: earlier project |
| 5 | What it is | An agentic workflow is a GitHub Action whose job is written in plain English and done by an AI agent | Teammate model; typical jobs |
| 6 | What it is | It can still get things wrong, so it is built to be checked, not trusted | Four risks with their safeguards, plus the bad-fit line; measured cost TODO |
| 7 | What it is | The agent never holds a write token | Run-jobs diagram; detection qualified, not overclaimed |
| 8 | What it is | The settings say when it runs, what it can read, and the one thing it can send | Real `update-docs.md` frontmatter |
| 9 | Proof | GitHub reports that 57 of 59 pull requests from its docs workflow were merged | 57/59 stat; TODO: our own pull request |
| 10 | The ask | Pick one stale page, and let an agent keep it current for a month | Decision first (TODO), four plain steps |
| 11–15 | Appendix | You debug it like any Action; The instructions are plain English (compile); You can start a workflow four ways; Try it yourself (links); Status and sources | Logs and audit; compile diagram; trigger routes; links; fact-check notes |

## Background: quotes and references (historical slide numbers; checked 16 Oct 2026)
- **Slide 1, the problem is old and real:** "Documentation is always outdated relative to the current state of a software system": about two-thirds of 45 developers agreed (Lethbridge, Singer & Forward, IEEE Software, 2003; old and small, say so)
- **Slide 1, autonomy ladder:** L1 to L5 levels (Feng et al., arXiv 2506.12469)
- **Slide 3, the big idea:** "Coding agents bring new, magical powers to repository automation" (Don Syme, GitHub Next, 13 Feb 2026)
- **Slide 3, plain English:** "authored in plain Markdown and executed with coding agents" (Don Syme & Peli de Halleux, GitHub Blog)
- **Slide 3, where it fits:** "A third pillar beside CI and CD" (gh-aw docs); Continuous AI is "the integration of AI into the SDLC, enhancing automation and collaboration" (GitHub Blog)
- **Slide 5, docs use case:** "Updates docs from recent code changes." / "Finds and fixes broken links in your docs." (gh-aw docs)
- **Slide 6, humans stay in charge (L4):** human review is the proposed pilot policy; `draft: true` is enforced for PR creation, but automatic merging is not universally prohibited.
- **Slide 6, safety:** "Agents read by default. Every write is checked before it lands." / "An API proxy holds the tokens, so the agent never sees them and cannot leak them." (gh-aw docs)
- **Slide 6, not a fit:** "They do not replace build, test, or release pipelines" (GitHub Blog)
- **Slide 6a, cost:** use official AI-credit controls and measured pilot usage; see the [cost reference](https://github.github.com/gh-aw/reference/cost-management/).
- **Slide 8, safe first step:** "Try it safely: staged: true previews every output without writing anything." (gh-aw docs)
- **Slide 9, empowerment:** "developers, teams and communities should be empowered to shape their use" (Don Syme, GitHub Next)
- **Slide 1, autonomy for everyone (paraphrase only):** Andrej Karpathy's "autonomy slider" and "Iron Man suits, not robots": AI that augments people, with humans in control ("Software Is Changing (Again)", YC AI Startup School, June 2025). Take exact wording from the video captions before quoting
- **Slide 1, where this is heading (secondhand, paraphrase):** Boris Cherny, creator of Claude Code, has said he no longer prompts Claude directly but writes loops that prompt it, shifting his job from writing code to orchestrating agents (Acquired interview, via WorkOS notes)
- **Slide 3, plain English (confirmed):** "The hottest new programming language is English" (Andrej Karpathy, X, 24 Jan 2023; traced by Quote Investigator)
- **Slide 7, customer proof, docs (verbatim):** "Inside of CNCF, we are benefiting from improved documentation automation along with improving team reporting across the organization." (Chris Aniszczyk, CTO, CNCF, GitHub Blog)
- **Slide 5 or 7, customer proof, maintainers (verbatim):** "No human can track what's trending or which problems affect the most users. I've built GitHub Agentic Workflows that analyze issues and surface what matters: that's the kind of judgment amplification that actually helps maintainers." (Franck Nijhof, Home Assistant, GitHub Blog)
- **Slide 6 or 9, confidence at scale (verbatim):** "The flexibility and built-in controls give us confidence to leverage Agentic Workflows across complex systems at Carvana." (Alex Devkar, Carvana, GitHub Blog)
- **Screenshots:** `reference/screenshots/` holds captures of the gh-aw docs, GitHub Blog post, customer quotes, Don Syme's post and the Karpathy quote origin (16 Oct 2026)
- **Status:** public preview since 11 Jun 2026, rechecked 17 Oct 2026 against the [GitHub changelog](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/). Technical additions checked against linked official sources in `deck-v1/deck.md` on 17 Oct 2026.
- **Sources:** github.github.com/gh-aw · github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows · githubnext.com/posts/dsyme-automate-repository-tasks-agentic-workflows · Lethbridge et al. 2003 (IEEE Software)
