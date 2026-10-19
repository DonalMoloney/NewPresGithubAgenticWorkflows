# Deck v1: outstanding work

**Version:** deck-v1, white with the approved purple accent on title and decision slides. 28 slides. Source of truth for titles: `../overview.md`.
Last updated: 18 Oct 2026

## 1. Needs your content
- Earlier-attempt story (slide "My earlier attempt..."): tool, what it solved, the gap. Notes lines 255-266 are TODO. Cut or hide the slide if still empty on the day; the hook in `hook-and-ending.md` must match it, not repeat it.
- Ask values: pilot repo, owner, spend limits, baseline (manual cost), keep/stop thresholds. `githubnext/agentics` is a candidate only (third-party); say so.
- Current autonomy level (slide "Use agents where interpretation adds value"): agree it, do not guess.
- Example collection: real repo URL, one verified workflow file, the chore it addresses.
- Real run artifacts: one completed run and PR URL, or a `gh aw logs` line, so cost terms read "measured" rather than "will be measured". Blocked on `gh auth refresh -h github.com -s workflow`.
- Public/private decision for the example-workflow repo before its URL goes on the appendix slide.
- Talk date and audience.

## 2. Verify before the talk
- Daily AI Credit cap default: `RESOURCES.md` says both docs pages now agree (5,000 AIC per workflow per day, `-1` disables). Re-check on the docs, then drop it from the "left off" caveat (notes around line 716 and the status slide).
- Does CI run on PRs opened by the safe-outputs job (`GITHUB_TOKEN` PRs normally do not trigger workflows)? Notes line 677 says unverified. State the answer or drop "CI still gates".
- `protected-files` semantics: amber TODO on the "same file also grants bash" slide. Do not call "docs only" a mechanism until confirmed.
- Detection rule: `RESOURCES.md` quotes one hard block (failed or skipped redaction blocks publication). Confirm wording against the threat-detection page before replacing the "disputed" caption.
- `RESOURCES.md` figures before use: per-run ceiling 1,400 AIC (1,000 agent + 400 detection) ~ $14; $0.006/min Linux runner; 2,688 of 4,034 bot PRs merged (66.6%); Aghajani et al. ICSE 2020 (59%, n=146); DORA 2025 secondary claims. Slide 12 still says ~$10 per run.
- Allowlisted-domain question: can an injected agent send data to a domain on the allowlist? Get the documented answer.

## 3. Optional improvements still open
- Cost slide: add a PR-volume estimate and a hard stop rule (plain-sentence-first cost slide and the Appendix 9 algebra are already done).
- Bounds slide: add `noop` pre-step skip, `max-turns` and "Use Schedules for Predictable Budgets" (RESOURCES.md section 9), once verified.
- Evidence slide: the 2,688 of 4,034 bot-authored PRs (66.6%) figure is re-verified with `gh` but lives only in the slide's notes; add it beside the three GitHub figures only if it fits.
- Detection wording: replace the "disputed" caption once the threat-detection page is re-read (see section 2).

## 4. Housekeeping
- `speaker-notes.md` is older than `deck.md`: stale, regenerate or retire.
- Kicker suffixes `01b` and `09b`: renumber everywhere (slides, notes, `overview.md`) if you want a clean sequence.
- `deck.html` and `deck.pdf` were regenerated after the final render check; re-run both after any further `deck.md` edit.

## 5. State after the final review pass (stopped 19 Oct 2026 for time)
The in-depth review (story, accuracy, visual) was followed by a content pass that was **stopped for time**. Full reports are in `review-findings.md` in this folder. "Applied" below was confirmed by searching the current `deck.md`, not from the editors' reports (which had not arrived); everything under "Not confirmed" needs a check against the deck before anyone relies on it.

### Applied (found in the current deck.md)
- 57/59 draft caveat: GitHub's workflow ran `draft: false`; auto-merge was added 20 Jan 2026 (#10890). Verified 19 Oct 2026.
- The lower-performing (about 43%) workflow from the same post is shown; `protected-files` is described as a sensitive-file guard, "docs only" as by instruction.
- Deck is 28 slides; `check_deck.py` shows 0 errors; `deck.html` and `deck.pdf` were current at last check.

### Still needs you
- Earlier-attempt story, ask values (repository, owner, budget, baseline, keep/stop rule, duration), a real run (PR, `gh aw logs`/`audit` output, committed `.lock.yml`), talk date and audience, library lesson and public/private decision (see sections 1-2).
- Daily AI Credit cap: re-read both the cost-management and frontmatter pages; state it only if they now agree, else leave it off slides.

### Not confirmed (check against `review-findings.md`)
- Overclaims: slide 8 "No write access" for prompt injection, run-pipeline "stages 1 to 3 hold no write permission", "closed in the same second it is read".
- CI-gate TODO (does CI run on the agent's PRs?): verify or keep the TODO.
- Story: blank slide 3; TODO inside slide 2's spoken transition; the ask repeated (keep two statements); slide 13 note opening; missing Transition lines on appendix slides; slides 6, 10, 11, 13, 14 over ~90 s.
- Visual: card-row-plus-callout sameness; diagram labels under 18px; right-margin drift; decision slide glow.

### Housekeeping
- `speaker-notes.md` is older than `deck.md`: regenerate or retire. Kicker suffixes `01b` / `09b`: renumber if wanted.

## 6. Style audit by peer session deck-v3-cc (19 Oct 2026)
- Nothing changed in deck-v1: its style block already follows the neutral-gap rule.
