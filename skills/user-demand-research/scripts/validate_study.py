#!/usr/bin/env python3
"""Validate a minimum SURE user-demand research study."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List


CONTRACT_FIELDS = {
    "decision",
    "target_users",
    "markets",
    "time_window",
    "allowed_sources",
    "prohibited_inferences",
    "stopping_rules",
}
EVIDENCE_FIELDS = {
    "id",
    "user_role",
    "scene_trigger",
    "task_outcome",
    "current_substitute",
    "friction_cost",
    "consequence",
    "evidence_level",
    "source_ref",
}
CARD_FIELDS = {
    "id",
    "opportunity",
    "target_user",
    "scene",
    "problem_evidence_ids",
    "solution_evidence_ids",
    "commercial_evidence_ids",
    "counter_evidence_ids",
    "status",
    "confidence",
    "gaps",
    "next_test",
}
LEVELS = {"E0", "E1", "E2", "E3", "E4+", "E4-", "E5"}


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    records = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        value = json.loads(line)
        if not isinstance(value, dict):
            raise ValueError(f"evidence line {line_number} must be an object")
        records.append(value)
    return records


def _missing(value: Dict[str, Any], required: Iterable[str]) -> List[str]:
    return sorted(field for field in required if field not in value or value[field] in (None, ""))


def validate_study(root: Path) -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []
    paths = {
        "contract": root / "research-contract.json",
        "evidence": root / "evidence.jsonl",
        "cards": root / "opportunity-cards.json",
    }
    missing_files = [name for name, path in paths.items() if not path.is_file()]
    if missing_files:
        return {
            "status": "fail",
            "study_dir": str(root),
            "checks": [{"id": "files", "status": "fail", "detail": ", ".join(missing_files)}],
        }

    contract = _load_json(paths["contract"])
    evidence = _load_jsonl(paths["evidence"])
    cards = _load_json(paths["cards"])
    contract_missing = _missing(contract, CONTRACT_FIELDS) if isinstance(contract, dict) else ["object"]
    checks.append(
        {
            "id": "research_contract",
            "status": "pass" if not contract_missing else "fail",
            "detail": "" if not contract_missing else "missing: " + ", ".join(contract_missing),
        }
    )

    evidence_errors: List[str] = []
    evidence_by_id: Dict[str, Dict[str, Any]] = {}
    for index, record in enumerate(evidence, start=1):
        missing = _missing(record, EVIDENCE_FIELDS)
        if missing:
            evidence_errors.append(f"record {index} missing {', '.join(missing)}")
            continue
        record_id = str(record["id"])
        if record_id in evidence_by_id:
            evidence_errors.append(f"duplicate evidence id {record_id}")
        if str(record["evidence_level"]) not in LEVELS:
            evidence_errors.append(f"{record_id} has invalid evidence level")
        evidence_by_id[record_id] = record
    checks.append(
        {
            "id": "evidence_records",
            "status": "pass" if evidence and not evidence_errors else "fail",
            "detail": "; ".join(evidence_errors) if evidence_errors else f"{len(evidence)} records",
        }
    )

    if not isinstance(cards, list):
        cards = []
    card_errors: List[str] = []
    for index, card in enumerate(cards, start=1):
        if not isinstance(card, dict):
            card_errors.append(f"card {index} is not an object")
            continue
        card_id = str(card.get("id") or index)
        missing = _missing(card, CARD_FIELDS)
        if missing:
            card_errors.append(f"{card_id} missing {', '.join(missing)}")
            continue
        if card["confidence"] not in {"low", "medium", "high"}:
            card_errors.append(f"{card_id} has invalid confidence")
        chains = {
            "problem": (card["problem_evidence_ids"], {"E1", "E2"}),
            "solution": (card["solution_evidence_ids"], {"E3"}),
            "commercial": (card["commercial_evidence_ids"], {"E4+", "E5"}),
        }
        all_ids = []
        for ids in (
            card["problem_evidence_ids"],
            card["solution_evidence_ids"],
            card["commercial_evidence_ids"],
            card["counter_evidence_ids"],
        ):
            all_ids.extend(str(value) for value in ids)
        unknown_ids = sorted(set(all_ids) - evidence_by_id.keys())
        if unknown_ids:
            card_errors.append(f"{card_id} references unknown evidence: {', '.join(unknown_ids)}")
        if card["status"] == "validated":
            for chain_name, (ids, accepted_levels) in chains.items():
                levels = {
                    str(evidence_by_id[str(value)]["evidence_level"])
                    for value in ids
                    if str(value) in evidence_by_id
                }
                if not levels.intersection(accepted_levels):
                    card_errors.append(f"{card_id} lacks {chain_name} evidence for validated status")
    checks.append(
        {
            "id": "opportunity_cards",
            "status": "pass" if cards and not card_errors else "fail",
            "detail": "; ".join(card_errors) if card_errors else f"{len(cards)} cards",
        }
    )

    failed = [check for check in checks if check["status"] == "fail"]
    return {
        "status": "pass" if not failed else "fail",
        "study_dir": str(root),
        "evidence_count": len(evidence),
        "opportunity_count": len(cards),
        "checks": checks,
    }


def main(argv: List[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_study.py STUDY_DIR", file=sys.stderr)
        return 2
    result = validate_study(Path(argv[1]).resolve())
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
