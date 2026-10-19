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

## 5. State after the final review pass (stopped 19 Oct 2026 for time)
The in-depth review (story, accuracy, visual) was followed by a content pass that was **stopped for time**. Full reports are in `review-findings.md` in this folder. "Applied" below was confirmed by searching the current `deck.md`, not from the editors' reports (which had not arrived); everything under "Not confirmed" needs a check against the deck before anyone relies on it.

### Applied (found in the current deck.md)
- 57/59 evidence caveat (GitHub measured "merged", not "accurate"; workflow ran `draft: false`, auto-merge since 20 Jan 2026). Verified 19 Oct 2026.
- Real `link-checker.lock.yml` (`copilot-requests: write`) is now reflected in the lock-file wording; the cost slide is retitled around "run count and per-run cap"; the close now says a page is "probably" wrong.
- Ask and method split into "three yeses today" and "decide keep or stop by a rule we set". Deck is 22 slides; `check_deck.py` shows 0 errors.

### Still needs you
- Earlier-attempt story, ask values (repository, owner, budget, baseline, keep/stop rule, duration), a real run (PR, `gh aw logs`/`audit` output, committed `.lock.yml`), talk date and audience, library lesson and public/private decision (see sections 1-2).
- Daily AI Credit cap: re-read both the cost-management and frontmatter pages; state it only if they now agree, else leave it off slides.

### Not confirmed (check against `review-findings.md`)
- `bash: [...]` allowlist syntax and exfiltration wording on the code slide; "$300 ceiling" vs the separate detection budget; "4 compiled" labelled self-reported.
- Story: gh-aw named before it is defined (slide 5), "next two slides" count on slide 9, missing Plain-line openers / double Transitions, slides over ~90 s.
- Visual: teammate map and ladder narrower than the text column, diagram text under 18px, mostly blank slides, card-grid sameness.

### Housekeeping
- **`deck.html` and `deck.pdf` are older than `deck.md`: regenerate** (`marp deck-v2/deck.md --allow-local-files -o deck-v2/deck.html </dev/null`). `speaker-notes.txt` is stale too. Delete or commit `deck-preview.html`.
- `sources.md`: rekey by claim text; add ledger rows for 98 / 98 / 6 / 4 / 0.

## 6. Style audit by peer session deck-v3-cc (19 Oct 2026)
- Applied (front-matter `style:` only): `.todo` is now `var(--dim)` text and dashed border on a `var(--surface)` background; the dashed chip and the TODO word stay, so gaps remain visible without colour.
- `deck.html` was regenerated by that session, but `deck.md` changed afterwards: **regenerate again** once all edits are final.
