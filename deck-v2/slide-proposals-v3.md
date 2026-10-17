# Slide proposals v3 — the Agentic Workflows library as credibility

Proposals only. Nothing here has been added to `deck.md`.

Everything factual below was verified directly against `DonalMoloney/Agentic-Workflows-Lib`
with `gh api` on **17 Oct 2026**. The verified-facts list and the caveats are at the
bottom of this file. Only the fenced **SLIDE** blocks are meant to be pasted into
`deck.md`.

---

## Placement

Current order (15 slides): 1 title · 2 docs-are-wrong · 3 autonomy ladder ·
4 earlier attempt · 5 what it is · 6 it will get things wrong · 7 no write token ·
8 the settings · 9 GitHub's 57/59 · 10 the ask · 11 debugging · 12 compile ·
13 four ways to run · 14 try it yourself · 15 status and sources.

**Slide A goes in as the new slide 10**, directly after GitHub's 57/59 proof slide and
directly before the ask, which becomes slide 11. It displaces nothing.

**Slide B goes in as the new slide 11**, after Slide A, with the ask becoming slide 12.
It displaces nothing.

Both sit inside the existing `<!-- header: Proof -->` section, so no header directive
changes are needed. The deck ends up at 17 slides.

Why here: slide 9 proves the idea works *for GitHub*. The ask (slide 10) then asks the
room to start from zero. These two slides fill that gap — the preparation is already
done — so the ask stops being "let's begin a project" and becomes "let's run what
exists". Put them before the ask or they are just trivia.

**One required edit to an existing slide if these are adopted:** slide 9's last speaker-note
line is `Transition: that's GitHub's number. Here's how we'd find ours.` That now needs to
hand over to Slide A instead, e.g. `Transition: that's GitHub's number. Here's what I've
already built against it.` Flagging only; I have not edited `deck.md`.

### The objection each slide retires

- **Slide A** retires *"this is a from-scratch project — who is going to do the work, and
  have you actually used this?"* It answers both: the work is done and committed, and the
  only missing step is the one the pilot is for.
- **Slide B** retires *"once an agent is loose in our repo, who owns it and what exactly
  can it write?"* The deck never answers ownership anywhere else. Slide 7 covers the
  mechanism; this covers the governance.

---

## SLIDE A — new slide 10

```markdown
---

## The library is already written and documented; running it is the one step left

<style scoped>h2 { margin-bottom: 18px; } table { font-size: 22px; } .muted { font-size: 20px; } .todo { font-size: 21px; }</style>

| What is written | What has not happened yet |
| --- | --- |
| **98** workflow briefs in `workflows/`, one file each | **0** have run inside GitHub Actions |
| **98** docs pages in `docs/workflows/` — one per workflow, filenames matched one to one | **4 of 98** compiled so far: `gh aw compile`, gh-aw v0.83.4, 0 errors, 0 warnings |
| **6** shared policy and prompt modules that workflows import instead of copying | No release tagged, and the sandbox repo does not exist yet |

<span class="muted">`DonalMoloney/Agentic-Workflows-Lib`, private. File counts verified via the GitHub API, 17 Oct 2026. The compile result and the "not yet run" column are the repository's own `agents.md` — my record of a local compile, not a CI result.</span>

<span class="todo">TODO: the one thing building this taught me, and whether this repo goes public before the talk.</span>

<!--
Plain line to say: I did not come here with a slide deck. I came with 98 of these already written and documented — and not one of them has ever run. That last part is the ask.
Say the right-hand column out loud. Do not let the room hear "98" and assume it is in production. The honest sentence is "written and documented, not yet executed".
Technical detail: 98 markdown briefs in workflows/, each with its own docs page in docs/workflows/ carrying a fixed required-fields table. Six shared modules under workflows/shared/ (policy, prompts, mcp, tools) are imported rather than copy-pasted, so a safety change lands in one place. aw.yml pins min-version v0.83.4.
Numbers and sources: the two 98s and the 6 are counts I verified through the GitHub API on 17 Oct 2026 — the workflows/ and docs/workflows/ filename sets are identical. The "4 compiled, 0 errors, 0 warnings" and "0 runs" come from the repo's own agents.md, which says plainly: the CI workflows have not executed inside actual GitHub Actions, the sandbox repo does not exist, no release is tagged.
Careful wording, say none of these: not "98 workflows running", not "98 compiled", not "in production", not "the org is using it". Only 4 of 98 have been compiled, and no .lock.yml files are committed to the repo at all.
Q: "So none of this actually works?" Four of them compile cleanly against the pinned gh-aw version, which means the frontmatter and safe-outputs are valid. What is unproven is runtime behaviour, and that is exactly what a month of real runs would prove.
Q: "Why 98 and not 4?" The briefs are the cheap part — they are plain English. Compiling, running and reviewing is the expensive part, and I deliberately stopped before spending that without agreement.
Q: "Can we see it?" It is private. TODO: decide before the talk whether it goes public — see the note on the appendix slide.
Q: "How long did this take you?" TODO: answer honestly; it is the question that makes the 98 land or sound like padding.
Transition: here is one of the 98, and it is aimed at exactly the problem I opened with.
-->
```

---

## SLIDE B — new slide 11

This one clears the bar: `readme-auto-updater` is the deck's own thesis as a real file, and
its docs page is a verifiable artifact rather than a description. Crucially it shows
something **no other slide shows** — an owner and a maturity label — so it is not a second
helping of slide 8's frontmatter.

```markdown
---

## Every workflow ships with a one-page spec, so you always know what it writes and who owns it

<style scoped>h2 { margin-bottom: 18px; } table { font-size: 23px; } .muted { font-size: 20px; } .todo { font-size: 20px; }</style>

| Field | `readme-auto-updater` |
| --- | --- |
| Purpose | Detects drift between the README and the current codebase after a push to `main`, and proposes a fix |
| Triggers | `push` (branches: `main`) |
| Writes | **1 pull request** — `create-pull-request`, `max: 1` |
| Access | `permissions: contents: read`; GitHub toolsets `context`, `repos` |
| Owner | <span class="todo">TODO: real owning team</span> |
| Maturity | **Experimental** — the label the library gives all 98 |

<span class="muted">Trimmed from `docs/workflows/readme-auto-updater.md` and its workflow frontmatter, verified 17 Oct 2026. Owner and install lines in the repo use a placeholder `acme-org` namespace, so they do not resolve as written.</span>

<!--
Plain line to say: this is the job description for one teammate out of 98 — and the page tells you, before you hire it, what it can touch, what it can send, and whose phone rings when it gets it wrong.
Callback to the teammate model from slide 5: purpose is the job description, triggers is the shift, access is the badge, writes is the outbox. Same four chips, now on a real page.
Technical detail: every one of the 98 docs pages uses this same required-fields table — purpose, triggers, writes, required secrets, shared imports, customization points, owner, maturity. The frontmatter backs it: permissions is contents: read only, and the single safe-output is capped at max: 1, so one run cannot open a pile of pull requests.
Numbers and sources: the table is trimmed from the repo's own docs page and workflow file, verified 17 Oct 2026. All 98 docs pages carry "Maturity: Experimental" — that is the library's own label on itself, not modesty for this room.
On draft: this file does not set draft: true, but it does not need to. sources.md line 60 records the safe-outputs-pull-requests page as saying draft is "a policy, not a default" with default true (verified 17 Oct 2026), so an omitted draft still yields a draft PR. Safe to say "it opens a draft" about this workflow.
Careful wording: the owner on the page is @acme-org/platform-devex, a placeholder, and the install command on that page points at a namespace that does not exist. Say "placeholder" if it is visible on screen. Never show that install line as if someone could run it.
Q: "Could this have written to our README already?" No. It has never run anywhere, and permissions are read-only — the pull request would be a proposal, reviewed like any other.
Q: "Why the README and not our real docs?" Same mechanism, different target path. The pilot picks the page.
Q: "Experimental means what, exactly?" Compiled and documented, never executed. Same honest line as the previous slide.
Transition: so the decision I need is small — pick one page, and let one of these run for a month.
-->
```

---

## Can this fill the appendix slide's TODO?

Slide 14's `TODO: My sites and example repository URLs` — **not as it stands.** Three
blockers, in order of how hard they are to clear:

1. **The repo is private.** A URL on that slide would 404 for the entire room. It is
   owner-visible only, confirmed by the API.
2. **The placeholder namespace.** Owners are `@acme-org/platform-devex`, and every docs
   page carries an install line like
   `gh aw add acme-org/agentic-workflows/<name>@v1 --pr`, which resolves to nothing.
   Publishing as-is invites someone to run a command that fails, on stage or after.
3. **`aw.yml` ships 2 of 98.** The manifest's `files:` list contains only
   `workflows/issue-triage.md` and `workflows/ci-doctor.md`, so a consumer installing
   from the manifest gets two workflows, not a library of 98.

Recommended handling: leave the TODO orange on slide 14 and keep Slides A and B as
*described* evidence rather than a link. If the speaker wants a public URL, the smallest
honest path is a stripped public sample — a handful of workflows plus their docs pages,
with the `acme-org` strings replaced and a README that states "compiled, never executed".
That is a decision only the speaker can make, which is why it is the TODO on Slide A.

---

## Facts verified via `gh api`, 17 Oct 2026

Independently checked; not taken from the briefing.

| Fact | Value |
| --- | --- |
| Repo | `DonalMoloney/Agentic-Workflows-Lib`, **private**, no description, 0 stars/forks |
| Created / last push | 2026-09-23 / 2026-09-23T13:17:35Z |
| Workflow briefs | **98** `.md` in `workflows/` (plus the `shared/` directory) |
| Docs pages | **98** `.md` in `docs/workflows/` |
| Filename parity | `diff` of both sorted name lists: **identical sets** |
| Shared modules | **6**: `policy/baseline-safety.md`, `policy/pr-writing.md`, `prompts/house-style.md`, `mcp/internal-docs.md`, `mcp/tavily.md`, `tools/jqschema.md` |
| Manifest | `aw.yml`: `manifest-version: "1"`, `min-version: v0.83.4`, name `Acme Agentic Workflows`, `files:` lists **only 2** workflows |
| CI files present | `.github/workflows/`: `validate.yml`, `release.yml`, `sandbox-smoke.yml`, `rollout.yml` |
| Compiled `.lock.yml` in repo | **0** — none committed anywhere in the tree (265 blobs scanned) |
| Seed workflows | 4: `issue-triage`, `ci-doctor`, `pr-review`, `weekly-repo-report` — the only ones listed individually in `CODEOWNERS` |
| Maturity labels | `Maturity: Experimental` matches **98/98** docs pages (code search) |
| `readme-auto-updater` frontmatter | `on: push: branches: [main]`, `permissions: contents: read`, `engine: copilot`, `tools.github.toolsets: [context, repos]`, `safe-outputs.create-pull-request.max: 1`, imports `baseline-safety` + `house-style` |

### Binding caveat, quoted from the repo's own `agents.md`

> All four seed workflows have been compiled for real with `gh aw compile` (`gh-aw`
> v0.83.4, the version now pinned in `aw.yml` and CI) — 0 errors, 0 warnings. What is
> still not real: the CI workflows haven't executed inside actual GitHub Actions, the
> sandbox repo doesn't exist yet (see `docs/sandbox-setup.md`), and no release has been
> tagged. **Do not describe those as operational until they demonstrably run.**

### Three corrections to the original brief

1. **"98 compiled" would be wrong.** Only the **4** seed workflows were compiled. The
   other 94 are briefs with docs pages. Both slides above say "4 of 98" on the slide
   itself, not only in the notes.
2. **No `.lock.yml` is committed.** The compile was local and left no artifact in the
   repo, so "compiled" rests entirely on the speaker's own `agents.md` note. That is
   fine to say, but it is a self-report, and the muted source line says so.
3. **`acme-org` is a placeholder throughout** — owners, CODEOWNERS teams and every
   install command. This is the single biggest trap: it makes the library look like an
   org-wide deployment at a company called Acme. Anyone reading a screenshot will assume
   a real org is running this.

### One real inconsistency with the current deck

**RESOLVED 17 Oct 2026 — not an inconsistency.** The concern was that slide 7 says a
workflow "can only open a **draft** pull request" while `workflows/readme-auto-updater.md`
sets only `create-pull-request: max: 1`, with no `draft: true`.

`deck-v2/sources.md` line 60 already settles it: the safe-outputs-pull-requests page says
"`draft` is a **policy**, not a default, so the agent cannot override it at runtime", and
records the **default as `true`**. So omitting `draft` still produces a draft pull request,
and slide 7's claim holds for the library workflow as well. No slide change needed, and the
TODO in Slide B's notes has been closed.
