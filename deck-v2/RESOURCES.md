# Deck v2: better resources and alternative slide content

Research pass, 18 Oct 2026. `todo.md` lists what is broken; this file lists **what better material exists to put there**.

Scoped to v2's arc — the story: a wrong page, nobody's job, the turn, the evidence, the ask. The material here is drawn mostly from **one source the deck already cites**, the Stack Overflow Developer Survey 2026, because a story deck is stronger with fewer sources to explain. Cost arithmetic and GitHub Actions pricing live in `../deck-v1/RESOURCES.md`; mechanism detail and frontmatter fields live in `../deck-v3/RESOURCES.md`. Deliberately not repeated here.

**Status labels** (deck vocabulary): **Measured** = counted, method named · **Documented** = gh-aw/GitHub docs · **Reported by GitHub** = GitHub's own claim · **Secondary** = press coverage, verify before use.

All figures fetched or counted **18 Oct 2026** from the pages cited at the end.

> **Slide numbers drift — confirm by title.** All three decks were edited while this file was being written: deck-v2 gained a slide and reordered, deck-v3 shifted by one from slide 5 on, and several deck-v1 titles changed. The numbers below were correct at **18 Oct 2026**; the **titles** are the reliable anchor. Check the title before editing a slide.

| § | Slide(s) | Title(s) as of 18 Oct 2026 |
|---|---|---|
| 1 | 2 | More than half of developers say outdated information gets in the way of their work |
| 2 | 3 | Nobody chose to let that page go stale: keeping it current is nobody's job |
| 3 | 8 | GitHub reports that 57 of 59 pull requests from its docs workflow were merged |
| 4 | 9 | It will get things wrong, so it is built to be checked, not trusted |
| 5 | 22 | Status and sources |
| 6 | 14, 22 | A month costs whatever we let it cost, and the run count is a line in a file we review · Status and sources |
| 7 | 21 | Try it yourself: my examples and the official docs |


---

## 1. Slide 2 (the hook): there is a stronger number on the page you already cite

The slide leads with **56.5% of 12,374** say outdated information gets in the way. Verified at source — but it is the **third** item in a 16-item question, and the same chart contains a figure that inverts far better.

**Measured.** Stack Overflow Developer Survey 2026, "What gets in the way of you getting the context you need for work?", n = 12,374:

| Rank | Barrier | % | Respondents |
|---|---|---|---|
| 1 | Information is incomplete | 63.2% | 7,825 |
| 2 | Important context lives in people's heads | 60.9% | 7,541 |
| 3 | **Information is outdated** | **56.5%** | **6,989** |
| 4 | Information is spread across too many tools | 53.4% | 6,603 |
| 5 | I do not know where to look | 30.8% | 3,816 |
| 6 | Important decisions are hard to find later | 26.1% | 3,226 |
| 7 | Different teams have different versions of the truth | 25.4% | 3,144 |
| 8 | Search does not return useful results | 23.3% | 2,881 |
| 9 | AI tools do not have enough context | 20.0% | 2,471 |
| 10 | I do not know which source is authoritative | 18.4% | 2,272 |
| 11 | AI tools use the wrong context | 16.8% | 2,075 |
| 12 | Access or permissions prevent me seeing what I need | 15.8% | 1,961 |
| — | **I usually have the context I need** | **9.6%** | **1,193** |
| — | I intentionally limit context (privacy/security) | 6.1% | 753 |
| — | Not applicable | 2.4% | 291 |

### The better hook number: **9.6%**

Only **1,193 of 12,374 developers — fewer than one in ten — say they usually have the context they need.**

Why it beats 56.5% for this slide:
- It is a **single, whole claim** instead of one item from a list, so it cannot be asked "what were the other options?"
- It is **stated by developers about themselves**, which is the room's own voice, not a statistic about documents.
- It sets up slide 3 exactly: if 9 in 10 lack context, no individual is failing — the system has no owner.
- The on-slide `.stat` style already exists for one big number, and "9.6%" reads at projector distance better than "56.5%".

Suggested slide text: **9.6%** / "of 12,374 developers say they usually have **the context they need** at work." Muted line: *Measured: Stack Overflow Developer Survey 2026, "What gets in the way of getting the context you need for work?" The page-is-wrong framing is this deck's.*

**Honesty gain:** the deck currently implies outdated information is *the* problem. It is third. Keeping 56.5% as a second line *with* its rank ("third of sixteen barriers, behind incomplete information and knowledge that lives in people's heads") is more defensible, and the three together are the same disease — which is the argument of the next slide.

Source: <https://survey.stackoverflow.co/2026/knowledge/data/context-problems>

---

## 2. Slide 3 ("keeping it current is nobody's job"): the deck's best argument is currently its only uncited one

The slide says in its own caption: *"This slide is the deck's own argument, not a cited finding."* It does not have to be. Two charts in the same survey are close to a direct measurement of it.

**Measured**, n = 12,374 (same question as above):
- **60.9% — "Important context lives in people's heads."** This *is* the slide's claim, measured. The knowledge exists; it was never written down. 7,541 developers.
- **25.4% — "Different teams have different versions of the truth."** The absence of an owner, stated as a symptom.
- **18.4% — "I do not know which source is authoritative."** Same, from the reader's side — which is precisely the slide's "next reader" character.

**Measured**, a second question, n = 12,678 — "what context do you need?":

| Context needed | % |
|---|---|
| Project goals or requirements | 85.2% |
| **Code, repositories, or technical documentation** | **73.3%** |
| Prior decisions and rationale | 44.0% |
| Related tickets, tasks, or issues | 36.9% |
| Business goals or product strategy | 33.0% |
| Pull requests, commit history, or release notes | 26.3% |

The survey's own framing of that chart: *"the work itself is the most important context."*

### Why this is the upgrade for slide 3

The slide has three characters — the author, the reviewer, the next reader — and asks the room to accept a logical argument. These numbers let each character carry a measured line instead:

| Character | Measured backing |
|---|---|
| The author (moved to the next ticket) | 60.9% say important context lives in people's heads |
| The reviewer (diff is in another file) | 25.4% say teams hold different versions of the truth |
| The next reader (works around it) | 18.4% do not know which source is authoritative |

And the frame for the whole slide: **documentation is the second-most-needed context (73.3%) and the third-biggest barrier (56.5%) — most needed, least owned.** That sentence is the slide's thesis with a denominator under it.

Keep the final line ("more discipline will not fix this") as the deck's own argument. The characters are now evidence; the conclusion stays interpretation.

Source: <https://survey.stackoverflow.co/2026/knowledge>

---

## 3. Slide 8 (57 of 59): the slide already has the better story in its own screenshot

The slide shows `img/real-pr-394.png` and apologises for it: *"A different workflow in the same repo — the link checker, not the docs updater."* That apology can become the strongest honesty beat in the deck.

**Measured**, GitHub search API, `githubnext/agentics`, link-checker pull requests on **10 Oct 2026**:

| PR | Outcome |
|---|---|
| **#394** `[link-checker] Fix broken documentation links` | **merged** (+3 / −3, 2 files) |
| #393 | closed, not merged |
| #392 | closed, not merged |
| #390 | closed, not merged |
| #387 | closed, not merged |
| #385 `[link-checker] Fix broken gh-aw reference links in cost-tracker docs` | closed, not merged |

**One agent, one day, six proposals, one merge.**

Why this is better than the current caption:
- The slide's own caveat is "merged is not the same as correct". This is that caveat **as an artifact**, in the same repo, about the same workflow as the screenshot already on the slide.
- It demonstrates the deck's central safety claim — a human decides — more convincingly than any diagram. Five of six were refused, by people, with no harm done.
- It pre-empts the sharpest audience question ("so it just floods you with PRs?") by answering it before it is asked, with the real number.
- It reframes the screenshot: #394 is not a weak substitute, it is *the one that survived*.

Suggested companion to the 57/59 panel: a small row of six marks, one filled. Muted line: *Measured: six link-checker pull requests in githubnext/agentics on 10 Oct 2026; one merged, five closed unmerged. Counted via the GitHub API, 18 Oct 2026.*

### And the repo-wide denominator, if the room wants scale

**Measured**, bot-authored PRs in public repos, 18 Oct 2026 (window: 2025-08-20 to 2026-10-18):

| Repository | Agent PRs | Merged | Closed unmerged | Merge rate |
|---|---|---|---|---|
| github/gh-aw | 4,034 | 2,688 | 1,346 | **66.6%** |
| githubnext/agentics | 52 | 31 | 20 (+1 open) | **59.6%** |

Read it as the planning assumption: **expect to reject about a third.** That is what "built to be checked" looks like at scale, and it is countable by anyone in the room — unlike 57/59.

**Caveat:** the filter is `author:app/github-actions`, i.e. every Actions-authored PR, not provably only agentic ones. In gh-aw the titles carry workflow-name prefixes (`[docs]`, `[dead-code]`, `[blog]`), strong evidence they are agentic — but say "bot-authored", not "agentic", to stay exact.

---

## 4. Slide 9 ("built to be checked, not trusted"): the room already agrees — show them

The slide asserts the design principle. The 2026 survey measured the audience's own position, and it matches the slide exactly.

**Measured.** Stack Overflow Developer Survey 2026, on when it is acceptable to trust AI:
- **48%** trust AI **when they can easily validate the answers**
- **16%** extend trust to most tasks that are not important work decisions
- **~7%** (press release: 6.6%) trust AI output for important work decisions

The survey's own conclusion, verbatim and quotable: **"That's why human-in-the-loop is the dominant mode of working with these tools."**

Why this belongs on slide 9:
- It converts the slide from *Donal asserting a safety posture* into *the room's own stated preference being satisfied by the design*. A draft pull request **is** the "easily validate the answer" affordance that 48% say is their condition for trust.
- The 48%-vs-7% gap is the whole argument for `draft: true` in one comparison, and it is someone else's number.
- It answers the sceptic without arguing: nobody is being asked to trust the agent. They are being asked to review a diff.

Suggested framing: *"48% of developers say they trust AI when they can easily check the answer. 7% trust it for important decisions. This is built for the 48%."*

Also usable (same page, n = 10,926): **31% of developers use AI tools 4+ hours a day.** Useful if the room needs reminding that this is not a hypothetical shift.

Source: <https://survey.stackoverflow.co/2026/ai>

---

## 5. Resolving the claim `todo.md` says to cut

`todo.md` marks this for removal: *"72.6% (n=12,996) say 'recent or clearly up to date' makes information trustworthy — not found in the 2026 survey. Keep it off the deck until a URL exists."* I could not find it either, on the knowledge page or its data pages. **It should stay cut.**

A verified replacement from the same page, which happens to justify the deck's own conventions:

**Measured**, n = 13,945 — importance of source attribution when judging an AI-generated technical answer:

| Rating | % |
|---|---|
| Very important | 52.1% (7,269) |
| Important | 26.5% (3,701) |
| Somewhat important | 14.0% (1,956) |
| Not very important | 5.4% (753) |
| Least important | 1.9% (266) |

**≈ 78.6% rate source attribution important or very important.** Stack Overflow's own press release gives 78.7% for the combined figure; the 0.1 point is rounding. If you want one unarguable number, use **"52.1% say source attribution is *very* important"**, which is read directly off the chart.

Where to use it: the status-and-sources slide (22), as the reason every slide carries a muted source line — *"78.6% of developers say source attribution matters when judging an AI answer, so every number here names where it came from."* It makes the deck's most pedantic convention into an audience-serving choice.

---

## 6. Slide 14 (cost): one correction, and one restriction that can be lifted

### Correction: the per-run ceiling is ~$14, not ~$10
**Documented, and currently wrong on the slide.** Threat detection has its own AI-credit budget that does **not** inherit the agent's:

> "Threat-detection runs have their own AI Credits budget, separate from the main agent's `max-ai-credits`. Detection does not inherit the main agent's budget — both caps apply independently."

Default detection budget **400 AIC**. So: 1,000 (agent) + 400 (detection) = **1,400 AIC ≈ $14** per run at 1 AIC = $0.01.

This *helps* the slide. Its argument is "both numbers are settings in a file we review" — there are three settings, and naming the one the audience would not have guessed makes the point better.

### The daily cap can go back on the slide
The slide and slide 22 both say the daily cap is left off because two docs pages disagree. **As of 18 Oct 2026 they agree:**
- Cost management: default guardrails include "5000 AI Credits per workflow per day (24-hour window)".
- Frontmatter, `max-daily-ai-credits`: "When omitted, the guardrail inherits the default daily limit (5000 AI Credits unless overridden)." `-1` disables it.

So the "We choose runs/month × capped cost per run = monthly ceiling" equation now has a **documented third term**: a per-workflow daily ceiling of 5,000 AIC (~$50) that applies whether or not anyone sets it. Remove the daily cap from the "left off on purpose" list on slide 22.

### The slide's own thesis is in the docs, verbatim
The cost-management page has a section titled **"Use Schedules for Predictable Budgets"** — which is exactly the slide's "a schedule is a known number; every push to main is not". Worth a muted citation, since it means this is GitHub's guidance and not only the deck's reasoning.

Sources: <https://github.github.com/gh-aw/reference/threat-detection/> · <https://github.github.com/gh-aw/reference/cost-management/> · <https://github.github.com/gh-aw/reference/frontmatter/>

---

## 7. Slide 21 (try it yourself): what the links actually are

**Measured** via the GitHub API, 18 Oct 2026 — worth knowing before inviting people to click:

| Repo | Visibility | Licence | Stars | Last push |
|---|---|---|---|---|
| `github/gh-aw` | public | MIT | 5,418 | 2026-10-18 |
| `githubnext/agentics` | public | MIT | 989 | 2026-10-13 |

Both public and MIT, so both are safe to put on a slide and safe for the audience to copy from. `githubnext/agentics` holds **58 workflow files**, including the `update-docs.md` this deck quotes, plus `daily-doc-updater.md`, `doc-updater.md`, `unbloat-docs.md`, `glossary-maintainer.md` and `link-checker.md` — the last four are the workflows behind the numbers on slide 8, so the slide's evidence and the slide's links finally point at the same place.

Still open (`todo.md`): Donal's own `DonalMoloney/Agentic-Workflows-Lib` is **private**, so it cannot be linked until he chooses to publish it. Ask before putting that URL on a slide.

---

## 8. Do not use

- **"~$10 per run" as the ceiling** — omits detection's 400 AIC (§6).
- **The daily-cap conflict** as an open issue — resolved (§6).
- **The 72.6% trustworthiness figure** — still unverifiable; use §5's replacement.
- **56.5% presented as the top barrier.** It is third of sixteen (§1).
- **"Agentic" for the 4,034 PR count.** Say "bot-authored" (§3).
- **DORA 2025 percentages.** Secondary coverage only; see `../deck-v1/RESOURCES.md` §8 for the one qualitative point worth keeping, in notes.
- **2025-survey AI numbers** (e.g. "66% say AI solutions are almost right but not quite", "29% trust accuracy"). Those are the **2025** survey, n≈49,000. The 2026 survey is a different sample (30,000+, 169 countries, published 6 Oct 2026). Do not mix years on one slide.

---

## Source list, all fetched or counted 18 Oct 2026

| Source | Used for |
|---|---|
| <https://survey.stackoverflow.co/2026/knowledge/data/context-problems> | Full 16-item barrier ranking, 9.6% "usually have the context I need", 56.5%/60.9%/25.4%/18.4% |
| <https://survey.stackoverflow.co/2026/knowledge> | 73.3% code/docs as needed context (n=12,678); source-attribution chart (n=13,945) |
| <https://survey.stackoverflow.co/2026/ai> | 48%/16%/~7% trust split; "human-in-the-loop is the dominant mode"; 31% use AI 4+ h/day |
| GitHub search + pulls API (`gh api`) | Link-checker 6 PRs on 2026-10-10; 4,034/2,688/1,346 gh-aw; 52/31/20 agentics; repo metadata |
| <https://github.github.com/gh-aw/reference/threat-detection/> | 400 AIC detection budget |
| <https://github.github.com/gh-aw/reference/cost-management/> | 5,000 AIC/day default, "Use Schedules for Predictable Budgets" |
| <https://github.github.com/gh-aw/reference/frontmatter/> | `max-daily-ai-credits` default now stated, `-1` disables |
