# Hook and ending: GitHub Agentic Workflows

Pick one hook and its matching ending by ticking `[x]`. Nothing is chosen yet.

Scope: opens before the title slide and bridges into slide 01 ("Faster shipping keeps reopening the documentation gap"). Closes after slide 08 ("Approve one workflow, one owner and a capped four-week pilot").

Facts used (nothing else is asserted):
- Stack Overflow Developer Survey 2026: 56.5% of 12,374 developers say outdated information makes it hard to get context. Supplied by the user as verified. It is not in `deck.md`, so say the source aloud.
- Deck takeaway (title slide, verbatim): "A controlled path from stale docs to a reviewed pull request."
- Slide 08 ask (from `deck.md`): approve one workflow, one owner and a capped four-week pilot. Documentation only, draft PRs, a person decides what merges.
- Honest limit (from slide 06 notes): cost per month is unknown until measured.
- Real public PR github/gh-aw #8716 is a slide 03 example. It is not used here, to avoid repeating it.

Timing: about 150 spoken words per minute. Every option is under 80 words, as requested. That puts the endings at roughly 30 to 40 seconds with pauses, below the usual 45 to 75 second target. If you want a longer close, say so and I will add a sentence.

---

## Hook (pick one)

### [ ] A (question), needs no personal story
Style: question plus verified statistic. About 58 words, 25 to 30 seconds.

> "When did you last stop trusting a page of documentation? [pause]
> You're not alone. In the Stack Overflow Developer Survey 2026, 56.5% of 12,374 developers said outdated information makes it hard to get context.
> The code moves on. The docs stay behind. [pause]
> Today: can an AI close that gap, and can we trust it to?"

Bridge into slide 01: "First, why faster shipping keeps reopening that gap."

Reason: the first sentence is 10 words and needs no context. The statistic gives the non-technical half of the room a reason to care before any product name appears.

### [ ] B (scene), uses your story (TODO slot)
Style: personal scene in progress. About 45 words plus your two fills, 25 to 35 seconds.

> "I built a tool for our docs. [TODO: tool name and what it did, one sentence.]
> It solved part of the problem. [pause]
> [TODO: your real moment. See the note below.]
> That gap is what today is about."

Bridge into slide 01: "Because faster shipping keeps reopening it."

What kind of moment fits: one concrete, visible instance of the gap the tool left. Examples of the kind of thing, not facts: a page you or someone else found out of date after the tool had run, what you saw, and what you did next. Use only what really happened.

Reason: it is the strongest opener once real, because the audience meets the problem through a person. If you use it, shorten the "My earlier attempt" card on slide 01 so the story is not told twice.

### [ ] C (surprising contrast), needs no personal story or statistic
Style: two-line contrast. About 47 words, 20 to 25 seconds.

> "Your code shipped today. Your documentation didn't. [pause]
> Same repository, two speeds. Every change is another chance for the docs to fall behind.
> This talk is about AI that does that upkeep, not just suggests it."

Bridge into slide 01: "So let's start with why faster shipping keeps reopening the gap."

Reason: shortest and sharpest. It uses the title kicker idea ("from AI that suggests to AI that does") without naming the product first. It makes no numerical claim.

---

## Ending (pick one, each paired to a hook)

Every ending reuses its hook's image and gives it a new meaning, states the slide 08 ask in one sentence, pairs it with the honest limit, and adds no new facts. The last line is under 12 words.

### [ ] A (echoes hook A)
Style: question answered. About 71 words, 30 to 35 seconds.

> "I asked when you last trusted a page of documentation. [pause]
> Here's a new answer: when a person reviewed every change.
> The ask: approve one workflow, one owner, and a capped four-week pilot.
> Documentation only. Draft pull requests. You decide what merges.
> The honest limit: we don't know the cost yet, and the pilot is how we'll find out.
> [slow] A controlled path from stale docs to a reviewed pull request. [pause]"

Reason: "trust" becomes something earned by review, not by docs that never go stale. The last line is 11 words and is the deck's own takeaway.

### [ ] B (echoes hook B), has a TODO slot
Style: story closed. About 75 words including the slot, 30 to 40 seconds.

> "At the start I told you about a tool I built for our docs, and the gap it left: [TODO: the gap, 3 to 5 words, same wording as your opening]. [pause]
> This pilot tests whether an agent can close that gap, with a person still deciding what merges.
> The ask: approve one workflow, one owner, and a capped four-week pilot.
> The honest limit: documentation only, and we don't know the cost until we measure.
> [slow] A controlled path from stale docs to a reviewed pull request. [pause]"

Reason: the earlier tool goes from a gap that was left to a gap being tested. "Tests whether" avoids promising the agent will succeed.

### [ ] C (echoes hook C)
Style: contrast flipped. About 56 words, 25 to 30 seconds.

> "Your code shipped today. Your documentation didn't. [pause]
> That sentence can change: a draft documentation pull request, waiting for a person to review.
> The ask: approve one workflow, one owner, and a capped four-week pilot.
> The honest limit: documentation only, and we don't know the cost until we measure.
> [slow] Code ships. Docs follow. A person decides. [pause]"

Reason: the same two sentences in the hook now describe a possible outcome ("can change"), not a result. The last line is 7 words.

---

## Recommendation

Recommended pair: **Hook A with Ending A**.
- It needs no unsupplied story, so it is ready to deliver today.
- It uses the only verified statistic, and the trust question is echoed with a new meaning.
- Swap to **B and B** once your real moment is supplied. That pair is the most personal and best matches slide 01's own story slot.

Two alternatives for the final line (these work with any ending, each under 12 words):
1. "The agent proposes. A person decides." (6 words, from the title slide card "The agent proposes; a person decides what merges.")
2. "Not AI that suggests. AI that does, with you deciding." (10 words, from the title kicker plus the review idea)

Default final line, used in Endings A and B: "A controlled path from stale docs to a reviewed pull request." (11 words, verbatim from the title slide.)

---

## Open TODOs

1. Hook B: the tool name and what it did (one sentence).
2. Hook B: your real moment showing the gap it left.
3. Ending B: the gap in 3 to 5 words, matching your hook wording.
4. Slide 08 decision fields (not needed to deliver the ending, but the ask names "one owner"): pilot repository and owner, per-run and total budget, week-four success thresholds, and who the decision-maker is.
5. Slide 01 "My earlier attempt" card (tool, what it solved, the gap) is still TODO. Hook B and this card must tell the same story once, not twice.

Cautions:
- The 56.5% / 12,374 figure comes from you and is not on any slide. Say "Stack Overflow Developer Survey 2026" aloud, and add an on-slide source if you show it.
- The ending does not state a cost figure or a safety guarantee, in line with the deck's "layers of control, not a guarantee" wording.
- I did not mention product status in any option. Note that your instructions and `deck.md`/`AGENTS.md` disagree on it (technical preview versus public preview since 11 Jun 2026). Settle that before it appears anywhere in the talk.

Hand-off: once ticked, the final text goes to `speaker-notes-writer` for the slide-level notes.
