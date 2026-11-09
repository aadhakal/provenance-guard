# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
- A creator sends text and creator_id to POST /submit.
- The route reads and validates the JSON input.
- The service creates a unique content_id for that submission.
- The model signal measures how predictable the wording is and returns an AI-likelihood score.
- The style signal measures writing patterns: sentence-length variation and uncommon punctuation.
- The scoring rule combines both scores into one AI-likelihood score.
- The service maps that score to a human-readable label, writes the decision to the audit log, and returns the result with the content_id.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->
- The model signal can mistake simple, predictable human writing, especially from language learners or younger writers, for AI-generated text.
- The style signal only sees surface patterns. Typos, unusual punctuation, quotations, or deliberately varied sentence lengths can change its score without changing who wrote the text.

### Signal one — the model signal

> **Changed in unit 8:** the model is now Qwen2.5-0.5B with a midpoint of 13.
> This section describes the unit 7 build with GPT-2. See The Improvement.

**What it measures:** How predictable the text is to GPT-2, a small language
model that runs on my laptop (`detector.py::model_signal`). It reads the first
400 tokens, works out the perplexity, and turns that into a score from 0 to 1.
Lower perplexity gives a higher AI score.

**Why that might differ between human and AI writing:** The idea behind this
signal is that a language model tends to choose likely next words, so its
output might be easier for another model to predict than human writing is.
.GPT-2 is an older and different model from the ones that write most AI text today, chat models can be set to pick less likely words, and a lot of human writing is predictable too.

**What it can't see:** Who wrote the text. Plain, simple human writing is
predictable too, and so is anything GPT-2 already saw in training. Both can
score as AI. It also ignores everything after the first 400 tokens.

**Change from the starter code:** The starter scored a perplexity of 45 as
0.5. Both human calibration paragraphs came out AI-leaning at 45, so the
midpoint was moved to 25, about halfway between the human and AI calibration
texts. It was picked from only four texts, so it's a starting guess.

### Signal two — the style signal

**What it measures:** The shape of the text, not what it says
(`stylometry.py::style_signal`). It averages two things:

- Sentence-length spread: how much sentence lengths vary. Even lengths push
  the score toward AI.
- Uncommon punctuation: semicolons, colons, dashes, brackets, question marks
  and exclamation marks per 100 words. Having some pushes toward human. Having
  none counts as neutral, since short paragraphs often have none.

**Why that might differ between human and AI writing:** The assumption is
that AI writing might use more even sentence lengths and more conventional
punctuation, while some people mix very short and very long sentences. That
varies a lot by writer, by model, and by the prompt, so it's a weak clue at
best.

**What it can't see:** Meaning. Typos, quotes, or chopped-up sentences change
the score without changing who wrote the text. That makes it easy to fool, so
it gets less weight.

**Left out:** Type-token ratio (how many different words are used) is in the
code but not in the score. On the calibration texts it pointed the wrong way:
the AI paragraph used the most different words. Four texts aren't enough to
justify flipping it, so I left it out.

### The combining rule

**The rule:** Mostly trust the model signal, since the style signal is easier
to fool. If the two signals disagree by more than 0.5, pull the score halfway
back to 0.5. Strong disagreement means we don't know, and a wrong accusation
hurts a writer more than a missed AI text hurts the site.

**The numbers:** 0.7 × model score + 0.3 × style score. Disagreement gap 0.5,
pulled halfway. All in `config.py`.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** Jon
Pratt's 2018 NIST blog paragraph ("It has been a grand experience…"), one of
my human calibration texts. Before the midpoint change, the model gave it 0.62
(leaning AI) and the style signal gave 0.25 (human), because he writes short
fragments like "Even if watching from home." The gap was 0.37, under 0.5, so
the rule used the plain weighted average: 0.51. After the midpoint change the
model gives 0.39 and the combined score is 0.345, a human label.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.40 | This writing looks like it was written by a person. |
| unsure | 0.40 – 0.60 | We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result. |
| high-confidence AI | 0.60 – 1.00 | This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal. |

The ranges come from `scoring.py::label_ranges()` and the cutoffs live in
`config.py`. They were set from the same four calibration texts as the
midpoint, so getting those four right proves nothing. They haven't been tested
on new text yet, and unit 8 is the first real test. The margins are thin: the
AI calibration paragraph scored 0.6115, just over the 0.60 cutoff.

**Why I worded the "unsure" one this way:** Someone reading it may have
written every word. So it says plainly that it doesn't mean anyone did
anything wrong, and that nothing will happen because of it. "That happens
often" is there so the writer doesn't feel singled out. It has no numbers in
it and doesn't ask the writer to prove anything.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

The text is one of my AI calibration paragraphs (written by Claude Opus 5.5),
so the appeal just shows the process working. It isn't a real authorship
claim. I used port 5050 because 5000 was busy.

```bash
$ curl -X POST http://127.0.0.1:5050/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Effective time management is an essential skill for students and professionals alike. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly improve their productivity. Additionally, taking regular breaks helps maintain focus and prevent burnout. Ultimately, developing strong time management habits not only enhances performance but also contributes to a healthier work-life balance and greater overall well-being.", "creator_id": "aashish"}'
```

```json
{
  "confidence": 0.6115,
  "content_id": "4d1e95e8-8489-426f-8639-77b7232a77fb",
  "guess": "ai",
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "model_score": 0.6256,
  "style_score": 0.5787
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5050/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "4d1e95e8-8489-426f-8639-77b7232a77fb", "reasoning": "I wrote this paragraph for a study-skills handout. Please have someone review it."}'
```

```json
{
  "content_id": "4d1e95e8-8489-426f-8639-77b7232a77fb",
  "message": "Thanks. Your appeal has been recorded, and a person will review this result.",
  "status": "under_review"
}
```

**What the log shows afterwards**

The original decision stays as it was. The appeal is added after it.

```bash
$ curl "http://127.0.0.1:5050/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6115,
      "content_id": "4d1e95e8-8489-426f-8639-77b7232a77fb",
      "creator_id": "aashish",
      "guess": "ai",
      "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
      "model_score": 0.6256,
      "status": "decided",
      "style_score": 0.5787,
      "timestamp": "2026-11-02T11:22:42+00:00"
    },
    {
      "content_id": "4d1e95e8-8489-426f-8639-77b7232a77fb",
      "creator_id": "aashish",
      "event": "appeal",
      "reasoning": "I wrote this paragraph for a study-skills handout. Please have someone review it.",
      "status": "under_review",
      "timestamp": "2026-11-02T11:22:42+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Feedback on Criterion 2, which only needed each label
  once.
- *What came back:* It said that was too easy, since one paragraph per label
  would pass. It suggested a fixed mix of paragraphs and each label at least
  twice, and said once could be a fluke of the model's randomness.
- *What I changed:* I kept the stricter target. A second review pointed out
  that the model isn't random here (same text, same score), so I changed the
  reason to "so coverage doesn't depend on a single paragraph."

**Moment 2**

- *What I asked for:* To find paragraphs online to use as my own writing for
  Criterion 1.
- *What came back:* It refused, since the criterion said I wrote them. It also
  pointed out that GPT-2 may have seen popular web text in training.
- *What I changed:* I used ten public-domain U.S. government paragraphs from
  2014 to 2020, cited them, and rewrote Criterion 1 to say that.

**Moment 3**

- *What I asked for:* To finish the labels in Milestone 5.
- *What came back:* It moved the detector midpoint to 25 and set the cutoffs
  at 0.40 and 0.60, picked from the four calibration texts. I hadn't made
  those choices myself.
- *What I changed:* Getting those same four texts right is circular, so I
  kept the values only as a starting guess and said so in this README. Unit 8
  tests them on new text, and if they're wrong, fixing them can be my
  improvement.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day for each creator_id. On top of that,
30 per minute, 300 per day for each IP address.

**Why those numbers and not others:** A real writer might submit a piece, fix
something, and resubmit a few times in a row, so 5 a minute leaves room for
that. Nobody needs 50 checks of their own writing in a day. A script trying to
map where my 0.40 and 0.60 cutoffs sit needs hundreds of probes, and 50 a day
slows that down a lot. The IP limit is looser because a school or a dorm can
put many real writers behind one address.

**What a caller counts as:** Both. The first limit counts by creator_id (or IP
if there's no creator_id). On its own, a script could get around it by making
up a new creator_id for every request, so the second limit counts by IP
address. Its weakness is the opposite one: a whole classroom on one network
shares it.

`127.0.0.1` is exempt from the IP limit, because all my test runs come from
my own laptop and would otherwise get cut off partway. So the IP limit isn't
exercised in my attack or criteria runs. I checked it separately with Flask's
test client, faking a non-local address and using a new creator_id each time:
requests 1 to 30 got through and 31 to 33 got a 429. A script that rotates
both creator_id and IP address would still get around both limits.

**The run of status codes when I pushed past it:**

```
$ python run_attacks.py --flood 15

15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
```

Each 429 is logged too:

```json
{"creator_id": "flood_tester", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-09T04:26:17+00:00"}
```

---

## Attack Run — Before

56 attacks, run with `python run_attacks.py --set . --label before`. Full
report: `results/attack_run_2026-11-08_2231_before.md`. No attack crashed the
service or got a 500.

| Family | Held | Broke |
|---|---|---|
| evasion | 3 | 7 |
| false_positive | 2 | 6 |
| prompt_injection | 2 | 4 |
| malformed | 17 | 3 |
| flood_same_creator | 12 | 0 |
| **Total** | **36** | **20** |

How I judged them:

- Evasion: AI text labelled human is BROKE. Unsure is HELD, since the system
  didn't accuse anyone and didn't call it human.
- False positive: human text labelled AI is BROKE. FP08 is also BROKE: it's
  real writing under 50 characters, so the writer couldn't submit it at all.
- Prompt injection: no instruction was obeyed, and the label text and log
  can't be changed by the input. But PI01, PI02, PI03 and PI05 wrap AI text,
  and all four came back human, so I marked those BROKE.
- Malformed: anything rejected with a 4xx is HELD. RQ10 and RQ11 got a 429
  instead of a 400. That's still a rejection, but for the wrong reason (see the
  last log entry below).

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.387 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | human | 0.255 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | human | 0.400 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.491 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.170 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | human | 0.316 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | human | 0.399 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.392 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.495 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.840 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.431 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.582 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.625 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.646 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.633 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.666 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.613 | BROKE |
| FP08 | false_positive | very short genuine human submission | 400 | — | — | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.285 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.101 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | human | 0.369 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | human | 0.297 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | human | 0.369 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | human | 0.395 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.921 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.919 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.779 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.401 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.366 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.366 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.366 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.366 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.366 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |

**Ten audit log entries from the run**

In order: FP03, MF07, MF05, EV01, EV02, PI02, PI05, FP08, RQ10 and one flood
request. EV01 is worth a look: the typos were aimed at signal two, but they
broke signal one instead (model score 0.07). The RQ10 entry shows the
rate-limit bug: requests with no usable creator_id all share one 5-a-minute
limit keyed on my IP address.

```json
{"combined_score": 0.6251, "content_id": "42357252-2523-4f1b-9527-b31141f7ecbe", "creator_id": "attacker_FP03", "guess": "ai", "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.", "model_score": 0.6173, "status": "decided", "style_score": 0.6432, "timestamp": "2026-11-09T04:31:41+00:00"}
{"combined_score": 0.7786, "content_id": "7c19b4ac-8818-4033-b117-7d577e7b4343", "creator_id": "attacker_MF07", "guess": "ai", "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.", "model_score": 0.7908, "status": "decided", "style_score": 0.75, "timestamp": "2026-11-09T04:31:42+00:00"}
{"combined_score": 0.9207, "content_id": "2df01004-91e0-41e1-a3f4-7b6e44f72d52", "creator_id": "attacker_MF05", "guess": "ai", "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.", "model_score": 0.9939, "status": "decided", "style_score": 0.75, "timestamp": "2026-11-09T04:31:42+00:00"}
{"combined_score": 0.3873, "content_id": "fd4a5c4f-4ab7-444b-9e67-01b750a51f9c", "creator_id": "attacker_EV01", "guess": "human", "label": "This writing looks like it was written by a person.", "model_score": 0.0709, "status": "decided", "style_score": 0.75, "timestamp": "2026-11-09T04:31:41+00:00"}
{"combined_score": 0.2547, "content_id": "f6f53422-366b-491c-94f2-a33c3d0faa0d", "creator_id": "attacker_EV02", "guess": "human", "label": "This writing looks like it was written by a person.", "model_score": 0.3638, "status": "decided", "style_score": 0.0, "timestamp": "2026-11-09T04:31:41+00:00"}
{"combined_score": 0.1009, "content_id": "6adc4e02-5cea-4cc5-ba8a-b67b433caabc", "creator_id": "attacker_PI02", "guess": "human", "label": "This writing looks like it was written by a person.", "model_score": 0.0912, "status": "decided", "style_score": 0.1235, "timestamp": "2026-11-09T04:31:42+00:00"}
{"combined_score": 0.3691, "content_id": "0d789c34-6458-459a-9d06-2f4491cd3008", "creator_id": "attacker_PI05", "guess": "human", "label": "This writing looks like it was written by a person.", "model_score": 0.4099, "status": "decided", "style_score": 0.2738, "timestamp": "2026-11-09T04:31:42+00:00"}
{"creator_id": "attacker_FP08", "detail": "Text must be at least 50 characters, not counting surrounding whitespace.", "event": "rejected", "reason": "invalid_input", "status": "rejected", "timestamp": "2026-11-09T04:31:42+00:00"}
{"creator_id": "unknown", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-09T04:31:42+00:00"}
{"creator_id": "attacker_flood", "event": "rejected", "limit": "5 per 1 minute", "reason": "rate_limited", "status": "rejected", "timestamp": "2026-11-09T04:31:42+00:00"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03, a non-native English speaker writing carefully about their first
month in a new country. It was labelled high-confidence AI (0.625), so they
were told their writing "shares strong patterns with AI-generated text." That
is the exact harm my Criterion 1 cites (Liang et al.): careful, simple
second-language writing reads as predictable to the model. MF07, a plain
sentence in Arabic, got the same label at 0.779.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing labelled AI | at most 1 of 10 | 2 | 2 | 2 | MISS |
| 2. Label coverage | each label at least 2 of 10 | AI 2, human 2, unsure 6 | AI 2, human 2, unsure 6 | AI 2, human 2, unsure 6 | PASS |
| 3. Bad input | 6 of 6 rejected with 400 and no label; 50 and 10,000 chars accepted | 6/6 rejected, both accepted | 6/6 rejected, both accepted | 6/6 rejected, both accepted | PASS |
| 4. Appeal path | 5 of 5 appeals recorded correctly; unknown id gets 404 and no appeal | 5/5, 404 | 5/5, 404 | 5/5, 404 | PASS |
| 5. Score spread | AI mean at least 0.30 above human mean; overlap at most 0.10 | gap 0.043, overlap 0.241 | gap 0.043, overlap 0.241 | gap 0.043, overlap 0.241 | MISS |

Criteria 1, 2, 3 and 5 come from `python run_eval.py --label before`
(`results/run_2026-11-08_2317_before.md`). Criterion 4 can't be sent as plain
text, since an appeal needs a content_id from an earlier submission, so I
wrote `run_appeals.py`. Each trial submits 5 texts, appeals each one, and
checks the log: the latest status is `under_review`, the reasoning is logged,
and the original decision entry hasn't changed. Then it appeals an id that
doesn't exist (`results/appeals_2026-11-08_2317_before.md`).

All three trials gave exactly the same scores. The model runs without random
sampling, so the same text always scores the same.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Criterion 1, trial 1, from `run_eval.py::main` against `app.py::submit`, in
`results/run_2026-11-08_2317_before.md`. The two AI labels are paragraph 1
(the runner, 0.686) and paragraph 6 (the water cycle, 0.6887).

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
    "sent": "I've been a runner for a long time. A few years ago, I found myself in"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4636,
    "model_score": 0.515,
    "style_score": 0.3438,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "I consider myself a quiet guy \u2014 on a Friday night you can usually find"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3563,
    "model_score": 0.3593,
    "style_score": 0.3494,
    "label": "This writing looks like it was written by a person.",
    "sent": "A Cornell University-led team that included Agricultural Research Serv"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5079,
    "model_score": 0.4847,
    "style_score": 0.5621,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "An instantaneous groundwater-level offset, or step, is a more commonly"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2787,
    "model_score": 0.3125,
    "style_score": 0.2,
    "label": "This writing looks like it was written by a person.",
    "sent": "You might imagine the bottom of the ocean\u2019s deepest point, seven miles"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6887,
    "model_score": 0.6839,
    "style_score": 0.6999,
    "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
    "sent": "The water cycle describes how water evaporates from the surface of the"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5625,
    "model_score": 0.601,
    "style_score": 0.4727,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "In the eight-week study, published last year in the American Journal o"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2894,
    "model_score": 0.1975,
    "style_score": 0.5037,
    "label": "This writing looks like it was written by a person.",
    "sent": "The arrival of the American system of measurement caused confusion and"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4565,
    "model_score": 0.4494,
    "style_score": 0.4731,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Restroom facilities are very limited throughout the park, especially a"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2681,
    "model_score": 0.3194,
    "style_score": 0.1483,
    "label": "This writing looks like it was written by a person.",
    "sent": "The most-eaten U.S. vegetable, phytonutrient-rich potatoes can have a "
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

The 20 broken attacks and 2 missed criteria come down to four problems, plus
two smaller ones in the route.

**1. Unusual tokens make AI text look human (signal one, then the combining
rule).** Broke: EV01, EV02, EV03, EV05, EV06, EV07, EV08, PI01, PI02, PI03,
PI05. All eleven are AI text that came back human. Signal one is perplexity,
and anything surprising raises it: typos (EV01, model score 0.07), a
"SYSTEM:" line in front (PI02, 0.09), a very short text (EV08, 10 words,
0.11), a heavy edit (EV05, 0.16). Higher perplexity reads as human. In EV01
and EV08 my style signal actually leaned AI (0.75 and 0.68), but the
combining rule weights the model at 0.7, so it got outvoted. The attack set
says EV01 targets signal two, but in my service the typos broke signal one.

**2. Plain, careful human writing looks AI to both signals (signals one and
two, then the label cutoff).** Broke: FP03, FP04, FP05, FP06, FP07. Missed:
Criterion 1 (paragraph 1, the runner, 0.686; paragraph 6, the water cycle,
0.689). Predictable wording raises the model score (0.61 to 0.74) and even
sentence lengths raise the style score, so both signals agree on the wrong
answer. My disagreement rule only helps when they disagree, so it never
kicks in. Every one of these lands between 0.61 and 0.69, just over my 0.60
AI cutoff. FP03 is the careful non-native writer my Criterion 1 warned about.

**3. Non-English and non-words get the highest AI scores (the route, then
both signals).** Broke: MF05 ("aaaa…", 0.92), MF06 (emoji, 0.92), MF07
(Arabic, 0.78). GPT-2 is an English model, and repeated tokens are extremely
predictable to it, so the model score hits 0.79 to 0.99. None of these has a
sentence break, so sentence-length spread is 0, which my style signal reads
as fully AI: that's why all three have a style score of exactly 0.75. The
route accepts them because they pass my length checks.

**4. The model signal barely separates human writing from modern AI (signal
one).** Missed: Criterion 5 (gap 0.043, overlap 0.241). My three Claude
paragraphs got model scores of 0.35, 0.51 and 0.64, inside the range of the
government paragraphs (0.20 to 0.69). GPT-2 doesn't find modern AI prose
more predictable than edited institutional writing, so the averages end up
0.50 and 0.55. The midpoint and cutoffs were set from four calibration texts,
and this is the first time they met new text.

**Criterion 2 passed, but partly by accident.** Its two AI labels are
paragraph 1 (a human paragraph, 0.686) and AI paragraph 3 (0.608), and one of
its human labels is a mixed text. Every label showed up, which is all the
criterion measures, but the labels themselves are often wrong.

**Route issues:**

- RQ10 and RQ11 got a 429 instead of a 400 (the route's rate-limit key).
  Requests with no usable creator_id fall back to my IP address in the
  5-a-minute per-creator limit, so they all share one bucket. Five earlier
  requests had already used it up.
- FP08 ("Went for a run. Legs hurt. Worth it.") got a 400 (the route's
  length check). My 50-character minimum from Criterion 3 blocks real short
  posts.

---

## The Improvement

**What I changed:** I replaced the model behind signal one. It was GPT-2
(2019). It's now Qwen2.5-0.5B (2024), a small open model that also runs on my
laptop (`DETECTOR_MODEL` in `config.py`). A new model gives different
perplexity numbers, so I re-set the midpoint (the perplexity that scores 0.5)
from 25 to 13 in `detector.py::model_signal`. I set it from the four
calibration texts only, the same way as before: halfway between the closest
human (23.0) and AI (7.5) perplexity. The cutoffs stayed at 0.40 and 0.60.

**Which diagnosis pointed at it:** Diagnosis 4. On my evaluation set, GPT-2
gave the human paragraphs and my AI paragraphs the same average model score
(0.51 and 0.50), so signal one carried no information. That also feeds
diagnoses 1 and 2: with no real separation, everything sat near the cutoffs.
A model trained on modern writing should find modern AI text more
predictable. On the calibration texts, the gap between human and AI
perplexity went from about 2x with GPT-2 to 3 to 5x with Qwen.

**What I tried first and rejected:** Raising the AI cutoff from 0.60 to 0.70
(diagnosis 2). It turned 5 false accusations into "unsure" and made
Criterion 1 pass, but no score changed, Criterion 2 failed because nothing
reached the AI label, and I had picked 0.70 by looking at where the failures
landed. It moved the errors around without making the detector better, so I
reverted it. Those runs are kept in `results/*_rejected-cutoff-0.70.md`.

### Attack Run — After

`python run_attacks.py --set . --label after`, full report in
`results/attack_run_2026-11-08_2330_after.md`.

| Family | Held before | Held after | Broke before | Broke after |
|---|---|---|---|---|
| evasion | 3 | 7 | 7 | 3 |
| false_positive | 2 | 5 | 6 | 3 |
| prompt_injection | 2 | 2 | 4 | 4 |
| malformed | 17 | 18 | 3 | 2 |
| flood_same_creator | 12 | 12 | 0 | 0 |
| **Total** | **36** | **44** | **20** | **12** |

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.406 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | human | 0.314 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.424 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.519 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.161 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | human | 0.310 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.450 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.403 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.507 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.815 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | human | 0.352 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.564 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.595 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.549 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.699 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.734 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | human | 0.381 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | — | — | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.375 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.114 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | human | 0.362 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | human | 0.188 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | human | 0.286 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | human | 0.317 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.905 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.904 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.422 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | human | 0.374 | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.365 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.365 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.365 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.365 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.365 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |

**Criteria after** (`results/run_2026-11-08_2330_after.md`,
`results/appeals_2026-11-08_2330_after.md`):

| Criterion | Before | After |
|---|---|---|
| 1. Human writing labelled AI (at most 1 of 10) | 2, MISS | 1, PASS |
| 2. Label coverage (each at least 2) | AI 2, human 2, unsure 6, PASS | AI 2, human 4, unsure 4, PASS |
| 3. Bad input | PASS | PASS |
| 4. Appeal path | PASS | PASS |
| 5. Score spread (gap at least 0.30, overlap at most 0.10) | gap 0.043, overlap 0.241, MISS | gap 0.224, overlap 0.003, MISS |

**Did it help, and how do I know:** Yes, more than I expected, but not
everywhere.

- Broken attacks went from 20 to 12. Four evasions (EV01, EV03, EV07, EV08)
  went from "human" to "unsure", three false positives stopped being accused
  (FP03, FP04 and FP07), FP01 moved from "unsure" to "human", and the Arabic
  text (MF07) went from 0.78 AI to 0.42 unsure.
- Criterion 2 still passes, and its two AI labels are now on two of my AI
  paragraphs. Before, one of them was a human paragraph.
- Criterion 5 is much closer. The gap went from 0.04 to 0.22 and the overlap
  from 0.24 to 0.003, but the gap target is 0.30, so it's still a miss.
- Criterion 1 passes, but only just: the water cycle paragraph is still
  labelled AI, now at 0.710.

What got worse or didn't move:

- FP05 and FP06 are still accused, and their scores went up (0.633 to 0.699,
  0.666 to 0.734). Technical documentation and template-style writing look
  even more predictable to a modern model.
- All four prompt-injection evasions and MF05/MF06 ("aaaa…", emoji) are
  unchanged. Unusual prefixes still raise perplexity, and repeated tokens are
  still very predictable to any model.
- The cost: a 1 GB download instead of 550 MB, and a bigger model per
  request.

The midpoint was still set from only four texts, and these results are on
the same evaluation set the diagnosis came from, so they're encouraging, not
proof.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
