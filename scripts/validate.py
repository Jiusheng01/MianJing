from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
qs = json.loads((root / "data/questions.json").read_text(encoding="utf-8"))
sources = json.loads((root / "data/sources.json").read_text(encoding="utf-8"))
source_ids = {s["id"] for s in sources}

assert len(qs) == 120, "question count mismatch"
assert len(sources) == 35, "source count mismatch"
assert len(source_ids) == len(sources), "duplicate source IDs"
assert len({q["id"] for q in qs}) == len(qs), "duplicate question IDs"
assert len({q["question"] for q in qs}) == len(qs), "duplicate question texts"
assert all(q["sources"] and set(q["sources"]) <= source_ids for q in qs), "orphan source ID"
assert all(s["url"].startswith("https://") for s in sources), "invalid source URL"
print(f'OK: {len(qs)} questions, {len(sources)} entries, {len(set(s["url"] for s in sources))} unique URLs')
