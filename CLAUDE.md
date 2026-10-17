@AGENTS.md

## Claude Code specifics
- After editing `draft-overview.html`, open it with Playwright and screenshot light and dark mode plus a phone-width viewport before saying it is done.
- The HTML is draft material for slides. When the user asks to build the final deck, use the `slides` skill and reuse the draft diagrams and wording rather than redesigning them.
- Keep edits surgical: change only the slide the user named.
- When creating the deck (in `deck-v1/`: `deck.md` content, `deck.html` slides), build from `slide-styling/title-slide.html`: it is the title slide and the reference for layout, blue neon palette (not red) and styling of every other slide. Reuse its structure and tokens rather than the `-v2` variants.
- Folder layout is in `AGENTS.md`. Keep `overview.md` at the root; draft HTML lives in `slide-styling/`.

## The example-workflow repo (resolves the `AGENTS.md` gotcha)
- It is **`DonalMoloney/Agentic-Workflows-Lib`** — private, last pushed 23 Sep 2026. Verified 17 Oct 2026 with `gh api`.
- Contents: 98 agentic workflow Markdown files in `workflows/`, 98 matching pages in `docs/workflows/`, and an `aw.yml` manifest (name "Acme Agentic Workflows", `min-version: v0.83.4`).
- **Status, per that repo's own `agents.md`:** the seed workflows compile cleanly with `gh aw compile` (v0.83.4, 0 errors, 0 warnings), but they **have never executed in GitHub Actions**, the sandbox repo described in its `docs/sandbox-setup.md` does not exist, and no release is tagged. Never describe them as operational, running, or in production.
- It is **private**, so it cannot be linked from a slide unless the user chooses to make it public. Ask before putting the URL on the appendix slide.
- Its own `.github/workflows/` holds ordinary CI YAML (`validate`, `release`, `rollout`, `sandbox-smoke`), not agentic workflows.

## Running `gh aw` for real
- `gh aw` v0.83.4 is installed; `gh` is authenticated as `DonalMoloney`.
- Installing or trialling a workflow pushes files under `.github/workflows/`, which the OAuth token **cannot** do without the `workflow` scope. Symptom: `refusing to allow an OAuth App to create or update workflow ... without 'workflow' scope`. Fix is interactive and must be run by the user: `gh auth refresh -h github.com -s workflow`.
- `gh aw trial` needs a repository context, and this folder is not a git repo, so pass `--clone-repo <owner/repo>` (clones that repo's contents into a throwaway host repo) or `--logical-repo <owner/repo>` (simulates the context only). The two flags are mutually exclusive.
- Trial creates and **retains** a private host repo, `DonalMoloney/gh-aw-trial` by default. Use `--delete-host-repo-before` to reuse it and `--delete-host-repo-after` to clean up.

## Deck design principles (all decks)
- **One idea per slide.** The title is the claim; the body is the evidence for it. If a slide overflows, split it into two claim-titled slides. Never shrink body text below 20px or code below 18px to make it fit.
- **Plain English first, technical second.** The room is mixed. Reuse the teammate model throughout: job description = markdown body, shift = `on:`, access badge = `permissions`/`tools`, outbox = `safe-outputs`.
- **Show mechanism over quotes.** A real setting (`draft: true`, `max-ai-credits`, the separate write job) beats a blog quote. Use quotes as support, not proof.
- **Real artifacts over invented examples.** Show `workflows/update-docs.md` from githubnext/agentics. Label it "trimmed" or "paraphrased" when cut.
- **Every number and quote carries a muted on-slide source,** plus its caveat: "illustrative", "reported by GitHub", "this deck's interpretation".
- **Never overclaim safety.** Do not say detection "always blocks" (`continue-on-error` defaults to `true`). Present "never merged automatically" as GitHub Blog guidance, not a hard limit.
- **When official sources conflict, leave the fact off the slide** and record the conflict on the deck's status and sources slide (e.g. the daily AI Credit cap default).
- **Say each fact once.** Do not repeat a point across slides.
- **Keep gaps visible** as orange TODO markers until the user supplies real content.

## Speaker notes (all decks)
- Give every slide a note. Write it in this order: the plain-English line to say, the technical detail, exact numbers and quotes with sources, then likely audience questions with answers.
- Put careful-wording warnings in the notes (what not to claim).
- Write TODO in a note rather than inventing the story or the ask.
