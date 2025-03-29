import sys
import re
from collections import defaultdict

def parse_crosshair_log(log_content):
    metrics = {
        'execution_time': 0.0,
        'total_iterations': 0,
        'confirmed_paths': 0,
        'unique_locations': set(),
        'smt_decisions': 0,
        'branch_points': 0,
        'conditions_analyzed': 0,
        'path_stats': defaultdict(int),
        'code_locations': defaultdict(int),
        'iterations': []
    }

    # Time tracking
    timestamps = []
    time_pattern = r'(\d+\.\d+)\|'

    # Important patterns
    patterns = {
        'iteration': r'analyze_calltree\(\) Iteration\s+(\d+)',
        'path_stats': r'Path tree stats\s+\{(.+?)\}',
        'smt_choice': r'choose_possible\(\) SMT chose',
        'location': r'\((calcualte_knapsack_fitness Function1\.py:\d+)\)',
        'condition': r'analyze\(\) Analyzing postcondition',
        'branch': r'smt_fork statespace.py:\d+\)'
    }

    for line in log_content.split('\n'):
        # Extract timestamps
        if time_match := re.search(time_pattern, line):
            timestamps.append(float(time_match.group(1)))

        # Track iterations
        if iter_match := re.search(patterns['iteration'], line):
            metrics['total_iterations'] = max(metrics['total_iterations'], int(iter_match.group(1)))
            metrics['iterations'].append(int(iter_match.group(1)))

        # Count confirmed paths
        if path_match := re.search(patterns['path_stats'], line):
            stats = path_match.group(1)
            confirmed = re.search(r'CONFIRMED:(\d+)', stats)
            if confirmed:
                metrics['confirmed_paths'] += int(confirmed.group(1))

        # Count SMT decisions
        metrics['smt_decisions'] += len(re.findall(patterns['smt_choice'], line))

        # Track unique code locations
        if loc_match := re.search(patterns['location'], line):
            metrics['unique_locations'].add(loc_match.group(1))
            metrics['code_locations'][loc_match.group(1)] += 1

        # Count conditions analyzed
        metrics['conditions_analyzed'] += len(re.findall(patterns['condition'], line))

        # Count branch points
        metrics['branch_points'] += len(re.findall(patterns['branch'], line))

    # Calculate execution time
    if timestamps:
        metrics['execution_time'] = timestamps[-1] - timestamps[0]

    # Convert set to a simple count
    metrics['unique_locations'] = len(metrics['unique_locations'])

    return metrics

def print_metrics(metrics):
    print(f"{'Metric':<25} | {'Value':>10}")
    print(f"{'-' * 36}")
    print(f"{'Execution Time (s)':<25} | {metrics['execution_time']:>10.3f}")
    print(f"{'Total Iterations':<25} | {metrics['total_iterations']:>10}")
    print(f"{'Confirmed Paths':<25} | {metrics['confirmed_paths']:>10}")
    print(f"{'SMT Decisions':<25} | {metrics['smt_decisions']:>10}")
    print(f"{'Branch Points':<25} | {metrics['branch_points']:>10}")
    print(f"{'Conditions Analyzed':<25} | {metrics['conditions_analyzed']:>10}")
    print(f"{'Unique Code Locations':<25} | {metrics['unique_locations']:>10}")

    print("\nMost Frequent Code Locations:")
    top_locs = sorted(metrics['code_locations'].items(), key=lambda x: x[1], reverse=True)[:5]
    for loc, count in top_locs:
        print(f"- {loc}: {count} hits")

def main():
    if len(sys.argv) < 2:
        print("Usage: python crosshair_parser.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    # If your file is encoded in UTF-16, use encoding='utf-16'.
    # Otherwise, use the encoding that matches your file format.
    with open(log_file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    metrics = parse_crosshair_log(content)
    print_metrics(metrics)

if __name__ == "__main__":
    main()
