"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# How many words type_token_ratio looks at, so long and short texts compare.
TTR_WINDOW = 60

# Fixed ranges for style_signal, chosen up front and checked against the
# calibration inputs (calibration_paragraphs.md), never the evaluation sets.
SPREAD_AI = 0.2     # sentences this even, or more, read as fully AI-like
SPREAD_HUMAN = 0.8  # sentences this varied, or more, read as fully human-like
PUNCT_HUMAN = 2.0   # uncommon marks per 100 words that count as fully human-like


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    Mine: standard deviation of sentence lengths in words, divided by the mean
    (coefficient of variation). 0 means every sentence is the same length;
    higher means more human. Fewer than two sentences returns 0.0, which reads
    as AI-ish here, but style_signal caps how much this signal can matter.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    Mine: computed over the first TTR_WINDOW words only, so length doesn't
    drive the result. Texts shorter than that use all their words.
    """
    tokens = words(text)[:TTR_WINDOW]
    if not tokens:
        return 0.0
    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    Mine: the less routine marks only — ; : ( ) ? ! and dashes (em, en, or a
    spaced hyphen) — per 100 words. Full stops and commas are left out because
    nearly all writing uses them at similar rates. Higher means more human.
    """
    n_words = len(words(text))
    if n_words == 0:
        return 0.0
    marks = sum(text.count(c) for c in ";:()?!—–") + text.count(" - ")
    return 100 * marks / n_words


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    Mine: the average of two measures, each mapped onto 0–1 with higher = AI.

      - Spread, inverted: SPREAD_HUMAN or above → 0.0, SPREAD_AI or below → 1.0,
        linear in between.
      - Punctuation, one-sided: none → 0.5 (a short paragraph often has none,
        so absence isn't evidence), PUNCT_HUMAN per 100 words or more → 0.0.

    Type-token ratio is computed but left out. On the calibration inputs it ran
    backwards (the clearly-AI paragraph had the most varied vocabulary), and
    four samples are too few to justify flipping it.
    """
    spread = sentence_length_spread(text)
    spread_ai = (SPREAD_HUMAN - spread) / (SPREAD_HUMAN - SPREAD_AI)
    spread_ai = min(max(spread_ai, 0.0), 1.0)

    punct_ai = 0.5 * (1 - min(punctuation_density(text) / PUNCT_HUMAN, 1.0))

    return (spread_ai + punct_ai) / 2


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text):.3f}   (higher = more likely AI)")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
