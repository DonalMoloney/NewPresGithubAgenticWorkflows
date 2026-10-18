# GitHub Agentic Workflows: presentation project

Content project, not software. It holds the outline and draft visuals for a talk on GitHub Agentic Workflows (`gh-aw`). A separate repo of ready-to-use example workflows backs slide 8.

## Files
| File | Role |
|------|------|
| `overview.md` | High-level content overview and source of truth: the narrative arc plus 9 slides, each with a title and a one-line content note. Detail is added later. |
| `slide-styling/draft-overview.html` | Draft, high-level slide material: one rough inline-SVG diagram per slide, plus a dated fact-check banner. Raw input for building the real slides, not the final deck. |
| `slide-styling/` | Title slide and slide-style explorations. `title-slide.html` (blue neon) is the base the final deck is built from; `title-slide-v2.html` and the `slide-styling*.html` files are alternates. |
| `deck-v1/` | Deck v1: `deck.md` (slide content) and `deck.html` (all slides in one file), built from `slide-styling/title-slide.html`. |
| `deck-v2/` | Deck v2: same files and shell as v1, new arc (hook, times changing, earlier attempt, what it is: model, parts, ways to run, types, key points, then example videos, images and links). |
| `deck-v3/` | Deck v3: a copy of `deck-v2/` taken 17 Oct 2026, same files and arc, worked on separately from v2. |
| `reference/` | Background material (`agents-draft.md`, `img.png`). Not part of the deck. |
| `.venv/`, `.playwright-mcp/` | Tooling artifacts. Do not edit or commit. |

No build, test or lint commands exist. Preview by opening `draft-overview.html` in a browser.

## Rules
- Treat `overview.md` as the canonical high-level content. Keep it brief: do not expand its bullets into full prose or speaker notes unless asked. Change it first, then update the matching slide in `draft-overview.html`.
- Keep slide titles as full-sentence claims, as in `overview.md`. Do not turn them into topic labels.
- Never invent facts, numbers or repo/workflow names. Leave `TODO` placeholders until the user supplies real values. Open ones: slide 6 our current autonomy level, slide 2 the gap, slide 7 repo and workflow file names, slide 8 checklist steps, slide 9 the ask.
- Verify any claim about `gh-aw` against GitHub's official docs and record the check date in the HTML fact-check banner.
- Product status: public preview since 11 Jun 2026, confirmed 17 Oct 2026 in the official GitHub changelog (github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview). It was technical preview from 13 Feb 2026. Re-check before stating any later change.
- Mark diagram content changed during a fact check in orange with underline, matching the existing banner convention.

## Draft HTML conventions
- Treat the diagrams as reusable slide content. Keep them simple and high level so they can be lifted into the final slides.
- Keep it a single file with inline CSS and SVG. No external dependencies.
- Use the existing CSS tokens on `:root` (`--accent`, `--good`, `--warn`, ...) and the SVG classes (`.box`, `.box-a`, `.box-g`, `.box-w`, `.gap`, `.ln-a`, `.ln-w`, `.t`, `.tb`, `.tm`). Do not hardcode colors.
- Keep the dark-mode overrides in sync with the light tokens.
- Give every SVG a descriptive `aria-label`/`role="img"`.
- Keep the layout working at phone width (max-width 1000px, 16px gutters).

## Gotchas
- Git repository on `main`, with `origin` at github.com/DonalMoloney/NewPresGithubAgenticWorkflows (private). Tooling folders are in `.gitignore`.
- The example-workflow repo is a different project and is not in this folder. Ask for its path or URL rather than guessing its contents.
