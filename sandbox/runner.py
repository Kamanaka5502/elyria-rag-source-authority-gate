from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from elyria_rag_source_gate import evaluate_rag_source

EXAMPLES = ROOT / "examples"
OUTPUTS = ROOT / "sandbox" / "outputs"


def main():
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(EXAMPLES.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        decision = evaluate_rag_source(data)
        rows.append({
            "file": path.name,
            "scenario": data.get("scenario"),
            "expected": data.get("expected_outcome"),
            "actual": decision["outcome"],
            "reasons": decision["reason_codes"],
            "remediation": decision["required_remediation"],
        })
    out = OUTPUTS / "sandbox-results.json"
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
