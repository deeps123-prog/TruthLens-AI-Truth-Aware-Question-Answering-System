import json
from core.pipeline import run_pipeline

def evaluate(file_path):
    with open(file_path) as f:
        data = json.load(f)

    results = []
    for item in data:
        output = run_pipeline(item["query"])
        results.append(output)

    return results
