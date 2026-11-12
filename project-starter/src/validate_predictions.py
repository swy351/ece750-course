"""Binary-output format and coverage checks only: no outcomes, no grading.
CLI: python src/validate_predictions.py predictions.csv ids.csv methods.csv
IDs CSV: id. Methods CSV: method,run_id. Predictions: id,method,run_id,prediction,score.
This starter's run_id contract supports repeated trials; other announced schemas may differ.
"""
import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path


def read_table(path, columns):
    with Path(path).open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != columns:
            raise ValueError(f'{path}: expected exact ordered columns {columns}')
        rows = list(reader)
    if not rows:
        raise ValueError(f'{path}: no records; a header-only starter is not complete')
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError(f'{path}: malformed row width')
    return rows


def validate(predictions, ids_file, methods_file):
    ids = [r['id'] for r in read_table(ids_file, ['id'])]
    methods = [(r['method'], r['run_id']) for r in read_table(methods_file, ['method', 'run_id'])]
    if any(not x.strip() or x != x.strip() for x in ids) or len(ids) != len(set(ids)):
        raise ValueError('Evaluation IDs must be nonblank, unique and free of surrounding whitespace')
    if any(not x.strip() or x != x.strip() for pair in methods for x in pair) or len(methods) != len(set(methods)):
        raise ValueError('Expected method/run pairs must be nonblank and unique')
    rows = read_table(predictions, ['id', 'method', 'run_id', 'prediction', 'score'])
    expected = {(i, m, r) for i in ids for m, r in methods}
    actual = [(x['id'], x['method'], x['run_id']) for x in rows]
    if len(actual) != len(set(actual)):
        raise ValueError('Duplicate id/method/run records')
    missing, extra = expected - set(actual), set(actual) - expected
    if missing or extra:
        raise ValueError(f'Coverage mismatch: {len(missing)} missing, {len(extra)} unexpected records')
    for row in rows:
        label, score = row['prediction'], row['score']
        if label not in {'0', '1', 'ABSTAIN'}:
            raise ValueError('prediction must be literal 0, 1 or ABSTAIN')
        if score == '':
            if label != 'ABSTAIN':
                raise ValueError('Only explicit abstentions may have blank scores')
        else:
            try:
                number = float(score)
            except ValueError:
                raise ValueError('score must be numeric or an allowed blank') from None
            if not math.isfinite(number) or not 0 <= number <= 1:
                raise ValueError('score must be finite and between 0 and 1')
    summary = []
    for m, run in methods:
        subset = [r for r in rows if (r['method'], r['run_id']) == (m, run)]
        summary.append({'method': m, 'run_id': run, 'n': len(subset),
                        'answered': sum(r['prediction'] != 'ABSTAIN' for r in subset),
                        'blank_scores': sum(r['score'] == '' for r in subset)})
    return {'status': 'format_and_coverage_passed', 'performance_evaluated': False,
            'note': 'Does not verify score orientation, leakage, truth, freeze timing or methodological validity.',
            'groups': summary}


if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise SystemExit('Usage: python validate_predictions.py predictions.csv ids.csv methods.csv')
    try:
        print(json.dumps(validate(*sys.argv[1:]), indent=2))
    except (ValueError, OSError) as e:
        raise SystemExit(str(e))
