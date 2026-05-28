"""Show the actual fingerprints the eval runner will look for."""
import json, re, yaml
from pathlib import Path

prompts_dir = Path("prompts")
for p in sorted(prompts_dir.iterdir()):
    rubric = p / "rubric.yaml"
    if not rubric.exists():
        continue
    data = yaml.safe_load(rubric.read_text(encoding="utf-8"))
    for tc in data.get("test_cases", []):
        inp = tc.get("input", "")
        if isinstance(inp, str):
            inp = {"input": inp}
        s = json.dumps(inp, sort_keys=True)
        fp = re.sub(r'\W+', '_', s)[:60]
        print(f"{p.name:30s} | {fp}.txt")
