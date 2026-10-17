# GitHub Agentic Workflows — Presentation Spine

**Story in one line:** We ship faster than our docs can keep up. AI agents can now do the work, not just suggest it. GitHub Agentic Workflows let them keep repos up to date automatically. Here's how, and here's what I'm asking for.

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
- **Footer:** my name · date

## Audience
Mixed: technical and non-technical. Titles and pictures are plain language for everyone; technical detail sits in a short "For the technical" line per slide.

## Presentation sequence

Main talk: title plus 11 slides. Eight appendix slides hold technical depth and supporting evidence.

### Slide 1 — Shipping faster quietly creates documentation debt
- **Shows:** 56.5% of 12,374 developers name outdated information as a context blocker (Stack Overflow 2026), plus the earlier attempt; tool and gap TODO.

### Slide 2 — Documentation debt builds up between doc passes
- **Shows:** illustrative chart (no data): code steps up with each change, docs catch up only at doc passes; the gap is the debt.

### Slide 3 — Agents move people from carrying changes to reviewing them
- **Shows:** two-row diagram: assistance (person carries the change by hand) versus workflow (agent proposes a draft PR, person reviews).

### Slide 4 — Agents add a third lane beside CI and CD
- **Shows:** CI "Builds it", CD "Ships it", Continuous AI "Improving your repo, around the clock" (gh-aw docs); predictable versus judgement is this deck's framing.

### Slide 5 — Good agent output is a diff you can judge at a glance
- **Shows:** real public PR #8716 with a simplified before/after; explicitly a Copilot follow-up, not our run.

### Slide 6 — Guardrails live in reviewable config, not the model
- **Shows:** the verified public Update Docs file, trimmed, with the teammate model.

### Slide 7 — Safety is designed in, not left to the model
- **Shows:** prepare → agent → detection → safe-output pipeline with the write boundary; detection is a layer, not a guarantee (outcomes in the appendix).

### Slide 8 — Price each run in AI credits and reviewer minutes
- **Shows:** equation: (AI credits + Actions minutes + reviewer minutes) ÷ accepted changes = cost per useful change; 1,000 AIC default cap; pilot limits TODO.

### Slide 9 — Four weeks turns opinion into evidence
- **Shows:** four-week timeline; week 1 previews outputs with `staged: true`; proposed measurements.

### Slide 10 — The pilot's risk is boxed in on five sides
- **Shows:** nested bounds: four weeks, capped spend (TODO), one repo and owner (TODO), docs only, draft PRs only; a person decides what merges.

### Slide 11 — The ask is small, capped and reversible
- **Shows:** proposed candidate, scope and go/no-go criteria; repo, owner, budget and thresholds TODO.

### Appendix 12 — Compilation turns that file into an Actions workflow
- **Shows:** compile-and-publish details for technical questions.

### Appendix 13 — Detection adds a review gate, not a safety guarantee
- **Shows:** threat, warning and permitted-output branches; failure behaviour qualified.

### Appendix 14 — GitHub reports strong results for selected docs workflows
- **Shows:** reported documentation merge counts, with sample caveats.

### Appendix 15 — Use agents where interpretation adds value
- **Shows:** task-fit guidance and autonomy TODO.

### Appendix 16 — Start with one workflow from the example collection
- **Shows:** the user’s example collection (repo/file TODO) and installation.

### Appendix 17 — A trial can run in a temporary private repository
- **Shows:** experimental trial in a temporary private repository.

### Appendix 18 — Staged mode previews safe outputs before they are applied
- **Shows:** staged-mode configuration and steps for technical questions.

### Appendix 19 — The technical claims are grounded in GitHub’s documentation
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
