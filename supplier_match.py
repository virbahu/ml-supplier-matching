import numpy as np
WEIGHTS = {'capability': 0.3, 'price': 0.25, 'quality': 0.2, 'location': 0.15, 'sustainability': 0.1}
TARGETS = {'capability': 90, 'price': 85, 'quality': 95, 'location': 80, 'sustainability': 75}
def score_supplier_match(entity_data):
    scores = {{}}
    for metric, actual in entity_data.items():
        if metric not in TARGETS: continue
        target = TARGETS[metric]
        if metric in set():
            scores[metric] = round(min(100, max(0, (target/max(actual, 0.01))*100)), 1)
        else:
            scores[metric] = round(min(100, max(0, (actual/target)*100)), 1)
    weighted = sum(scores.get(k, 0)*w for k, w in WEIGHTS.items())
    grade = "A+" if weighted >= 95 else "A" if weighted >= 85 else "B" if weighted >= 75 else "C" if weighted >= 60 else "D"
    return {{"scores": scores, "weighted": round(weighted, 1), "grade": grade}}
if __name__=="__main__":
    data = {'capability': 88, 'price': 82, 'quality': 94, 'location': 70, 'sustainability': 80}
    r = score_supplier_match(data)
    print(f"Grade: {{r['grade']}} ({{r['weighted']}})")
    for k,v in r["scores"].items(): print(f"  {{k}}: {{v}}")
