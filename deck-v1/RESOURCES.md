# Deck v1: better resources and alternative slide content

Research pass, 18 Oct 2026. Companion to `sources.md`-style checking, but the opposite job: `todo.md` lists what is broken, this file lists **what better material exists to put there**.

Scoped to v1's arc — the business case: cost, risk, baseline, decision. Material that suits v2's story or v3's mechanism act is in those folders' `RESOURCES.md` and is deliberately **not** repeated here.

**How to read a status label** (same vocabulary as the decks):
**Measured** = counted, method named · **Documented** = gh-aw or GitHub docs · **Reported by GitHub** = GitHub's own claim · **Peer-reviewed** = published study · **Secondary** = press/vendor coverage, verify before use.

Every item below was fetched or counted on **18 Oct 2026**. Nothing here is invented; where a number is still unknown, it says so.

> **Slide numbers drift — confirm by title.** All three decks were edited while this file was being written: deck-v2 gained a slide and reordered, deck-v3 shifted by one from slide 5 on, and several deck-v1 titles changed. The numbers below were correct at **18 Oct 2026**; the **titles** are the reliable anchor. Check the title before editing a slide.

| § | Slide(s) | Title(s) as of 18 Oct 2026 |
|---|---|---|
| 1 | 26 | Cost per accepted change is a formula the pilot fills in, not a number we have *(Appendix 9)* |
| 2 | 13, 26 | A cheap run nobody merges is still expensive · Appendix 9 above |
| 3 | 27 | The technical claims are grounded in GitHub's documentation *(Appendix 10)* |
| 4 | 7 | A dialog title leaked into a menu, and the fix is three lines |
| 5 | 8 | GitHub reports 85–100% of documentation pull requests merged in three of its workflows |
| 6 | 12, 20 | The agent job is read-only; writes happen in a separate job · Detection adds a review gate, not a safety guarantee *(Appendix 3)* |
| 7 | 2, 3 | Outdated documentation already costs developers time · Documentation debt accrues between doc passes |
| 8 | 14, 15 | Four weeks turns opinion into evidence · Week four ends in a decision we agreed in advance |
| 9 | 13, 16 | A cheap run nobody merges is still expensive · The downside is bounded by five proposed limits |


---

## 1. "Cost per accepted change is a formula the pilot fills in" — slide 26, Appendix 9: three of seven TODO symbols can be resolved now

*(The cost material was split since this pass began: slide 13 `11 / COST` now carries the plain-language version, "(AI credits + compute + reviewer time) ÷ changes accepted"; the LaTeX formula and symbol table moved to Appendix 9, slide 26. The rates below fill in that symbol table; the ceiling correction in §2 belongs on slide 13.)*

The equation has seven symbols; five are TODO or "NOT MEASURED". Three are answerable from primary sources today, which turns the slide from an IOU into arithmetic.

### `p_m` — price per Actions minute → **$0.006**
**Documented.** GitHub's billing docs give per-minute rates by SKU:

| Runner | Billing SKU | Per-minute (USD) |
|---|---|---|
| Linux 1-core (x64) | `actions_linux_slim` | $0.002 |
| **Linux 2-core (x64)** | **`actions_linux`** | **$0.006** |
| Linux 2-core (arm64) | `actions_linux_arm` | $0.005 |
| Windows 2-core (x64) | `actions_windows` | $0.010 |
| macOS | — | $0.062 |

Source: <https://docs.github.com/en/billing/concepts/product-billing/github-actions>

### The `M · p_m` term may be **zero**, which is a better slide than a cheaper one
**Documented, same page, verbatim:** "GitHub Actions usage is free for self-hosted runners and for public repositories that use standard GitHub-hosted runners."

So compute cost depends on a pilot decision the deck already has to make:

| Pilot repo | Actions minutes cost |
|---|---|
| **Public**, standard GitHub-hosted runner | **$0** |
| **Private** | Free quota first — 2,000 min/mo (Free), 3,000 (Team), 50,000 (Enterprise Cloud) — then $0.006/min Linux 2-core |

Caveat to keep beside it: **larger runners are always charged**, even on public repos or inside quota. Storage is separate: $0.25/GB/mo shared storage, $0.07/GB/mo Actions cache.

### `M` has a documented **upper bound**, so the worst case is computable
**Documented** (gh-aw cost management), verbatim: "a 20-minute timeout on the agentic step, a 60-minute timeout on the generated agent job, a 10-minute timeout on the generated detection job".

Worst-case wall-clock ≈ 70 runner-minutes per run → **≈ $0.42 per run** on a private repo, **$0** public. Compute is not the cost driver; inference and reviewer time are. That is a strong, honest line for a finance-minded room.

Source: <https://github.github.com/gh-aw/reference/cost-management/>

### `w` and `R` stay as organisation inputs — but name the method
Do not invent a reviewer rate. Give the measurement instead, so week one produces the number:

- `R` (reviewer minutes): the pilot's own measurement. Log review start/end on each draft PR for four weeks.
- `w` (reviewer cost/min): your organisation's loaded cost. A deck should take it as an input, not assert it.
- `A` (AI credits per run), **Documented:** `gh aw logs` surfaces elapsed duration, token usage, AIC and turn count per run. Costliest runs over 30 days:

```bash
gh aw logs --start-date -30d --verbose --json | \
  jq '[.episodes[] | {episode: .episode_id, aic: .total_aic}]'
```

`gh aw audit <run-id>` deep-dives one run's token usage, tool calls and inference spend.

> **Honesty flag for slides 13 and 26.** `todo.md` item 3 is right: `A` and `N_acc` are labelled "measured, `gh aw logs`" but nothing has ever run. Change to **"will be measured"**. Everything above is a *documented rate*, not a measured result.

---

## 2. Correction that affects the headline cost figure: the per-run ceiling is ~$14, not ~$10

**Documented, and currently wrong on the deck.** Threat detection has its **own** AI-credit budget that does **not** inherit the agent's:

> "Threat-detection runs have their own AI Credits budget, separate from the main agent's `max-ai-credits`. Detection does not inherit the main agent's budget — both caps apply independently."

Default detection budget: **400 AIC**, resolved at compile time as `${{ vars.GH_AW_DEFAULT_DETECTION_MAX_AI_CREDITS || '400' }}`. Override per output with `safe-outputs.<output>.threat-detection.max-ai-credits`.

So the documented default ceiling for one run:

| Component | Default cap | At 1 AIC = $0.01 |
|---|---|---|
| Agent job (`max-ai-credits`) | 1,000 AIC | ~$10 |
| Detection job (separate budget) | 400 AIC | ~$4 |
| **Per-run ceiling** | **1,400 AIC** | **~$14** |
| Per workflow per day (`max-daily-ai-credits`) | 5,000 AIC | ~$50 |

Keep the existing caveat: AIC is "computed on a best-effort basis using pricing data sourced from the models.dev catalog and may not exactly match your provider's actual billing."

Sources: <https://github.github.com/gh-aw/reference/threat-detection/> · <https://github.github.com/gh-aw/reference/cost-management/>

---

## 3. "The technical claims are grounded in GitHub's documentation" — slide 27, Appendix 10: one of the two "unresolved conflicts" is now resolved

The slide lists the daily AI-credit cap default as an unresolved conflict between docs pages. **As of 18 Oct 2026 the two pages agree.**

- Cost management: default guardrails include "5000 AI Credits per workflow per day (24-hour window)".
- Frontmatter, `max-daily-ai-credits`: "When omitted, the guardrail inherits the default daily limit (5000 AI Credits unless overridden)." Set `-1` to disable explicitly.

**Action:** drop the daily-cap conflict from the unresolved list and state the 5,000/day default plainly. The *second* conflict (whether failed detection blocks) still stands — see §6, which sharpens it rather than resolving it.

Sources: <https://github.github.com/gh-aw/reference/frontmatter/> · <https://github.github.com/gh-aw/reference/cost-management/>

---

## 4. "A dialog title leaked into a menu, and the fix is three lines" — slide 7, `06 / THE REAL EXAMPLE`: a better diff that needs no run from us

`todo.md` item 8 says PR #8716 is an unrelated accessibility fix and should be swapped "for a real docs-drift PR (needs a real run)". **It does not need a run.** A real documentation-agent PR exists in a public repo:

| PR | What it is | Diff | Merged |
|---|---|---|---|
| **github/gh-aw#68654** | `[docs] Update glossary — daily scan` | **+8 / −0, 1 file** | 2026-10-14 |

<https://github.com/github/gh-aw/pull/68654>

Why it beats #8716 for this slide:
- It is a **documentation** workflow, so the slide no longer needs its "different workflow, shows output size only" apology.
- Eight added lines in one file *is* the claim "the unit of review is one small diff" — no simplification of the diff needed, so the "Diff simplified" caveat goes too.
- The `[docs]` prefix is the gh-aw convention of naming the workflow that opened the PR, which makes the provenance visible on the screenshot itself.

**Measured** via GitHub API, 18 Oct 2026.

> **Note, 18 Oct 2026.** This slide has since been retitled *"A dialog title leaked into a menu, and the fix is three lines"* — the title now describes the #8716 accessibility fix itself. Swapping in #68654 therefore means **retitling the slide too**, e.g. *"A glossary drifted from the code, and the fix is eight lines"*. The claim-as-title convention still holds; only the claim changes.

Alternative if a larger diff is wanted to show the review burden honestly: **github/gh-aw#69936** `[dead-code] chore: remove dead functions`, **+0 / −201 across 4 files**, merged 2026-10-18 — an agent *deleting* code. Useful for slide 10's "too wide a diff" failure mode, but it is assigned to deck-v3 as a mechanism example; using it in both decks would duplicate.

---

## 5. "GitHub reports 85–100% of documentation pull requests merged in three of its workflows" — slide 8, `07 / THE EVIDENCE`: a public denominator that answers the cherry-pick objection

**Update:** the slide has since been retitled *"GitHub reports 85–100% of documentation pull requests merged in three of its workflows"* and now shows all three denominators (57/59, 88/103, 10/10). `todo.md` item 8's cherry-pick concern is **addressed**. What is still missing is a denominator **anyone in the room can recount** — all three of GitHub's samples are still GitHub's own, small, and unnamed as to repo.

**Measured**, GitHub search API, 18 Oct 2026, bot-authored pull requests in public repositories:

| Repository | Agent PRs | Merged | Closed unmerged | Merge rate |
|---|---|---|---|---|
| **github/gh-aw** | 4,034 | 2,688 | 1,346 | **66.6%** |
| githubnext/agentics | 52 | 31 | 20 (+1 open) | **59.6%** |

Window: oldest bot PR 2025-08-20, newest 2026-10-18. Query shape:

```bash
gh api -X GET search/issues \
  --raw-field q='repo:github/gh-aw is:pr is:merged author:app/github-actions' \
  --jq '.total_count'
```

Why this is the stronger slide for a business case:
- **~67% with n=4,034 is more persuasive than 96% with n=59.** It is verifiable, the denominator is stated, and it pre-empts "those are GitHub's own cherry-picked repos".
- It sets a defensible planning assumption: **expect to reject about a third** of what the agent proposes. That flows straight into the decision-rule thresholds (slide 15) and slide 14's `N_acc`.
- It strengthens, not weakens, the deck's thesis. A third rejected is what "the human decides what merges" looks like in practice.

**Caveat to put on the slide:** the filter is `author:app/github-actions`, which is every GitHub Actions-authored PR in those repos, not provably only agentic-workflow ones. In gh-aw the titles carry workflow-name prefixes (`[docs]`, `[dead-code]`, `[spec-enforcer]`, `[blog]`, `[linter-miner]`), which is strong evidence they are agentic, but say "bot-authored" rather than "agentic" to stay exact. Merged still is not the same as correct.

---

## 6. "The agent job is read-only" (slide 12) and "Detection adds a review gate, not a safety guarantee" (slide 20, Appendix 3): the one thing that genuinely does hard-block

The deck is right to refuse "detection always blocks" (`continue-on-error` defaults to `true`). But there **is** a documented hard block, which gives the appendix something affirmative to say:

> "a failed or skipped redaction blocks publication for an active detection run even when detection uses `continue-on-error`."

**Documented**, <https://github.github.com/gh-aw/reference/threat-detection/>

This is a better appendix slide than "failure behaviour is disputed in the docs" (that appendix slide's current caption, which `todo.md` item 14 notes hurts trust). Replace the shrug with the precise rule: *detection findings* default to a caution; *failed secret redaction* blocks publication regardless.

Also documented and not yet on any v1 slide — **Supply Chain Protection (`protected-files`)**, a non-AI guardrail that restricts which paths an output may touch. This is the mechanism `todo.md` item 4 asks for, where it says "docs only is enforced by prompt wording, not a mechanism": `protected-files` is the mechanism. Confirm its exact semantics on the safe-outputs page before claiming path enforcement.

---

## 7. "Outdated documentation already costs developers time" (slide 2) and "Documentation debt accrues between doc passes" (slide 3): a peer-reviewed citation for an argument now carried by assertion

Slide 3 extends Cunningham's 1992 technical-debt metaphor and is labelled "Illustrative · no data". There is real published data for the documentation-specific version.

**Peer-reviewed.** Aghajani et al., *Software Documentation: The Practitioners' Perspective*, ICSE 2020, DOI [10.1145/3377811.3380405](https://dl.acm.org/doi/10.1145/3377811.3380405). Two surveys, **146 practitioners**. Share rating each up-to-dateness issue as relevant:

| Issue | % of 146 |
|---|---|
| Missing documentation for a new feature/component | **69%** |
| Outdated / obsolete references | **64%** |
| **Code-documentation inconsistency** | **59%** |
| Outdated installation instructions | 54% |
| Missing documentation for a new release | 53% |
| Outdated example | 51% |
| Outdated version information | 32% |
| Outdated screenshot | 29% |

The paper's own wording on the 59%: code-documentation inconsistency "is perceived as an important issue by practitioners (59% of them) and is one of the top recurring issues they face."

**Caveat that must travel with it:** 125 of the 146 respondents were employed at a single corporation (ABB), with 21 from developer-oriented social sites. It is not a broad random sample — say "a 2020 study of 146 practitioners, most at one company".

Why it fits v1 specifically: this is the deck that already cites Cunningham (1992) and Saltzer & Schroeder (1975). A third peer-reviewed citation keeps that register, and gives slides 2–3 a number that is about *documentation drift* rather than about context-finding in general.

---

## 8. "Week four ends in a decision we agreed in advance" (slide 15) and "Four weeks turns opinion into evidence" (slide 14): name the risk the pilot could create

The deck measures accepted fixes, total effort and budget. The industry evidence suggests a fourth thing worth watching, and naming it first is more credible than being asked about it.

**Secondary — verify at <https://dora.dev> before putting on a slide.** Coverage of the DORA 2025 State of DevOps report reports that AI adoption now correlates with **higher delivery throughput and higher instability**, and that the bottleneck moves downstream into testing, code review and QA. Trust lags usage: ~90% report using AI at work; roughly a quarter report high trust in its outputs (the "trust paradox").

Use on the decision-rule slide as a stated pilot risk: *if the agent raises proposal volume, review becomes the constraint* — which is exactly why `R` (reviewer minutes) is in Eq. 1 and must be measured, not assumed. Do **not** put the percentages on a slide from secondary coverage; either read the primary report or keep it in notes as a qualitative point.

---

## 9. Cost controls the deck does not yet mention (slide 13 `11 / COST`, slide 16 `14 / THE BOUNDS`)

All **Documented** on the cost-management page, and all relevant to "the downside is capped before anything runs":

- **Skip the agent cheaply.** Emit a `noop` to `$GH_AW_SAFE_OUTPUTS` from `steps:` / `pre-agent-steps:` — "The harness exits before starting the AI engine, so no AI Credits are charged." A conditional pre-step (e.g. nothing changed) makes most runs free.
- **`max-turns`** caps agent iterations; **`max-turn-cache-misses`** caps cache misses. Org default via `GH_AW_DEFAULT_MAX_TURNS`.
- **`user-rate-limit`** limits how often a single user can trigger a workflow — relevant if the pilot ever uses a comment trigger.
- **Cheaper models** per workflow; the docs recommend smaller models for routine tasks.
- **Schedules beat event triggers for budgeting.** "Use Schedules for Predictable Budgets". A daily schedule is ~30 runs/month, a known number; `push` to `main` is not a number anyone controls. (The example `update-docs.md` uses `push`, so the pilot should narrow the trigger — this also answers `todo.md` item 6.)
- **Batching** lets providers cache shared context across items, cutting credits.
- **Org-wide defaults** via `GH_AW_DEFAULT_MAX_AI_CREDITS`, `GH_AW_DEFAULT_MAX_DAILY_AI_CREDITS` — the lever for "capped before anything runs" at org level rather than per file.
- **At scale:** OpenTelemetry cost export, and a GitHub repo `github/agentic-ops` referenced for automatic optimisation at scale (unverified beyond the mention — check before citing).

---

## 10. Do not use

- **"~$10 per run" as the ceiling.** It omits detection's separate 400 AIC budget. Use ~$14, or say "1,000 AIC for the agent plus 400 for the detection pass".
- **The daily-cap conflict** as an open issue (§3).
- **57/59 alone.** Either show all three of GitHub's samples with denominators, or lead with the public 2,688/4,034 (§5).
- **DORA percentages from secondary coverage** (§8) on a slide.
- **"Measured, `gh aw logs`"** for `A` and `N_acc` until a run exists.
- **Self-hosted-runner per-minute fee.** Coverage says a $0.002/min charge for self-hosted runners on private repos was announced then postponed; sources disagree on its status. Leave it off.

---

## Source list, all fetched or counted 18 Oct 2026

| Source | Used for |
|---|---|
| <https://docs.github.com/en/billing/concepts/product-billing/github-actions> | `p_m` = $0.006/min, free on public repos, plan quotas, storage rates |
| <https://github.github.com/gh-aw/reference/cost-management/> | 20/60/10-min timeouts, 1,000 AIC/run, 5,000 AIC/day, `gh aw logs`/`audit`, noop skip, batching, schedules |
| <https://github.github.com/gh-aw/reference/threat-detection/> | 400 AIC detection budget, redaction hard block, protected files |
| <https://github.github.com/gh-aw/reference/frontmatter/> | `max-daily-ai-credits` default resolved, `max-turns`, `user-rate-limit` |
| GitHub search + pulls API (`gh api`) | 4,034 / 2,688 / 1,346 gh-aw bot PRs; agentics 52/31/20; PR #68654 diff +8/−0 |
| <https://dl.acm.org/doi/10.1145/3377811.3380405> (PDF read) | Aghajani et al. ICSE 2020, n=146, up-to-dateness percentages |
| DORA 2025 coverage (secondary) | Review-bottleneck risk — verify at <https://dora.dev> |
