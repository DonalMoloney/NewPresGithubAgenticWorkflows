---
marp: true
theme: default
paginate: true
size: 16:9
title: Repos that keep themselves up to date
description: GitHub Agentic Workflows — from AI that suggests to AI that does
style: |
  section {
    background: #050507;
    color: #ececec;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    padding: 56px 72px;
  }
  section::after { color: #a3a3a3; }
  header { color: #a3a3a3; font-size: 16px; letter-spacing: 0.12em; text-transform: uppercase; top: 24px; left: 72px; }
  h1, h2 { color: #ececec; letter-spacing: -0.03em; }
  h1 { font-size: 64px; }
  h2 { font-size: 40px; }
  strong { color: #b9d0ee; }
  code { background: #141414; color: #b9d0ee; padding: .12em .3em; }
  pre { background: #0d0f14; border: 1px solid #23324a; border-radius: 8px; }
  pre code { background: transparent; color: #d6e2f3; padding: 0; }
  pre code span { color: #d6e2f3 !important; }
  pre code .hljs-attr, pre code .hljs-section, pre code .hljs-bullet { color: #8fb0dc !important; }
  table { border-collapse: collapse; }
  table tr, table tr:nth-child(2n) { background: transparent; }
  table th, table td, table tr:nth-child(2n) td {
    background: transparent;
    color: #ececec;
    border: 1px solid #2a3344;
  }
  table th { color: #b9d0ee; background: #0d0f14; }
  blockquote {
    border-left: 5px solid #8fb0dc;
    color: #ececec;
    font-size: 24px;
    margin: 20px 0;
    padding-left: 20px;
  }
  .lead { text-align: center; justify-content: center; }
  section.lead h1, section.lead h2, section.lead p { text-align: center; }
  .muted { color: #a3a3a3; }
  .todo { color: #e9a35c; }
  .stat { font-size: 120px; font-weight: 700; color: #b9d0ee; line-height: 1; letter-spacing: -0.04em; }
---

<!-- _class: lead -->

# Repos that keep themselves up to date

## GitHub Agentic Workflows: from AI that suggests to AI that does

<span class="muted">Donal Moloney</span> · <span class="todo">TODO: talk date and audience</span>

<!--
Open with the promise, not the product: a repo whose docs keep up with its code.
"Today: what GitHub Agentic Workflows are, how they stay safe, and a one-month pilot I'd like us to try."
Mixed room: plain-English version first on every slide; the technical detail is there for those who want it.
-->

---

<!-- header: Why now -->

## Somewhere in our docs, a page is wrong right now, and nobody knows which one

<div class="stat">56.5%</div>

of 12,374 developers say **outdated information** makes it hard to get the context they need.

<span class="muted">Stack Overflow Developer Survey 2026</span>

<!--
Pause after the title. Let people think of their own stale page.
56.5% of 12,374 developers name outdated information as a blocker.
TODO: the "72.6% say recent or clearly up to date makes information trustworthy (n=12,996)" line could not be found in the 2026 survey on 17 Oct 2026; don't say it until a source URL is found.
Older backup if challenged: about two-thirds of 45 developers agreed docs are "always outdated" (Lethbridge et al., IEEE Software, 2003). The problem is old; what's new is the speed.
-->

---

## As AI climbs the autonomy ladder, we ship more code than ever

<style scoped>h2 { margin-bottom: 12px; } p { margin: 10px 0; } ul { font-size: 25px; margin: 10px 0; } .muted { font-size: 20px; }</style>

![Autonomy ladder from L1 Operator to L5 Observer, with gh-aw at L4 Approver w:1136 h:255](img/autonomy-ladder.svg)

- **43.2 million** pull requests merged per month, up 23% year over year.
- **Nearly 1 billion** commits in 2025, up 25.1%.

<span class="muted">Measured: GitHub Octoverse 2025. Ladder: Feng et al., arXiv 2506.12469, illustrative; the L4 placement is this deck’s interpretation.</span>

<!--
Plain line: each step up this ladder, the AI does more of the work and we do less, and the volume of code keeps climbing.
Technical: the ladder runs L1 Operator to L5 Observer (Feng et al.). L4 Approver is my reading of gh-aw: the agent does the work, a human approves the consequential step, the PR. It is not the paper's classification of gh-aw.
Numbers: only the Octoverse figures are measured: 43.2M PRs merged per month (+23%), nearly 1 billion commits in 2025 (+25.1%). Don't claim a measured docs gap; slide 2's survey is the docs evidence. The link from more code to staler docs is this deck's interpretation.
Q: "Is AI really behind the growth?" Octoverse reports the growth; don't attribute all of it to AI.
TODO: say which level we are at today.
Transition: I've tried to close this gap before.
-->

---

## I built something similar before, and it showed me what was missing

| What I built | What worked | What was missing |
| --- | --- | --- |
| <span class="todo">TODO</span> | <span class="todo">TODO</span> | <span class="todo">TODO</span> |

<span class="todo">TODO: Add screenshot and the specific lesson from the earlier project.</span>

<!--
TODO: tell the story of the earlier project in three beats: what I built, what worked, what was missing.
End on the gap, because the next part of the talk answers it.
-->

---

<!-- header: What it is -->

## An agentic workflow is a GitHub Action whose job is written in plain English and done by an AI agent

**Classic Action:** you script every step. **Agentic workflow:** you describe the goal, and the agent plans the steps.

| Think of it as a new teammate | In the workflow |
| --- | --- |
| Job description | Markdown body |
| Shift | `on:` |
| Access badge | `permissions`, `tools`, `network` |
| Outbox you check | `safe-outputs` |

**Typical jobs:** maintain the repo (**docs**, triage, dependencies), improve code (reviews, security), report (metrics). <span class="muted">gh-aw home page and gallery; grouping is this deck’s.</span>

<!--
Plain line: a classic Action is a recipe; an agentic workflow is a brief.
Then the teammate model, which carries the rest of the talk:
- job description = the markdown body
- shift = the trigger, on:
- access badge = permissions, tools and network
- outbox you check = safe-outputs. It can't send anything you haven't allowed.
Typical jobs: three groups from the gh-aw home page, tasks from the gallery; the grouping is mine. Point at docs: that's this talk's job and the lowest-risk place to start.
Q: "Is this just Copilot in CI?" No: Copilot is one of several engines; what's new is the read-only agent plus checked outputs.
Aside if asked, not on the slide: the docs also name patterns like ChatOps, IssueOps and LabelOps.
Transition: before I show you the file, the question everyone is already asking.
-->

---

## It can still get things wrong, so it is built to be checked, not trusted

<style scoped>h2 { margin-bottom: 20px; } p { font-size: 24px; margin: 16px 0; } .muted { font-size: 20px; }</style>

**Wrong edits →** it can only open a **draft** pull request, and a human reviews it. `draft: true` is a policy the agent cannot override. <span class="muted">Never merged automatically: GitHub Blog guidance, not a hard limit.</span>

**Prompt injection →** read-only by default, every write checked, threat detection on by default.

**Cost →** capped per run: 1,000 AI Credits (~$10) by default, and you choose the model. <span class="todo">TODO: our own measured cost per run.</span>

**Not a fit →** it does not replace build, test or release pipelines. <span class="muted">gh-aw docs (safe outputs, cost management); GitHub Blog.</span>

<!--
Be honest first: it will sometimes be wrong. The design assumes that.
Wrong edits: PRs open as drafts; the docs call draft "a policy, not a default", so the agent can't override it. "Never merged automatically" is GitHub Blog guidance, not a hard limit, since an experimental merge output exists.
Cost: a per-run budget is on by default, 1,000 AI Credits; 1 AIC = $0.01, so about $10. The docs call AIC best-effort, so it may not match the bill exactly.
If asked about a daily cap: two docs pages disagree on its default, so I've left it out.
Q: "Could it replace our CI or release pipeline?" No: it's not for build, test or release pipelines; it's for work that needs interpretation. That limit is on the slide now, because naming it early buys trust.
Say the quote out loud rather than putting it on the slide: "Getting an agent to open a pull request was never the hard part. Trusting it enough to merge is." (May Walter, CTO, Hud.io, GitHub changelog, 11 Jun 2026.)
Transition: so trust is the real question. Here is what the design does about it.
-->

---

## The agent never holds a write token: writes happen in a separate, checked job

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } ul { font-size: 24px; margin: 10px 0; } .muted { font-size: 20px; }</style>

![Activation, then a read-only Agent job, then a Detection job with no write access, then a Safe outputs job with a scoped write token, then a draft PR a human reviews w:1136 h:245](img/run-jobs.svg)

- The agent runs in a sandboxed container behind a firewall allowlist.
- An API proxy keeps the engine’s auth token out of the agent’s container.
- Detection scans every proposed output before anything is written. <span class="muted">A failed check defaults to a caution notice, not a hard block.</span>

<span class="muted">gh-aw architecture documentation. Status: public preview since 11 Jun 2026 (GitHub changelog).</span>

<!--
Plain version: the intern drafts it, a checker reviews it, and only then does the post room send it.
Technical version: least privilege by job boundary. "The agent job runs with minimal read-only permissions, while write operations are deferred to separate jobs" (gh-aw architecture docs). The model never runs in a job that has write scopes.
Detection looks for prompt injection, secret leaks and malicious patches. A detected threat blocks the writes.
Careful wording: don't say it "always blocks". By default, continue-on-error is true, so a detection warning or failure becomes a caution notice rather than a block.
Q: "Which AI does the work?" Engine choice is a setting: GitHub Copilot, Claude Code, Codex, Antigravity (experimental) and Pi; Copilot is the usual default. Gemini is listed but deprecated in favour of Antigravity.
Careful wording: the docs list six jobs (adding pre-activation and conclusion); the diagram simplifies, so don't say "four jobs".
Q: "Is it GA?" No: public preview since 11 Jun 2026 (GitHub changelog).
Transition: that separation doesn't make it right, only checkable. Here is the whole job, in fifteen lines.
-->

---

## The settings say when it runs, what it can read, and the one thing it can send

<style scoped>pre { font-size: 20px; margin: 10px 0; } .cols { display: grid; grid-template-columns: 1.1fr 1fr; gap: 32px; align-items: start; } ul { font-size: 24px; }</style>

<div class="cols">
<div>

```yaml
on:
  push:
    branches: [main]
permissions: read-all
network: defaults
safe-outputs:
  create-pull-request:
    draft: true
tools:
  github:
    toolsets: [all]
  web-fetch:
  bash: true
```

</div>
<div>

- **Shift:** every push to `main`
- **Access badge:** read-only; network limited to basic infrastructure
- **Outbox:** one draft pull request
- **Tools:** broad **reads** — `bash` and the GitHub toolsets stay inside the read-only, firewalled job. The outbox above is still the only way out.

</div>
</div>

<span class="muted">Frontmatter trimmed from `workflows/update-docs.md` in githubnext/agentics.</span>

<!--
This is a real file, trimmed: update-docs.md from githubnext/agentics. Not a made-up example.
Walk it against the teammate chips from the last slide: shift = every push to main; badge = read-all plus network: defaults (the firewall); outbox = one draft pull request.
Transition: that is the entire job description. Now, what does a run like this actually produce?
Expect the question "bash: true?" Yes, tools are broad, but the agent job is read-only and its network goes through the firewall. Writes happen later, in a separate job (the "never holds a write token" slide).
-->

---

<!-- header: Proof -->

## GitHub reports that 57 of 59 pull requests from its docs workflow were merged

<style scoped>.stat { margin-bottom: 28px; }</style>

<div class="stat">57 / 59</div>

Daily Documentation Updater pull requests merged (96%). <span class="muted">gh-aw blog, 13 Jan 2026; reported by GitHub, small sample.</span>

<span class="todo">TODO: screenshots and recordings of a real pull request, issue and comment (link and length for each).</span>

<!--
Plain line: when GitHub ran its own docs agent, people reviewed what it proposed and merged almost all of it.
The number is GitHub's own, from the gh-aw blog ("Meet the Workflows: Continuous Documentation", 13 Jan 2026): 57 of 59 docs PRs merged. Also reported there: Documentation Unbloat 88 of 103, Glossary Maintainer 10 of 10.
Caveat out loud: reported by GitHub, small samples; the post doesn't say which repos. Merged is not the same as correct.
TODO: show the outcome first (the PR screenshot), then the recording of the run behind it. Runs take minutes, so use recordings; a live run is a bonus only.
Outside evidence if asked: "Inside of CNCF, we are benefiting from improved documentation automation along with improving team reporting across the organization." Chris Aniszczyk, CNCF, GitHub Blog, 13 Feb 2026.
Transition: that's GitHub's number. Here's how we'd find ours.
-->

---

<!-- header: The ask -->

## Pick one stale page, and let an agent keep it current for a month

**Decision I need:** <span class="todo">TODO: pilot repository, owner, one-month timeframe, and success measure.</span>

1. **Choose** one stale page and its repository.
2. **Try it safely:** nothing is written to our repo until we choose.
3. **Review** every pull request it opens, for a month.
4. **Decide:** keep, change, or stop.

**Would we get 96%?** Unknown; that is what the pilot measures.

<!--
Callback to slide 2: "a page is wrong right now". Let's pick one and fix it for good.
The ask: TODO (pilot repo, owner, timeframe, success measure, and the decision I need from this room).
Commands for engineers, if asked: gh extension install github/gh-aw; gh aw init, then gh aw new update-docs; gh aw trial, then staged: true; approve the first PR. The first two take minutes.
Supporting guidance: "Start with low-risk outputs such as comments, drafts, or reports before enabling pull request creation." (GitHub Blog)
Q: "What does it cost?" The per-run default is 1,000 AI Credits (about $10); TODO: the pilot budget.
Transition: thank you; these slides stay up for questions.
-->

---

<!-- header: Appendix -->
## You debug it like any Action: every run leaves logs you can audit

1. **Review the change:** the `.md` workflow and generated `.lock.yml` in the pull request.
2. **Watch the run:** Activation, Agent, Detection, and Safe outputs jobs.
3. **Dig in:** `gh aw logs <workflow>` across runs, `gh aw audit <run-id>` for one run.

> “Treat the workflow Markdown as code. Review changes, keep it small, and evolve it intentionally.”
>
> <span class="muted">GitHub Blog</span>

<!--
Backup for "how would we know what it did?". Nothing new to learn operationally: it's an Actions run.
Three levels: review the workflow change in a PR, watch the jobs in the Actions UI, then use the CLI.
gh aw logs analyzes logs and artifacts across runs; the home page says it lists tokens, AIC and turns per run. gh aw audit gives a detailed report for one run.
For managers: there's a receipt for every run.
-->

---

## The instructions are plain English, and one command locks them into a GitHub Action

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } pre { margin: 10px 0; }</style>

<style scoped>pre { font-size: 22px; }</style>

```markdown
---
(on:, permissions, network, safe-outputs)
---
Update the docs to match the code that changed, and open a draft PR.
```

![update-docs.md compiled by gh aw compile into update-docs.lock.yml, which GitHub Actions runs w:1136 h:205](img/compile-flow.svg)

<span class="muted">Body paraphrased; the real file’s instructions are longer.</span>

<!--
Below the frontmatter is the job description, in plain English. The real body is longer (style rules, what to check); this one line is a paraphrase.
gh aw compile turns the markdown into a .lock.yml, ordinary GitHub Actions YAML. You commit both, and both get reviewed.
For non-technical listeners: the settings are the rules, the body is the request, and compile turns them into something GitHub already knows how to run.
Q: "Do I need to edit the YAML?" No: edit the markdown and recompile; the lock file is generated.
Transition: so when does it run?
-->

---

## You can start a workflow four ways: on a repo event, on a schedule, by hand, or by asking in a comment

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } ul { font-size: 23px; margin: 10px 0; }</style>

![Four trigger routes converge on one workflow run w:1136 h:225](img/trigger-routes.svg)

**Try it safely first**

- `gh aw trial` runs a workflow in a temporary private repository (experimental).
- `staged: true` under `safe-outputs:` previews every output and writes nothing.

<!--
Four ways to start a shift: something happens in the repo, a clock, a button, or someone asks in a comment.
Schedules can be fuzzy ("daily") rather than exact cron times.
Two safety nets before it can touch our repo: gh aw trial uses a throwaway private repo (marked experimental in the docs); staged: true runs for real but only previews what it would write, in the run summary.
Q: "Can anyone trigger it with a comment?" by default only users with admin, maintainer or write role can trigger it; the pre-activation job checks this (gh-aw triggers and architecture docs).
Appendix slide: pull it up if someone asks how a run gets started.
-->

---

## Try it yourself: my examples and the official docs

- <span class="todo">TODO: My sites and example repository URLs</span>
- `github.github.com/gh-aw`
- `github.github.com/gh-aw/gallery`
- `github.com/githubnext/agentics`
- GitHub Blog announcement and public-preview changelog

<!--
Leave this up during questions.
The agentics repo is where today's update-docs.md came from.
TODO: my own examples and URLs.
-->

---

## Status and sources

- Fact-checked 17 Oct 2026 against the gh-aw documentation, GitHub changelog, Stack Overflow Developer Survey 2026, Octoverse 2025, GitHub Next, and the GitHub Blog sources cited on each slide.
- Status: **public preview since 11 Jun 2026** (GitHub changelog). The gh-aw docs site still links a technical-preview deck; treat that as a leftover.
- Left off on purpose: the daily AI Credit cap (cost-management page says 5,000 per workflow per day by default; frontmatter page says `max-daily-ai-credits` is disabled by default), and “always blocks” for detection (`continue-on-error` defaults to `true`, turning detection warnings/failures into a caution notice).

<!--
Backup slide; don't present it. Render with: marp deck.md
-->
