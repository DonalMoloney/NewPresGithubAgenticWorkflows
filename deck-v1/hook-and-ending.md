# Hook and ending: GitHub Agentic Workflows

Pick one hook and its matching ending by ticking `[x]`. Nothing is chosen yet.

Scope: opens before the title slide and bridges into slide 01 ("Shipping faster quietly creates documentation debt"). Closes after slide 10 (the ask: "Approve a four-week, docs-only pilot").

Main arc this file is written against (10 slides): 01 documentation debt, 02 debt chart, 03 role shift from carrying to reviewing, 04 real PR #8716 (a different workflow), 05 real `update-docs.md`, 06 only a separate job can write, 07 cost per useful change, 08 four-week pilot, 09 risk boxed in on five sides, 10 the ask. "Agents add a third lane beside CI and CD" is treated as appendix. Note: the current `deck.md` still has it as main slide 04 (11 main slides), so its kickers have not been renumbered yet.

Facts used (nothing else is asserted):
- Slide 01 shows the Stack Overflow Developer Survey 2026 stat (56.5%). The spoken hook does not read it. Each hook sets up the question, then the bridge hands the number to the slide.
- Wording from `deck.md` notes: "A controlled path from stale docs to a reviewed pull request." and "The agent proposes; a person decides what merges." Both are in the title-slide notes, not on a slide face.
- The ask, as you supplied it: "Approve a four-week, docs-only pilot". The slide 10 title in `deck.md` is currently "The ask is small, capped and reversible", so the ask sentence is not yet on the slide. Spend limits, repository and owner are still TODO there.
- Honest limit (slide 07 notes): cost per month is unknown until measured.
- Draft PRs and a person deciding what merges: slides 09 and 10.

Timing: about 150 spoken words per minute. Every option, bridge included, is under 80 words. That puts endings at roughly 25 to 35 seconds with pauses, below the usual 45 to 75 second target. If you want a longer close, say so and I will add a sentence.

---

## Hook (pick one)

### [ ] A (question), needs no personal story
Style: relatable question, then a handoff to the slide. About 50 words, 20 to 25 seconds.

> "When did a page of documentation last mislead you? [pause]
> You followed the steps. They were wrong. The code had moved on.
> Was that just you?
> Today: can an AI fix that, and can we trust it to?"

Bridge into slide 01: "Stack Overflow's 2026 survey asked developers what makes context hard to get. Here's what they said."

Reason: the first sentence is 9 words and needs no context. "Was that just you?" opens a gap that slide 01's number answers, so the stat lands as news, not a repeat. The bridge says "context", matching the survey question, not "docs".

### [ ] B (scene), uses your story (TODO slots)
Style: personal scene in progress. About 45 words plus your fills, 25 to 35 seconds.

> "I built a tool for our docs. [TODO: tool name and what it did, one sentence.]
> It solved part of the problem. [pause]
> [TODO: your real moment. See the note below.]
> Has that happened to you?"

Bridge into slide 01: "Stack Overflow's 2026 survey asked developers something close to that. Here's what they said."

What kind of moment fits: one concrete, visible instance of the gap the tool left. For example, a page found out of date after the tool had run, what you saw, and what you did next. This describes the kind of moment only, not facts. Use only what really happened.

Reason: the strongest opener once real, because the audience meets the problem through a person. "Has that happened to you?" sets up the stat. Slide 01 already has a "My earlier attempt" card ("It tackled part of the problem.") with the same TODO. Tell the story once: either here or on the card, and shorten the other.

### [ ] C (surprising contrast), needs no personal story
Style: two-line contrast. About 60 words, 25 to 30 seconds.

> "Your code shipped today. Your documentation didn't. [pause]
> Same repository, two speeds. Every change is another chance for the docs to fall behind.
> This talk is about AI that does that upkeep, not just suggests it.
> But how much does that gap really cost?"

Bridge into slide 01: "Stack Overflow's 2026 survey asked developers what makes context hard to get. Here's what they said."

Reason: shortest and sharpest. The closing question hands over to the stat. It uses the title kicker idea ("from AI that suggests to AI that does") without naming the product first. It states no number itself.

---

## Ending (pick one, each paired to a hook)

Every ending reuses its hook's image and gives it a new meaning, states the slide 10 ask in one sentence, pairs it with the honest limit, and adds no new facts. The last line is under 12 words.

### [ ] A (echoes hook A)
Style: question answered. About 66 words, 25 to 30 seconds.

> "At the start I asked when a page of documentation last misled you. [pause]
> Picture the fix arriving as a draft pull request, with a person deciding what merges.
> The ask: approve a four-week, docs-only pilot.
> The honest limit: we don't know the cost yet. The pilot is how we find out.
> [slow] A controlled path from stale docs to a reviewed pull request. [pause]"

Reason: the misleading page becomes a draft that someone checked before it merged. The last line is 11 words and is the deck's own takeaway wording.

### [ ] B (echoes hook B), has a TODO slot
Style: story closed. About 72 words including the slot, 30 to 35 seconds.

> "At the start I told you about a tool I built for our docs, and the gap it left: [TODO: the gap, 3 to 5 words, same wording as your opening]. [pause]
> This pilot tests whether an agent can close that gap, with a person still deciding what merges.
> The ask: approve a four-week, docs-only pilot.
> The honest limit: we don't know the cost until we measure.
> [slow] A controlled path from stale docs to a reviewed pull request. [pause]"

Reason: the earlier tool goes from a gap that was left to a gap being tested. "Tests whether" avoids promising success. This matches the slide 10 note to name the earlier attempt's gap as the first thing the pilot tests.

### [ ] C (echoes hook C)
Style: contrast flipped. About 62 words, 25 to 30 seconds.

> "Your code shipped today. Your documentation didn't. [pause]
> That sentence can change: a draft documentation pull request, waiting for a person to review.
> The ask: approve a four-week, docs-only pilot.
> The honest limit: we don't know the cost until we measure.
> [slow] Code ships. A draft follows. A person decides. [pause]"

Reason: the same two sentences from the hook now describe a possible outcome ("can change"), not a result. The last line is 8 words. "A draft follows" avoids implying the docs always catch up.

---

## Recommendation

Recommended pair: **Hook A with Ending A**.
- It needs no unsupplied story, so it is ready to deliver today.
- Its question ("Was that just you?") sets up the slide 01 stat without reading it, and the "misled" image is echoed with a new meaning.
- Swap to **B and B** once your real moment is supplied. That pair is the most personal and fits slide 01's own story slot.

Two alternatives for the final line (these work with any ending, each under 12 words):
1. "The agent proposes. A person decides." (6 words, from the title-slide notes: "The agent proposes; a person decides what merges.")
2. "Not AI that suggests. AI that does, with you deciding." (10 words, from the title kicker plus the review idea)

Default final line, used in Endings A and B: "A controlled path from stale docs to a reviewed pull request." (11 words, from the title-slide notes.)

---

## Open TODOs

1. Hook B: the tool name and what it did (one sentence).
2. Hook B: your real moment showing the gap it left.
3. Ending B: the gap in 3 to 5 words, matching your hook wording.
4. Slide 10 decision fields (the ask names a pilot, so be ready to be asked): pilot repository and owner, per-run and total budget, week-four success thresholds, and who the decision-maker is.
5. Slide 01 "My earlier attempt" card (tool, what it solved, the gap) is still TODO. Hook B and this card must tell the same story once, not twice.

Cautions:
- The stat is on slide 01 with its source. Do not read it aloud in the hook. Say "Stack Overflow's 2026 survey" in the bridge only, and keep the word "context": the survey is a multi-select question about context in general, not a measure of documentation alone.
- The ask wording "Approve a four-week, docs-only pilot" came from you. Make the slide 10 title or body say the same words, or the close will not match the screen.
- The third-lane slide is still main slide 04 in `deck.md`. Renumber the kickers once you move it to the appendix, or the slide numbers in this file will not match.
- The endings state no cost figure and no safety guarantee, in line with the deck's "layers of control, not a guarantee" wording.
- Product status is not mentioned in any option. Your instructions say technical preview; `AGENTS.md` and appendix slide 8 say public preview since 11 Jun 2026. Settle that before it appears in the talk.

Hand-off: once ticked, the final text goes to `speaker-notes-writer` for the slide-level notes.
