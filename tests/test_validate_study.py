from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "skills/user-demand-research/scripts/validate_study.py"
SAMPLE = ROOT / "examples/sample-study"


class ValidateStudyTests(unittest.TestCase):
    def test_sample_study_passes(self) -> None:
        completed = subprocess.run(
            ["python3", str(VALIDATOR), str(SAMPLE)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertEqual("pass", json.loads(completed.stdout)["status"])

    def test_validated_card_without_commercial_evidence_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source in SAMPLE.iterdir():
                (target / source.name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
            cards = json.loads((target / "opportunity-cards.json").read_text(encoding="utf-8"))
            cards[0]["commercial_evidence_ids"] = []
            (target / "opportunity-cards.json").write_text(json.dumps(cards), encoding="utf-8")
            completed = subprocess.run(
                ["python3", str(VALIDATOR), str(target)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(1, completed.returncode)
        self.assertIn("lacks commercial evidence", completed.stdout)


if __name__ == "__main__":
    unittest.main()
