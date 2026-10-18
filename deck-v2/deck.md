---
marp: true
theme: default
paginate: true
size: 16:9
title: Repos that keep themselves up to date
description: GitHub Agentic Workflows — from AI that suggests to AI that does
style: |
  :root {
    --bg: #ffffff;
    --surface: #f6f8fa;
    --line: #d0d7de;
    --line-soft: #e6eaef;
    --text: #1f2328;
    --dim: #59636e;
    --accent: #0969da;
    --accent-soft: #ddf4ff;
    --caution: #9a6700;
  }
  section {
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    padding: 84px 72px 104px;
    line-height: 1.5;
    place-content: start;
  }
  section.lead { place-content: safe center; }
  section::after { color: var(--dim); font-size: 18px; }
  header {
    color: var(--dim); font-size: 17px; letter-spacing: 0.1em; text-transform: uppercase;
    top: 26px; left: 72px;
  }
  header::before {
    content: ''; display: inline-block; vertical-align: middle;
    width: 20px; height: 2px; margin: -2px 12px 0 0; border-radius: 2px;
    background: var(--accent);
  }
  h1, h2 { margin-top: 0; color: var(--text); letter-spacing: -0.02em; max-width: 1060px; }
  h1 { font-size: 64px; line-height: 1.1; }
  h2 { font-size: 40px; line-height: 1.16; }
  strong { color: var(--text); font-weight: 700; }
  section > p, section > ul, section > ol { max-width: 1000px; }
  li::marker { color: var(--dim); }
  code { background: var(--surface); color: var(--text); padding: .12em .32em; border-radius: 4px; border: 1px solid var(--line-soft); }
  pre { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; }
  pre code { background: transparent; color: var(--text); padding: 0; border: 0; }
  pre code span { color: var(--text) !important; }
  pre code .hljs-attr, pre code .hljs-section, pre code .hljs-bullet { color: var(--accent) !important; }
  table { border-collapse: collapse; }
  table tr, table tr:nth-child(2n) { background: transparent; }
  table th, table td, table tr:nth-child(2n) td {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--line);
    padding: 10px 16px;
  }
  table th { color: var(--text); background: var(--surface); letter-spacing: .01em; }
  blockquote {
    border-left: 3px solid var(--line);
    color: var(--text);
    font-size: 24px;
    margin: 20px 0;
    padding-left: 22px;
  }
  .lead { text-align: center; justify-content: center; }
  section.lead h1, section.lead h2, section.lead p { text-align: center; }
  section.lead > p { margin-left: auto; margin-right: auto; }
  .lede {
    font-size: 26px; line-height: 1.35; color: var(--text);
    max-width: 980px; margin: 0 0 20px;
  }
  .muted { color: var(--dim); font-size: 20px; line-height: 1.4; }
  .todo { color: var(--caution); font-size: 20px; }
  .stat {
    font-size: 120px; font-weight: 700; color: var(--accent); line-height: 1;
    letter-spacing: -0.04em;
  }
  .source {
    position: absolute; left: 72px; right: 120px; bottom: 22px; margin: 0;
    color: var(--dim); font-size: 20px; line-height: 1.3;
  }
  .turn {
    margin-top: 22px; padding: 18px 24px;
    border-left: 4px solid var(--accent); border-radius: 4px 10px 10px 4px; background: var(--accent-soft);
    font-size: 25px; line-height: 1.35;
  }
  .turn em { font-style: normal; font-weight: 700; color: var(--text); }
  .cards { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
  .card {
    background: var(--surface); border: 1px solid var(--line);
    border-radius: 10px; padding: 18px 22px 16px; position: relative;
  }
  .card::before {
    content: ''; position: absolute; top: -1px; left: 22px; width: 26px; height: 3px;
    border-radius: 2px; background: var(--accent);
  }
  .card p { margin: 6px 0 0; font-size: 22px; line-height: 1.4; }
  .card .muted { font-size: 20px; }
  .k {
    font-size: 18px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
    color: var(--accent);
  }
---

<style scoped>
section {
  display: grid; grid-template-columns: 1fr 1.1fr; align-items: center; align-content: center; column-gap: 24px;
  padding: 40px 40px 40px 72px;
  background:
    radial-gradient(130% 110% at 50% 45%, transparent 40%, rgba(0,0,0,.62) 100%),
    radial-gradient(64% 3% at 73% 49%, rgba(223,231,247,.36), transparent 70%),
    radial-gradient(105% 12% at 73% 49%, rgba(143,176,220,.18), transparent 74%),
    radial-gradient(52% 72% at 72% 48%, rgba(143,176,220,.30), transparent 70%),
    radial-gradient(42% 56% at 8% 8%, rgba(143,176,220,.14), transparent 72%),
    radial-gradient(28% 40% at 100% 100%, rgba(185,208,238,.14), transparent 70%),
    linear-gradient(135deg, #070a10 0%, #0f1828 56%, #050507 100%);
}
.brand p { display: flex; align-items: center; gap: 16px; margin: 0; font-size: 40px; font-weight: 700; letter-spacing: -.01em; color: #f0f6fc; }
h1 { margin: 48px 0 0; font-size: 60px; line-height: 1.12; letter-spacing: -.025em; font-weight: 800; color: #f0f6fc; text-shadow: 0 0 40px rgba(143,176,220,.28); }
.rule { margin-top: 32px; width: 72px; height: 6px; border-radius: 12px; background: linear-gradient(90deg, #8fb0dc 0%, #b9d0ee 100%); box-shadow: 0 0 22px rgba(143,176,220,.6); }
.sub { margin: 32px 0 0; font-size: 24px; line-height: 1.35; color: #b9d0ee; }
.meta p { margin: 20px 0 0; font-size: 20px; }
.loop p { margin: 0; }
.loop img { width: 100%; height: auto; display: block; filter: drop-shadow(0 0 22px rgba(185,208,238,.26)); }
.muted { color: #9aa7b8; }
.todo { color: #f0c05a; }
section::after { color: #9aa7b8; }
</style>

<div>
<div class="brand">

![GitHub mark w:56 h:56](img/github-mark.svg) GitHub

</div>

# Repos that keep themselves up to date

<div class="rule"></div>
<div class="sub">GitHub Agentic Workflows: from AI that suggests to AI that does</div>
<div class="meta">

<span class="muted">Donal Moloney</span> · <span class="todo">TODO: talk date and audience</span>

</div>
</div>
<div class="loop">

![Cycle diagram: the GitHub Octocat mark at the centre of a loop of six steps, Plan, Code, Test, Review, Open PR and Monitor, connected by glowing arrows](img/title-loop.svg)

</div>

<!--
Open with the promise, not the product: a repo whose docs keep up with its code.
"Today: what GitHub Agentic Workflows are, how they stay safe, and a one-month pilot I'd like us to try."
Mixed room: plain-English version first on every slide; the technical detail is there for those who want it.
-->

---

<!-- header: Why now -->
<!-- _class: lead -->

<style scoped>.stat { font-size: 180px; margin: 28px 0 20px; text-align: center; } p { font-size: 28px; max-width: 880px; }</style>

## Somewhere in our docs, a page is wrong right now, and nobody knows which one

<div class="stat">56.5%</div>

of 12,374 developers say **outdated information** gets in the way of the context they need at work.

<div class="source">Stack Overflow Developer Survey 2026</div>

<!--
Pause after the title. Let people think of their own stale page.
56.5% of 12,374 developers name outdated information as a blocker.
TODO: the "72.6% say recent or clearly up to date makes information trustworthy (n=12,996)" line could not be found in the 2026 survey on 17 Oct 2026; don't say it until a source URL is found.
Older backup if challenged: about two-thirds of 45 developers agreed docs are "always outdated" (Lethbridge et al., IEEE Software, 2003). The problem is old; what's new is the speed.
Transition: so why is it still wrong? Nobody decided to let it rot.
-->

---

## Nobody chose to let that page go stale: keeping it current is nobody's job

<style scoped>
h2 { margin-bottom: 14px; }
.cards { grid-template-columns: repeat(3, 1fr); gap: 16px; }
.card p { font-size: 21px; }
.turn { margin-top: 24px; }
</style>

<p class="lede">Three people could have fixed it. Each had a better reason not to.</p>

<div class="cards">
<div class="card"><div class="k">The author</div><p>Shipped the change that made the page wrong, and moved to the next ticket. The code was the deliverable. The page was not.</p></div>
<div class="card"><div class="k">The reviewer</div><p>Is reading a diff against the clock. The stale sentence is in another file, in another folder, and nothing fails without it.</p></div>
<div class="card"><div class="k">The next reader</div><p>Hits the wrong page, works around it, and has no reason to adopt a file they have never edited.</p></div>
</div>

<div class="turn">So more discipline will not fix this. The update is <em>always worth doing and never worth doing now</em> — and a job that never wins the week needs an owner with nothing else competing for the time.</div>

<div class="source">This slide is the deck's own argument, not a cited finding.</div>

<!--
Plain line: nobody in this room is careless. That page is wrong because fixing it never wins the week.
Walk the three, quickly, and let people recognise themselves: the author has already moved on; the reviewer is reading code against the clock and the doc is somewhere else entirely; the next person finds it wrong, routes around it, and has no claim on a file they have never touched.
Then the turn, slowly: always worth doing, never worth doing now. Pause there. That sentence is the whole reason the rest of the talk exists.
Careful wording: there is no number on this slide on purpose. This is reasoning, not a finding — do not say "studies show" or imply the survey on the previous slide measured ownership. It measured that outdated information blocks people, not why.
Q: "Isn't this just bad process? Add docs to the definition of done." Most teams already have. The checklist competes for the same minutes as the work it is attached to, so it loses to the same pressure. If a checklist had solved it, slide 2 would not be true.
Q: "So assign someone to own the docs." The work is a few minutes spread across every repo and every change, so it is never a whole job in any one place — which is exactly why it never gets staffed.
Q: "Are you saying our team is sloppy?" No, the opposite: this happens to disciplined teams, which is the point.
Transition: and the amount of change this applies to is going up fast.
-->

---

## We ship more code than ever, and we are choosing how much of each change to hand to an agent

<style scoped>h2 { margin-bottom: 12px; } p { margin: 10px 0; } ul { font-size: 25px; margin: 10px 0; }</style>

![Autonomy ladder from L1 Operator to L5 Observer, with gh-aw at L4 Approver w:1136](img/autonomy-ladder.svg)

- **43.2 million** pull requests merged per month, up 23% year over year.
- **Nearly 1 billion** commits pushed in 2025, up 25.1%.

<div class="source">Measured: GitHub Octoverse 2025. Ladder: Feng et al., arXiv 2506.12469, illustrative; the L4 placement is this deck’s interpretation.</div>

<!--
Plain line: the volume of code keeps climbing, and separately, we get to decide how much of each change an agent does. The ladder is the menu of choices, not a prediction.
Careful wording: the title deliberately does not say the autonomy climb causes the volume climb. Octoverse measures the volume; the ladder is an illustrative framework. Say "and", never "because".
Technical: the ladder runs L1 Operator to L5 Observer (Feng et al.). L4 Approver is my reading of gh-aw: the agent does the work, a human approves the consequential step, the PR. It is not the paper's classification of gh-aw.
Numbers: only the Octoverse figures are measured: 43.2M PRs merged per month (+23%), nearly 1 billion commits in 2025 (+25.1%). Don't claim a measured docs gap; slide 2's survey is the docs evidence. The link from more code to staler docs is this deck's interpretation.
Q: "Is AI really behind the growth?" Octoverse reports the growth; don't attribute all of it to AI.
TODO: say which level we are at today.
Transition: I've tried to close this gap before.
If the earlier-attempt slide is cut, use this transition instead: "So that is the pressure. Here is what the tool actually is." The arc holds without it.
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
DAY-OF FALLBACK: if this is still empty on the day, CUT THIS SLIDE. An all-TODO table on screen costs more credibility than the beat is worth, and the arc survives: the previous slide (more code, more autonomy) leads straight into "what it is". Use the alternate transition in that slide's note.
Careful: if the earlier project failed because the work had no owner, that is the same point the "nobody's job" slide already makes. In that case do not re-explain it here — say "I hit exactly what we just described" in one line and move to what was technically missing instead.
-->

---

<!-- header: What it is -->

## An agentic workflow is a GitHub Action you brief instead of script

<style scoped>h2 { margin-bottom: 10px; } p { margin: 8px 0; } .lede { font-size: 22px; margin: 0 0 10px; } img { width: 1070px; }</style>

<p class="lede">A GitHub Action is a job your repository runs by itself whenever something happens in it.</p>

![Four pairs: job description to the Markdown body, shift to on, access badge to permissions tools and network, outbox you check to safe-outputs; a classic Action is steps you write, an agentic workflow is a brief w:1136](img/teammate-model.svg)

<div class="source">The teammate mapping is this deck's model, not GitHub terminology.</div>

<!--
The title is the whole idea. Say it, pause, then: it is still a GitHub Action; the difference is that you brief it instead of scripting it.
The gloss line is there for anyone who does not know what an Action is — read it aloud, do not skip it, and do not apologise for it. Half the room needs it and the other half loses nothing.
Then the teammate model, which carries the rest of the talk:
- job description = the markdown body
- shift = the trigger, on:
- access badge = permissions, tools and network
- outbox you check = safe-outputs. It can't send anything you haven't allowed.
Say the typical jobs out loud rather than listing them on the slide: maintain the repo (docs, triage, dependencies), improve code (reviews, security), report (metrics). Those three groups are from the gh-aw home page and the tasks are from the gallery, but the grouping is mine — say so. Then point at docs: that's this talk's job and the lowest-risk place to start.
Q: "Is this just Copilot in CI?" No: Copilot is one of several engines; what's new is the read-only agent plus checked outputs.
Aside if asked, not on the slide: the docs also name patterns like ChatOps, IssueOps and LabelOps.
Transition: that is what it is. The fair next question is whether it actually works.
-->

---

<!-- header: Does it work? -->

## GitHub reports that 57 of 59 pull requests from its docs workflow were merged

<style scoped>
.cols { display: grid; grid-template-columns: 0.78fr 1.22fr; gap: 36px; align-items: center; margin-top: 16px; }
.stat { font-size: 132px; margin-bottom: 18px; }
.cols p { font-size: 26px; margin: 0; }
.shot img { width: 100%; display: block; border: 1px solid var(--line); border-radius: 10px; }
.shot .muted { font-size: 20px; margin: 10px 0 0; }
</style>

<div class="cols">
<div>
<div class="stat">57 / 59</div>
<p>A 96% merge rate for its Daily Documentation Updater.</p>
</div>
<div class="shot">

![Merged pull request 394 in githubnext/agentics, titled link-checker Fix broken documentation links, opened by the github-actions bot and merged into main, showing two files changed with three additions and three deletions and a structured summary table of the links it fixed](img/real-pr-394.png)

<p class="muted">A different workflow in the same repo — the link checker, not the docs updater.</p>
</div>
</div>

<div class="source">Number: gh-aw blog, 13 Jan 2026; reported by GitHub, small sample — merged is not the same as correct. Screenshot: real merged PR <code>githubnext/agentics#394</code>, captured 18 Oct 2026.</div>

<!--
Plain line: when GitHub ran its own docs agent, people reviewed what it proposed and merged almost all of it.
The number is GitHub's own, from the gh-aw blog ("Meet the Workflows: Continuous Documentation", 13 Jan 2026): 57 of 59 docs PRs merged. Also reported there: Documentation Unbloat 88 of 103, Glossary Maintainer 10 of 10.
Caveat out loud: reported by GitHub, small samples; the post doesn't say which repos. Merged is not the same as correct.
The screenshot is a real merged PR, githubnext/agentics#394, opened by the github-actions bot on 9 Oct 2026 and merged the next day: 2 files, +3 -3, with its own summary table.
Say what it is and what it is not: it is the link checker, not the Daily Documentation Updater the 57/59 refers to. Same repo, same mechanism, different job. Do not let the room merge the two.
Best detail on the slide, worth saying out loud: further down that PR the agent reports about 80 other "broken" links, works out that most are its own regex catching trailing markdown punctuation, and changes none of them. It fixed 2 and left 80 alone. That is the interpretation argument in one artifact.
TODO: replace with a PR from our own pilot once the run happens; that needs the workflow token scope (gh auth refresh -h github.com -s workflow).
Outside evidence if asked: "Inside of CNCF, we are benefiting from improved documentation automation along with improving team reporting across the organization." Chris Aniszczyk, CNCF, GitHub Blog, 13 Feb 2026.
Transition: so it works for GitHub, on GitHub’s repos. The next question is whether it is safe to point at ours.
-->

---

<!-- header: Is it safe? -->

## It will get things wrong, so it is built to be checked, not trusted

<style scoped>h2 { margin-bottom: 12px; } .lede { font-size: 24px; margin: 0 0 20px; } .card .todo { font-size: 20px; }</style>

<p class="lede">You would review a new teammate's first pull request. This one cannot skip that step.</p>

<div class="cards">
<div class="card"><div class="k">Wrong edits</div><p>The workflow file decides. <code>draft: true</code> opens a draft the agent cannot override — but it is set per workflow, not guaranteed by the platform.</p><p class="muted">Never merged automatically: GitHub Blog guidance, not a hard limit.</p></div>
<div class="card"><div class="k">Prompt injection</div><p>The agent is read-only and fenced in. The next slide shows how.</p></div>
<div class="card"><div class="k">Cost</div><p>Bounded per run by default, but a month's bill depends on how often it starts. We come back to that before the ask.</p></div>
<div class="card"><div class="k">Not a fit</div><p>It does not replace build, test or release pipelines.</p></div>
</div>

<div class="source">gh-aw docs (safe outputs, cost management); GitHub Blog.</div>

<!--
Be honest first: it will sometimes be wrong. The design assumes that.
Wrong edits: when a workflow sets draft: true the docs call it "a policy, not a default", so the agent cannot override it. Do NOT say "it can only ever open drafts" — verified 17 Oct 2026, githubnext/agentics ships update-docs.md with draft: true AND link-checker.md with draft: false, and the link checker's PR #394 was merged as a normal PR. The guarantee is per workflow, and it is ours to set. "Never merged automatically" is GitHub Blog guidance, not a hard limit, since an experimental merge output exists.
Cost: a per-run budget is on by default, 1,000 AI Credits; 1 AIC = $0.01, so about $10. The docs call AIC best-effort, so it may not match the bill exactly.
If asked about a daily cap: two docs pages disagree on its default, so I've left it out.
Q: "Could it replace our CI or release pipeline?" No: it's not for build, test or release pipelines; it's for work that needs interpretation. Say the limit out loud as well as showing it; naming it early buys trust.
Say the quote out loud rather than putting it on the slide: "Getting an agent to open a pull request was never the hard part. Trusting it enough to merge is." (May Walter, CTO, Hud.io, GitHub changelog, 11 Jun 2026.)
Transition: so trust is the real question. Here is what the design does about it.
-->

---

## The agent never holds a write token: a separate, checked job does the writing

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } ul { font-size: 24px; margin: 10px 0; } .muted { font-size: 20px; } .lede { margin: 16px 0 6px; }</style>

![Four jobs in a row with a write-token row beneath: the Agent job has none, the Detection job has none, and only the separate Safe outputs job holds a scoped write token; only the proposed output is handed between jobs w:1136](img/run-jobs.svg)

<p class="lede">The teammate drafts the letter; someone else holds the key to the postbox.</p>

- Detection scans every proposed output before anything is written. <span class="muted">A failed check defaults to a caution notice, not a hard block (continue-on-error is true).</span>

<div class="source">gh-aw architecture documentation; four of its six jobs shown.</div>

<!--
The postbox line is on the slide; say it, then extend it: the checker in the middle is a separate job that reads what the teammate wrote before anyone posts anything.
Technical version: least privilege by job boundary. "The agent job runs with minimal read-only permissions, while write operations are deferred to separate jobs" (gh-aw architecture docs). The model never runs in a job that has write scopes.
Detection looks for prompt injection, secret leaks and malicious patches. A detected threat blocks the writes.
Careful wording: don't say it "always blocks". By default, continue-on-error is true, so a detection warning or failure becomes a caution notice rather than a block.
Q: "Which AI does the work?" Engine choice is a setting: GitHub Copilot, Claude Code, Codex, Antigravity (experimental) and Pi; Copilot is the usual default. Gemini is listed but deprecated in favour of Antigravity.
Careful wording: the docs list six jobs (adding pre-activation and conclusion); the diagram simplifies, so don't say "four jobs".
Q: "Is it GA?" No: public preview since 11 Jun 2026 (GitHub changelog).
Transition: that separation does not make it right, only checkable. So here is the whole job it gets checked against, in thirteen lines.
-->

---

## Thirteen lines say when it runs, what it can read, and the one thing it can send

<style scoped>pre { font-size: 22px; margin: 10px 0; padding: 22px 24px; } .cols { display: grid; grid-template-columns: 1.1fr 1fr; gap: 40px; align-items: start; margin-top: 8px; } ul { font-size: 25px; margin: 0; } li { margin-bottom: 12px; } .turn { font-size: 21px; margin-top: 20px; padding: 14px 18px; }</style>

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
- **Tools:** broad **reads** — `bash`, `web-fetch`, every GitHub read toolset.

<div class="turn">Yes, that is a lot of access. All of it runs <em>inside the read-only, firewalled job</em> from the previous slide, and the outbox is still the only way anything leaves.</div>

</div>
</div>

<div class="source">Frontmatter trimmed from <code>workflows/update-docs.md</code> in githubnext/agentics.</div>

<!--
This is a real file, trimmed: update-docs.md from githubnext/agentics. Not a made-up example.
Walk it against the teammate pairs from the teammate slide: shift = every push to main; badge = read-all plus network: defaults (the firewall); outbox = one draft pull request.
Transition: that is one job description. I have already written ninety-eight of them.
The objection is now answered on the slide, so raise it yourself before the room does: point at bash: true and toolsets: [all] and say "yes, that is a lot of access" out loud. Volunteering it is what buys the answer credibility. Then the box: read-only job, firewall on the way out, writes in a separate job.
If pressed further: nothing here can write. The write token only exists in the safe-outputs job, two slides back.
-->

---

<!-- header: What I've built -->

## The library is already written and documented; running it is the one step left

<style scoped>h2 { margin-bottom: 20px; } table { font-size: 24px; width: 100%; } td, th { padding: 14px 18px; }</style>

| Already written | Still unproven |
| --- | --- |
| **98** workflow briefs in `workflows/`, one file each | **0** have ever run inside GitHub Actions |
| **98** matching docs pages, one per workflow | **4 of 98** compiled locally; the other 94 are briefs |
| **6** shared policy and prompt modules, imported rather than copied | No release tagged, and the sandbox repo does not exist |

<div class="source"><code>DonalMoloney/Agentic-Workflows-Lib</code>, private. File counts verified via the GitHub API, 17 Oct 2026. The compile result and the "not yet run" column are the repository's own <code>agents.md</code>, a self-report, not a CI result.</div>

<span class="todo">TODO: the one thing building this taught me, and whether the repo goes public before the talk.</span>

<!--
Plain line to say: I didn't come here with a slide deck. I came with 98 of these already written and documented, and not one of them has ever run. That last part is the ask.
Say the right-hand column out loud. Do not let the room hear "98" and assume production. The honest sentence is "written and documented, not yet executed".
Technical detail: 98 markdown briefs in workflows/, each with a docs page in docs/workflows/ carrying the same required-fields table. Six shared modules under workflows/shared/ are imported rather than copy-pasted, so a safety change lands in one place. aw.yml pins min-version v0.83.4.
Numbers and sources: both 98s and the 6 were verified through the GitHub API on 17 Oct 2026; the two filename sets are identical. "4 compiled, 0 errors" and "0 runs" come from the repo's own agents.md.
Careful wording, say none of these: not "98 workflows running", not "98 compiled", not "in production", not "the org is using it". Only 4 of 98 were compiled, and no .lock.yml files are committed at all. The acme-org owner and install strings in that repo are placeholders and resolve to nothing, so never show an install line as runnable.
Q: "So none of this actually works?" Four compile cleanly against the pinned gh-aw version, so the frontmatter and safe-outputs are valid. Runtime behaviour is unproven, and that is exactly what a month of real runs would prove.
Q: "Why 98 and not 4?" The briefs are the cheap part, they are plain English. Compiling, running and reviewing is the expensive part, and I stopped before spending that without agreement.
Q: "Can we see it?" It is private. TODO: decide before the talk whether it goes public.
Q: "How long did this take you?" TODO: answer honestly; it is the question that makes 98 land or sound like padding.
Transition: so the decision is small. But before I ask for it, the question that actually decides it: what would a month of this cost?
-->

---

<!-- header: The ask -->

## A month costs whatever we let it cost, and the run count is a line in a file we review

<style scoped>
h2 { margin-bottom: 12px; }
.lede { margin-bottom: 20px; }
.eq { display: grid; grid-template-columns: 1fr auto 1fr auto 1fr; gap: 14px; align-items: start; }
.eq .op { font-size: 40px; color: var(--dim); padding-top: 42px; }
.term { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px 20px; position: relative; }
.term::before { content: ''; position: absolute; top: -1px; left: 20px; width: 26px; height: 3px; border-radius: 2px; background: var(--accent); }
.term.out { border-color: var(--accent); background: var(--accent-soft); }
.big { font-size: 25px; font-weight: 700; margin: 6px 0 8px; color: var(--text); }
.term p { font-size: 20px; line-height: 1.35; margin: 0; }
.turn { font-size: 23px; margin-top: 20px; }
</style>

<p class="lede">The per-run spend is capped out of the box. What a month costs is a decision about how often it is allowed to start.</p>

<div class="eq">
<div class="term"><div class="k">We choose</div><div class="big">runs per month</div><p>A schedule is a known number: daily is about thirty. Every push to <code>main</code>, as the example file used, is not a number anyone controls.</p></div>
<div class="op">×</div>
<div class="term"><div class="k">Capped by default</div><div class="big">cost per run</div><p>1,000 AI Credits, about $10. The model is also ours to pick.</p></div>
<div class="op">=</div>
<div class="term out"><div class="k">What we commit</div><div class="big">the monthly ceiling</div><p class="todo">TODO: our cap, our expected run count, and the ceiling I am asking for.</p></div>
</div>

<div class="turn">There is no surprise bill here. Both numbers are <em>settings in the workflow file</em>, reviewed in a pull request like any other code.</div>

<div class="source">gh-aw cost management docs; 1 AI Credit = $0.01, which the docs call best-effort. The daily cap is left off on purpose: two docs pages disagree on its default.</div>

<!--
Plain line: the only way this gets expensive is if we let it run constantly, and how often it runs is one line we write.
Walk the equation left to right. The left term is the one people miss: the real file I showed earlier triggers on every push to main, which is fine for GitHub's repo and wrong for a first pilot. For us, a daily schedule is about thirty runs a month and it is a number we can predict.
Numbers: the per-run default is 1,000 AI Credits and 1 AIC is $0.01, so about $10. The docs describe AI Credit accounting as best-effort, so do not present it as an invoice figure.
Careful wording: do not quote a daily cap. The cost-management page says 5,000 per workflow per day by default; the frontmatter page says max-daily-ai-credits is disabled by default. They disagree, so it stays off the slide — it is on the status slide if anyone asks.
Before committing any budget you can price it with nothing landing: staged: true runs the workflow for real and writes nothing, so a week of staged runs gives a real figure. That setting is on the pilot slide; mention it here, do not put it on this slide twice.
Q: "What about Actions minutes?" Those are on top of AI Credits and are the ordinary Actions bill; for one docs workflow on one repo it is small, but I have not measured it. TODO if someone wants the number.
Q: "What if it loops or retries?" The per-run cap is the backstop: the run stops when it hits the credit ceiling.
Transition: so here is what I am actually asking for.
-->

---

## Pick one stale page, and let an agent keep it current for a month

<style scoped>
h2 { margin-bottom: 20px; }
.card .todo { font-size: 20px; }
.need { margin-top: 18px; padding: 14px 22px; border-left: 4px solid var(--accent); border-radius: 4px 10px 10px 4px; background: var(--accent-soft); font-size: 24px; }
</style>

<div class="cards">
<div class="card"><div class="k">Hypothesis</div><p>An agent can keep one page current at a quality we would merge.</p></div>
<div class="card"><div class="k">Method</div><p>One page, one repository, four weeks. Staged first (<code>staged: true</code> runs it for real and writes nothing), then draft pull requests only, every one reviewed.</p></div>
<div class="card"><div class="k">Measure</div><p>Two numbers: the share of its pull requests we merge without edits, and whether the page is actually right at the end of the month.</p><p class="muted">Merge rate alone measures agreement, not freshness. GitHub's 96% is a number to test, not to assume.</p></div>
<div class="card"><div class="k">Decision rule</div><p class="todo">TODO: the result that means keep, the result that means stop.</p></div>
</div>

<div class="need"><strong>What I need today:</strong> <span class="todo">TODO: the pilot repository, its owner, and a budget.</span></div>

<!--
Callback to slide 2: "a page is wrong right now". Let's pick one and settle it.
Frame it as an experiment, not a project: one hypothesis, one method, two measures, one decision rule. That is also the honest framing — we do not know the answer yet, and this is the cheapest way to find out.
Why two measures: merge rate on its own only tells us we agreed with it, and slide 2's problem was a page being wrong, not a pull request being disagreeable. So at the end of the month someone reads the page cold and says whether it is right. Expect a reviewer to make exactly this point; better that it comes from you.
Third number worth tracking if anyone asks for it: reviewer minutes per merged pull request. If it costs more time to review than to fix by hand, the pilot has failed even at a 100% merge rate.
The ask: TODO (pilot repo, owner, budget, and the decision rule). Do not present the 96% as a target we expect to hit; it is GitHub's figure for GitHub's repos, reported by them, on a small sample.
Commands for engineers, if asked: gh extension install github/gh-aw; gh aw init, then gh aw new update-docs; gh aw trial, then staged: true; approve the first PR. The first two take minutes.
Supporting guidance: "Start with low-risk outputs such as comments, drafts, or reports before enabling pull request creation." (GitHub Blog)
Q: "What does it cost?" The per-run default is 1,000 AI Credits (about $10); TODO: the pilot budget.
Transition: thank you; these slides stay up for questions.
-->

---

<!-- header: Appendix -->

## A misled agent is boxed in by layers, not by any single wall

<style scoped>h2 { margin-bottom: 12px; } p { margin: 8px 0; }</style>

![Three numbered layers: 1, the container where the agent sits with opt-in tools; 2, the gates out; 3, only what the workflow lists. All traffic leaves through a Squid proxy limited to an allowlist, an API proxy holding the engine token, and an MCP gateway the documentation itself calls a weak boundary w:1136](img/agent-blast-radius.svg)

<div class="source">gh-aw architecture and network reference. The MCP gateway caveat is the documentation's own wording.</div>

<!--
Plain line: the agent works in a sealed room. It can only talk to the phone numbers we put on the list, and someone else holds the keys.
Technical: the agent is containerised and its egress goes through a proxy with a domain allowlist. Tools are opt-in under `tools:` — `bash: ["gh issue comment"]` limits bash to that one command. `network: defaults` is basic infrastructure only and is what you get if you omit `network:`; `network: {}` is no access at all.
The API proxy matters for a different reason: it keeps the engine's auth token out of the agent's container, so a prompt-injected agent has no credential to exfiltrate.
Careful wording: the MCP gateway is drawn dashed on purpose. The docs say it "is not a strong security boundary against a compromised or malicious agent". Say that out loud — the defence is layers, not any one wall. Claiming otherwise is the fastest way to lose a security-minded room.
Q: "So it can't call out at all?" It can, but only to domains on the list. That list is in the workflow file and gets reviewed like any other code.
Appendix slide: pull it up if someone presses on prompt injection, or asks what stops the agent calling out to anything it likes.
-->

---

<!-- header: Appendix -->
## You debug it like any Action: every run leaves logs you can audit

1. **Review the change:** the `.md` workflow and generated `.lock.yml` in the pull request.
2. **Watch the run:** the Activation, Agent, Detection and Safe outputs jobs — four of the six.
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

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } pre { margin: 10px 0; font-size: 22px; }</style>

```markdown
---
(on:, permissions, network, safe-outputs)
---
Update the docs to match the code that changed, and open a draft PR.
```

![update-docs.md compiled by gh aw compile into update-docs.lock.yml, which GitHub Actions runs w:1136](img/compile-flow.svg)

<span class="muted">Body paraphrased; the real file’s instructions are longer.</span>

<!--
Below the frontmatter is the job description, in plain English. The real body is a page of style rules — it names the Diataxis framework and forbids pushing to the default branch; this one line is a paraphrase.
gh aw compile turns the markdown into a .lock.yml, ordinary GitHub Actions YAML. You commit both, and both get reviewed.
For non-technical listeners: the settings are the rules, the body is the request, and compile turns them into something GitHub already knows how to run.
Q: "Do I need to edit the YAML?" No: edit the markdown and recompile; the lock file is generated.
Transition: so when does it run?
-->

---

## You start a workflow four ways: a repo event, a clock, a button, or a comment

<style scoped>h2 { margin-bottom: 14px; } p { margin: 10px 0; } ul { font-size: 23px; margin: 10px 0; }</style>

![Four trigger routes converge on one workflow run w:1136](img/trigger-routes.svg)

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

<style scoped>
li code { background: var(--surface); border: 1px solid var(--line); border-radius: 6px; }
</style>

## Try it yourself: my examples and the official docs

- <span class="todo">TODO: My sites and example repository URLs</span>
- `https://github.github.com/gh-aw` — the docs, and `/gallery` for ready-made workflows
- `https://github.com/githubnext/agentics` — where this deck’s example `update-docs.md` comes from
- <span class="muted">`https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview`</span>

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
