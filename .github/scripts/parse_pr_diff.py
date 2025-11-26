#!/usr/bin/env python3
import re
import json
import sys

def parse_diff(path):
    lines = {}
    curr_file = None
    lineno = None
    hunk_re = re.compile(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@')
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        for raw in f:
            line = raw.rstrip('\n')
            if line.startswith('+++ b/'):
                curr_file = line[6:]
                lines[curr_file] = []
                lineno = None
                continue
            m = hunk_re.match(line)
            if m:
                lineno = int(m.group(1))
                continue
            if curr_file is not None and lineno is not None:
                if line.startswith('+') and not line.startswith('+++'):
                    lines[curr_file].append(lineno)
                    lineno += 1
                else:
                    if not line.startswith('-'):
                        lineno += 1
    return lines


def main():
    if len(sys.argv) < 3:
        print('Usage: parse_pr_diff.py <pr.diff> <out.json>')
        sys.exit(2)
    diff_path = sys.argv[1]
    out_path = sys.argv[2]
    parsed = parse_diff(diff_path)
    with open(out_path, 'w') as out:
        json.dump(parsed, out, indent=2)
    print(f'Parsed changed lines for {len(parsed)} files and wrote {out_path}')


if __name__ == '__main__':
    main()
