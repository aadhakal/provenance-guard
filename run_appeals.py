#!/usr/bin/env python3
"""
Criterion 4, the appeal path, three trials.

    python app.py                              # in one terminal
    python run_appeals.py --label before       # in another

run_eval.py only sends text, and an appeal needs a content_id from an earlier
submission, so this does it separately. Each trial submits 5 texts, appeals
each one, and checks the log. Then it appeals an id that doesn't exist.
"""

import argparse
import datetime as dt
import json

import requests

import audit
import config
import scenarios

URL = f"http://{config.HOST}:{config.PORT}"
APPEALS_PER_TRIAL = 5


def check_appeal(text: str, creator_id: str) -> dict:
    """Submit, appeal, and check what criterion 4 asks for."""
    submitted = requests.post(f"{URL}/submit", json={"text": text, "creator_id": creator_id}).json()
    content_id = submitted["content_id"]
    decision_before = audit.entries_for(content_id)[0]

    reasoning = f"I wrote this myself ({creator_id})."
    response = requests.post(f"{URL}/appeal", json={"content_id": content_id, "reasoning": reasoning})

    entries = audit.entries_for(content_id)
    appeals = [e for e in entries if e.get("event") == "appeal"]
    return {
        "content_id": content_id,
        "status_code": response.status_code,
        "latest_status": entries[-1].get("status"),
        "reasoning_logged": any(e.get("reasoning") == reasoning for e in appeals),
        "decision_unchanged": entries[0] == decision_before,
    }


def check_unknown_id() -> dict:
    """An id that was never issued: 404 and no appeal entry."""
    content_id = f"does-not-exist-{dt.datetime.now().timestamp()}"
    response = requests.post(f"{URL}/appeal", json={"content_id": content_id, "reasoning": "test"})
    appeals = [e for e in audit.entries_for(content_id) if e.get("event") == "appeal"]
    return {"status_code": response.status_code, "appeal_entries": len(appeals)}


def passed(appeal: dict) -> bool:
    return (appeal["status_code"] == 200 and appeal["latest_status"] == "under_review"
            and appeal["reasoning_logged"] and appeal["decision_unchanged"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    args = parser.parse_args()

    texts = scenarios.HUMAN_REFERENCE[:APPEALS_PER_TRIAL]
    trials = []
    for trial in range(1, args.trials + 1):
        appeals = [check_appeal(text, f"eval_appeal_t{trial}_{i}") for i, text in enumerate(texts, 1)]
        unknown = check_unknown_id()
        ok = all(passed(a) for a in appeals) and unknown == {"status_code": 404, "appeal_entries": 0}
        trials.append({"appeals": appeals, "unknown_id": unknown, "pass": ok})
        print(f"  trial {trial}: {sum(passed(a) for a in appeals)}/{len(appeals)} appeals ok, "
              f"unknown id -> {unknown['status_code']}, {'PASS' if ok else 'MISS'}")

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = ["# Criterion 4: appeal path" + (f" ({args.label})" if args.label else ""), "",
             "- Produced by: `run_appeals.py::main`", ""]
    for n, trial in enumerate(trials, 1):
        lines += [f"**Trial {n}: {'PASS' if trial['pass'] else 'MISS'}**", "", "```json",
                  json.dumps(trial, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
