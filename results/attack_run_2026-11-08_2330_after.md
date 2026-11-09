# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 23:30
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `235e1b9f-ced0-4078-a1e8-6ecb9004eb88` | unsure | 0.406 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `a8df1951-8fbe-4db6-b262-c9b8fa7d53cc` | human | 0.314 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `86efbf47-d21c-4337-bf77-d67f96744eee` | unsure | 0.424 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3fe3ee2a-225e-4d0a-8014-e805b6dca75d` | unsure | 0.519 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bc439654-2cc2-4f3d-a92e-f1cf4c10a3f8` | human | 0.161 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `cb1f7d80-0417-45a0-becc-04cdbb1084a9` | human | 0.310 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d7f533cf-d588-48cc-bbf4-0f771b99ba26` | unsure | 0.450 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `ce60575c-fada-4106-be37-a5f6aec854e4` | unsure | 0.403 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `852b6e5f-04e0-4b24-b140-3aff5972c3d8` | unsure | 0.507 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `ea82785a-f78a-4d0f-b85c-7226127950b6` | ai | 0.815 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `94965773-94c4-40c0-8fce-51add352ce4c` | human | 0.352 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `3ab044a8-5fa0-4d79-99a5-b9e73953e86a` | unsure | 0.564 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e04d09b8-d11f-456c-b5d3-4daf211f8e64` | unsure | 0.595 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `ba5a80c0-d29c-4f35-89ce-5c235e1e4616` | unsure | 0.549 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `e6ecef82-c190-43f9-8250-d080152feb74` | ai | 0.699 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `343366b4-20ab-4cc8-a48a-56bf47b3b259` | ai | 0.734 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `9a8041d5-d792-44a2-a2f7-ecaa9790ad2e` | human | 0.381 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `1ba1146e-1dd0-4ba3-b185-c5f019134db8` | human | 0.375 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `973372ed-2027-4981-ac19-f968b1c1a382` | human | 0.114 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d3cae9b7-cc0a-4d3a-8efe-5a650bacb18e` | human | 0.362 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c9860197-e4f6-42b2-86bf-84c645e57dd1` | human | 0.188 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `daa31e25-fbdb-4df4-aa48-8b128c516415` | human | 0.286 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | `361a4bb3-566b-4d48-badd-d22aceea382c` | human | 0.317 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | `21e1e9d1-f270-4686-8c97-b345db1d17f4` | ai | 0.905 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `aaeba4da-a9ed-45a1-8ae2-8fe72681c660` | ai | 0.904 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `e19f4938-5425-4841-b246-d0cf06902a6b` | unsure | 0.422 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `4ff6b8f1-a6d9-44b5-92cd-16d813d0338b` | human | 0.374 | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `407042e6-d70d-41f0-ae87-ca851c6b877a` | human | 0.365 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66b7d4f6-1883-4205-a76d-75981d4f0e43` | human | 0.365 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ae623641-7f6e-4d26-b8aa-6997bb4a6df1` | human | 0.365 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5a5e906a-f6bd-4147-af54-0ab1fb2e9247` | human | 0.365 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b4acb7ab-ec68-484f-a05c-e7a52ef196c5` | human | 0.365 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "235e1b9f-ced0-4078-a1e8-6ecb9004eb88",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4061,
  "model_score": 0.1247,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "a8df1951-8fbe-4db6-b262-c9b8fa7d53cc",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3142,
  "model_score": 0.4488,
  "style_score": 0.0,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "86efbf47-d21c-4337-bf77-d67f96744eee",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4237,
  "model_score": 0.4719,
  "style_score": 0.3113,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "3fe3ee2a-225e-4d0a-8014-e805b6dca75d",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5189,
  "model_score": 0.4198,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bc439654-2cc2-4f3d-a92e-f1cf4c10a3f8",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.1605,
  "model_score": 0.1429,
  "style_score": 0.2015,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "cb1f7d80-0417-45a0-becc-04cdbb1084a9",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3104,
  "model_score": 0.3363,
  "style_score": 0.25,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d7f533cf-d588-48cc-bbf4-0f771b99ba26",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4495,
  "model_score": 0.4278,
  "style_score": 0.5,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "ce60575c-fada-4106-be37-a5f6aec854e4",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4025,
  "model_score": 0.1438,
  "style_score": 0.681,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "852b6e5f-04e0-4b24-b140-3aff5972c3d8",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5068,
  "model_score": 0.4981,
  "style_score": 0.5271,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "ea82785a-f78a-4d0f-b85c-7226127950b6",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8153,
  "model_score": 0.9125,
  "style_score": 0.5884,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "94965773-94c4-40c0-8fce-51add352ce4c",
  "creator_id": "attacker_FP01",
  "guess": "human",
  "confidence": 0.3519,
  "model_score": 0.2733,
  "style_score": 0.5354,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "3ab044a8-5fa0-4d79-99a5-b9e73953e86a",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5636,
  "model_score": 0.4981,
  "style_score": 0.7164,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "e04d09b8-d11f-456c-b5d3-4daf211f8e64",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5948,
  "model_score": 0.5741,
  "style_score": 0.6432,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "ba5a80c0-d29c-4f35-89ce-5c235e1e4616",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5491,
  "model_score": 0.5226,
  "style_score": 0.6111,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "e6ecef82-c190-43f9-8250-d080152feb74",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6986,
  "model_score": 0.704,
  "style_score": 0.6859,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "343366b4-20ab-4cc8-a48a-56bf47b3b259",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7338,
  "model_score": 0.8408,
  "style_score": 0.484,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "9a8041d5-d792-44a2-a2f7-ecaa9790ad2e",
  "creator_id": "attacker_FP07",
  "guess": "human",
  "confidence": 0.3805,
  "model_score": 0.4117,
  "style_score": 0.3076,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "1ba1146e-1dd0-4ba3-b185-c5f019134db8",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3749,
  "model_score": 0.3794,
  "style_score": 0.3645,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "973372ed-2027-4981-ac19-f968b1c1a382",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1136,
  "model_score": 0.1093,
  "style_score": 0.1235,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "d3cae9b7-cc0a-4d3a-8efe-5a650bacb18e",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.3625,
  "model_score": 0.3546,
  "style_score": 0.3808,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c9860197-e4f6-42b2-86bf-84c645e57dd1",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.1878,
  "model_score": 0.1242,
  "style_score": 0.3361,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "daa31e25-fbdb-4df4-aa48-8b128c516415",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.2859,
  "model_score": 0.2911,
  "style_score": 0.2738,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "361a4bb3-566b-4d48-badd-d22aceea382c",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.317,
  "model_score": 0.2191,
  "style_score": 0.5455,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "21e1e9d1-f270-4686-8c97-b345db1d17f4",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9051,
  "model_score": 0.9716,
  "style_score": 0.75,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "aaeba4da-a9ed-45a1-8ae2-8fe72681c660",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9044,
  "model_score": 0.9706,
  "style_score": 0.75,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "e19f4938-5425-4841-b246-d0cf06902a6b",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.4219,
  "model_score": 0.2813,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "4ff6b8f1-a6d9-44b5-92cd-16d813d0338b",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.3742,
  "model_score": 0.0334,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "407042e6-d70d-41f0-ae87-ca851c6b877a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3647,
  "model_score": 0.0062,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "66b7d4f6-1883-4205-a76d-75981d4f0e43",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3647,
  "model_score": 0.0062,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "ae623641-7f6e-4d26-b8aa-6997bb4a6df1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3647,
  "model_score": 0.0062,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "5a5e906a-f6bd-4147-af54-0ab1fb2e9247",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3647,
  "model_score": 0.0062,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "b4acb7ab-ec68-484f-a05c-e7a52ef196c5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3647,
  "model_score": 0.0062,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
