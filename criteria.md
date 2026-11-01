# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Across each of three trials of ten human-written paragraphs published before
2022 (U.S. government public-domain sources, listed in
`human_reference_sources.md`), at most one paragraph may receive a
high-confidence AI label.



**Why this target:**

This permits at most a 10% false-positive rate in my small evaluation set.
That is still too high for an automatic penalty, so a high-confidence AI
result in this system must lead to human review and an appeal option, not
punishment. In a study of five detectors on authentic student work, false
positive rates ranged from 9.8% to 45.8%; even a two-detector combination had
a 5.2% false-positive rate, which the authors concluded was still too high to
use alone ([Paustian and Slinger, 2024](https://doi.org/10.3389/feduc.2024.1374889)).
I used public-domain U.S. government writing from 2014 to 2020 because it is
human-written, predates widely available generative AI, and can be shared in
this repository. It is edited institutional prose, not student writing, so a
pass here does not guarantee the same rate on student work.
Another study found that seven detectors unanimously classified 19.8% of
human-written TOEFL essays as AI-generated, showing a particular risk for
second-language writing ([Liang et al., 2023](https://doi.org/10.1016/j.patter.2023.100779)).
A result above this limit means the service is too likely to make harmful
accusations and needs adjustment.


---

## 2.

Using a fixed set of ten paragraphs committed before testing (4 human
paragraphs from Criterion 1, 3 unedited AI output, 3 mixed human/AI), each of
the three labels
(high-confidence human, unsure, high-confidence AI) must appear at least twice
in every one of three trials.



**Why this target:**

I want to check that all three labels work when real text goes through the
whole service. If everything comes back unsure, the service avoids making
useful distinctions. If nothing comes back unsure, it may be forcing decisions
when the evidence is weak. Requiring every label in each trial helps me catch
problems in the signals, the combining rule, or the label thresholds. I require
each label twice so its coverage does not depend on a single paragraph.

This tests whether the labels are reachable, not whether they are correct;
correctness is measured separately. The paragraphs are chosen and committed
before testing so I can't swap inputs just to make the criterion pass.


---

## 3.

In each of three trials, the service must reject all six invalid requests:
missing `text`, empty text, whitespace-only text, a number instead of text,
text under 50 characters after trimming whitespace, and text containing 10,001
characters. Each must return HTTP 400 with an error message and no authorship
label. Text of exactly 50 and exactly 10,000 characters must be accepted and
labelled.



**Why this target:**

A missing field or a number should produce an error instead of crashing the
service. Empty text should never receive an authorship label. I chose a
50-character minimum to avoid classifying tiny fragments that give the signals
little evidence. I chose 10,000 characters as the maximum request length for
this prototype. I will test both sides of each limit (49 and 50 characters,
10,000 and 10,001 characters), so a service that rejected everything could not
pass.

*Note:* the 10,000-character limit is a request limit only. The detector
reads just the first 400 tokens (`DETECTOR_MAX_TOKENS` in `config.py`), so
accepting a long submission does not mean evaluating all of it.



---

## 4.

Across each of three trials, every appeal on an existing decision (5 per
trial) must return success and appear in the audit log with the writer's
reasoning. The latest recorded status for that content ID must be
`under_review`, while the original decision entry stays unchanged. Appeals for
an unknown content ID must return HTTP 404 and create no appeal entry.



**Why this target:**

Criterion 1 accepts up to one false accusation in ten only because a
high-confidence AI label leads to human review and an appeal, not punishment.
If an appeal can be lost, ignored, or overwrite the original decision, that
safeguard doesn't exist. The appeal path is my own code with no model
involved, so I expect every appeal to work.



---

## 5.

Using the paragraph set from Criterion 2, across each of three trials, the
average combined score of the 4 human paragraphs must be at least 0.30 lower
than the average of the 3 unedited AI paragraphs, and the highest-scoring
human paragraph may exceed the lowest-scoring AI paragraph by at most 0.10.



**Why this target:**

Criterion 1 limits false accusations and Criterion 2 shows each label is
reachable, but neither shows the scores actually separate human from AI
writing. A service could pass both while scoring everything near the middle.
I chose a 0.30 average gap because I want a noticeable separation on a score
scale from zero to one. This is my target for the prototype; it is not a
research-established cutoff. The second
condition stops one strong group average from hiding heavy overlap between
individual paragraphs. The mixed paragraphs are left out because there is no
single right score for them.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
