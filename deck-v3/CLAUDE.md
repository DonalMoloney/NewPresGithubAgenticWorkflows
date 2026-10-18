# Deck v3

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp deck-v3/deck.md --allow-local-files --images png -o <scratchpad>/slide.png` | Render every slide to PNG for checking (the flag lets Marp load the diagrams in `deck-v3/img/`) |
| `marp deck-v3/deck.md --notes -o <scratchpad>/notes.txt` | Export speaker notes |
| `python3 deck-v3/check_deck.py` | Check notes, scoped font sizes and image paths; lists visible TODOs. Tests: `cd deck-v3 && python3 -m unittest test_check_deck` |

## Story and content
- Arc: hook → times changing → earlier attempt → what it is (model, parts, ways to run, types, key points) → example videos, images and links → pilot ask.
- Design for a mixed technical and non-technical audience. Each slide has one main point, written as a short, full-sentence claim. The title slide may use the product name.
- Split a slide when it asks the audience to understand two ideas. Keep related slides together, each with a distinct purpose.
- Use `../overview.md` for the brief narrative. Keep its titles and the matching draft diagrams aligned when the story changes.
- Keep facts, illustrative examples, proposals and measured results visibly distinct. Never imply a placeholder is a real workflow, demo or customer result.
- Verify gh-aw claims against official GitHub sources. Date the check and cite sources on the slide; keep qualifications beside the claim they limit.
- Keep TODOs for unknown repo names, workflow files, owners, budgets, baselines and decisions. Move presenter-only preparation into notes, but keep material gaps visible.
- End the main talk with the decision and next step. Put references after it as an appendix.
- Show `staged: true` on the ways-to-run slide and the pilot slide only.

## Visual language
- Build on `../slide-styling/title-slide.html`: near-black canvas, restrained blue neon accents, pale text, thin borders, generous space. No red theme.
- Make slide 1 look like `../slide-styling/title-slide.html`: GitHub mark and wordmark, then the deck's title as a large heading with a short glowing blue rule beneath it on the left; the Octocat inside the six-step loop (Plan, Code, Test, Review, Open PR, Monitor) on the right; radial blue glow behind. Reuse its SVG and colours rather than redesigning. Keep "Open PR", never "Deploy": gh-aw does not deploy.
- Keep all theme CSS in the front-matter `style:` block (background `#050507`, text `#ececec`, accent `#8fb0dc` / `#b9d0ee`, muted `#a3a3a3`, gaps `#e9a35c`). Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.
- Use one grid, title position, footer, spacing scale and page numbering. Orange is for unresolved details or cautions; green sparingly for permitted outcomes.
- Headlines 40 px or larger, body at least 20 px, code at least 18 px. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison. Keep tables and code blocks dark: Marp's default theme makes `tr` and `pre` light, so the overrides in `style:` must stay.
- Use `.muted` for sources, `.todo` for gaps, `.stat` for one big hook number.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Label conceptual diagrams as illustrative. Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.
- Give diagrams descriptive SVG labels; do not convey meaning by colour alone.

## Speaker notes
- Every slide, including the title and status/sources slide, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size and at phone width. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.md` is the only source. `deck.html` is **generated from it** — never hand-edit `deck.html`, and regenerate it after changing `deck.md`:
  `marp deck-v3/deck.md --allow-local-files -o deck-v3/deck.html </dev/null`
  It keeps `img/*.svg` as relative links, so `deck.html` must stay in `deck-v3/` beside `img/`. (The `</dev/null` is required: marp hangs waiting on stdin otherwise.)
