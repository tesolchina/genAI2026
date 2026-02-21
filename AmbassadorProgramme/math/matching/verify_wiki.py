#!/usr/bin/env python3
"""Verify the Wikipedia Scheveningen 10-board table against our constraints."""

n = 10
m = 5

# Parse Wikipedia table: "A1-B1" means A1 first, "B5-A5" means B5 first
wiki_schedule = [
    # Round 1
    ["A1-B1", "A2-B2", "A3-B3", "A4-B4", "B5-A5", "B6-A6", "B7-A7", "A8-B8", "B9-A9", "B10-A10"],
    # Round 2
    ["B2-A1", "B1-A2", "B8-A3", "B3-A4", "A5-B10", "A6-B5", "A7-B6", "B4-A8", "A9-B7", "A10-B9"],
    # Round 3
    ["A1-B3", "A2-B8", "A3-B4", "A4-B10", "B6-A5", "B7-A6", "B9-A7", "A8-B1", "B2-A9", "B5-A10"],
    # Round 4
    ["B4-A1", "B3-A2", "B10-A3", "A4-B6", "A5-B7", "B8-A6", "A7-B5", "A8-B9", "B1-A9", "A10-B2"],
    # Round 5
    ["A1-B5", "A2-B4", "B9-A3", "B7-A4", "B1-A5", "A6-B10", "B8-A7", "B2-A8", "A9-B3", "A10-B6"],
    # Round 6
    ["B6-A1", "A2-B7", "A3-B1", "A4-B9", "A5-B8", "A6-B2", "B10-A7", "B5-A8", "B4-A9", "B3-A10"],
    # Round 7
    ["A1-B7", "B5-A2", "B2-A3", "B1-A4", "B4-A5", "B9-A6", "A7-B3", "A8-B10", "A9-B6", "A10-B8"],
    # Round 8
    ["B8-A1", "B6-A2", "A3-B5", "A4-B2", "A5-B9", "A6-B1", "A7-B4", "B3-A8", "B10-A9", "B7-A10"],
    # Round 9
    ["A1-B9", "A2-B10", "A3-B7", "B5-A4", "B2-A5", "B3-A6", "B1-A7", "A8-B6", "A9-B8", "B4-A10"],
    # Round 10
    ["B10-A1", "B9-A2", "B6-A3", "B8-A4", "A5-B3", "A6-B4", "A7-B2", "B7-A8", "A9-B5", "A10-B1"],
]

def parse_match(s):
    """Parse 'A1-B3' or 'B5-A2'. Returns (a_index, b_index, a_goes_first)."""
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

# Build L and F matrices
L = [[0]*n for _ in range(n)]
F = [[0]*n for _ in range(n)]

for r in range(n):
    for match_str in wiki_schedule[r]:
        a_idx, b_idx, a_first = parse_match(match_str)
        L[r][a_idx] = b_idx
        F[r][a_idx] = 1 if a_first else 0

# Verify
errors = []

# 1. Latin square
for r in range(n):
    if sorted(L[r]) != list(range(n)):
        errors.append(f"Round {r+1}: row not a permutation: {L[r]}")
for i in range(n):
    col = [L[r][i] for r in range(n)]
    if sorted(col) != list(range(n)):
        errors.append(f"A{i+1}: column not a permutation: {col}")

# 2. Each pair exactly once
pair_count = {}
for r in range(n):
    for i in range(n):
        j = L[r][i]
        pair = (i, j)
        pair_count[pair] = pair_count.get(pair, 0) + 1
for (i, j), cnt in pair_count.items():
    if cnt != 1:
        errors.append(f"Pair (A{i+1}, B{j+1}) appears {cnt} times")

# 3. Row sums (per-round A-first count)
for r in range(n):
    s = sum(F[r])
    if s != m:
        errors.append(f"Round {r+1}: A-first count = {s}, expected {m}")

# 4. Column sums (per A-player first count)
for i in range(n):
    s = sum(F[r][i] for r in range(n))
    if s != m:
        errors.append(f"A{i+1}: first count = {s}, expected {m}")

# 5. B-player balance
for j in range(n):
    b_second = 0
    for r in range(n):
        for i in range(n):
            if L[r][i] == j and F[r][i] == 1:
                b_second += 1
    if b_second != m:
        errors.append(f"B{j+1}: second count = {b_second}, expected {m}")

# 6. Per-round B-first count
for r in range(n):
    b_first = sum(1 for i in range(n) if F[r][i] == 0)
    if b_first != m:
        errors.append(f"Round {r+1}: B-first count = {b_first}, expected {m}")

if errors:
    print("VERIFICATION FAILED:")
    for e in errors:
        print(f"  {e}")
else:
    print("ALL CHECKS PASSED for Wikipedia Scheveningen 10-board table!")

# Print stats
print("\nA-player first counts:")
for i in range(n):
    s = sum(F[r][i] for r in range(n))
    print(f"  A{i+1}: {s} first, {n-s} second")

print("\nB-player second counts:")
for j in range(n):
    b_second = sum(1 for r in range(n) for i in range(n) if L[r][i] == j and F[r][i] == 1)
    b_first = sum(1 for r in range(n) for i in range(n) if L[r][i] == j and F[r][i] == 0)
    print(f"  B{j+1}: {b_first} first, {b_second} second")

print("\nPer-round balance:")
for r in range(n):
    a_first = sum(F[r])
    print(f"  Round {r+1}: A-first={a_first}, B-first={n - a_first}")

# Print pairings
print("\nPairings (Latin square L):")
for r in range(n):
    print(f"  Round {r+1}: {L[r]}")

print("\nColor matrix F:")
for r in range(n):
    print(f"  Round {r+1}: {F[r]}")
