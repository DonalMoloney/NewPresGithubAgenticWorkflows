# Deck v2: claim ledger

Every factual claim, number, quote and product setting in `deck.md` (slides and speaker notes), re-checked against the source on 2026-10-17; gh-aw docs, changelog, GitHub Blog and agentics rows re-checked 2026-10-18 (survey, Octoverse and paper rows still 2026-10-17). Slide numbers count the title slide as 1, so the status and sources slide is 15.

## Mismatches found

1. **Slide 9, bullet 2: "An API proxy holds the tokens; the agent never sees them."** The architecture page does not say this. It says the proxy "may hold endpoint-specific credentials" and labels it "Agent auth-token isolation". It also warns that an in-container identifier should be treated "as leaked by design". Suggested wording: *"An API proxy routes model traffic and keeps the engine's auth token out of the agent's container."* Or drop the "never sees them" clause.
2. **Slide 2 note: "72.6% (n=12,996) say 'recent or clearly up to date' makes information trustworthy."** I could not find this on survey.stackoverflow.co/2026 (the knowledge page has no such question) or in coverage of the survey. Mark it TODO or cut it until a URL is found.
3. **Slide 8 note: role check on commenters.** The claim holds; this item is a precision fix. The architecture page puts "Pre-activation checks (role/permission)" in the pre-activation job, and the triggers page gives the default allowlist as `[admin, maintainer, write]` (exact match). Suggested note wording: *"Only users with admin, maintainer or write role can trigger it by default; the pre-activation job checks this."*
4. **Slide 12, muted caveat: "GitHub's own repos".** The 13 Jan 2026 blog post gives the 57/59 figure but does not say which repos it comes from. Suggested: *"(gh-aw blog, 13 Jan 2026; reported by GitHub, small sample)"*.
5. **Slide 9 note, engine list (minor).** The engines page lists `copilot`, `claude`, `codex`, `gemini` (deprecated in favour of `agy`), `agy` (Google Antigravity CLI, experimental) and `pi`. The note leaves out Gemini. This is only a problem if someone asks "what about Gemini?".
6. **Slides 9 and 11, job list (minor).** The architecture page has six jobs: Pre-Activation, Activation, Agent, Detection, Safe Output Jobs and Conclusion. The slides show four. That is a fine simplification, but don't say "four jobs" out loud as a fact.

7. **Home page vs architecture page (18 Oct 2026).** The gh-aw home page says "An API proxy holds the tokens, so the agent never sees them"; the architecture page says the proxy "may hold endpoint-specific credentials" and that the in-container identifier is "leaked by design". The deck uses the architecture wording (mismatch 1), so no change.

No other contradictions found. The status (public preview since 11 Jun 2026), the daily-cap conflict and the `continue-on-error: true` default all re-confirmed today.

## Ledger

Status key: **verified** = source says it today · **changed** = source now says something different · **could not verify** = not found in an official source · **conflicting** = official sources disagree.

| Slide | Claim | Source | Checked | Status | Caveat |
| --- | --- | --- | --- | --- | --- |
| 2 | 56.5% say "information is outdated" gets in the way of context | https://survey.stackoverflow.co/2026/knowledge (data: /2026/knowledge/data/context-problems) | 2026-10-17 | verified | Question: "What gets in the way of you getting the context you need for work?" 6,989 of 12,374 respondents. |
| 2 | n = 12,374 | same | 2026-10-17 | verified | |
| 2 (note) | 72.6% (n=12,996) say "recent or clearly up to date" makes information trustworthy | https://survey.stackoverflow.co/2026/knowledge | 2026-10-17 | could not verify | Not on the knowledge page or in survey coverage. See mismatch 2. |
| 2 (note) | About two-thirds of 45 respondents agreed docs are "always outdated" (Lethbridge et al., IEEE Software, 2003) | https://courses.cs.duke.edu//cps196.1/fall11/classwork/Lethbridge-Singer-Forward-2003.pdf | 2026-10-17 | verified | 44% somewhat agree + 24% strongly agree = 68% of 45. The statement is "Documentation is always outdated relative to the current state of a software system." This is a course-hosted copy of the paper, not the publisher's page. |
| 3 | 43.2M pull requests merged per month, up 23% YoY | https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ | 2026-10-17 | verified | Monthly average (35M in 2024 to 43.2M in 2025). Octoverse window is 1 Sep 2024 to 31 Aug 2025 (per secondary coverage). |
| 3 | Nearly 1 billion commits in 2025, up 25.1% | same | 2026-10-17 | verified | Octoverse says "pushed". |
| 3 | Autonomy ladder Operator, Collaborator, Consultant, Approver, Observer (Feng et al.) | https://arxiv.org/abs/2506.12469 | 2026-10-17 | verified | Names and order verified from the abstract (Feng, McDonald, Zhang). L1 to L5 numbering not checked in the full text. |
| 3 | gh-aw sits at L4 Approver | (none) | 2026-10-17 | n/a: interpretation | Already labelled as this deck's interpretation; the paper does not mention gh-aw. |
| 3 (note) | Octoverse does not attribute all growth to AI | Octoverse post above | 2026-10-17 | verified | Careful-wording point, not a claim. |
| 5 | Agent plans the steps from a plain-English goal; Markdown body = instructions | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | "describe automation goals in natural language". |
| 5 | Settings: `on:`, `permissions`, `tools`, `network`, `safe-outputs` | https://github.github.com/gh-aw/reference/frontmatter/ | 2026-10-18 | verified | The teammate mapping is the deck's model. |
| 5 | Typical jobs: maintain (docs, triage, dependencies), improve code (reviews, security), report (metrics) | https://github.github.com/gh-aw/ · https://github.github.com/gh-aw/gallery/ | 2026-10-18 | verified | Home page groups: Maintain / Improve code / Report and plan. Gallery tasks include Documentation Maintenance, Issue Triage, Dependency Analysis, Pull Request Review, Security Review, Metrics and Analytics. Grouping is labelled as the deck's. |
| 5 (note) | Copilot is one of several engines | https://github.github.com/gh-aw/reference/engines/ | 2026-10-18 | verified | |
| 5 (note) | Docs name ChatOps, IssueOps and LabelOps patterns | https://github.github.com/gh-aw/patterns/chat-ops/ | 2026-10-18 | verified | IssueOps and LabelOps are in the same Design Patterns sidebar. |
| 6 | Frontmatter is from `workflows/update-docs.md` in githubnext/agentics (trimmed) | https://raw.githubusercontent.com/githubnext/agentics/main/workflows/update-docs.md | 2026-10-18 | verified | Shown lines match. Trimmed out: `workflow_dispatch`, `protected-files: fallback-to-issue`, `labels`, `timeout-minutes: 15`, commented `engine.model: small`. |
| 6 | `network: defaults` = basic infrastructure only | https://github.github.com/gh-aw/reference/network/ | 2026-10-18 | verified | "Basic infrastructure (certificates, JSON schema, Ubuntu, package mirrors)". Also the default when `network:` is omitted. |
| 6 | `permissions: read-all` = read-only agent job | update-docs.md · https://github.github.com/gh-aw/introduction/architecture/ | 2026-10-18 | verified | |
| 6 | Outbox: one draft PR | https://github.github.com/gh-aw/reference/safe-outputs/ | 2026-10-18 | verified | `create-pull-request` default max 1 per run. |
| 6 | Shift: every push to `main` | update-docs.md | 2026-10-18 | verified | The real file also allows a manual run (`workflow_dispatch`). |
| 7 | `gh aw compile` turns Markdown into a `.lock.yml` GitHub Actions file | https://github.github.com/gh-aw/setup/cli/ | 2026-10-18 | verified | "Compile Markdown workflows to GitHub Actions YAML." |
| 7 (note) | Commit both `.md` and `.lock.yml` | https://github.github.com/gh-aw/setup/quick-start/ | 2026-10-18 | verified | "Commit **both** files". "Both get reviewed" is the deck's advice. |
| 7 (note) | Edit the Markdown and recompile; don't hand-edit the lock file | same | 2026-10-18 | verified | The quick start says to regenerate with `gh aw compile`; it doesn't explicitly forbid hand edits. |
| 7 | Body paraphrased | update-docs.md | 2026-10-18 | verified | The real body is a long technical-writer prompt (Diátaxis, never push to the default branch). |
| 8 | Triggers: `issues`, `pull_request`, `push`; fuzzy `daily`/`hourly`/`weekly`, cron; `workflow_dispatch`, UI, API, `gh aw run`; `slash_command`, `label_command` | https://github.github.com/gh-aw/reference/triggers/ | 2026-10-18 | verified | |
| 8 | `gh aw trial` runs in a temporary private repo (experimental) | https://github.github.com/gh-aw/experimental/trial-ops/ · https://github.github.com/gh-aw/setup/cli/ | 2026-10-18 | verified | TrialOps page: "TrialOps features are experimental." The CLI page itself doesn't label `trial` experimental. Default repo name is `gh-aw-trial`. |
| 8 | `staged: true` under `safe-outputs:` previews and writes nothing | https://github.github.com/gh-aw/reference/staged-mode/ | 2026-10-18 | verified | The preview goes in the Actions step summary. The docs say "Staging is not a sandbox": custom jobs, scripts, external MCP servers and custom credentials are not skipped. |
| 8 (note) | The pre-activation job role-checks the commenter on command triggers | https://github.github.com/gh-aw/introduction/architecture/ · https://github.github.com/gh-aw/reference/triggers/ | 2026-10-18 | verified | Architecture: "Pre-activation checks (role/permission)" protect against "Unauthorized users". Triggers: exact-match allowlist, default `[admin, maintainer, write]`. Neither page explicitly ties the two together for `slash_command`. See mismatch 3. |
| 9 | Agent job is read-only; writes deferred to separate jobs | https://github.github.com/gh-aw/introduction/architecture/ | 2026-10-18 | verified | Quoted verbatim in the note. |
| 9 | Agent runs in a sandboxed container behind a firewall allowlist | same | 2026-10-18 | verified | AWF "containerizes the agent"; Squid proxy "controls the agent's egress traffic via a configurable domain allowlist". |
| 9 | API proxy holds the tokens; agent never sees them | same | 2026-10-18 | changed | Docs say "may hold endpoint-specific credentials" and "Agent auth-token isolation", and warn some identifiers are "leaked by design". See mismatch 1. |
| 9 | Detection job has no write access (diagram) | same | 2026-10-18 | verified | "The detection agent runs in a separate job with no write permissions." |
| 9 | Safe-outputs job has a scoped write token | https://github.github.com/gh-aw/reference/safe-outputs/ | 2026-10-18 | verified | E.g. "a separate job with `issues: write`". |
| 9 | Detection scans for prompt injection, secret leaks, malicious patches | https://github.github.com/gh-aw/reference/threat-detection/ | 2026-10-18 | verified | Automatically enabled when safe outputs are configured; `threat-detection: false` disables it. |
| 9 | A detected threat blocks the writes | same | 2026-10-18 | verified | "If any threat is detected (`true`), the workflow fails and safe outputs are blocked." But `continue-on-error` defaults to `true`, so detection warnings and failures give a caution notice instead of a block. Don't say "always blocks". |
| 9 (note) | `continue-on-error` defaults to `true` | same | 2026-10-18 | verified | |
| 9 (note) | Engines: Copilot, Claude Code, Codex, Antigravity (experimental), Pi | https://github.github.com/gh-aw/reference/engines/ | 2026-10-18 | verified | Docs also list `gemini` (deprecated in favour of `agy`). See mismatch 5. |
| 9 (note) | Copilot is the default engine | same | 2026-10-18 | verified | "Copilot CLI is the default". |
| 9, 15 | Public preview since 11 Jun 2026 | https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview | 2026-10-18 | verified | Technical preview from 13 Feb 2026: https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/ |
| 10 | `draft: true` cannot be overridden by the agent | https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/ | 2026-10-18 | verified | "`draft` is a **policy**, not a default, so the agent cannot override it at runtime." Default `true`. |
| 10 | PRs never merged automatically (GitHub Blog guidance, not a hard limit) | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | Blog: "pull requests are never merged automatically". An experimental `merge-pull-request` output exists (policy gates; merges to the default branch always refused). |
| 10 | Prompt injection: read-only by default, checked writes, threat detection | architecture + threat-detection pages | 2026-10-18 | verified | |
| 10 | 1,000 AI Credits per run by default (`max-ai-credits`) | https://github.github.com/gh-aw/reference/cost-management/ · https://github.github.com/gh-aw/reference/frontmatter/ | 2026-10-18 | verified | Both pages agree. Overridable via `GH_AW_DEFAULT_MAX_AI_CREDITS`. |
| 10 | ~$10 (1 AIC = $0.01) | cost-management | 2026-10-18 | verified | AIC is "computed on a best-effort basis" and may not match the bill. |
| 10 | Configurable models | cost-management · update-docs.md | 2026-10-18 | verified | Docs suggest smaller models for routine tasks. |
| 10 | May Walter quote, CTO Hud.io, GitHub changelog 11 Jun 2026 | https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview | 2026-10-18 | verified | Exact wording matches. |
| 10 (note) | Not for build, test or release pipelines | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | "They do not replace build, test, or release pipelines". |
| 10 (note), 15 | Daily AI Credit cap default | cost-management vs frontmatter | 2026-10-18 | conflicting | Cost management: "5000 AI Credits per workflow per day" by default. Frontmatter: `max-daily-ai-credits` "is disabled by default when omitted". Keep it off the slides. |
| 11 | Watch the run: Activation, Agent, Detection, Safe outputs jobs | architecture | 2026-10-18 | verified | Simplified: Pre-Activation and Conclusion jobs also exist. |
| 11 | `gh aw logs` across runs; `gh aw audit <run-id>` for one run | https://github.github.com/gh-aw/setup/cli/ | 2026-10-18 | verified | |
| 11 (note) | Home page: `gh aw logs` lists tokens, AIC and turns per run | https://github.github.com/gh-aw/ · cost-management | 2026-10-18 | verified | |
| 11 | "Treat the workflow Markdown as code…" (GitHub Blog) | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | Blog post 13 Feb 2026. |
| 12 | Daily Documentation Updater: 57 of 59 PRs merged (96%) | https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/ | 2026-10-18 | verified | Reported by GitHub. The page doesn't state which repos. See mismatch 4. |
| 12 (note) | Documentation Unbloat 88 of 103; Glossary Maintainer 10 of 10 | same | 2026-10-18 | verified | 85% and 100%. |
| 12 (note) | Chris Aniszczyk (CNCF) quote, GitHub Blog, 13 Feb 2026 | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | Title: CTO, Cloud Native Computing Foundation. |
| 13 | `gh extension install github/gh-aw` | https://github.github.com/gh-aw/setup/cli/ | 2026-10-18 | verified | |
| 13 | `gh aw init`, then `gh aw new update-docs` | same | 2026-10-18 | verified | `new` creates a template in `.github/workflows/`. A real copy of agentics' file would come via `gh aw add-wizard githubnext/agentics/<name>` (path for update-docs not confirmed). |
| 13 | `gh aw trial`, then `staged: true` | see slide 8 rows | 2026-10-18 | verified | |
| 13 | "Start with low-risk outputs…" (GitHub Blog) | https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/ | 2026-10-18 | verified | |
| 14 | `github.github.com/gh-aw`, `/gallery`, `github.com/githubnext/agentics` | URLs as listed | 2026-10-18 | verified | All resolve. |
| 15 | gh-aw docs site still links a technical-preview deck | https://github.github.com/gh-aw/ | 2026-10-18 | verified | "The technical preview deck: concepts, security model and examples" (PDF). |
