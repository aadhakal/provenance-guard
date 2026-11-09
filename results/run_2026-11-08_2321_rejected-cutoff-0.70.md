# Run log — after

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-08 23:21

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. human reference writing |  |   |   |   |  |
| 2. label coverage |  |   |   |   |  |
| 3. bad input |  |   |   |   |  |
| 5. score spread |  |   |   |   |  |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### human reference writing

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.6887,
    "model_score": 0.6839,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.6887,
    "model_score": 0.6839,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.6887,
    "model_score": 0.6839,
    "style_score": 0.6999,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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

### label coverage

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3262,
    "model_score": 0.2163,
    "style_score": 0.5825,
    "label": "This writing looks like it was written by a person.",
    "sent": "The arrival of the American system of measurement caused confusion and"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4343,
    "model_score": 0.4212,
    "style_score": 0.4649,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "We had planned to spend the whole day in the park, but the notice made"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4989,
    "model_score": 0.5067,
    "style_score": 0.4806,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The water cycle describes how water evaporates from the surface of the"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3262,
    "model_score": 0.2163,
    "style_score": 0.5825,
    "label": "This writing looks like it was written by a person.",
    "sent": "The arrival of the American system of measurement caused confusion and"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4343,
    "model_score": 0.4212,
    "style_score": 0.4649,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "We had planned to spend the whole day in the park, but the notice made"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4989,
    "model_score": 0.5067,
    "style_score": 0.4806,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The water cycle describes how water evaporates from the surface of the"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3262,
    "model_score": 0.2163,
    "style_score": 0.5825,
    "label": "This writing looks like it was written by a person.",
    "sent": "The arrival of the American system of measurement caused confusion and"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4343,
    "model_score": 0.4212,
    "style_score": 0.4649,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "We had planned to spend the whole day in the park, but the notice made"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4989,
    "model_score": 0.5067,
    "style_score": 0.4806,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The water cycle describes how water evaporates from the surface of the"
  }
]
```

### bad input

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4059,
    "model_score": 0.1241,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The bus came late again, so I walked home instead."
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9195,
    "model_score": 0.9922,
    "style_score": 0.75,
    "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4059,
    "model_score": 0.1241,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The bus came late again, so I walked home instead."
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9195,
    "model_score": 0.9922,
    "style_score": 0.75,
    "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \n\t  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 42, \"creator_id\": \"eval_bad_number\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4059,
    "model_score": 0.1241,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "The bus came late again, so I walked home instead."
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9195,
    "model_score": 0.9922,
    "style_score": 0.75,
    "label": "This writing shares strong patterns with AI-generated text. This is an automated estimate, not proof, and it can be wrong. A person will review it before any decision is made, and if you wrote it yourself, you can appeal.",
    "sent": "The bus came late again, so I walked home instead. The bus came late a"
  }
]
```

### score spread

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.686,
    "model_score": 0.69,
    "style_score": 0.6768,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
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
    "guess": "unsure",
    "confidence": 0.4454,
    "model_score": 0.3511,
    "style_score": 0.6655,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Tree rings offer scientists a detailed record of past climate conditio"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5851,
    "model_score": 0.5144,
    "style_score": 0.75,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "Urban heat islands form when cities replace natural land cover with pa"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.608,
    "model_score": 0.6372,
    "style_score": 0.54,
    "label": "We can't tell whether this was written by a person or with help from AI. That happens often, and it doesn't mean anyone did anything wrong. No action will be taken based on this result.",
    "sent": "When I first started gardening, I assumed it would be a relaxing way t"
  }
]
```
