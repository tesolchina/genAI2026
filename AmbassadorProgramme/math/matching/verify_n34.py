#!/usr/bin/env python3
"""Independent verification of the n=34 solution from solution_34.txt."""

n = 34
m = 17

def parse_match(s):
    parts = s.split('-')
    left, right = parts[0], parts[1]
    if left.startswith('A'):
        a_idx = int(left[1:]) - 1
        b_idx = int(right[1:]) - 1
        return a_idx, b_idx, True
    else:
        b_idx = int(left[1:]) - 1
        a_idx = int(right[1:]) - 1
        return a_idx, b_idx, False

# Read solution
rounds = []
with open('solution_34.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0].startswith('第'):
            matches = parts[1:]
            rd = [parse_match(m) for m in matches]
            rounds.append(rd)

print("=" * 70)
print(f"INDEPENDENT VERIFICATION OF n={n} SOLUTION")
print("=" * 70)

all_pass = True
checks = 0

# Check structure
checks += 1
if len(rounds) != n:
    print(f"FAIL: {len(rounds)} rounds, expected {n}")
    all_pass = False
else:
    print(f"PASS: {n} rounds present")

checks += 1
if all(len(r) == n for r in rounds):
    print(f"PASS: {n} matches per round")
else:
    print(f"FAIL: not all rounds have {n} matches")
    all_pass = False

# Constraint 1: each pair exactly once
pair_count = {}
for r_idx, rd in enumerate(rounds):
    for a, b, f in rd:
        pair = (a, b)
        pair_count[pair] = pair_count.get(pair, 0) + 1

checks += 1
missing = sum(1 for i in range(n) for j in range(n) if pair_count.get((i,j),0) == 0)
dups = sum(1 for p, c in pair_count.items() if c > 1)
if missing == 0 and dups == 0:
    print(f"PASS: All {n*n} pairs appear exactly once")
else:
    print(f"FAIL: {missing} missing pairs, {dups} duplicate pairs")
    all_pass = False

# Constraint 2: each player plays once per round
checks += 1
ok = True
for r_idx, rd in enumerate(rounds):
    a_players = sorted([a for a, b, f in rd])
    b_players = sorted([b for a, b, f in rd])
    if a_players != list(range(n)) or b_players != list(range(n)):
        print(f"FAIL: Round {r_idx+1} players not permutation")
        ok = False
        all_pass = False
if ok:
    print(f"PASS: Each player plays exactly once per round")

# Constraint 3: per-round balance
checks += 1
ok = True
for r_idx, rd in enumerate(rounds):
    a_first = sum(1 for a, b, f in rd if f)
    if a_first != m:
        print(f"FAIL: Round {r_idx+1}: A-first={a_first}")
        ok = False
        all_pass = False
if ok:
    print(f"PASS: Each round has {m} A-first and {m} B-first")

# Constraint 4a: A-player overall balance
checks += 1
ok = True
for i in range(n):
    fc = sum(1 for rd in rounds for a, b, f in rd if a == i and f)
    if fc != m:
        print(f"FAIL: A{i+1} first={fc}")
        ok = False
        all_pass = False
if ok:
    print(f"PASS: All A-players have first={m}, second={m}")

# Constraint 4b: B-player overall balance
checks += 1
ok = True
for j in range(n):
    fc = sum(1 for rd in rounds for a, b, f in rd if b == j and not f)
    if fc != m:
        print(f"FAIL: B{j+1} first={fc}")
        ok = False
        all_pass = False
if ok:
    print(f"PASS: All B-players have first={m}, second={m}")

print(f"\n{'=' * 70}")
if all_pass:
    print(f"FINAL: ALL {checks} CHECKS PASSED")
else:
    print(f"FINAL: SOME CHECKS FAILED")
print(f"{'=' * 70}")
