# Deck v1: proposed technical slide additions

Proposal only. Nothing here is in `../overview.md` yet. Change it first if any slide is accepted (AGENTS.md rule).

## Core idea and where it is thin
**Core idea:** our docs can't keep up with how fast we ship, and gh-aw lets an agent keep them current inside GitHub Actions, with controls tight enough that a four-week pilot is low-risk.

**Technically thinnest points:**
1. **Slide 4** packs the file, the compile step, the trigger, the job split and safe outputs into one diagram. Engineers never see a real file.
2. **Slide 6** argues "it's controlled" with one quote. The pipeline that enforces control (detection gate, firewall, draft-PR policy) is not shown, and cost is a TODO.
3. **Slides 8 and 9** ask for a safe pilot but never show how to test without touching our repo, or how we would measure it.

**Fix needed in deck.md:** "Status and sources" says technical preview and "Do not claim public preview". That is wrong. gh-aw has been in **public preview since 11 Jun 2026** (GitHub changelog). Note: the gh-aw docs home page still links a "technical preview deck", so cite the changelog, not the docs home page.

---

## A. After slide 4: the annotated workflow file
- **Title:** The whole workflow is one short file: the frontmatter sets the limits, the plain-English body sets the job
- **Why:** turns slide 4's claim into something engineers can read, and links straight to the demo (slide 5: "the markdown file behind it").
- **Visual:** a code card, frontmatter on the left, 4 to 5 callouts on the right. Use only verified keys:
  ```yaml
  ---
  on: daily                      # fuzzy schedule; adds manual runs too
  permissions:
    contents: read               # agent job is read-only
  network: defaults              # firewall allowlist
  safe-outputs:
    create-pull-request:
      title-prefix: "[docs] "
      labels: [documentation]
      draft: true                # policy; agent can't override
  max-ai-credits: TODO           # per-run budget
  ---
  Find docs that are out of date with recent code changes
  and open a PR that fixes them.
  ```
- **Bullets:** frontmatter = the contract (trigger, permissions, network, allowed writes, budget) · body = the task in plain English · `gh aw compile` turns it into a pinned `.lock.yml` Actions workflow.
- **Sources:** frontmatter keys: /reference/frontmatter/ · `on: daily` expands to schedule + `workflow_dispatch`: /reference/schedule-syntax/ · `draft` "is a policy, not a default, so the agent cannot override it at runtime" (default true): /reference/safe-outputs-pull-requests/ · `network:` allowlist: /introduction/architecture/
- **Caution:** illustrative, not our file. Real file name: **TODO** (slide 7). Exact `network:` and `permissions:` values should be checked against the file we actually demo.
- **Audience:** technical: "I can review this like any YAML in a PR". Non-technical: "the rules sit on top, in plain view, and the job is plain English".

## B. After slide 4 (or the top half of slide 6): the run pipeline
- **Title:** Every run passes through separate jobs, and nothing is written until a threat check approves it
- **Why:** this is the mechanism behind "every write is checked". It turns slide 6's quote into a diagram.
- **Visual:** left-to-right pipeline of 5 boxes, with a gate before the last one:
  `Pre-activation` (role check, skip rules) → `Activation` (sanitise event text, validate lock file) → `Agent` (read-only, sandboxed container, firewall) → `Detection` (pass/fail) → **gate** → `Safe outputs` (the only job with write scopes: PR, issue, comment)
- **Bullets:**
  - The agent runs read-only in a container. Outbound traffic goes through a domain allowlist (Agent Workflow Firewall).
  - An API proxy holds the tokens, so the agent never sees them.
  - The detection job scans the agent's output and patch for prompt injection, secret leaks and malicious patches. If it finds a threat, "safe outputs are blocked". If detection itself fails, nothing is written (fail-safe).
  - Compile time: schema validation, expression safety checks and SHA-pinned actions.
- **Sources:** /introduction/architecture/ (job list, AWF, Squid allowlist, compile checks) · /reference/threat-detection/ ("automatically enabled when safe outputs are configured") · changelog 11 Jun 2026 (read-only, sandbox behind firewall, threat detection job) · gh-aw home page (API proxy)
- **Audience:** technical: separation of duties, with write scopes only in a job the model never runs in. Non-technical: "the agent drafts, a separate guard checks the draft, and only then does anything change".

## C. Inside Part 2, after B or merged into slide 6: cost and observability
- **Title:** Every run has a hard budget and leaves a receipt we can audit
- **Why:** fills slide 6's "cost per run" TODO with real controls, and gives slide 9's "measure and tune" week a real tool.
- **Visual:** two halves. Left, a "budget" card: per-run AI credits, daily cap, turn cap, timeout. Right, a terminal: `gh aw logs` (duration, tokens, AIC, turns per run) → `gh aw audit <run-id>` (one run's tools, tokens, estimated cost).
- **Bullets:**
  - 1 AI Credit (AIC) = $0.01. Defaults: `max-ai-credits` 1000 per run, `max-daily-ai-credits` 5000 per workflow per day.
  - Agentic step times out at 20 min by default; `max-turns` caps iterations.
  - `skip-if-match` / `skip-if-no-match` skip the agent in the cheap pre-activation job.
  - A typical run is a 10 to 30 s pre-activation job plus a 1 to 15 min agent job.
  - AIC is "best-effort" and "may not exactly match your provider's actual billing". Say so.
- **Sources:** /reference/cost-management/ · /setup/cli/ (logs, audit)
- **Audience:** technical: "budget limits live in the file, and logs give per-run data". Managers: "spend is capped by default, and we get a per-run cost report for the pilot review".
- **TODO:** our real cost per run, measured during the pilot. Drop the Register/DevClass "two premium requests" figure; it isn't from official docs.

## D. Before slide 8 (or replacing its TODO steps): test without risk
- **Title:** We can run it on a throwaway repo, or in preview mode, before it can write to ours
- **Why:** slides 8 and 9 rest on "safely". This shows the two concrete safety nets and supplies steps 2 and 3 for slide 8.
- **Visual:** two lanes. Lane 1: `gh aw trial` → temporary private repo → results back in the console. Lane 2: `safe-outputs: staged: true` → run in our repo → preview in the step summary, no writes.
- **Bullets:**
  - `gh aw trial`: "Test workflows in temporary private repositories" (default repo name `gh-aw-trial`), started with `workflow_dispatch`.
  - `staged: true` under `safe-outputs:`: "every write operation is skipped". The preview appears in the Actions step summary. Can be set per output.
  - Then `gh aw compile` and `gh aw run` for a real run.
- **Sources:** /setup/cli/ (trial, compile, run) · /experimental/trial-ops/ (TrialOps is in the docs' **experimental** section; say so) · /reference/safe-outputs/ (Staged Mode)
- **Audience:** technical: a ready checklist. Managers: "week 1 of the pilot writes nothing".

## E. Optional, after slide 5: evidence from GitHub's own docs workflows
- **Title:** GitHub's own docs agents get most of their pull requests merged
- **Why:** the only measured outcome available. It backs the demo with numbers, not just a quote.
- **Visual:** small bar chart of merged/proposed PRs: Daily Documentation Updater 57/59 (96%), Documentation Unbloat 88/103 (85%), Glossary Maintainer 10/10.
- **Sources:** gh-aw blog, "Meet the Workflows: Continuous Documentation", 13 Jan 2026 (Syme, de Halleux, Kiefer)
- **Caveats:** GitHub's numbers on its own repos. The post does not say which repo they were measured in. Small samples. Label them "reported by GitHub".
- **Audience:** everyone: "this is already working at GitHub".

---

## Ranked shortlist
1. **B, run pipeline**: strongest support for the "controlled" claim the pilot ask depends on.
2. **A, annotated file**: makes slide 4 concrete and sets up the demo.
3. **D, test without risk**: closes slide 8's TODO and de-risks the ask.
4. **C, cost and receipts**: closes slide 6's cost TODO and gives the pilot its metrics.
5. **E, evidence**: optional, non-technical. Use it if the room is manager-heavy.

## Cut or merge to keep length (target +2 to +3 net)
- **Slide 4 → A.** Keep slide 4's one-line diagram as the header strip of A, then drop the separate slide 4 (net 0).
- **Slide 6 → B + C.** Move "safety limits" into B and "cost" into C. Slide 6 keeps only "not a good fit" plus the L4 autonomy note, or that note moves into B's footer.
- **Slide 8 ← D.** D supplies slide 8's steps. Merge them into one slide unless engineers are the main audience.
- **Slide 2** is still TODO. If the gap is never named, merge it into slide 1.

## Risks spotted while checking
- **Status line in deck.md is wrong.** It should say public preview since 11 Jun 2026. Also update `overview.md` "Status", which carries the same error.
- **"Never merged automatically" (slide 6)** is GitHub Blog guidance, not a hard limit. The docs list an experimental `merge-pull-request` safe output, which refuses default-branch merges. gh-aw's own internal `daily-doc-updater.md` appears to enable auto-merge (read via a fetch summary; verify the raw file). Present it as the default policy (`draft: true`) plus guidance, not a guarantee.
- **Engines differ between docs pages.** The home page lists Copilot, Claude Code, Codex, Antigravity and Pi. "How they work" lists Copilot (default), Claude Code, Codex, Gemini and Pi. If engines are mentioned, say "Copilot by default, others supported".

## Checked: 17 Oct 2026
- https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview
- https://github.github.com/gh-aw/
- https://github.github.com/gh-aw/introduction/architecture/
- https://github.github.com/gh-aw/introduction/how-they-work/
- https://github.github.com/gh-aw/reference/frontmatter/
- https://github.github.com/gh-aw/reference/schedule-syntax/
- https://github.github.com/gh-aw/reference/safe-outputs/
- https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/
- https://github.github.com/gh-aw/reference/threat-detection/
- https://github.github.com/gh-aw/reference/cost-management/
- https://github.github.com/gh-aw/setup/cli/
- https://github.github.com/gh-aw/experimental/trial-ops/ (via search result summary only)
- https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/
- https://github.com/github/gh-aw/blob/main/.github/workflows/daily-doc-updater.md (raw, fetch summary)
