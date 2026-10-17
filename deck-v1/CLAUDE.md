# Deck v1

Follow `../AGENTS.md` and `../CLAUDE.md`. Design and speaker-note principles live in the root `CLAUDE.md`; this file adds deck-specific rules. An explicit request to review the whole deck authorizes changes to every slide.

## Commands
Run from the project root. `<scratchpad>` is the session scratchpad directory.

| Command | Description |
|---------|-------------|
| `marp --html deck-v1/deck.md -o deck-v1/deck.html` | Render `deck.html` from `deck.md` |
| `marp deck-v1/deck.md --images png -o <scratchpad>/slide.png` | Render every slide to PNG for checking |
| `marp deck-v1/deck.md --notes -o <scratchpad>/notes.txt` | Export speaker notes |

## Story and content
- Arc: documentation problem → earlier attempt → agentic workflow → visible example → controls → safe first use → pilot decision.
- Design for a mixed technical and non-technical audience. Each slide has one main point, written as a short, full-sentence claim. The title slide may use the product name.
- Split a slide when it asks the audience to understand two ideas. Keep related slides together, each with a distinct purpose.
- Use `../overview.md` for the brief narrative. Keep its titles and the matching draft diagrams aligned when the story changes.
- Keep facts, illustrative examples, proposals and measured results visibly distinct. Never imply a placeholder is a real workflow, demo or customer result.
- Verify gh-aw claims against official GitHub sources. Date the check and cite sources on the slide; keep qualifications beside the claim they limit.
- Keep TODOs for unknown repo names, workflow files, owners, budgets, baselines and decisions. Move presenter-only preparation into notes, but keep material gaps visible.
- End the main talk with the decision and next step. Put references after it as an appendix.
- Show `staged: true` on the staged-mode slide and the pilot slide only.

## Visual language
- Build on `../slide-styling/title-slide.html`: near-black canvas, restrained blue neon accents, pale text, subtle glow, thin borders, generous space. No red theme.
- Keep all theme CSS in the front-matter `style:` block (background `#0c0c0c`, text `#ececec`, accent `#8fb0dc` / `#b9d0ee`, muted `#a3a3a3`, gaps `#e9a35c`). Use `<style scoped>` for one-slide tweaks; never change the global theme to fix one slide.
- Use one grid, title position, footer, spacing scale and page numbering. Orange is for unresolved details or cautions; green sparingly for permitted outcomes.
- At 1280 × 720: 44–54 px headlines, 26–32 px body, at least 20 px code. Compact citations may be smaller. Never shrink essential content to keep a slide count.
- Process diagram for sequence, paired panels for comparison, code card with adjacent annotations for a file, chart for measured outcomes. Tables only when rows and columns help comparison. Keep tables and code blocks dark.
- Use `.muted` for sources, `.todo` for gaps, `.stat` for one big hook number.
- Remove decorative quotes, audience labels and repeated prose. Every visual must explain something.
- Label conceptual diagrams as illustrative. Show denominators and source dates for statistics. No invented screenshots, logos or demo outcomes.
- Give diagrams descriptive SVG labels; do not convey meaning by colour alone.

## Speaker notes
- Every slide, including the title and source appendix, has Marp speaker notes in a plain HTML comment `<!-- … -->` after the slide body. Directive comments like `<!-- _class: lead -->` are not notes; keep them in separate comments.
- Notes follow the root order (plain-English line, technical detail, numbers and sources, audience questions) and end with a transition. Do not merely repeat the slide.
- Put technical depth, commands, source qualifications, preparation TODOs and fallback demo steps in notes. Keep essential qualifications on the slide too.
- Keep `speaker-notes.md` in sync as the rehearsal copy.

## Verification
- After any edit, render and look at every changed slide. Nothing may run off the bottom edge or overlap; table and code text must be readable. Check dense code and data slides at full size and at phone width. Compiling is not a visual check.
- Confirm every slide has a note.
- `deck.html` is generated from `deck.md`: never edit it directly. Re-render it, and update `deck.pdf`, after `deck.md` changes.
