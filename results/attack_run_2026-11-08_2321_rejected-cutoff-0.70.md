# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 23:21
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `4ca1a4b9-dc35-4976-b464-4d03d3ac9ae4` | human | 0.387 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `2018c3ed-2ef3-400b-9b71-dabd60d4e809` | human | 0.255 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `b83d77aa-f989-4479-8760-85bcf5ff1b95` | human | 0.400 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `59e1214c-c227-4667-b9fc-03011b0e1320` | unsure | 0.491 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `7801a361-1ce4-4918-9e45-34015711eef4` | human | 0.170 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b5f27297-56e8-4a77-ad1b-c2561d22907d` | human | 0.316 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `46f4361b-db87-4abf-b0f5-0c163f0b973f` | human | 0.399 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `c6de4299-2312-4283-b312-3ba5b2b7ec59` | human | 0.392 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3898cbd4-d03d-47ed-a4a1-560aa9928638` | unsure | 0.495 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `abf69ce0-5503-4a63-abbe-9e95be91e320` | ai | 0.840 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `65ae6ace-768c-4f64-817e-8dda07c9f548` | unsure | 0.431 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c62ec4ec-9fae-4e22-86e9-585cf909fef3` | unsure | 0.582 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `df6f93e4-54b1-4d27-8bcb-7ba32ecfb92b` | unsure | 0.625 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `55bb0192-a2c6-44c2-a6f3-14bc30722c6a` | unsure | 0.646 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `04e4dc4e-6b92-4cd0-9020-737002705a2a` | unsure | 0.633 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `487ef893-5986-4b18-adf1-6a7cec7136fb` | unsure | 0.666 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `cd93ce12-7825-4b6b-98a4-42d18c5d304e` | unsure | 0.613 | HELD |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — | BROKE |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0827d492-7ab2-47d1-8218-254c5f36b165` | human | 0.285 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `a6912b24-ee67-4cb6-af7f-fce72188023d` | human | 0.101 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d333a000-c842-42ca-9f0c-a11a7a81463c` | human | 0.369 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `989eebe5-1c24-44ca-8878-a8a0d7ecc974` | human | 0.297 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `7b46ec5c-2db0-4ba1-a049-b6985f7b97de` | human | 0.369 | BROKE |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cb6374a4-1097-4bb3-b9d3-9b2ef35b5816` | human | 0.395 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 200 | `3eb46b24-e049-466f-98fd-1f489b0f6a5d` | ai | 0.921 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `c6f0bb85-083f-4869-9f3b-85804752af18` | ai | 0.919 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `9eee2551-39b7-4fdc-b08b-1e75c1f896a6` | ai | 0.779 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `e9e040bf-bba8-497e-ae49-09e578a7c71a` | unsure | 0.401 | HELD |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a08a158c-454d-44be-8afb-09526c693ed3` | human | 0.366 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `df8fdcfd-cb38-447e-8b1d-80a7d87454f0` | human | 0.366 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5e9d447a-0312-4b98-94de-11cee4f318b8` | human | 0.366 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `04a1ee2b-3d83-41fb-b9d2-ab2219037da9` | human | 0.366 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `385648fe-6e06-401d-a972-5f37900484cc` | human | 0.366 | HELD |
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
  "content_id": "4ca1a4b9-dc35-4976-b464-4d03d3ac9ae4",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3873,
  "model_score": 0.0709,
  "style_score": 0.75,
  "label": "This writing looks like it was written by a person.",
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
  "content_id": "2018c3ed-2ef3-400b-9b71-dabd60d4e809",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.2547,
  "model_score": 0.3638,
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
  "content_id": "b83d77aa-f989-4479-8760-85bcf5ff1b95",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.4,
  "model_score": 0.438,
  "style_score": 0.3113,
  "label": "This writing looks like it was written by a person.",
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
  "content_id": "59e1214c-c227-4667-b9fc-03011b0e1320",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4914,
  "model_score": 0.3806,
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
  "content_id": "7801a361-1ce4-4918-9e45-34015711eef4",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.1696,
  "model_score": 0.1559,
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
  "content_id": "b5f27297-56e8-4a77-ad1b-c2561d22907d",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3155,
  "model_score": 0.3435,
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
  "content_id": "46f4361b-db87-4abf-b0f5-0c163f0b973f",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.3993,
  "model_score": 0.3561,
  "style_score": 0.5,
  "label": "This writing looks like it was written by a person.",
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
  "content_id": "c6de4299-2312-4283-b312-3ba5b2b7ec59",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3915,
  "model_score": 0.1125,
  "style_score": 0.681,
  "label": "This writing looks like it was written by a person.",
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
  "content_id": "3898cbd4-d03d-47ed-a4a1-560aa9928638",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4954,
  "model_score": 0.4818,
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
  "content_id": "abf69ce0-5503-4a63-abbe-9e95be91e320",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8403,
  "model_score": 0.9483,
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
  "content_id": "65ae6ace-768c-4f64-817e-8dda07c9f548",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4313,
  "model_score": 0.3867,
  "style_score": 0.5354,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
  "content_id": "c62ec4ec-9fae-4e22-86e9-585cf909fef3",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.5822,
  "model_score": 0.5247,
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
  "content_id": "df6f93e4-54b1-4d27-8bcb-7ba32ecfb92b",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6251,
  "model_score": 0.6173,
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
  "content_id": "55bb0192-a2c6-44c2-a6f3-14bc30722c6a",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.6457,
  "model_score": 0.6606,
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
  "content_id": "04e4dc4e-6b92-4cd0-9020-737002705a2a",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6331,
  "model_score": 0.6104,
  "style_score": 0.6859,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
  "content_id": "487ef893-5986-4b18-adf1-6a7cec7136fb",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6659,
  "model_score": 0.7438,
  "style_score": 0.484,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
  "content_id": "cd93ce12-7825-4b6b-98a4-42d18c5d304e",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6131,
  "model_score": 0.7441,
  "style_score": 0.3076,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
  "content_id": "0827d492-7ab2-47d1-8218-254c5f36b165",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2854,
  "model_score": 0.2515,
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
  "content_id": "a6912b24-ee67-4cb6-af7f-fce72188023d",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1009,
  "model_score": 0.0912,
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
  "content_id": "d333a000-c842-42ca-9f0c-a11a7a81463c",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.3689,
  "model_score": 0.3638,
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
  "content_id": "989eebe5-1c24-44ca-8878-a8a0d7ecc974",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.2973,
  "model_score": 0.2807,
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
  "content_id": "7b46ec5c-2db0-4ba1-a049-b6985f7b97de",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3691,
  "model_score": 0.4099,
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
  "content_id": "cb6374a4-1097-4bb3-b9d3-9b2ef35b5816",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.3949,
  "model_score": 0.3304,
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
  "content_id": "3eb46b24-e049-466f-98fd-1f489b0f6a5d",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9207,
  "model_score": 0.9939,
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
  "content_id": "c6f0bb85-083f-4869-9f3b-85804752af18",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9195,
  "model_score": 0.9921,
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
  "content_id": "9eee2551-39b7-4fdc-b08b-1e75c1f896a6",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7786,
  "model_score": 0.7908,
  "style_score": 0.75,
  "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
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
  "content_id": "e9e040bf-bba8-497e-ae49-09e578a7c71a",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4008,
  "model_score": 0.1095,
  "style_score": 0.75,
  "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
  "content_id": "a08a158c-454d-44be-8afb-09526c693ed3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3665,
  "model_score": 0.0114,
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
  "content_id": "df8fdcfd-cb38-447e-8b1d-80a7d87454f0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3665,
  "model_score": 0.0114,
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
  "content_id": "5e9d447a-0312-4b98-94de-11cee4f318b8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3665,
  "model_score": 0.0114,
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
  "content_id": "04a1ee2b-3d83-41fb-b9d2-ab2219037da9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3665,
  "model_score": 0.0114,
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
  "content_id": "385648fe-6e06-401d-a972-5f37900484cc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3665,
  "model_score": 0.0114,
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
