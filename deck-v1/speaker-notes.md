# Speaker notes — GitHub Agentic Workflows


17 main-talk slides including title; 8 appendix slides. Rehearsal copy generated from deck-v1/deck.md.


## 1 · GitHub Agentic Workflows

Say: [hook, no statistic] "When did a page of documentation last mislead you? [pause] You followed the steps. They were wrong. The code had moved on. Was that just you? Today's question is whether an AI agent can fix that, and on what terms we could trust it to." Roadmap: "I will define the problem, show one real change and one real workflow file, explain the controls and the cost, and end with a small proposal."

Detail: the idea in one line. We describe the task, keep documentation aligned with code, and we review the result. The agent proposes; a person decides what merges. A controlled path from stale docs to a reviewed pull request.

Evidence: the loop on this slide is illustrative. gh-aw does not deploy; the step is "Open PR" because agents open pull requests and every write is checked before it lands (github.github.com/gh-aw, checked 12 Oct 2026).

Careful wording: do not read the survey number here; it belongs to the next slide. The proposal is a bounded documentation pilot, not a commitment to automate every repository task. Treat all pilot details as proposals until the owner and repository are agreed.

Questions:
Q: Is this a proposal to automate everything? A: No. One documentation workflow, with a person reviewing every result.
Q: Is this generally available? A: No. It has been in public preview since 11 Jun 2026, so features and defaults can change.

Transition: "Stack Overflow's 2026 survey asked developers what makes context hard to get. Here's what they said."


## 2 · Outdated documentation already costs developers time

Say: "In that survey, 56.5 percent of developers named outdated information as a reason context is hard to get. I will call the accumulated cost documentation debt, borrowing Ward Cunningham's technical-debt metaphor."

Analogy: interest on a loan nobody is tracking. Each release adds a little; no one sees the balance until a reader trips over it.

Detail: tell the earlier-project story here in one sentence, using a real limitation. TODO: supply the tool, what it solved and the remaining gap. Do not claim manual copying, manual triggering or any other behaviour unless confirmed. The two opening slides are combined so the audience reaches the example quickly.

Evidence: Stack Overflow Developer Survey 2026, "Which of the following make it difficult to get the context you need for work? Select all that apply." Outdated information: 56.5% (6,989 of 12,374). Checked 17 Oct 2026. The metaphor is Cunningham's technical debt, from his 1992 OOPSLA experience report.

Careful wording: it is a multi-select industry survey about context in general, not a measurement of our documentation or of documentation alone. "Documentation debt" is this deck's framing, by analogy with technical debt; the survey shows the cost (outdated information blocks people), not a rate of drift. Our own drift is not yet measured.

Questions:
Q: What failed in the earlier approach? A: Answer with the confirmed limitation; until it is supplied, keep the gap marked TODO.
Q: Is this our data? A: No. It is an industry survey, not our repositories; our own drift is not yet measured.

Transition: "If that is the cost, the next question is the mechanism: how does the debt build up?"


## 3 · Documentation debt accrues between doc passes

Say: "Documentation rarely fails all at once. Each shipped change adds a small liability, and each doc pass repays only part of it, so the balance never returns to zero."

Analogy: a ledger. Every shipped change is a charge, every doc pass a partial repayment; the hatched area is the running balance.

Detail: the blue staircase is shipped changes; the dashed line is documentation, which only moves when someone does a doc pass. The hatched area is what readers hit: instructions that no longer match the code.

Evidence: none. This is a conceptual picture, labelled illustrative on the slide. It extends Cunningham's (1992) technical-debt metaphor to documentation. The only number in this part of the talk is the survey on the previous slide.

Careful wording: "documentation debt" is this deck's analogy with technical debt. Do not present the chart shape as measured; we have not measured our own drift.

Questions:
Q: Is this our data? A: No, it is illustrative. Measuring our own gap is part of what the pilot does.
Q: Why not just do more doc passes? A: That is the manual fix we already rely on; the cost is people's time, and it is the step that gets skipped when shipping is busy.

Transition: "So the question is who repays it. Before I answer that, I want you to know exactly what I am going to ask for, so you can judge everything that follows against it."


## 4 · The ask is four weeks, one repository, and docs only

Say: "Before I show you anything, here is what I am going to ask for at the end, so you can weigh every slide against it. Four weeks. One repository. Documentation only. Every change arrives as a draft pull request, and a person decides whether it merges."

Analogy: telling the room the price before the demonstration. If the ask is small, saying it early costs nothing and buys attention; if you hide it, people spend the talk guessing.

Detail: this slide exists because the ask used to arrive only on the last slide, which left the audience with no yardstick for the evidence. Do not go through the bounds here - that is the decision slide. State the shape, say the numbers are still blank, and move on. Thirty seconds at most. If someone asks for the budget now, say it is the last open question and you will come back to it.

Evidence: none required. The shape of the ask - four weeks, one repository, docs only, draft pull requests, human merge - is this deck's proposal, stated on the decision slide. No external claim is made here.

Careful wording: do not present this as agreed or approved. Do not give a budget figure, a repository name or an owner: those are genuinely undecided and the gap line at the foot of the slide says so. Do not say "small" or "cheap" - cost is the one thing we have not measured.

Questions:
Q: What will it cost? A: That is the honest gap, and the cost slide is coming. We set explicit caps before anything runs.
Q: Which repository? A: Not decided. Naming it is part of what I am asking for today.

Transition: "That is the ask. Everything from here is the evidence for and against it, starting with what actually changes."


## 5 · Agents shift the human role from execution to review

Say: "The change is one of role, not headcount. Today a person carries each change into the repository by hand; with an agentic workflow, the person reviews a change that has already been prepared."

Analogy: from author to editor. A journal editor does not write the paper; they decide whether it is fit to publish. The agent drafts; you edit and decide.

Detail: the workflow gives the agent a task and controlled access to repository context. The agent can inspect information, use tools, and propose an output through the configured mechanism. The output can be a pull request, issue or comment; for this talk, keep the example on a documentation draft pull request. Point at the dashed box: that manual step is the one the workflow removes. The blue box is where the person now sits: reviewing.

Evidence: illustrative comparison, this deck's framing. Copilot is the default engine.

Careful wording: this is not a claim that every chat tool or agent behaves identically. The workflow still needs good instructions, appropriate permissions and a reviewer. Avoid listing alternative engines; the supported set is not the point of this slide. Do not imply fewer people; the person still decides what merges.

Questions:
Q: How is this different from asking Copilot Chat? A: Chat gives you a suggestion to carry into the repo yourself. The workflow runs in GitHub Actions and hands back a PR, issue or comment through the outputs it is allowed.
Q: Which model runs it? A: Copilot is the default engine. Others can be configured, but that is not the point of this talk.

Transition: "Shifting the role only helps if the split is unambiguous. So here is exactly who does what."

Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/


## 6 · The agent drafts; a person decides what merges

Say: "There are two unspoken questions in this room right now. Does this replace people, and does it turn review into rubber-stamping? So let me be exact about who does what."

Analogy: a draughtsman and the engineer who signs the drawing. The draughtsman prepares the work; the signature, and the responsibility that comes with it, stays with the engineer.

Detail: read the left column, then the right. The agent reads the repository, drafts a change and opens a draft pull request. A person owns the workflow file, reviews the diff, decides what merges, and can switch the whole thing off. Then say the honest sentence on the slide: this moves work from writing to judging - it does not remove it. If volume rises, review time rises with it, and that is exactly why reviewer minutes are a measured quantity in the pilot rather than an assumption.

Evidence: draft: true is enforced pull-request creation policy (PR policy reference, checked 17 Oct 2026). Everything else here is an argument, labelled on the slide as this deck's framing. Reviewer minutes are not measured yet.

Careful wording: do not promise that nobody's job changes, and do not promise headcount is unaffected - neither is ours to promise, and the deck's own notes say not to imply fewer people. Say only what the pilot does. Human merge is our proposed pilot policy, not a product guarantee; gh-aw does not universally prohibit automatic merging. Do not claim review gets easier.

Questions:
Q: Does this replace writers or reviewers? A: No. It changes what the work is: less drafting, more judging. Whether that is a net saving is what the pilot measures.
Q: Won't people just approve whatever it writes? A: That is the real risk, and it is why the pilot is one repository with a named owner and a small number of changes. If we cannot review them properly, that is a result worth having.
Q: Who is accountable for a bad merge? A: The person who approved it, exactly as today.

Transition: "That is the division of labour. But it raises a fair objection, and I want to meet it head on: why hand this to an agent at all, when we already automate things with scripts?"


## 7 · Judging whether the words still match the code is where an agent earns its place

Say: "There is a fair objection here, and I want to meet it head on. We already automate things. Why hand this to an agent instead of writing a script?"

Analogy: a spellchecker versus an editor. A spellchecker applies a fixed rule and is better than a person at it. Deciding whether a paragraph still tells the truth is not a rule, and no spellchecker has ever done it.

Detail: read the left card first and concede it properly - if a deterministic tool solves the task, the tool wins every time. It is cheaper, it is faster, and its failures are predictable. Then the right card: the documentation question is "does this explanation still describe what this code now does", which requires reading the code and the prose and forming a view. There is no rule that expresses it, which is why it has stayed a manual job. Finish on the takeaway: this sits beside CI, it does not replace it. Build, test and release still gate everything the agent proposes.

Evidence: the gh-aw docs position Continuous AI as a third pillar beside CI and CD (docs home, checked 17 Oct 2026). The split between mechanical and judgement work is this deck's framing, labelled as such on the slide, not GitHub's wording.

Careful wording: do not claim agents are better than scripts, or that scripts cannot do documentation work - many documentation chores are mechanical and should stay mechanical. The claim is narrow: the specific task of deciding whether prose still matches code needs interpretation. Do not say this replaces or improves CI.

Questions:
Q: Couldn't a linter catch this? A: For anything with a fixed rule, yes, and we should use one. A linter cannot tell you that a paragraph describes behaviour the code no longer has.
Q: Why not generate the docs from the code? A: That works where docs are a projection of code, like API reference. It does not work for explanation, which is the part that goes stale and the part readers rely on.
Q: Isn't an LLM overkill? A: It may be. That is a cost question, and the cost slide is how we answer it with numbers rather than opinion.

Transition: "So the work needs judgement. Here is what that judgement actually produced, in a real repository."


## 8 · A dialog title leaked into a menu, and the fix is three lines

Say: "The unit of review is the diff. Here is a real one: a modal heading was leaking into the page navigation, and the whole fix can be judged in a few seconds."

Analogy: a good footnote. Small enough that a reader can check it without having to trust the author.

Detail: open the linked PR and its Files changed tab. The patch replaces an h3 with a styled div, keeping heading semantics through ARIA attributes. The slide condenses the source to emphasise that change; it is not the complete literal patch. Use the actual PR as the demonstration, not a fabricated screenshot. Fallback: keep the real PR open before presenting; the on-slide excerpts remain if the network fails. Do not wait for a live run.

Evidence: github/gh-aw PR #8716, merged 3 Jan 2026. GitHub's 13 Jan Continuous Documentation post links it as an outcome in the Documentation Noob Tester causal chain. It is a Copilot coding-agent follow-up.

Careful wording: PR #8716 came from a different workflow. It is not evidence that the githubnext/agentics Update Docs file produced this PR. It improves documentation usability; it does not demonstrate code-to-prose drift repair. "Judge at a glance" is a design principle we propose, illustrated by one real PR, not a claim that all agent PRs are small.

Questions:
Q: Is this our run? A: No. It is an explicitly labelled public example.
Q: Where is the workflow run? A: TODO: supply the user's completed run and PR URLs before replacing this with the intended end-to-end demo. The public PR alone does not verify an end-to-end execution trace for the workflow slide.

Transition: "That is one pull request, honestly labelled. One is not evidence. Here is what GitHub reports at volume."

Sources (checked 17 Oct 2026):
https://github.com/github/gh-aw/pull/8716
https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/


## 9 · GitHub reports 85–100% of documentation pull requests merged in three of its workflows

Say: "GitHub reports high merge rates for three of its own documentation workflows. I show them to motivate measurement, not to predict our result."

Detail: this is the only outcome evidence in the main talk, so handle it carefully. The bars use the reported rates, while the visible denominators keep the scale of the samples clear. We are showing three selected workflows; the same post includes others with lower merge rates. Say the denominators out loud - 59 pull requests is a small sample, and saying so is what makes the number usable rather than salesy.

Evidence: reported by GitHub, 13 Jan 2026 (Continuous Documentation post), not independently reproduced. Daily Documentation Updater 57 of 59 merged (96%); Documentation Unbloat 88 of 103 (85%); Glossary Maintainer 10 of 10 (100%).

Careful wording: these are selected small samples, not a forecast for our pilot. A merged PR is evidence of acceptance, not a direct measurement of accuracy, time saved or return on investment. The post does not explicitly identify the repository for these measurements.

Questions:
Q: Will we get 96%? A: These are small, selected samples reported by GitHub, not a forecast. We will measure our own.
Q: Which repository were these measured in? A: The post does not explicitly identify it.

Transition: "Those are good numbers, from someone else's repositories. Now the honest part, and the question you should be asking: what happens when it is wrong?"

Sources (checked 17 Oct 2026):
GitHub: Continuous Documentation: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/


## 10 · It will be wrong sometimes, and that has to be survivable

Say: "I have shown you a good result. Now the honest part. This will sometimes be wrong, and a pilot that cannot survive being wrong is not worth running. So here are the four ways it fails."

Analogy: hiring a capable new starter. You do not assume their first week is flawless; you scope the work so that a mistake is cheap and visible. Nothing here depends on the agent being right.

Detail: walk the four cards left to right. Confidently wrong is the model misreading code and writing confident prose about it; this is the one a reviewer must catch by reading, and the reason the output is a diff. Too wide a diff is scope creep, which is why the instructions and trigger are narrow. Poisoned input is prompt injection: text planted in an issue or pull request body that the agent reads as instruction. Spend with no merge is the economic failure, and the reason the next slides measure cost per accepted change rather than cost per run. Deliberately do not re-explain the write split or detection here; those are the next two slides and this slide only names what they answer.

Evidence: prompt injection is named in GitHub's own threat-detection reference, which documents the detection job looking for "prompt injection attempts, secret leaks, and malicious code patches" (checked 17 Oct 2026). AI-credit caps are in the cost-management reference. The other three failure modes follow from the nature of the task and are labelled on the slide as this deck's framing, not GitHub's.

Careful wording: do not say the controls prevent these; say they bound them. Detection is a layer, not a guarantee, and continue-on-error defaults to true. Do not give a number for how often any of these happens, in GitHub's repositories or ours - we have not measured it, and the slide says so. Do not promise that a reviewer always catches confidently wrong prose; that is the residual risk the pilot is meant to size.

Questions:
Q: How often will it be wrong? A: We do not know, and I will not guess. Week one runs with staged: true, which shows what it would have written without writing it. That is the first measurement we get.
Q: Isn't confidently wrong documentation worse than stale documentation? A: It is the sharpest objection to this whole proposal, and it is why the output is a draft pull request rather than a commit. A wrong draft is closed in the same second it is read. Stale documentation has no such moment.
Q: Who is accountable when a wrong page gets merged? A: The reviewer who approved it, exactly as with any other pull request. That does not change.

Transition: "Each of those needs a limit rather than a promise. The limits are not in the model - they are in a file we can read."

Sources (checked 17 Oct 2026):
Threat detection: https://github.github.com/gh-aw/reference/threat-detection/
Cost management: https://github.github.com/gh-aw/reference/cost-management/


## 11 · The limits live in a file you can read, not in the model

Say: "The design choice that matters is where the limits live. They live in a short file we review like code, not in the model's judgement. Read it as a new teammate's onboarding sheet."

Analogy: the onboarding sheet for a new teammate (shift, access badge, outbox, job description), written by the employer, not by the new hire.

Detail: walk down the file rather than reading it aloud. The shift (on:) says when they work, the access badge (permissions) says what they can touch, the outbox (safe-outputs) says what they may hand in, and the job description (the Markdown body) says what the work is. The full file also declares workflow_dispatch for manual runs, network: defaults, the github, web-fetch and bash tools, PR labels, protected-files: fallback-to-issue and a 15-minute timeout; the body continues with voice, style and step-by-step instructions. There is no budget in this example file; we would add a per-run AI-credit limit for the pilot, as on the cost slide. Compilation details are in the appendix.

Evidence: the real Update Docs workflow from githubnext/agentics, trimmed for the slide. The mission sentence shown is quoted verbatim. draft: true is enforced PR-creation policy (PR policy reference).

Careful wording: draft is not a suggestion the agent can override, but it is not a universal promise that all gh-aw workflows require human merging. Read-all permissions describe the agent job's repository token; writes happen only through the safe-output jobs. The limits (trigger, permissions, allowed outputs) are compiled settings, so they hold regardless of what the model decides. The quality of the work still depends on the model and the instructions.

Questions:
Q: Is this our file? A: No. It is a public example we would start from and adapt; our repository and file are still to be confirmed.
Q: Can the agent change its own permissions or turn off draft? A: Not at runtime. The frontmatter is compiled into the workflow, and changing it means editing, recompiling and reviewing the file.
Q: Will it open a PR on every push? A: It runs on every push to main; whether it proposes a change depends on what it finds. For the pilot we can narrow the trigger, and week one's staged preview shows the volume before any PR is written.

Transition: "Configuration sets the limits. The next slide shows how the run itself is divided, so that the agent never holds write access."

Sources (checked 17 Oct 2026):
update-docs.md: https://github.com/githubnext/agentics/blob/main/workflows/update-docs.md
PR policy: https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/


## 12 · The agent job is read-only; writes happen in a separate job

Say: "The part that reasons is not the part that writes. The reasoning part runs with least privilege — an old idea in computer security, from Saltzer and Schroeder in 1975."

Analogy: the four-eyes principle in banking. The clerk who prepares a payment is not the one who releases it. Here the agent prepares; a separate job releases.

Detail: the diagram groups five stages into three readable phases. Pre-activation handles role and skip checks. Activation sanitises event text and validates the lock file. The agent then works in its isolated runtime with read-only repository access and a network allowlist; the API proxy isolates authentication tokens, so the agent does not see them. The agent can edit its local workspace to prepare a patch; read-only describes repository and API permissions, not an inability to draft file changes. Detection inspects the output and patch before the configured safe-output jobs act with the permissions they need. The docs describe blocking when a threat is detected, and permitting a warning with a human review requirement before merge. The outcome diagram is in the appendix.

Evidence: "The agent job runs with minimal read-only permissions" and "write operations are deferred to separate jobs that execute only after the agent completes" (Architecture, checked 17 Oct 2026). The detection job is documented to look for "prompt injection attempts, secret leaks, and malicious code patches". Saltzer and Schroeder, "The Protection of Information in Computer Systems" (1975).

Careful wording: the four-eyes comparison is an analogy for the job split; do not imply a second human approves every run. the failure case is deliberately not stated as a rule. The same reference describes fail-safe behaviour and says continue-on-error defaults to true, permitting warnings and failures with a caution notice. Do not say detection always blocks; test explicit settings before relying on either. Say permissions, not tokens: the page does not describe tokens per job. Do not promise that isolation or detection catches every problem; these are layers of control, not a guarantee, with human review still part of our proposed pilot. Least privilege is used in Saltzer and Schroeder's sense and is safe to attribute to them. Do NOT attribute "separation of privilege" to them for the job split: in their 1975 paper that term means requiring two independent keys, which is the four-eyes analogy above, not the read/write split. Call the split privilege separation and mark it as this deck's framing, not GitHub's wording.

Questions:
Q: Could a bad PR still get through? A: Yes; detection is a layer, not a guarantee. The pilot keeps draft PRs and human review.
Q: What if the detector crashes? A: The docs are inconsistent, so verify that case in a trial before enabling writes.
Q: What if someone plants instructions in an issue or PR? A: That is prompt injection. Detection is documented to look for it, and the agent has no write access either way. A layer, not a guarantee.

Transition: "Those controls limit what a run can write. They say nothing about what it spends, or whether it was worth it."

Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/
Threat detection: https://github.github.com/gh-aw/reference/threat-detection/


## 13 · A cheap run nobody merges is still expensive

Say: "The right unit of cost is not the run but the accepted change. A cheap run that nobody merges still costs credits, Actions minutes and a reviewer's attention."

Analogy: measure yield, not throughput. A laboratory judges a method by its cost per valid result, not its cost per experiment run.

Detail: the equation is the metric the pilot measures: credits, Actions minutes and reviewer minutes, divided by accepted changes. AIC is a budgeting and comparison unit, based on model-pricing data. The agentic step defaults to a 20-minute timeout, and max-turns can cap iterations. Skip rules can avoid unnecessary agent execution. Detection has its own AI-credit cap. Use gh aw logs to inspect duration and usage, then gh aw audit <run-id> to understand tool calls and estimated cost for a specific run. Measure review effort as well as inference: a cheap run that creates substantial rework may not be useful.

Evidence: 1 AIC is about $0.01, estimated. The documented per-run default is 1,000 AIC, roughly $10 of estimated inference. AIC accounting is best-effort and can differ from the provider's bill; GitHub Actions minutes add another cost component. Reviewer minutes are not yet measured.

Careful wording: do not quote a default for the daily AI-credit cap. Official sources disagree on it, so it is left off the slide and recorded on the appendix; if asked, say we will set our own daily cap explicitly. The 1,000 AIC default is not a recommended spend for our pilot, and the real bill can differ. We need limits appropriate to the selected task.

Questions:
Q: What will this cost per month? A: We do not know until we measure. We will set explicit per-run and daily caps and read the numbers from gh aw logs and gh aw audit.
Q: Is AIC our bill? A: No. It is an estimate; billing may differ, and Actions minutes are a separate cost.

Transition: "That metric gives us something we can test in a short, measurable pilot."


## 14 · Four weeks turns opinion into evidence

Say: "I propose we treat this as an experiment, not a purchase. Four weeks, with success criteria agreed before we start, so that the result can tell us to stop as readily as to continue."

Analogy: a small, pre-registered trial. Decide what success looks like before seeing the data, so the result cannot be argued into shape afterwards.

Detail: week one reviews configuration and previews results. Week two enables draft PRs with human review. Week three records outcomes and tunes the workflow. Week four produces a continue, change or stop decision. In week one, set staged: true under safe-outputs so proposed outputs appear in the Actions step summary instead of being written. Disable it, recompile and publish before week two. TrialOps is an optional earlier experiment; trial and staged-mode details are in the appendix.

Evidence: four weeks is a proposed duration, not a measured outcome. Record accepted versus proposed changes, verified documentation problems, reviewer minutes and total run costs. Compare effort against an agreed manual baseline; record rejected or reworked proposals too.

Careful wording: describing the pilot as a falsifiable experiment is our recommendation, not an agreed plan. Numeric thresholds still require agreement. Staged mode still runs the workflow and consumes resources; only the writes are skipped.

Questions:
Q: What counts as success? A: The decision slide defines the fields and proposed qualitative criteria. Numeric thresholds still require agreement before we start.
Q: What does week one actually produce? A: Proposed outputs in the Actions step summary, with no writes. The run still costs.

Transition: "Four weeks only helps if we agree now what the result has to show. Here is what I propose we decide in advance."


## 15 · Week four ends in a decision we agreed in advance

Say: "Four weeks only helps if we agree now what the result has to show. Otherwise we will argue about the data afterwards, and whoever is most enthusiastic will win that argument. So here is what I propose we decide in advance."

Analogy: pre-registering a trial. You write down what would count as success before you see the data, precisely so the data can disappoint you.

Detail: three criteria. Useful fixes accepted - documentation problems a reviewer agreed were genuinely real, not merely merged. Less total effort than doing it by hand, measured against a baseline we agree before we start. And spend inside the caps. Say plainly that none of the three has a number yet, and that agreeing those numbers is part of what you are asking for today. Then say the sentence that matters: these are set so that the result can tell us to stop.

Evidence: nothing external. These are the proposed qualitative criteria from the decision slide's notes, now stated on a slide. The thresholds, and the manual baseline, are genuinely undecided and the gap line says so.

Careful wording: do not present these as agreed - they are a recommendation. Do not invent thresholds, a baseline, or a budget figure. Note that a merged pull request is evidence of acceptance, not of accuracy, which is why the first criterion says a reviewer agreed the problem was real rather than simply counting merges.

Questions:
Q: What if we only hit two of the three? A: Then we have a real decision rather than a reflex, and that is the point of agreeing them now.
Q: Who decides? A: The named owner, with you. Naming that person is one of the open fields on the next-but-one slide.
Q: What is the manual baseline? A: Undecided, and it is the hardest of the three. We need an honest estimate of what we spend on this today before week one starts.

Transition: "So that is what the upside has to look like. Now the downside."


## 16 · The downside is bounded by five proposed limits

Say: "Every way this could go wrong is fenced in. Four weeks, a capped budget, one repository with one owner, docs only, draft PRs only, and a person decides what merges."

Analogy: a containment protocol. Each ring limits a different kind of failure: time, money, place, scope and output.

Detail: time is the pilot length; spend is per-run plus daily caps we set explicitly; scope is the update-docs workflow; output is draft pull requests, which the agent cannot override at runtime; the merge decision stays with a person under pilot policy.

Evidence: four weeks is proposed. Spend limits, repository and owner are TODO. draft: true is enforced PR-creation policy (PR policy reference).

Careful wording: "boxed in" describes our proposed configuration and policy, not a guarantee. Detection is a layer, not a fence. Human approval before merge is our policy, not a product limit.

Questions:
Q: What is the worst case? A: A wrong draft PR that a reviewer closes, plus the spend up to the cap. That is why the cap and owner must be set before week one.
Q: Can we stop early? A: Yes. Switch the workflow off at any point.

Transition: "With the downside bounded, we are back where we started. You already know the ask - here it is with the fields we need to fill in together."


## 17 · Approve a four-week, docs-only pilot

Say: "The ask: approve a four-week, docs-only pilot, with a named owner, explicit spending limits and a decision at week four."

Analogy: a two-way door, in Jeff Bezos's terms (Amazon 2015 letter to shareholders): a reversible decision, so it can be made quickly and walked back if it fails.

Detail: propose adapting the public githubnext/agentics workflows/update-docs.md already shown. It is a candidate, not the user's confirmed workflow. Name the repository and accountable reviewer before enabling runs. Set explicit per-run and daily limits plus a total pilot budget; a named owner monitors total spend and pauses the workflow when needed. After the close, take questions; the appendix holds compilation, where agents fit beside CI and CD, detection outcomes, evidence, task selection, installation, trials, staged mode and source conflicts.

Evidence: four weeks is proposed. All monetary values and success thresholds remain TODO pending the user's decisions. The candidate file is linked on the slide. Proposed qualitative criteria are useful accepted documentation fixes, lower total effort than the agreed baseline and spending within budget; these are recommendations, not agreed commitments.

Careful wording: attribute "two-way door" to Bezos (Amazon 2015 shareholder letter, Type 1 vs Type 2 decisions); it is an analogy, not evidence. do not call it capped until the budget fields are filled. It is reversible because the workflow can be switched off at any time and anything merged went through normal review. Do not imply that a four-week total budget is automatically enforced by a per-run setting. The closing below is recommended ending A in deck-v1/hook-and-ending.md, not yet ticked there. TODO: once slide 1's earlier-attempt story exists, name its gap here as the first thing the pilot tests.

Questions:
Q: What happens if output is unsafe or spend exceeds a limit? A: Proposed policy: pause, inspect and decide whether to resume.
Q: What must we approve today? A: The exact scope, repository, owner, budget and thresholds. TODO: confirm the decision-maker and fill every decision field before presenting this as a final approval request.

Transition (close the talk): "At the start I asked when a page of documentation last misled you. [pause] Picture the fix arriving as a draft pull request, with a person deciding what merges. The ask: approve a four-week, docs-only pilot. The honest limit: we don't know the cost yet. The pilot is how we find out. [slow] A controlled path from stale docs to a reviewed pull request. [pause]"


## 18 · Compilation turns that file into an Actions workflow

Say: "Authoring and execution are separate steps. We write a Markdown file, compile it into an ordinary Actions workflow, and review both before anything runs."

Detail: we edit the Markdown source, compile it with gh aw compile, review the generated lock file, and publish both files. GitHub Actions executes the generated workflow; it does not interpret arbitrary Markdown on its own. For manual runs, the workflow needs workflow_dispatch, which the example file declares. After any configuration change, recompile and publish before testing it.

Evidence: compilation includes schema validation and expression safety checks, and generated Actions references are pinned to commit SHAs (Architecture, CLI).

Careful wording: these checks help constrain configuration; they do not prove that the agent will make a correct documentation edit.

Questions:
Q: Why compile instead of running the Markdown directly? A: Actions runs YAML. Compiling validates the configuration and pins actions to commit SHAs, and the lock file can be reviewed like any other workflow.
Q: What if someone edits the Markdown and forgets to recompile? A: The lock file is what runs, and activation validates it. Recompile and publish after every change.

Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/
CLI: https://github.github.com/gh-aw/setup/cli/


## 19 · Agents add a third lane beside CI and CD

Say: "We already automate building and shipping. This adds a third kind of automation, for work that needs judgement, such as keeping docs in sync, and a person still reviews what it produces."

Detail: the gh-aw docs describe Continuous AI alongside CI and CD. Their examples include triage, docs kept in sync with code, tests and fixes. It does not replace the build or test pipeline; those checks still validate proposed changes. It compiles to an ordinary GitHub Actions workflow.

Evidence: gh-aw docs home page, checked 17 Oct 2026: "A third pillar beside CI and CD", with CI captioned "Builds it", CD "Ships it" and Continuous AI "Improving your repo, around the clock".

Careful wording: the split into predictable versus judgement work is this deck's framing, not GitHub's wording. "Third lane" paraphrases the docs' "third pillar". Do not claim it replaces CI or CD.

Questions:
Q: Why not just script the docs update? A: When a deterministic tool solves it, use the tool. Deciding whether an explanation still matches the code is the part that needs interpretation.
Q: Does it run in our existing Actions? A: Yes, it compiles to an ordinary GitHub Actions workflow; details are in the appendix.


## 20 · Detection adds a review gate, not a safety guarantee

Say: "Detection is another check, not a guarantee that every unsafe change is caught."

Detail: the docs describe blocking when a threat is detected, permitting warnings with a human review requirement, and separate jobs applying permitted outputs. Diagnostic tracking issues may also be created. Test explicit settings in the chosen workflow before relying on them.

Evidence: official Threat Detection reference, checked 17 Oct 2026. The same reference describes fail-safe behaviour and says continue-on-error defaults to true, permitting warnings and failures with a caution notice.

Careful wording: the failure case is deliberately not assigned an unconditional branch. Do not claim detection always blocks or that nothing can be written after a failed check. draft: true is an enforced creation policy, not a universal prohibition on automatic merging.

Questions:
Q: Could a bad PR get through? A: Yes; the pilot keeps human review.
Q: What if the detector crashes? A: Verify that case in a trial before enabling writes.

Sources: https://github.github.com/gh-aw/reference/threat-detection/


## 21 · Use agents where interpretation adds value

Say: "Use an agent where the task needs interpretation, and a deterministic tool where it does not."

Detail: documentation maintenance requires judging whether an explanation still matches the code. That is the kind of work this pilot explores. Keep its scope narrow enough that a reviewer can tell whether the proposal is right. The agent does not need to replace the build or test pipeline, and those checks can continue to validate proposed changes.

Evidence: none beyond the linked cost guidance. TODO: establish our actual current autonomy level and the tasks we would keep entirely with a person.

Careful wording: if discussing the autonomy ladder, describe L4 Approver only as this deck's interpretation of Feng et al., not a GitHub classification. Do not put an unconfirmed level on the slide.

Questions:
Q: Why not let it fix code too? A: The pilot keeps scope narrow so a reviewer can tell whether a change is right. Build, test and release stay in deterministic CI.
Q: What autonomy level are we at today? A: TODO: agree this before presenting; do not guess.

Sources (checked 17 Oct 2026):
Cost guidance: https://github.github.com/gh-aw/reference/cost-management/


## 22 · Start with one workflow from the example collection

Say: "Start from one existing workflow, and review it as you would a new colleague's access request."

Detail: this is where the example-workflow repository becomes useful. It is a separate project and its contents have not been supplied here. Walk through its trigger, tool access, allowed outputs and cost limits before installing it. The add-wizard command shown is a template, not an executable reference to our repository.

Evidence: none yet. TODO: insert the real repository URL, one verified workflow file, and the specific chore it is intended to address.

Careful wording: introduce the workflow as a starting point to review and adapt, not a plug-in guarantee. Do not display a fabricated directory tree.

Questions:
Q: Can we use an example workflow unchanged? A: Treat it as a starting point. Review its instructions, permissions, network, outputs and budget before adding it. TODO: name the workflow.

Sources (checked 17 Oct 2026):
CLI: https://github.github.com/gh-aw/setup/cli/


## 23 · A trial can run in a temporary private repository

Say: "A trial lets us observe a run away from the pilot repository. It changes where the run happens, not whether it costs anything."

Detail: use the default temporary-private-repository mode. Replace the workflow placeholder with the verified file or reference and review its credentials and configuration first. Inspect the reported results and saved trial artifacts.

Evidence: TrialOps is documented as experimental. The trial command also supports running against a specified host repository. Trials can consume Actions and model resources and create outputs inside the trial repository.

Careful wording: do not use the host-repository option while describing this as an isolated temporary run. This is a boundary for the experiment, not a universal no-side-effects mode. Confirm cleanup rather than promising that every trial repository disappears automatically.

Questions:
Q: Does a trial touch our repository? A: Not in the default mode, which runs in a temporary private repository. Do not use the host-repository option if isolation is the point.
Q: Is a trial free? A: No. It uses Actions minutes and model credits.

Sources (checked 17 Oct 2026):
CLI: https://github.github.com/gh-aw/setup/cli/
TrialOps — experimental: https://github.github.com/gh-aw/experimental/trial-ops/


## 24 · Staged mode previews safe outputs before they are applied

Say: "Staged mode lets us see what the agent would have written, before it writes anything."

Detail: put staged: true under safe-outputs, at the global level shown, so the configured safe outputs are previewed instead of applied. It can also be scoped to individual output types, but that is not the configuration shown here. Compile the workflow, publish both files, and trigger a run with workflow_dispatch, for example using gh aw run with the confirmed workflow identifier. The example file declares that trigger. Inspect the Actions step summary to see the proposed output. After accepting the preview, disable staging, recompile and publish, then run to create a draft PR under the pilot's human-review policy.

Evidence: staged mode reference and CLI, linked on the slide.

Careful wording: staging is about safe-output writes; it does not imply the run consumes no resources or that arbitrary additional steps have no effects. Review the whole workflow.

Questions:
Q: Does staged mode stop the agent running? A: No. The workflow still runs and costs; only the safe-output writes are skipped and shown in the step summary.
Q: Can staging apply to only some outputs? A: Yes, it can be scoped to individual output types, but the pilot uses the global setting shown.

Sources (checked 17 Oct 2026):
Staged mode: https://github.github.com/gh-aw/reference/safe-outputs/#staged-mode
CLI: https://github.github.com/gh-aw/setup/cli/


## 25 · The technical claims are grounded in GitHub’s documentation

Say: "Every technical claim in the talk traces to GitHub's own documentation, checked on 17 October 2026. Where official sources disagree, I have left the fact off the slides."

Detail: this is a reference appendix, not a second closing slide. For questions, return to the specific slide and use its linked official documentation. Local background material remains in overview.md and reference/. The unresolved TODOs are intentional and require project details before delivery.

Evidence: the official June 11 changelog establishes public-preview status; technical preview began earlier. Two facts are deliberately off the main slides because official sources conflict. First, the default daily AI-credit cap. Second, the threat-detection page says both that with continue-on-error true (the default) detection failures "produce a caution notice instead of blocking safe outputs", and that if detection itself fails "safe outputs are not applied".

Careful wording: do not repeat the old technical-preview-only claim from earlier drafts. The feature set and defaults can change, so recheck these sources before presenting at a later date. The evidence slide has its own report date and must not be described as current pilot results. Test the detection failure case in a trial before relying on either reading.

Questions:
Q: Is this generally available? A: No. It has been in public preview since 11 Jun 2026, so features and defaults can change.
Q: What is the default daily AI-credit cap? A: Official sources disagree, so we will set our own explicitly.

Sources (checked 17 Oct 2026):
Public-preview changelog: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/
Official docs: https://github.github.com/gh-aw/
