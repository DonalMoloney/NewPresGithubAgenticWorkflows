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
