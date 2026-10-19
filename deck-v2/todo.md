# Deck v2: outstanding work

**Version:** deck-v2, white with one blue accent (commit 7bd8137). Arc: Why now, What it is, Does it work, Is it safe, What I've built, The ask, Appendix. Worked on separately from v1 and v3.
Last updated: 18 Oct 2026

## 1. Needs your content
- Earlier-attempt story (slide 6): built / worked / missing, plus screenshot and transition line. If empty on the day, cut it (fallback is in the notes).
- The ask: pilot repo, owner, budget, baseline (how wrong the page is today), keep/stop rule; name the page.
- Autonomy level: where the team sits today on the ladder.
- Talk date and audience (title slide).
- Library lesson: the one thing building the 98 taught you; how long it took; public or private for the example-workflow repo.
- Real run artifacts: your own PR/`gh aw logs`/lock file (slide with "no real lock file seen yet"). Blocked on the `workflow` token scope.
- Your own example and repo URLs (Try it yourself slide).

## 2. Verify before the talk
- Daily AI Credit cap default: RESOURCES.md says both pages now agree (5,000 AIC/workflow/day, `-1` disables). Re-check, then remove it from the "left off" captions (cost slide source, status slide, notes ~lines 410, 625-632, 825-829).
- Does CI run on the agent's own PRs? Not stated anywhere in the deck.
- `protected-files` and `environment:` semantics before either is claimed as a docs-only or approval gate.
- Allowlisted-domain question: amber TODO on the layers slide.
- RESOURCES.md figures before use: detection's separate 400 AIC (ceiling 1,400 AIC ~ $14; slide still says 1,000 / about $10); 9.6% "usually have the context they need" (n=12,374); 78.6% rate source attribution important (n=13,945); 48% trust when they can validate; 2,688 of 4,034 bot PRs merged; six link-checker PRs on 10 Oct 2026 (#394 merged, five closed).
- 72.6% trustworthiness line (n=12,996): still unsourced; keep it off the slide (note TODO at line 189).
- Ladder L1-L5 numbering: only the names are verified from the abstract; verify the full paper or show names only.

## 3. Optional improvements still open
- Hook: swap 56.5% for the stronger 9.6% line (RESOURCES.md section 1, verify first); cite the three characters on the nobody's-job slide.
- Evidence slide: six marks, one filled (the six link-checker PRs), or add the 66.6% bot-authored denominator. Re-check with `gh pr list` before using.
- Staging wording: "previews every safe output" or "rehearsal, not performance" instead of "writes nothing" on the `staged: true` slides (notes already carry the "not a sandbox" caveat).
- Network diagram: confirm the allowlist arrow and the crossed arrow for unlisted domains are drawn, not only the snippet.
- Teammate-model slide: plain term first, code term small beneath (not applied last pass).
- API-proxy `aria-label` for `agent-blast-radius.svg` in `deck.md`: replace "holding the engine token" with "keeps the engine's auth token out of the agent's container" if it still says the old wording.

## 4. Housekeeping
- `sources.md`: slide numbers are stale (rekey by claim text); add ledger rows for 98 briefs, 98 docs pages, 6 shared modules, 4 compiled, 0 runs.
- Replace "slide 9's `update-docs.md`" on the pilot slide with "the `update-docs.md` shown earlier" if it is still there.
- Regenerate `deck.html`, `deck.pdf`, `speaker-notes.txt` after the last edit; delete or commit `deck-preview.html`.
- Run `python3 deck-v2/check_deck.py`; it lists the visible TODOs.
