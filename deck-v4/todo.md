# Deck v4: what is still left

**Version:** deck-v4, dark stage, one red accent, bigger and bolder type, TED-style spine. Copy of deck-v3 taken 18 Oct 2026.
**State:** design, order, wording and notes are finished. Visible TODO markers were removed from the slides on request, so the gaps below are only recorded here and in the speaker notes. Slide numbers are current as of the last build (23 slides: 16 main, 7 appendix).

## 1. Content only you can supply
- **Slide 5, earlier attempt:** the three cards (what I built, what worked, what was missing) are empty. The third beat must land on "it only ran when a person remembered to run it", or change the transition into the turn. If the story will not be ready, cut the slide; nothing else depends on it.
- **Slide 15, the ask:** the five answers (repository, page owner, credit budget, how stale it is now, keep or stop rule).
- **Slide 16, the month:** the actual keep/stop rule. Also confirm the split (one staged week, three review weeks) is what you want; it is this deck's proposal, not GitHub's guidance.
- **Pilot workflow:** choose `update-docs` or `readme-auto-updater`, then make the file slide (9), the one-page spec (appendix, 20) and the ask match.
- **Title slide:** talk date and audience.
- **Slide 14, what I've built:** the one thing building the 98 taught you, how long it took, and whether the library repo goes public. Do not put its URL on a slide until it does.
- **Slide 7, the result:** one real linked pull request and a recording of the run behind it (candidates in `RESOURCES.md`: `github/gh-aw` #69936, #69394, #68929 as of 18 Oct 2026). Never show a screenshot that is not a real PR.
- **Links slide (22):** your own sites and example repository URLs.

## 2. Verify before the talk
- Can an injected agent send data to a domain that is on the allowlist? It is the open question inside the layers diagram (slide 13); say "I don't have a documented answer" until confirmed.
- Push and fork-PR behaviour for the role check (triggers, appendix 18). Currently only documented for comment and dispatch triggers.
- The daily AI Credit cap default: the two docs pages disagree, so it is left off the slides and recorded on the status slide.
- `environment:` as an approval gate and `protected-files:` as path enforcement: unverified on purpose, do not claim either.
- The one documented hard block (a failed or skipped redaction stops publication): re-verify in the docs before saying it.
- Autonomy ladder L1 to L5 labels against the full paper (appendix 19), or show names only.
- The "72.6% say recent information is trustworthy" line stays in notes only until a source URL is found.
- Cost: runs per month times the per-run cap (default 1,000 AI Credits, about $10, best-effort) before stating any total or calling it small.

## 3. Housekeeping not done
- `sources.md` is carried over from v3 and keyed to v3 slide numbers. Rekey it by claim text.
- No PDF or speaker-notes export has been made for v4. Run `marp deck-v4/deck.md --allow-local-files --pdf </dev/null` and `marp deck-v4/deck.md --notes -o <path>` when the content is final.
- `RESOURCES.md` sections below the v4 block still use v3 slide numbers; match by title.
- Re-run `python3 deck-v4/check_deck.py` and regenerate `deck.html` after any edit (`marp deck-v4/deck.md --allow-local-files -o deck-v4/deck.html </dev/null`).
- Rehearse with the notes as spoken lines; the first line of each note is what you say out loud.

## 4. Ideas not built
- A "what we will see" slide pulling the `gh aw logs` and `gh aw audit` commands out of the appendix.
- A "what we won't do" slide listing the limits.
- A real, rights-cleared image for the hook slide (never an invented screenshot).
