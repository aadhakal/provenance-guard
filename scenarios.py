"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

from pathlib import Path

# ── The fixed paragraph set ───────────────────────────────────────────────────
# Criterion 2 promises these were committed before testing. Fill them in and
# commit BEFORE you look at any scores, and don't swap them afterwards.

def _paragraphs(filename: str) -> list[str]:
    """One paragraph per blank-line-separated block of a reference file."""
    text = (Path(__file__).parent / filename).read_text(encoding="utf-8")
    return [block.strip() for block in text.split("\n\n") if block.strip()]


# Criterion 1: ten human-written paragraphs, public-domain U.S. government
# writing from 2014-2020. Sources are in human_reference_sources.md, in the
# same order.
HUMAN_REFERENCE = _paragraphs("human_reference_paragraphs.md")

# Criteria 2 and 5: the human four are reused from HUMAN_REFERENCE.
COVERAGE_HUMAN = HUMAN_REFERENCE[:4]

# Unedited AI output. Model and instruction are in ai_reference_sources.md.
COVERAGE_AI = _paragraphs("ai_reference_paragraphs.md")

# Human and AI sentences combined in known proportions. Which parts came from
# where is in mixed_reference_sources.md, in the same order.
COVERAGE_MIXED = _paragraphs("mixed_reference_paragraphs.md")

# ── Criterion 3 boundaries ────────────────────────────────────────────────────
# Ordinary words, so these test the character limits and not the detector's
# 3-token minimum (fifty dashes is 50 characters but only 2 tokens).
SENTENCE_50 = "The bus came late again, so I walked home instead."
_FILLER = (SENTENCE_50 + " ") * 200
TEXT_10000 = _FILLER[:10_000]
TEXT_10001 = _FILLER[:10_001]


SCENARIOS = [
    {
        "name": "human reference writing",
        "criterion": 1,
        # At most 1 of these 10 may be labelled high-confidence AI, per trial.
        "texts": HUMAN_REFERENCE,
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Each of the three labels must appear at least twice, per trial.
        "texts": COVERAGE_HUMAN + COVERAGE_AI + COVERAGE_MIXED,
    },
    {
        "name": "bad input",
        "criterion": 3,
        # The first six must get a 400 and no label; the last two must be
        # accepted and labelled.
        "bodies": [
            {"creator_id": "eval_bad_missing"},  # no text field at all
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"text": 42, "creator_id": "eval_bad_number"},
            {"text": SENTENCE_50[:-1], "creator_id": "eval_bad_49_chars"},
            {"text": TEXT_10001, "creator_id": "eval_bad_10001_chars"},
            {"text": SENTENCE_50, "creator_id": "eval_ok_50_chars"},
            {"text": TEXT_10000, "creator_id": "eval_ok_10000_chars"},
        ],
    },
    # Criterion 4 (the appeal path) can't be a scenario: it needs a submission
    # first, then an appeal against the content_id that came back. Test it by
    # hand or extend run_eval.py once /appeal exists (Milestone 5), and say
    # which in the write-up.
    {
        "name": "score spread",
        "criterion": 5,
        # Mean human score must be at least 0.30 below mean AI score, and the
        # top human may beat the bottom AI by at most 0.10, per trial.
        "texts": COVERAGE_HUMAN + COVERAGE_AI,
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
