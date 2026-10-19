# Deck v3: outstanding work

**Version:** deck-v3, warm paper with indigo serif. Copy of deck-v2 taken 17 Oct 2026; same arc, worked on separately.
Last updated: 18 Oct 2026

## 1. Needs your content
- Earlier-attempt story (slide 4): three beats plus screenshot; confirm the landing line "it only ran when a person remembered to run it", or cut.
- The ask (slide 18): repo, owner, credit budget, baseline, keep/stop rule.
- Pilot-workflow decision: `update-docs` or `readme-auto-updater`; use one name on the file, trigger and ask slides, or label the ask "library format, not the pilot workflow".
- Autonomy level today (ladder slide).
- Talk date and audience.
- Library lesson (what building the 98 taught you), time taken, public or private for the example-workflow repo.
- One real linked PR plus a recording (slide 16 amber slot); commit the `.lock.yml` for the 4 compiled workflows so "compiled" becomes an artifact.
- Your own example and repo URLs.

## 2. Verify before the talk
- Daily AI Credit cap default: RESOURCES.md says both pages agree (5,000 AIC/day, `-1` disables). Re-check, then move it from "left off" (status slide, line ~849) into the guardrail table.
- Does CI run on the agent's own PRs? Not addressed in the deck.
- Write-access check on the trigger slide: documented only for comment and dispatch triggers; push and fork-PR behaviour is an amber TODO.
- `protected-files` and `environment:` semantics before either is claimed.
- Allowlisted-domain data question (amber TODO on the layers slide; the notes carry the sharp version).
- RESOURCES.md figures before use: 344 agentic workflows with 344 committed lock files in `github/gh-aw`; 2,688 of 4,034 bot PRs merged; PRs #69936, #69394, #68929; detection's separate 400 AIC (ceiling 1,400 AIC ~ $14, slide says 1,000 / ~$10); 50 documented frontmatter settings; `gh aw logs ... --json | jq` recipe.
- 72.6% trustworthiness line: unsourced, keep it in notes only (line 142).
- Ladder L1-L5 labels: verify the full paper or show names only.
- `gh aw audit` P14 wording appears in both body and note; confirm uniqueness before any edit.

## 3. Optional improvements still open
- "98 and 0" slide: a comparison column (344 workflows run by GitHub on itself) only after re-verifying it from RESOURCES.md; keep it as big stats, not a table.
- Mock `gh aw logs` terminal card, using documented output shape only.
- Staging wording: "rehearsal, not performance" instead of "writes nothing".
- Detection: name the one documented hard block (failed redaction) once re-verified.

## 4. Housekeeping
- `sources.md`: slide numbers are stale (rekey by claim text); add ledger rows for 98 / 98 / 6 / 4 / 0.
- Regenerate `deck.html`, `deck.pdf`, `speaker-notes.txt` after the last edit.
- Run `python3 deck-v3/check_deck.py`.

## 5. State after the final review pass (stopped 19 Oct 2026 for time)
The in-depth review (story, accuracy, visual) was followed by a content pass that was **stopped for time**. Full reports are in `review-findings.md` in this folder. "Applied" below was confirmed by searching the current `deck.md`, not from the editors' reports (which had not arrived); everything under "Not confirmed" needs a check against the deck before anyone relies on it.

### Applied (found in the current deck.md)
- 57/59 draft caveat on the evidence slide and in the notes (`draft: false` on 27 Dec 2025; auto-merge added 20 Jan 2026). Verified 19 Oct 2026.
- The "three limits" vs four title mismatch is gone. Deck is 22 slides; `check_deck.py` shows 0 errors; `deck.html` was current at last check.

### Still needs you
- Earlier-attempt story, ask values (repository, owner, budget, baseline, keep/stop rule, duration), a real run (PR, `gh aw logs`/`audit` output, committed `.lock.yml`), talk date and audience, library lesson and public/private decision (see sections 1-2).
- Daily AI Credit cap: re-read both the cost-management and frontmatter pages; state it only if they now agree, else leave it off slides.

- Pilot workflow stays an open decision: `update-docs` vs `readme-auto-updater`.

### Not confirmed (check against `review-findings.md`)
- Run-jobs plain labels ("Drafts the letter" etc.) vs the real jobs (some hold `copilot-requests: write`); each injection-path "what limits the damage" claim must be documented.
- Story: slides 14 and 15 repeat each other (four safety slides in a row); ladder (slide 4) duplicates the turn (slide 6) and slide 6's note contradicts itself; the close does not echo the opening on the slide; slide 19 overloaded; slide 5 empty hinge; missing Plain-line openers; slides over ~90 s.
- Visual: footer collisions on slides 6, 7, 9, 11; no hierarchy among the ask's TODO pills; competing big stats on 2, 3, 16; amber overuse; inconsistent card styles; diagram labels under 18px on 4 and 15.
- Style pass by the peer session `deck-v3-cc` (front-matter `style:`, the ask slide's scoped block, `img/title-loop.svg`) may be unfinished: check the Octocat colours on the title slide.

### Housekeeping
- `deck.pdf` and `speaker-notes.txt` are older than `deck.md`: regenerate.
- `sources.md`: rekey by claim text; add ledger rows for 98 / 98 / 6 / 4 / 0.

## 6. Style audit by peer session deck-v3-cc (19 Oct 2026)
- Applied (front-matter `style:`): `strong` now `var(--ink)` (was the tinted `--hi`, on 41 bold runs); `.todo` now `var(--muted)` instead of `var(--warn)`, with the ▲ glyph kept.
- Applied (scoped blocks): ask slide `.need div` border and text to `var(--line)` / `var(--muted)`, dashed outline kept; evidence slide `.slot` border to `var(--line)`.
- Assets: `img/title-loop.svg` fully retinted to the v3 tokens (arrowhead moved from a hardcoded fill to a `.arrowhead` class); `img/github-mark.svg` `#1f2328` to `#26211b`. All nine v3 assets are now on the warm palette.
- **Still open:** in `img/pilot-timeline.svg` the step-4 "DECIDE" badge and its TODO box are amber while steps 1-3 are indigo, which disagrees with the neutral gap styling elsewhere. Retint it.
- **Still open:** `--line` / `--line-soft` contrast on the cream canvas is 2.05:1 and 1.43:1 (panel fill 1.09:1), so card borders are thin on a projector. Darkening them restyles every card, table and code block, so it needs a human eye on a real render.
- `deck.html` was regenerated by that session, but `deck.md` changed afterwards (the ask-slide rewrite with `pilot-timeline.svg`): **regenerate again** once all edits are final. No `.pdf` was touched.
