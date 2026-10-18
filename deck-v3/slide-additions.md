# Deck v2: proposed technical slides

Proposals only. Nothing here is in `deck.md` yet. Checked against official sources on 17 Oct 2026. Status: public preview since 11 Jun 2026.

## Core idea and where it is thin
**Core idea:** an AI agent in a GitHub Action can keep a repo's docs current on its own, and every change it makes still comes to us as a PR we review, so we never have to trust it blindly.

**Technically thinnest points:**
- **"Built to be checked" rests on quotes, not mechanism.** Slides 8–9 quote "sandboxed", "firewall" and "threat detection" but never show *why* a misled agent can't write. That separation is the real answer to May Walter's "trusting it enough to merge" quote.
- **Slide 5's `update-docs.md` is generic.** A real file exists that does exactly what the title promises: `update-docs.md` in githubnext/agentics.
- **After the PR, nothing.** Nothing covers how you would see what the agent did, or how spend is capped. Slide 9's cost line is the only mention.

---

## A. A real docs workflow: the job described on the title slide, in one file
- **Where:** replaces the generic example on slide 5 (or goes straight after it). It turns "repos that keep themselves up to date" from a slogan into a file.
- **Title:** One short file tells an agent to update the docs on every push to main and open a draft PR
- **Visual:** the real frontmatter with 4 callouts (trigger, read-only, firewall, outbox), and the body as one sentence:
  ```yaml
  on:
    push:
      branches: [main]          # 1 shift: every push to main
    workflow_dispatch:
  permissions: read-all         # 2 access badge: read only
  network: defaults             # 3 firewall: basic infrastructure only
  safe-outputs:
    create-pull-request:        # 4 outbox: a draft PR, nothing else
      draft: true
      protected-files: fallback-to-issue
      labels: [automation, documentation]
  tools:
    github:
      toolsets: [all]
    web-fetch:
    bash: true
  timeout-minutes: 15
  ```
  Body (paraphrased): review the diff, find docs that no longer match, update them, open a focused draft PR, never push to main.
- **Bullets:** it maps onto slide 4's teammate chips one for one · `protected-files: fallback-to-issue` means it opens a review issue instead of a PR if protected files are touched · install pattern: `gh aw add-wizard <owner>/<repo>/<workflow-name>`
- **Sources:** raw file at github.com/githubnext/agentics/blob/main/workflows/update-docs.md (agentics README: "Documentation Update on Push to Main") · `fallback-to-issue` and the add-wizard format: gh-aw safe-outputs reference and quick start
- **TODO:** confirm the exact `add-wizard` path for this file before putting it on the slide (the documented example is `githubnext/agentics/repo-status`)
- **Audience:** technical: the four security levers are visible in 15 lines. Non-technical: "this is the whole job description."

## B. Inside a run: the reader and the writer are different jobs
- **Where:** replaces the pipeline on slide 8 (merge). This is the mechanism behind "built to be checked".
- **Title:** Each run is split into separate jobs, so the agent that reads the repo never holds the keys to change it
- **Visual:** six boxes left to right, with a lock icon on the write jobs only:
  `pre-activation` (role check, stop-after) → `activation` (sanitize input, validate lock file) → **`agent`** (read-only) → **`detection`** (no write access, gates what follows) → **safe-output jobs** (scoped writes, e.g. PR = `contents: write` + `pull-requests: write`) → `conclusion` (summary)
- **Bullets:**
  - "The agent job runs with minimal read-only permissions" and "write operations are deferred to separate jobs that execute only after the agent completes"
  - Detection scans the agent's output and patch for `prompt_injection`, `secret_leak` and `malicious_patch`. "If the detection agent identifies threats, the workflow terminates before any writes are externalized"
  - Detection is "automatically enabled" when safe outputs are configured. Custom checks (e.g. Semgrep, TruffleHog) go in `threat-detection` steps
  - Default PR cap: `create-pull-request` max 1 per run
- **Sources:** gh-aw architecture page · threat-detection reference · safe-outputs reference
- **Caveat to check:** the threat-detection page says `continue-on-error` defaults to `true` and turns warnings and failures into a caution notice instead of a block. Confirm how that fits with "terminates before any writes" before saying "always blocks" out loud.
- **Audience:** technical: least privilege by job boundary. Non-technical: "the intern drafts it, a checker reviews it, and only then does the post room send it."

## C. The agent works in a firewalled box with an allowlist
- **Where:** fold into slide 9 as the visual for the "prompt injection" safeguard, or place it right after B.
- **Title:** The agent runs in a container that can only reach the domains and tools we list
- **Visual:** a container box (the agent) → Squid proxy (allowlist) → internet. MCP servers sit in their own small boxes beside it, behind an MCP gateway. Below it, a code strip: `network: defaults` · `network: { allowed: [defaults, python, "api.example.com"] }` · `network: {}` = no access
- **Bullets:**
  - AWF "containerizes the agent" and its proxy "controls the agent's egress traffic via a configurable domain allowlist"
  - Omitting `network:` gives `defaults` (basic infrastructure only)
  - Tools are opt-in under `tools:` (e.g. `bash: ["gh issue comment"]` limits bash to that one command)
  - Docs are candid: the MCP gateway "is not a strong security boundary against a compromised or malicious agent". Defense comes from layers, not any one wall
- **Sources:** architecture page · network reference · frontmatter reference
- **Audience:** technical: egress is controlled, not just permissions. Non-technical: "even a tricked agent can't phone home."

## D. Every run leaves an audit trail, and spend is capped by default
- **Where:** after slide 9, or as the first slide of Part 3 before the recordings. It answers "how would we know what it did?" and replaces the vague cost line.
- **Title:** Every run can be audited from the terminal, and runaway runs are stopped by default limits
- **Visual:** a terminal card on the left, a "default limits" card on the right
  - `gh aw logs`: analyzes many runs (tool use, network patterns, errors; `--firewall`)
  - `gh aw audit <run-id>`: one run's root cause, tool use, firewall analysis, token and cost metrics
  - `gh aw outcomes`: were the safe outputs accepted, rejected, ignored or pending?
  - Limits: 20 min agent step · 1000 AI Credits per run · `max-ai-credits`, `max-daily-ai-credits`, `timeout-minutes`, `engine.model`
- **Bullets:** the docs suggest cheaper models for routine tasks · `update-docs.md` itself comments "you can use a small model to keep costs down"
- **Sources:** CLI reference · debugging page · cost-management reference · frontmatter reference
- **Conflict to resolve:** the cost page says the default is "5000 AI Credits per workflow per day", but the frontmatter page says `max-daily-ai-credits` is disabled by default. Leave the daily default off the slide until checked. Slide 9 also bills cost in "premium requests" while the docs now use AI Credits. TODO: reconcile.
- **Audience:** technical: observable and debuggable like any CI job. Non-technical: "there's a receipt for every run, and a spending cap."

---

## Ranked shortlist
1. **B: separate jobs.** It is the strongest support for "checked, not trusted" and replaces slide 8, so it adds no length.
2. **A: real `update-docs.md`.** It is the core idea made concrete and replaces slide 5's example.
3. **D: audit trail and limits.** It closes the trust loop and fixes the cost wording.
4. **C: firewall.** Good depth, but it should be folded into slide 9 rather than standing alone.

## Keeping length (13 slides now)
- **Merge** B into slide 8 and A into slide 5. Both are swaps, so +0 slides.
- **Fold** C into slide 9's prompt-injection pair. +0.
- **Add** D as the only new slide. That makes 14.
- **To get back to 13:** fold slide 7 (three job types) into a strip on slide 4 or 6, and move slide 6's "try it safely" line onto slide 12, where `gh aw trial` and `staged: true` already appear.

## Checked: 17 Oct 2026
- https://github.github.com/gh-aw/introduction/architecture/
- https://github.github.com/gh-aw/reference/frontmatter/
- https://github.github.com/gh-aw/reference/safe-outputs/
- https://github.github.com/gh-aw/reference/threat-detection/
- https://github.github.com/gh-aw/reference/network/
- https://github.github.com/gh-aw/reference/cost-management/
- https://github.github.com/gh-aw/setup/cli/
- https://github.github.com/gh-aw/setup/quick-start/
- https://github.github.com/gh-aw/troubleshooting/debugging/
- https://github.com/githubnext/agentics (README) and `workflows/update-docs.md` (raw)
- Status: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview (public preview since 11 Jun 2026)
