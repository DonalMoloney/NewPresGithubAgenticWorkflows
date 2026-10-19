# Deck v4: better resources and alternative slide content

Research pass, 18 Oct 2026. `todo.md` lists what is broken; this file lists **what better material exists to put there**.

Scoped to v3's arc — **demonstrate before you defend**: the mechanism act (slides 7–13) then the safety act (14–16), then proof. So the material here is mechanism and real artifacts. Survey and audience evidence is in `../deck-v2/RESOURCES.md`; cost arithmetic and GitHub Actions pricing in `../deck-v1/RESOURCES.md`. Deliberately not repeated here.

**Status labels** (deck vocabulary): **Measured** = counted, method named · **Documented** = gh-aw docs · **Reported by GitHub** = GitHub's own claim · **Self-reported** = my repo.

All figures fetched or counted **18 Oct 2026**.

> **Slide numbers drift — confirm by title.** All three decks were edited while this file was being written: deck-v2 gained a slide and reordered, deck-v3 shifted by one from slide 5 on, and several deck-v1 titles changed. The numbers below were correct at **18 Oct 2026**; the **titles** are the reliable anchor. Check the title before editing a slide.

| § | Slide(s) | Title(s) as of 18 Oct 2026 |
|---|---|---|
| 1 | 11, 18 | (compile-flow continuation of "The instructions are plain English…") · Ninety-eight of these are written and documented, and not one has ever run |
| 2 | 17 | GitHub reports that 57 of 59 pull requests from its docs workflow were merged |
| 3 | 13 | Thirteen lines say when it runs, what it can read, and the one thing it can send |
| 4 | 16 | A misled agent is boxed in by layers, not by any single wall |
| 5 | 14, 15 | It will get things wrong, so it is built to be checked, not trusted · The agent never holds a write token: a separate, checked job does the writing |
| 6 | 23 | Status and sources |
| 7 | 8 | It does three kinds of work, and documentation is the safest corner to start in |
| 8 | 21 | You debug it like any Action: every run leaves logs you can audit |



## v4 additions (18 Oct 2026)

Deck v4 is a TED-style redesign of v3 with a tighter spine (one question, one number, one turn, one ask; the rest is appendix). Everything below the next table was written for v3 and still applies, but **its slide numbers are v3's**: use the titles. New material found for v4 is listed here first, each with a primary source fetched 18 Oct 2026.

| New finding | Source | Where it landed in v4 |
|---|---|---|
| **The 57/59 figure is the best row of seven.** Same post: Glossary Maintainer 10/10, Multi-device Docs Tester 2/2, Documentation Unbloat 88/103 (85%), **Documentation Noob Tester 9/21 (43%)**, **Slide Deck Maintainer 2/5 (40%)**; Blog Auditor is audit-only. The post does not say which repos. Authors: Don Syme, Peli de Halleux, Mara Kiefer. | https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/ | "Proof" slide line, notes, status slide. It makes 96% believable and shows why the pilot measures its own number. |
| **Peli's Agent Factory**: the team says it has built and run over 100 agentic workflows in `github/gh-aw`, mostly on the project itself, some at scale in GitHub internal repos. A Factory Tour Workshop repo is linked from the package README. Reported by GitHub, not independently counted. | https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/ | Links slide (appendix). The 344 count in section 1 below is the measured version. |
| **An honest practitioner account**: Nicolas Fränkel, dev.to 16 Apr 2026 (first on blog.frankel.ch, 12 Apr). Pushed Markdown without compiling it, hit permission problems, later got the documentation workflow working. Third-party and anecdotal. | https://dev.to/nfrankel/a-github-agentic-workflow-9b7 | Earlier-attempt slide notes (outside voice); links slide as a labelled anecdote. |
| **Docs site status lag**: the gh-aw home page still labels itself "Technical preview" and links a technical-preview deck; the changelog confirms public preview from 11 Jun 2026. | https://github.github.com/gh-aw/ and the changelog link below | Status slide. |
| **Learning paths on the docs site**: Quick start, Creating workflows, Using at scale, a hands-on workshop, topic pages for Security architecture, Cost management, Safe outputs, Threat detection, Integrity filtering, Self-hosted runners, Engines, OpenTelemetry and Outcomes. | https://github.github.com/gh-aw/ | Links slide. "Outcomes" and "Using at scale" are unread; read before citing. |
| **Customer quotes in the public-preview changelog** (Carvana, Marks & Spencer, Hud.io). Vendor-published quotes: colour, not proof. The Hud.io line is already used in notes. | https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview | Notes only. |
| **Talk craft (second-hand, not verified against the book)**: Chris Anderson, *TED Talks: The Official TED Guide to Public Speaking* (2016). A review summarises a one-idea throughline stated in under 15 words and four ways to open. I could not confirm the exact wording from the book itself. | Book; review summarised at francistapon.com | Design rationale for the spine, not cited on any slide. Verify against the book before quoting. |

Not found, so not used: a formal GitHub case study with metrics for documentation workflows (searched 18 Oct 2026).

**v4 title map (use titles, not v3 numbers):** the question and the 56.5% slides are new framing around the survey number; "Ninety-eight of these are written and documented…" is the v3 slide of the same name; the three-kinds-of-work, triggers, autonomy ladder, one-page spec and debugging slides moved to the appendix.

---

## 1. The single strongest fact this deck does not yet have: GitHub runs 344 of these on gh-aw itself

**Measured**, GitHub contents API on `github/gh-aw/.github/workflows`, 18 Oct 2026 — 737 entries returned, well inside the API's 1,000-entry page limit, so this is a complete count, not a truncated one:

| In `github/gh-aw/.github/workflows` | Count |
|---|---|
| **Agentic workflow `.md` files** | **344** |
| **Committed `.lock.yml` files** | **344** |
| Ordinary CI `.yml` (not agentic) | 41 |
| Other files | 8 |

The repo is **public, MIT licensed, 5,418 stars**, created 2025-08-12, last pushed 2026-10-18.

```bash
gh api repos/github/gh-aw/contents/.github/workflows \
  --jq '[.[].name] | {md: (map(select(endswith(".md")))|length),
                      lock: (map(select(endswith(".lock.yml")))|length)}'
```

### Why this is worth two different slides

**(a) Slide 11 (compile flow) — the 1:1 pairing is proof, not advice.**
The slide's diagram says both the authored `.md` and the generated `.lock.yml` "are committed and reviewed together in a pull request". **344 ↔ 344, exactly** — in GitHub's own repository, every single authored workflow has its compiled lock file committed beside it. Zero exceptions in 344 cases. That turns a documented instruction ("Commit **both** files") into an observed practice, which is a much better muted line: *Measured: 344 agentic workflow files and 344 committed lock files in github/gh-aw, counted 18 Oct 2026.*

**(b) Slide 18 — it is the counterweight that makes the honesty land.**
Slide 18 says, correctly and bravely, that 98 of Donal's workflows are written and **not one has ever run**. On its own that is a confession. Beside the 344 it becomes a *comparison*, and the slide's argument gets stronger:

| | `DonalMoloney/Agentic-Workflows-Lib` | `github/gh-aw` |
|---|---|---|
| Workflow briefs written | 98 | 344 |
| Compiled lock files committed | 4 (self-reported, none committed) | **344** |
| Ever run in GitHub Actions | **0** | thousands (see §2) |

The honest reading to say out loud: *"The gap between those two columns is not a gap in the technology. It is the gap this pilot closes."* That is a far better use of slide 18 than an apology, and it needs no new work from Donal — only a count anyone can repeat.

---

## 2. Slide 17 (the 57/59 slide): a public denominator, and three artifacts of different kinds

### The number that survives scrutiny
**Measured**, GitHub search API, bot-authored pull requests, window 2025-08-20 → 2026-10-18:

| Repository | Agent PRs | Merged | Closed unmerged | Merge rate |
|---|---|---|---|---|
| **github/gh-aw** | 4,034 | 2,688 | 1,346 | **66.6%** |
| githubnext/agentics | 52 | 31 | 20 (+1 open) | 59.6% |

GitHub's 57/59 (96%) is **Reported by GitHub** with an unstated set of repos and n=59. This is **Measured**, public, n=4,034, and recountable live. For a mechanism-first deck the lower number is the better one: *about a third of what the agent proposes gets rejected by a person* is the review loop working, which is precisely what slides 13–15 just argued.

**Caveat:** the filter is `author:app/github-actions` — every Actions-authored PR, not provably only agentic ones. The workflow-name prefixes in the titles are strong evidence. Say "bot-authored", not "agentic".

### Three real artifacts, each a different kind of work
Slide 17 has a TODO for "screenshots and recordings of a real pull request, issue and comment". These are public, merged, and need no token scope and no run of Donal's own. They are chosen to map onto slide 7's three kinds of work, and are **different PRs from the one deck-v2 uses** (`#394`), so the two decks do not show the same screenshot:

| Kind of work (slide 8) | Real merged PR | Diff | Merged |
|---|---|---|---|
| **Improve code** | [github/gh-aw#69936](https://github.com/github/gh-aw/pull/69936) `[dead-code] chore: remove dead functions — 2 functions removed` | **+0 / −201**, 4 files | 2026-10-18 |
| **Report and plan** | [github/gh-aw#69394](https://github.com/github/gh-aw/pull/69394) `[blog] Agent of the Day – 2026-10-16` | **+49 / −0**, 1 file | 2026-10-16 |
| **Maintain** | [github/gh-aw#68929](https://github.com/github/gh-aw/pull/68929) `[community] Update community contributions in README` | **+10 / −9**, 1 file | 2026-10-15 |

**Measured** via the pulls API, 18 Oct 2026.

Why these three: they show that the *shape of the output is the same* — a reviewable pull request — regardless of whether the agent deleted 201 lines of code, wrote a blog post, or edited a README. That is the mechanism claim of the whole deck, demonstrated three ways on one slide. The `[dead-code]` one is especially useful: an agent **deleting** code is the case the room worries about, and it still arrives as a diff someone approved.

---

## 3. Slide 13 (the thirteen-line file): the deck shows five settings of about fifty

The slide's title is "Thirteen lines say when it runs, what it can read, and the one thing it can send", and it is already honest that the frontmatter is trimmed. Quantifying the trim makes the slide stronger and arms the Q&A.

**Measured** from the frontmatter reference's own section headings: **50 documented frontmatter settings**. Slide 13 shows five (`on:`, `permissions:`, `network:`, `safe-outputs:`, `tools:`).

The ones most worth knowing exist, grouped by the question an audience member would actually ask:

| "Can you limit…" | Documented field |
|---|---|
| …how long it can think? | `timeout-minutes:`, and `jobs.agent.timeout-minutes` |
| …how much it can spend? | `max-ai-credits:`, `max-daily-ai-credits:` |
| …how many times it loops? | `max-turns:`, `max-turn-cache-misses:` |
| …how often a person can trigger it? | `user-rate-limit:` |
| …which files it may touch? | `protected-files:` (safe-outputs, supply-chain protection) |
| …whether a human must approve first? | `environment:` — GitHub **Environment Protection** |
| …running two at once? | `concurrency:` |
| …whether it runs at all this time? | `if:` conditional execution |
| …which identity it writes as? | `github-app:` |
| …how strict the compiler is? | `strict:` |

Full documented set also includes `description:`, `intent:`, `emoji:`, `labels:`, `metadata:`, `imports:`, `import-schema:`, `pre-steps:`/`steps:`/`pre-agent-steps:`/`post-steps:`/`jobs:`, `docker-image-pull-policy:`, `cache:`, `checkout:`, `ambient-folders:`, `engine:` (+ `model-routing:`, `driver:`, `extensions:`), `skills:`, `plugins:`, `mcp-scripts:`, `threat-detection-suppress:`, `run-name:`, `runs-on:`, `runs-on-slim:`, `env:`, `excluded-env:`, `secrets:`, `container:`, `services:`, `observability:`, `resources:`, `runtimes:`, `run-install-scripts`, `source:`, `redirect:`, `tracker-id:`, `private:`, `check-for-updates`, `features:`.

### The two that change what the deck can claim

- **`environment:` (Environment Protection).** GitHub environments support required reviewers. If that applies here, a workflow can be made to **wait for a named human to approve before the write job runs** — a mechanism-level gate, not a review-after-the-fact. This is potentially the single best answer to "what stops it writing something bad", and it is not on any slide in any deck. **Verify the exact semantics on the frontmatter page before claiming it**; do not put it on a slide until confirmed, but it is the highest-value thing on this list.
- **`protected-files:`** restricts which paths an output may touch. v3 slide 20 proposes a docs-only pilot; "docs only" is currently enforced by the wording of the prompt. `protected-files:` is the mechanism that could enforce it. Same instruction: confirm semantics first.

Source: <https://github.github.com/gh-aw/reference/frontmatter/>

---

## 4. Slide 16 (layers, not one wall): there is exactly one documented hard block — use it

The deck is careful never to say detection "always blocks", because `continue-on-error` defaults to `true`. That caution is right, and it leaves the safety act with nothing that *definitely* stops a bad write. There is one, documented verbatim:

> "a failed or skipped redaction blocks publication for an active detection run even when detection uses `continue-on-error`."

**Documented**, <https://github.github.com/gh-aw/reference/threat-detection/>

This is the precise, defensible version of the layered claim, and it fits the slide's existing glyph language (`#g-lock` for an enforced boundary, `#g-warn` + dashed for a weak one):

| Layer | What happens on failure | Glyph |
|---|---|---|
| Threat detection finding | Defaults to a **caution notice** (`continue-on-error: true`) | `#g-warn`, dashed |
| **Secret redaction** failed or skipped | **Blocks publication**, regardless of `continue-on-error` | `#g-lock` |
| MCP gateway | Docs' own wording: not a strong security boundary | `#g-warn`, dashed |
| Agent job write credential | None — writes deferred to a separate job | `#g-nokey` |

So the honest sentence for the act is: *"One thing here is a wall and the rest are speed bumps — and the deck will tell you which."* That is more persuasive than claiming more walls than exist, and it is the strongest possible form of the deck's own rule against overclaiming safety.

Also documented and not yet on a slide: **`threat-detection-suppress:`** exists as a frontmatter field, i.e. detection can be suppressed per workflow. A sceptic may find this; better to know it first.

---

## 5. Slides 14 and 15: the complete documented guardrail set, and a correction

### Correction: the per-run ceiling is ~$14, not ~$10
Slide 14 says "capped per run: 1,000 AI Credits (~$10) by default". **Documented and incomplete** — detection has its own budget that does not inherit the agent's:

> "Threat-detection runs have their own AI Credits budget, separate from the main agent's `max-ai-credits`. Detection does not inherit the main agent's budget — both caps apply independently."

Default **400 AIC**, compiled as `${{ vars.GH_AW_DEFAULT_DETECTION_MAX_AI_CREDITS || '400' }}`, overridable per output via `safe-outputs.<output>.threat-detection.max-ai-credits`.

This is a *gift* to slide 15, whose whole point is that detection is a separate job: it has a separate budget too. The separation is structural, not cosmetic.

### The full default guardrail table
**Documented** (cost management), verbatim: "a 20-minute timeout on the agentic step, a 60-minute timeout on the generated agent job, a 10-minute timeout on the generated detection job, 1000 AI Credits per workflow run, and 5000 AI Credits per workflow per day (24-hour window)."

| Guardrail | Default | Override |
|---|---|---|
| Agentic step timeout | 20 min | `timeout-minutes` |
| Agent job timeout | 60 min | `jobs.agent.timeout-minutes` |
| Detection job timeout | 10 min | `jobs.detection.timeout-minutes` |
| AI credits per run (agent) | 1,000 AIC (~$10) | `max-ai-credits` |
| AI credits per run (detection) | **400 AIC (~$4)** | `safe-outputs.*.threat-detection.max-ai-credits` |
| AI credits per workflow per day | 5,000 AIC (~$50) | `max-daily-ai-credits` |

**Per-run documented ceiling: 1,400 AIC ≈ $14.** Keep the existing caveat that AIC is "computed on a best-effort basis using pricing data sourced from the models.dev catalog and may not exactly match your provider's actual billing".

Sources: <https://github.github.com/gh-aw/reference/cost-management/> · <https://github.github.com/gh-aw/reference/threat-detection/>

---

## 6. Slide 23 (status and sources): one listed conflict is now resolved

The slide lists the daily AI-credit cap as a docs conflict kept off the deck. **As of 18 Oct 2026 the two pages agree:**

- Cost management: defaults include "5000 AI Credits per workflow per day (24-hour window)".
- Frontmatter, `max-daily-ai-credits`: "When omitted, the guardrail inherits the default daily limit (5000 AI Credits unless overridden)." `-1` disables it explicitly; an object form supplies a GitHub App token for the guardrail's own API calls.

**Action:** remove the daily cap from "left off on purpose" and state the 5,000/day default (it belongs in §5's table). The *other* item in that bullet — not claiming detection "always blocks" — stays, and §4 makes it sharper rather than removing it.

---

## 7. Slide 8 (three kinds of work): real workflow names instead of gallery categories

The slide uses the gh-aw home page's own groups with gallery task names. Those are legitimate but generic. The same three groups can be filled with **workflows that demonstrably exist and demonstrably ran**, which suits a deck whose thesis is "demonstrate before you defend".

**Measured** — workflow-name prefixes observed on *merged* pull requests in `github/gh-aw`, 18 Oct 2026. In gh-aw, PR titles are prefixed with the workflow that opened them:

| Group | Observed live workflows (from merged PR titles) |
|---|---|
| **Maintain** | `[docs]`, `[instructions]`, `[community]`, `[actions]`, `[link-checker]` |
| **Improve code** | `[dead-code]`, `[spec-enforcer]`, `[linter-miner]`, `[eslint-miner]`, `[jsweep]`, `[avenger]`, `[log]` |
| **Report and plan** | `[blog]` (a daily "Agent of the Day" post) |

**Measured** — `githubnext/agentics` holds **58 workflow files**, public and MIT, including the four the decks already reference plus their siblings: `update-docs.md`, `daily-doc-updater.md`, `doc-updater.md`, `unbloat-docs.md`, `glossary-maintainer.md`, `link-checker.md`, `issue-triage.md`, `ci-doctor.md`, `pr-fix.md`, `grumpy-reviewer.md`, `malicious-code-scan.md`, `daily-perf-improver.md`, `daily-test-improver.md`, `accessibility-review.md`, `repo-ask.md`.

Two useful consequences:
- Slide 17's 57/59 cites GitHub's *Daily Documentation Updater*, *Documentation Unbloat* and *Glossary Maintainer*. The files behind those names are `daily-doc-updater.md`, `unbloat-docs.md` and `glossary-maintainer.md` in a public MIT repo. **The deck's evidence and the deck's links can finally point at the same artifacts** — worth saying on slide 22.
- `[spec-enforcer]` and `[dead-code]` are workflows that police the codebase rather than document it. If the room asks "what else would you run after docs?", those are real answers with merged PRs behind them, not speculation.

---

## 8. Slide 21 (debugging): make the commands concrete

`todo.md` lists a mock terminal card as a visual gap and marks real `gh aw logs` output as blocked on the `workflow` token scope. The **shape** of the output is documented, so the card can be built now and swapped for a real capture later.

**Documented**: `gh aw logs` surfaces per-run metrics — elapsed duration, token usage, AIC and turn count — before you decide what to optimise. `gh aw audit <run-id>` deep-dives one run's token usage, tool calls and inference spend, with Metrics and Performance Metrics sections.

Documented recipe, usable verbatim on the slide:

```bash
# Top 10 costliest logical executions over the past 30 days by AI credits
gh aw logs --start-date -30d --verbose --json | \
  jq '[.episodes[] | {episode: .episode_id, aic: .total_aic}]'
```

Also documented, and a good Q&A answer for "how would this work at our scale": **OpenTelemetry** export for tracking costs at scale, and a repo `github/agentic-ops` referenced for automatic optimisation at scale. (The `agentic-ops` repo is named on the cost page but I did not verify its contents — do not describe it beyond "GitHub references a companion repo for this".)

Note for the deck's wording: `total_aic` is described as the preferred cost metric for Claude, Codex and Copilot runs because it maps to provider billing at 1 AIC = $0.01.

Source: <https://github.github.com/gh-aw/reference/cost-management/>

---

## 9. Do not use

- **"~$10 per run" as the documented ceiling** — omits detection's 400 AIC (§5).
- **The daily-cap conflict** as unresolved (§6).
- **`environment:` as a human approval gate, or `protected-files:` as path enforcement** — both are real documented fields, but their exact semantics are unverified. Do not put either on a slide until confirmed (§3).
- **"Agentic" for the 4,034 PR count.** Say "bot-authored" (§2).
- **`github/agentic-ops` described as a product or toolkit** — only its mention is verified (§8).
- **The 72.6% trustworthiness figure.** Still unverifiable; see `../deck-v2/RESOURCES.md` §5 for a sourced replacement if a survey number is wanted.
- **Any claim that 344 workflows "run daily"** — 344 files are committed and thousands of PRs exist, but run frequency per workflow was not measured. Say "344 committed, with 2,688 merged bot pull requests over 14 months".

---

## Source list, all fetched or counted 18 Oct 2026

| Source | Used for |
|---|---|
| GitHub contents API, `github/gh-aw/.github/workflows` | 344 `.md` / 344 `.lock.yml` / 41 plain `.yml`; 737 entries (not truncated) |
| GitHub search + pulls API | 4,034 / 2,688 / 1,346 bot PRs; PRs #69936, #69394, #68929 diffs; workflow-name prefixes; agentics 58 files |
| <https://github.github.com/gh-aw/reference/frontmatter/> | 50 documented frontmatter sections; `environment:`, `protected-files:`, `max-turns:`, `user-rate-limit:`, `strict:`, `threat-detection-suppress:` |
| <https://github.github.com/gh-aw/reference/threat-detection/> | 400 AIC detection budget; redaction hard block; detection suppression |
| <https://github.github.com/gh-aw/reference/cost-management/> | 20/60/10-min timeouts; 1,000 and 5,000 AIC defaults; `gh aw logs`/`audit`; jq recipe; OpenTelemetry; `agentic-ops` mention |
