# Deck v2

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp deck-v2/deck.md --allow-local-files --images png -o <scratchpad>/slide.png` | Render every slide to PNG for checking (the flag lets Marp load the diagrams in `deck-v2/img/`) |
| `marp deck-v2/deck.md --notes -o <scratchpad>/notes.txt` | Export speaker notes |
| `python3 deck-v2/check_deck.py` | Check notes, scoped font sizes and image paths; lists visible TODOs. Tests: `cd deck-v2 && python3 -m unittest test_check_deck` |

## Story and content
- Arc, as section headers (reordered 17 Oct 2026): **Why now** (hook → why it persists → more code, more autonomy → earlier attempt) → **What it is** → **Does it work?** → **Is it safe?** → **What I've built** → **The ask** (what a month costs, then the ask itself) → **Appendix**. Proof sits before safety on purpose: the room asks "what is it, does it work, is it safe" in that order, and it breaks up what used to be three consecutive safety slides.
- The code slide must stay after the write-token slide: its rebuttal box says "the read-only, firewalled job from the previous slide". Showing the file earlier means showing `bash: true` and `toolsets: [all]` before anything has fenced them.
- Design for a mixed technical and non-technical audience. Each slide has one main point, written as a short, full-sentence claim. The title slide may use the product name.
- Split a slide when it asks the audience to understand two ideas. Keep related slides together, each with a distinct purpose.
- `../overview.md` describes **deck-v1**, not this deck: a different palette and different slide titles throughout. Verified 17 Oct 2026. Do not sync deck-v2 to it, and do not rewrite it to match deck-v2 — deck-v1 and deck-v3 are worked on in parallel sessions. If deck-v2 ever needs a canonical spine, give it its own file.
- Keep facts, illustrative examples, proposals and measured results visibly distinct. Never imply a placeholder is a real workflow, demo or customer result.
- Verify gh-aw claims against official GitHub sources. Date the check and cite sources on the slide; keep qualifications beside the claim they limit.
- Keep TODOs for unknown repo names, workflow files, owners, budgets, baselines and decisions. Move presenter-only preparation into notes, but keep material gaps visible.
- End the main talk with the decision and next step. Put references after it as an appendix.
- Show `staged: true` on the ways-to-run slide and the pilot slide only.

## Visual language
- **White content slides, one dark title slide.** Slide 1 keeps the look of `../slide-styling/title-slide.html` and its own scoped colours; slides 2 onward use the light theme in the front-matter `style:` block. No glows, gradients or tinted canvases on content slides. Decided 18 Oct 2026; this replaces the earlier dark theme.
- Make slide 1 look like `../slide-styling/title-slide.html`: GitHub mark and wordmark, then the deck's title as a large heading with a short glowing rule beneath it on the left; the Octocat inside the six-step loop (Plan, Code, Test, Review, Open PR, Monitor) on the right. Reuse its SVG and colours rather than redesigning. Keep "Open PR", never "Deploy": gh-aw does not deploy.
- Keep all theme colours in the front-matter `style:` block as role-named `:root` custom properties (`--bg`, `--surface`, `--line`, `--text`, `--dim`, `--accent`, `--accent-soft`, `--caution`). Values live only there; this file names roles, not colours. Use the token, never a literal colour, in new rules. Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.
- **One accent, for structure only:** `.k` labels, header and card rules, `.stat`, YAML keys, diagram strokes and the one highlighted box in a diagram. Everything else is neutral. If a slide shows the accent in more than about three places, pull some back to neutral.
- **Emphasis by weight, not colour.** `strong`, inline code and table headers stay in the text colour. Tiers: `--dim` → `--text` → bold → `.stat`.
- `--caution` is for `.todo` and genuine cautions only. Permitted and denied outcomes (in `run-jobs.svg`) use distinct success/danger colours, always paired with ✓/✗ glyphs and words, never colour alone. Do not use the danger colour anywhere else.
- Use one grid, title position, footer, spacing scale and page numbering.
- Headlines 40 px or larger, body at least 20 px, code at least 18 px. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison. Tables and code blocks sit on `--surface` with `--line` borders; the overrides in `style:` replace Marp's default striped rows.
- Use `.muted` for sources, `.todo` for gaps, `.stat` for one big hook number, `.lede` for the plain-English restatement of the claim, and `.turn` for the one takeaway box (tinted panel, accent left border). A whole sentence in `**bold**` is not a lede — use the class.
- Slides are top-aligned (`place-content: start` overrides the default theme's centring; `_class: lead` re-centres). Put a slide's source in `<div class="source">` (fixed footer), not inline. For 2–4 parallel points use `.cards` > `.card` with a `.k` label, not bold-led paragraphs.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Label conceptual diagrams as illustrative. Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.
- Give diagrams descriptive SVG labels; do not convey meaning by colour alone.
- Every `img/*.svg` carries its palette as `:root` custom properties in its own `<style>` block, so recolouring is a find/replace, not a redraw. Keep it that way. `title-loop.svg` and `github-mark.svg` belong to the dark title slide; the other six use the light content palette and must match the `style:` tokens.

## Speaker notes
- Every slide, including the title and status/sources slide, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size and at phone width. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.md` is the only source. `deck.html` is **generated from it** — never hand-edit `deck.html`, and regenerate it after changing `deck.md`:
  `marp deck-v2/deck.md --allow-local-files -o deck-v2/deck.html </dev/null`
  It keeps `img/*.svg` as relative links, so `deck.html` must stay in `deck-v2/` beside `img/`. (The `</dev/null` is required: marp hangs waiting on stdin otherwise.)

## Pending work
- `todo.md` in this folder is the consolidated list of patches and proposed slides not yet applied. Check it before starting any editing session.
