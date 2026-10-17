# Speaker notes — GitHub Agentic Workflows


9 main-talk slides including title; 8 appendix slides.


## 1 · GitHub Agentic Workflows

Open with the practical problem: documentation is useful only while it reflects the code people actually run. This talk explores whether a repository agent can take on the recurring maintenance work while we retain review of the result.

The proposal is a bounded documentation pilot, not a commitment to automate every repository task. We will look at a readable workflow, the controls around a run, and a way to evaluate the result. Treat all pilot details as proposals until the owner and repository are agreed.

Likely questions:
Q: Is this a proposal to automate everything? A: No. One documentation workflow, with a person reviewing every result.

Transition: first, why this chore deserves attention.


## 2 · Shipping faster quietly creates documentation debt

Plain-English line: every relevant code change creates another opportunity for the documentation to fall behind. I have already tried to address part of that maintenance task.

Technical detail: tell the earlier-project story here in one sentence, using a real limitation. TODO: supply the tool, what it solved and the remaining gap. Do not claim manual copying, manual triggering or any other behaviour unless confirmed. The two opening slides are combined so the audience reaches the example quickly.

Numbers and sources: Stack Overflow Developer Survey 2026, "Which of the following make it difficult to get the context you need for work? Select all that apply." Outdated information: 56.5% (6,989 of 12,374). Checked 17 Oct 2026. Careful wording: it is a multi-select industry survey about context in general, not a measurement of our documentation or of documentation alone.

Audience question: What failed in the earlier approach? Answer with the confirmed limitation; until it is supplied, keep the gap marked TODO.

Title framing: 'documentation debt' is this deck's framing, by analogy with technical debt; the survey shows the cost (outdated information blocks people), not a rate of drift.

Transition: a repository agent can carry the task through to a reviewable result.


## 3 · Agents move people from carrying changes to reviewing them

Explain the shift in responsibility: the workflow gives the agent a task and controlled access to repository context. The agent can inspect information, use tools, and propose an output through the configured mechanism. The output can be a pull request, issue or comment; for this talk, keep the example focused on a documentation draft pull request. Point at the orange box: that manual step is the one the workflow removes. The person does not disappear; they move from carrying the change to reviewing it.

This comparison is illustrative, not a claim that every chat tool or agent has identical behaviour. The workflow still needs good instructions, appropriate permissions and a reviewer. Copilot is the default engine; avoid listing alternatives because the supported set is not the point of this slide.

Likely questions:
Q: How is this different from asking Copilot Chat? A: Chat gives you a suggestion to carry into the repo yourself. The workflow runs in GitHub Actions and hands back a PR, issue or comment through the outputs it is allowed.
Q: Which model runs it? A: Copilot is the default engine. Others can be configured, but that is not the point of this talk.

Title framing: the insight is a role shift, not headcount. Do not imply fewer people; the person still decides what merges.

Transition: before explaining how it works, here is the result a reviewer sees.

Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/


## 4 · Good agent output is a diff you can judge at a glance

Plain-English line: here is a real, small documentation-site fix that a reviewer can understand. An error-dialog heading had appeared in the page table of contents even when it was not useful navigation.

Technical detail: open the linked PR and its Files changed tab. The patch replaces an h3 with a styled div, keeping heading semantics through ARIA attributes. The slide condenses the source to emphasise that change; it is not the complete literal patch. The PR was merged on 3 Jan 2026. Use the actual PR as the demonstration, not a fabricated screenshot.

Numbers and sources: github/gh-aw PR #8716; GitHub’s 13 Jan Continuous Documentation post links it as an outcome in the Documentation Noob Tester causal chain. This is a Copilot coding-agent follow-up, not evidence that the separate githubnext/agentics Update Docs file produced this PR. It improves documentation usability; it does not demonstrate code-to-prose drift repair.

Audience questions: Is this our run? No: it is an explicitly labelled public example. Where is the workflow run? TODO: supply the user's completed run and PR URLs before replacing this with the intended end-to-end demo. The public PR alone does not verify an end-to-end execution trace for the next slide's workflow.

Fallback: keep the real PR open before presenting. The on-slide source excerpts remain available if the network fails. Do not wait for a live run.

Title framing: this is a design principle we are proposing, illustrated by one real PR; it is not a claim that all agent PRs are small.

Transition: but that PR came from a different workflow. Here is the file we would actually start from, one built to keep docs in step with code.

Sources (checked 17 Oct 2026):
https://github.com/github/gh-aw/pull/8716
https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/


## 5 · Guardrails live in reviewable config, not the model

Think of the file as a new teammate's onboarding sheet. The shift says when they work, the access badge says what they can touch, the outbox says what they may hand in, and the job description says what the work is. Walk down the file rather than reading it aloud.

This is the real Update Docs workflow from githubnext/agentics, trimmed for the slide. The full file also declares workflow_dispatch for manual runs, network: defaults, the github, web-fetch and bash tools, PR labels, protected-files: fallback-to-issue and a 15-minute timeout; the body continues with voice, style and step-by-step instructions. The mission sentence shown is quoted verbatim.

The draft setting is enforced PR-creation policy, not a suggestion the agent can override. It is not a universal promise that all gh-aw workflows require human merging. Read-all permissions describe the agent job's repository token; writes happen only through the safe-output jobs.

Likely questions:
Q: Is this our file? A: No. It is a public example we would start from and adapt; our repository and file are still to be confirmed.
Q: Can the agent change its own permissions or turn off draft? A: Not at runtime. The frontmatter is compiled into the workflow, and changing it means editing, recompiling and reviewing the file.
Q: Will it open a PR on every push? A: It runs on every push to main; whether it proposes a change depends on what it finds. For the pilot we can narrow the trigger, and week one's staged preview shows the volume before any PR is written.
Q: Where is the budget? A: Not in this example file. We would add a per-run AI-credit limit for the pilot; that is on the cost slide.

Compilation details are in the appendix.

Title framing: the limits (trigger, permissions, allowed outputs) are compiled settings, so they hold regardless of what the model decides. The quality of the work still depends on the model and the instructions.

Transition: the generated run separates the agent from the jobs that apply outputs.

Sources (checked 17 Oct 2026):
update-docs.md: https://github.com/githubnext/agentics/blob/main/workflows/update-docs.md
PR policy: https://github.github.com/gh-aw/reference/safe-outputs-pull-requests/


## 6 · Safety is designed in, not left to the model

The diagram groups five stages into three readable phases. Pre-activation handles role and skip checks. Activation sanitises event text and validates the lock file. The agent then works in its isolated runtime with read-only repository access and a network allowlist; the API proxy isolates authentication tokens.

The agent can edit its local workspace to prepare a patch. Read-only here describes repository/API permissions, not an inability to draft file changes. Detection inspects the output and patch before the configured safe-output jobs act with the permissions they need.

The docs describe blocking when a threat is detected, and permitting a warning with a human review requirement before merge. The failure case is deliberately not stated as a rule: the same reference describes fail-safe behaviour and says continue-on-error defaults to true, permitting warnings/failures with a caution notice. Test explicit settings before relying on either. The outcome diagram is in the appendix.

Docs wording: "The agent job runs with minimal read-only permissions" and "write operations are deferred to separate jobs that execute only after the agent completes" (Architecture, checked 17 Oct 2026). Say permissions, not tokens: the page does not describe tokens per job.

Avoid promising that isolation or detection catches every problem. These are layers of control, with human review still part of our proposed pilot.

Likely questions:
Q: Can the agent see our secrets? A: The API proxy holds the authentication tokens, so the agent does not see them.
Q: Can it reach any website? A: No. Outbound traffic goes through a network allowlist.
Q: Could a bad PR still get through? A: Yes; detection is a layer, not a guarantee. The pilot keeps draft PRs and human review.
Q: What if the detector crashes? A: The docs are inconsistent, so verify that case in a trial before enabling writes.
Q: What if someone plants instructions in an issue or PR? A: That is prompt injection. The detection job is documented to look for "prompt injection attempts, secret leaks, and malicious code patches", and the agent has no write access either way. A layer, not a guarantee.

Title framing: say it as separation of duties. That is this deck's description of the documented design (read-only agent job, separate write jobs). Do not claim it makes the system safe in every case; detection and review are further layers.

Transition: those controls limit what a run can write, but not what it spends or whether it was worth it.

Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/
Threat detection: https://github.github.com/gh-aw/reference/threat-detection/


## 7 · Price each run in AI credits and reviewer minutes

AIC is a budgeting and comparison unit, based on model-pricing data. The documented per-run default is 1,000 AIC, roughly $10 of estimated inference at 1 AIC = $0.01; it is not a recommended spend for our pilot, and the real bill can differ. We need to set limits appropriate to the selected task.

Careful wording: do not quote a default for the daily AI-credit cap. Official sources disagree on it, so it is left off the slide and recorded on the appendix. If asked, say we will set our own daily cap explicitly.

The agentic step defaults to a 20-minute timeout, and max-turns can cap iterations. Skip rules can avoid unnecessary agent execution. Detection has its own AI-credit cap. AIC accounting is best-effort and can differ from the provider’s bill; GitHub Actions minutes add another cost component.

Use logs to inspect duration and usage, then audit a specific run to understand tool calls and estimated cost. Measure review effort as well as inference: a cheap run that creates substantial rework may not be useful.

Likely questions:
Q: What will this cost per month? A: We do not know until we measure. We will set explicit per-run and daily caps and read the numbers from gh aw logs and gh aw audit.
Q: Is AIC our bill? A: No. It is an estimate; billing may differ, and Actions minutes are a separate cost.

Title framing: the point is total cost of a useful change. AI credits are an estimate; reviewer minutes are not yet measured, which is what the pilot is for.

Transition: that gives us a sequence for a short, measurable pilot.

Sources (checked 17 Oct 2026):
Cost management: https://github.github.com/gh-aw/reference/cost-management/
CLI: https://github.github.com/gh-aw/setup/cli/


## 8 · Four weeks turns opinion into evidence

Plain-English line: use four weeks to learn whether the maintenance benefit justifies the review effort and cost.

Technical detail: week one reviews configuration and previews results. Week two enables draft PRs with human review. Week three records outcomes and tunes the workflow. Week four produces a continue-or-stop decision. In week one, set staged: true under safe-outputs so proposed outputs appear in the Actions step summary instead of being written; the workflow still runs and consumes resources. Disable it, recompile and publish before week two. TrialOps is an optional earlier experiment; trial and staged-mode details are in the appendix.

Numbers and sources: four weeks is a proposed duration, not a measured outcome. Record accepted versus proposed changes, verified documentation problems, reviewer minutes and total run costs. Compare effort against an agreed manual baseline; record rejected or reworked proposals too.

Audience questions: What counts as success? The next slide defines the decision fields and proposed qualitative criteria. Numeric thresholds still require agreement.

Title framing: the pilot replaces debate with our own numbers; week four is an explicit continue, change or stop decision.

Transition: here is the specific approval we need to make that pilot runnable.


## 9 · The ask is small, capped and reversible

Plain-English line: approve a documentation-only trial with a named owner, explicit spending limits and a decision after four weeks.

Technical detail: propose adapting the public githubnext/agentics workflows/update-docs.md already shown. It is a candidate, not the user's confirmed workflow. Name the repository and accountable reviewer before enabling runs. Set explicit per-run and daily limits plus a total pilot budget; a named owner monitors total spend and pauses the workflow when needed. Do not imply that a four-week total budget is automatically enforced by a per-run setting.

Numbers and sources: four weeks is proposed. All monetary values and success thresholds remain TODO pending the user's decisions. The candidate file is linked on the slide. Proposed qualitative criteria are useful accepted documentation fixes, lower total effort than the agreed baseline and spending within budget; these are recommendations, not agreed commitments.

Audience questions: What happens if output is unsafe or spend exceeds a limit? Proposed policy: pause, inspect and decide whether to resume. What must we approve today? The exact scope, repository, owner, budget and thresholds. TODO: confirm the decision-maker and fill every decision field before presenting this as a final approval request.

Closing line: return to the title promise, a controlled path from stale docs to a reviewed pull request. Options for the opening and closing are in deck-v1/hook-and-ending.md. TODO: once slide 1's earlier-attempt story exists, name its gap here as the first thing the pilot tests.

Title framing: reversible means we can switch the workflow off at any point, and anything merged went through normal review as ordinary commits. Spending limits are still TODO.

Transition: end the main talk here and take questions. The appendix holds compilation, detection outcomes, evidence, task selection, installation, trials, staged mode and source conflicts.


## 10 · Compilation turns that file into an Actions workflow

Distinguish authoring from execution. We edit the Markdown source, compile it, review the generated lock file, and publish both files. GitHub Actions executes the generated workflow; it does not interpret arbitrary Markdown on its own.

Compilation includes schema validation and expression safety checks, and generated Actions references are pinned to commit SHAs. These checks help constrain configuration; they do not prove that the agent will make a correct documentation edit. After any configuration change, recompile and publish before testing it.

For manual runs, the workflow needs workflow_dispatch, which the example file declares.

Likely questions:
Q: Why compile instead of running the Markdown directly? A: Actions runs YAML. Compiling validates the configuration and pins actions to commit SHAs, and the lock file can be reviewed like any other workflow.
Q: What if someone edits the Markdown and forgets to recompile? A: The lock file is what runs, and activation validates it. Recompile and publish after every change.


Sources (checked 17 Oct 2026):
Architecture: https://github.github.com/gh-aw/introduction/architecture/
CLI: https://github.github.com/gh-aw/setup/cli/


## 11 · Detection adds a review gate, not a safety guarantee

Plain-English line: detection is another check, not a guarantee that every unsafe change is caught.

Technical detail: the docs describe blocking when a threat is detected, permitting warnings with a human review requirement, and separate jobs applying permitted outputs. The failure case is deliberately not assigned an unconditional branch: the same reference describes fail-safe behaviour and says continue-on-error defaults to true, permitting warnings/failures with a caution notice. Test explicit settings in the chosen workflow before relying on them. Diagnostic tracking issues may also be created.

Numbers and sources: official Threat Detection reference, checked 17 Oct 2026. Do not claim detection always blocks or that nothing can be written after a failed check.

Audience questions: Could a bad PR get through? Yes; the pilot keeps human review. What if the detector crashes? Verify that case in a trial before enabling writes. Draft:true is an enforced creation policy, not a universal prohibition on automatic merging.


Sources: https://github.github.com/gh-aw/reference/threat-detection/


## 12 · GitHub reports strong results for selected docs workflows

These counts are reported by GitHub, not measurements we have independently reproduced. The source gives merge rates of 96%, 85% and 100% respectively. The bars use those reported rates, while the visible denominators keep the scale of the samples clear.

The post does not explicitly identify the repository for these measurements. We are showing three selected workflows; the same post includes others with lower merge rates. A merged PR is useful evidence of acceptance, but it is not a direct measurement of accuracy, time saved or return on investment.

This is an optional evidence slide if time is short. Use it to motivate measurement, not to promise our pilot will match these results.

Likely questions:
Q: Will we get 96%? A: These are small, selected samples reported by GitHub, not a forecast. We will measure our own.
Q: Which repository were these measured in? A: The post does not explicitly identify it.


Sources (checked 17 Oct 2026):
GitHub: Continuous Documentation: https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/


## 13 · Use agents where interpretation adds value

A documentation maintenance task requires interpreting whether an explanation still matches the code. That is the kind of work this pilot is intended to explore. Keep its scope narrow enough that a reviewer can tell whether the proposal is right.

When a deterministic tool can solve the task reliably, use it. The agent does not need to replace the build or test pipeline, and those checks can continue to validate proposed changes.

If discussing the autonomy ladder, describe L4 Approver only as this deck’s interpretation of Feng et al., not a GitHub classification. TODO: establish our actual current autonomy level and the tasks we would keep entirely with a person. Do not put an unconfirmed level on the slide.

Likely questions:
Q: Why not let it fix code too? A: The pilot keeps scope narrow so a reviewer can tell whether a change is right. Build, test and release stay in deterministic CI.
Q: What autonomy level are we at today? A: TODO: agree this before presenting; do not guess.


Sources (checked 17 Oct 2026):
Cost guidance: https://github.github.com/gh-aw/reference/cost-management/


## 14 · Start with one workflow from the example collection

This is where your example-workflow repository becomes useful. It is a separate project and its contents have not been supplied here. TODO: insert the real repository URL, one verified workflow file, and the specific chore it is intended to address. Do not display a fabricated directory tree.

Introduce the workflow as a starting point to review and adapt, not a plug-in guarantee. Walk through its trigger, tool access, allowed outputs and cost limits before installing it. The add-wizard command shown is a template, not an executable reference to our repository.

Likely questions:
Q: Can we use an example workflow unchanged? A: Treat it as a starting point. Review its instructions, permissions, network, outputs and budget before adding it. TODO: name the workflow.


Sources (checked 17 Oct 2026):
CLI: https://github.github.com/gh-aw/setup/cli/


## 15 · A trial can run in a temporary private repository

Use the default temporary-private-repository mode to explore execution away from the pilot repository. TrialOps is documented as experimental. The trial command also supports running against a specified host repository, so do not use that option while describing this as an isolated temporary run.

Replace the workflow placeholder with the verified file or reference and review its credentials and configuration first. Trials can consume Actions and model resources and create outputs inside the trial repository. This is a boundary for the experiment, not a universal no-side-effects mode.

Inspect the reported results and saved trial artifacts. Confirm cleanup rather than promising that every trial repository disappears automatically.

Likely questions:
Q: Does a trial touch our repository? A: Not in the default mode, which runs in a temporary private repository. Do not use the host-repository option if isolation is the point.
Q: Is a trial free? A: No. It uses Actions minutes and model credits.


Sources (checked 17 Oct 2026):
CLI: https://github.github.com/gh-aw/setup/cli/
TrialOps — experimental: https://github.github.com/gh-aw/experimental/trial-ops/


## 16 · Staged mode previews safe outputs before they are applied

Put staged:true under safe-outputs, at the global level shown, so the configured safe outputs are previewed instead of applied. It can also be scoped to individual output types, but that is not the configuration shown here.

Compile the workflow, publish both files, and trigger a run with workflow_dispatch, for example using gh aw run with the confirmed workflow identifier. The example file declares that trigger. Inspect the Actions step summary to see the proposed output.

Staging is about safe-output writes; it does not imply the run consumes no resources or that arbitrary additional steps have no effects. Review the whole workflow. After accepting the preview, disable staging, recompile and publish, then run to create a draft PR under the pilot’s human-review policy.

Likely questions:
Q: Does staged mode stop the agent running? A: No. The workflow still runs and costs; only the safe-output writes are skipped and shown in the step summary.


Sources (checked 17 Oct 2026):
Staged mode: https://github.github.com/gh-aw/reference/safe-outputs/#staged-mode
CLI: https://github.github.com/gh-aw/setup/cli/


## 17 · The technical claims are grounded in GitHub’s documentation

This is a reference appendix, not a second closing slide. The official June 11 changelog establishes public-preview status. Technical preview began earlier; do not repeat the old technical-preview-only claim from earlier drafts.

The technical material was checked on October 17, 2026. The feature set and defaults can change, so recheck these sources before presenting at a later date. The evidence slide has its own report date and must not be described as current pilot results.

Two facts are deliberately off the main slides because official sources conflict. First, the default daily AI-credit cap. Second, the threat-detection page says both that with continue-on-error true (the default) detection failures "produce a caution notice instead of blocking safe outputs", and that if detection itself fails "safe outputs are not applied". Test the failure case in a trial before relying on either.

For questions, return to the specific slide and use its linked official documentation. Local background material remains in overview.md and reference/. The unresolved TODOs are intentional and require your project details before delivery.

Likely questions:
Q: Is this generally available? A: No. It has been in public preview since 11 Jun 2026, so features and defaults can change.

Sources (checked 17 Oct 2026):
Public-preview changelog: https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/
Official docs: https://github.github.com/gh-aw/
