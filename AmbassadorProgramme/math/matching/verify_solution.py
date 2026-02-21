#!/usr/bin/env python3
"""
Comprehensive verification of the n=10 solution against ALL original problem constraints.

Original constraints (from problem1.md):
(1) n rounds, each player plays every opponent from the other team exactly once.
(2) Each player's opponent differs every round; in each match one goes first, one goes second.
(3) Each round: m players from each team go first, m go second.
(4) After all rounds: every player's first count = second count = m.
"""

n = 10
m = 5

# The solution schedule from solution.md
schedule_text = """
第1轮 A1-B1 A2-B2 A3-B3 A4-B4 A5-B5 B6-A6 B7-A7 B8-A8 B9-A9 B10-A10
第2轮 B2-A1 B9-A2 A3-B4 B6-A4 A5-B7 B10-A6 A7-B3 A8-B1 A9-B8 B5-A10
第3轮 B8-A1 B7-A2 A3-B5 A4-B10 B1-A5 B9-A6 B6-A7 A8-B4 A9-B3 A10-B2
第4轮 A1-B9 A2-B4 A3-B10 B2-A4 B8-A5 A6-B5 B1-A7 B3-A8 B7-A9 A10-B6
第5轮 B6-A1 B1-A2 B2-A3 A4-B7 A5-B9 B3-A6 A7-B4 B5-A8 A9-B10 A10-B8
第6轮 B4-A1 B5-A2 B9-A3 A4-B3 B2-A5 A6-B8 B10-A7 A8-B7 A9-B6 A10-B1
第7轮 A1-B7 B10-A2 B6-A3 B5-A4 B3-A5 A6-B1 A7-B8 A8-B9 A9-B2 B4-A10
第8轮 A1-B5 A2-B3 B8-A3 B1-A4 A5-B10 A6-B2 B9-A7 A8-B6 B4-A9 B7-A10
第9轮 A1-B10 A2-B8 B7-A3 A4-B9 A5-B6 B4-A6 A7-B5 B2-A8 B1-A9 B3-A10
第10轮 B3-A1 A2-B6 A3-B1 B8-A4 B4-A5 A6-B7 A7-B2 B10-A8 B5-A9 A10-B9
""".strip()

def parse_match(s):
    """Parse 'A1-B3' or 'B5-A2'. Returns (a_index_0based, b_index_0based, a_goes_first)."""
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

# Parse all rounds
rounds = []
for line in schedule_text.split('\n'):
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    round_label = parts[0]  # e.g. "第1轮"
    matches = parts[1:]
    round_data = []
    for match_str in matches:
        a_idx, b_idx, a_first = parse_match(match_str)
        round_data.append((a_idx, b_idx, a_first))
    rounds.append(round_data)

print("=" * 70)
print("COMPREHENSIVE VERIFICATION OF n=10 SOLUTION")
print("=" * 70)

all_pass = True
total_checks = 0

# ============================================================
# CHECK 0: Correct number of rounds and matches per round
# ============================================================
print(f"\n--- CHECK 0: Structure ---")
total_checks += 1
if len(rounds) != n:
    print(f"  FAIL: Expected {n} rounds, got {len(rounds)}")
    all_pass = False
else:
    print(f"  PASS: {n} rounds present")

total_checks += 1
matches_per_round_ok = all(len(r) == n for r in rounds)
if not matches_per_round_ok:
    print(f"  FAIL: Not all rounds have {n} matches")
    all_pass = False
else:
    print(f"  PASS: Each round has {n} matches")

# ============================================================
# CONSTRAINT (1): n rounds, each A_i plays each B_j exactly once
# ============================================================
print(f"\n--- CONSTRAINT (1): Each pair plays exactly once ---")

pair_count = {}
for r_idx, rd in enumerate(rounds):
    for a_idx, b_idx, a_first in rd:
        pair = (a_idx, b_idx)
        if pair not in pair_count:
            pair_count[pair] = []
        pair_count[pair].append(r_idx + 1)

# Check every pair (A_i, B_j) exists
missing_pairs = []
duplicate_pairs = []
for i in range(n):
    for j in range(n):
        cnt = len(pair_count.get((i, j), []))
        if cnt == 0:
            missing_pairs.append(f"(A{i+1}, B{j+1})")
        elif cnt > 1:
            rnds = pair_count[(i, j)]
            duplicate_pairs.append(f"(A{i+1}, B{j+1}) in rounds {rnds}")

total_checks += 1
if missing_pairs:
    print(f"  FAIL: Missing pairs: {missing_pairs[:5]}{'...' if len(missing_pairs) > 5 else ''}")
    all_pass = False
else:
    print(f"  PASS: All {n*n} pairs (A_i, B_j) appear at least once")

total_checks += 1
if duplicate_pairs:
    print(f"  FAIL: Duplicate pairs: {duplicate_pairs[:5]}")
    all_pass = False
else:
    print(f"  PASS: No pair appears more than once")

# ============================================================
# CONSTRAINT (2a): Each player plays exactly one match per round
# ============================================================
print(f"\n--- CONSTRAINT (2a): Each player plays exactly once per round ---")

a_per_round_ok = True
b_per_round_ok = True
for r_idx, rd in enumerate(rounds):
    a_players = [a for a, b, f in rd]
    b_players = [b for a, b, f in rd]
    if sorted(a_players) != list(range(n)):
        print(f"  FAIL: Round {r_idx+1}: A-players not a permutation: {[x+1 for x in sorted(a_players)]}")
        a_per_round_ok = False
        all_pass = False
    if sorted(b_players) != list(range(n)):
        print(f"  FAIL: Round {r_idx+1}: B-players not a permutation: {[x+1 for x in sorted(b_players)]}")
        b_per_round_ok = False
        all_pass = False

total_checks += 1
if a_per_round_ok:
    print(f"  PASS: Each A-player plays exactly once per round")
total_checks += 1
if b_per_round_ok:
    print(f"  PASS: Each B-player plays exactly once per round")

# ============================================================
# CONSTRAINT (2b): Each player's opponent differs every round
# (This is guaranteed by constraint (1) but let's check explicitly)
# ============================================================
print(f"\n--- CONSTRAINT (2b): Different opponents each round ---")

total_checks += 1
a_opponents_ok = True
for i in range(n):
    opponents = []
    for r_idx, rd in enumerate(rounds):
        for a, b, f in rd:
            if a == i:
                opponents.append(b)
    if sorted(opponents) != list(range(n)):
        print(f"  FAIL: A{i+1} opponents: {[x+1 for x in opponents]} (not all different B-players)")
        a_opponents_ok = False
        all_pass = False
if a_opponents_ok:
    print(f"  PASS: Each A-player faces a different B-player each round (all 10 B-players)")

total_checks += 1
b_opponents_ok = True
for j in range(n):
    opponents = []
    for r_idx, rd in enumerate(rounds):
        for a, b, f in rd:
            if b == j:
                opponents.append(a)
    if sorted(opponents) != list(range(n)):
        print(f"  FAIL: B{j+1} opponents: {[x+1 for x in opponents]}")
        b_opponents_ok = False
        all_pass = False
if b_opponents_ok:
    print(f"  PASS: Each B-player faces a different A-player each round (all 10 A-players)")

# ============================================================
# CONSTRAINT (3): Each round: m A-players go first, m B-players go first
# ============================================================
print(f"\n--- CONSTRAINT (3): Per-round balance (m=5 first from each team) ---")

total_checks += 1
round_balance_ok = True
for r_idx, rd in enumerate(rounds):
    a_first_count = sum(1 for a, b, f in rd if f)
    a_second_count = sum(1 for a, b, f in rd if not f)
    b_first_count = a_second_count  # when A goes second, B goes first
    b_second_count = a_first_count  # when A goes first, B goes second
    
    if a_first_count != m:
        print(f"  FAIL: Round {r_idx+1}: A-first={a_first_count}, expected {m}")
        round_balance_ok = False
        all_pass = False
    if b_first_count != m:
        print(f"  FAIL: Round {r_idx+1}: B-first={b_first_count}, expected {m}")
        round_balance_ok = False
        all_pass = False

if round_balance_ok:
    print(f"  PASS: Every round has exactly {m} A-players going first and {m} B-players going first")

# Print round-by-round detail
print(f"\n  Round-by-round detail:")
for r_idx, rd in enumerate(rounds):
    a_first_names = [f"A{a+1}" for a, b, f in rd if f]
    b_first_names = [f"B{b+1}" for a, b, f in rd if not f]
    print(f"    Round {r_idx+1:2d}: A-first={a_first_names}  B-first={b_first_names}")

# ============================================================
# CONSTRAINT (4): After all rounds, each player first=m, second=m
# ============================================================
print(f"\n--- CONSTRAINT (4): Overall balance (each player: first=5, second=5) ---")

# A-player first/second counts
total_checks += 1
a_balance_ok = True
print(f"\n  A-player totals:")
for i in range(n):
    first_count = 0
    second_count = 0
    for r_idx, rd in enumerate(rounds):
        for a, b, f in rd:
            if a == i:
                if f:
                    first_count += 1
                else:
                    second_count += 1
    status = "OK" if first_count == m and second_count == m else "FAIL"
    if status == "FAIL":
        a_balance_ok = False
        all_pass = False
    print(f"    A{i+1:2d}: first={first_count}, second={second_count}  [{status}]")

if a_balance_ok:
    print(f"  PASS: All A-players have first={m}, second={m}")

# B-player first/second counts
total_checks += 1
b_balance_ok = True
print(f"\n  B-player totals:")
for j in range(n):
    first_count = 0
    second_count = 0
    for r_idx, rd in enumerate(rounds):
        for a, b, f in rd:
            if b == j:
                if f:
                    # A goes first, so B goes second
                    second_count += 1
                else:
                    # A goes second, so B goes first
                    first_count += 1
    status = "OK" if first_count == m and second_count == m else "FAIL"
    if status == "FAIL":
        b_balance_ok = False
        all_pass = False
    print(f"    B{j+1:2d}: first={first_count}, second={second_count}  [{status}]")

if b_balance_ok:
    print(f"  PASS: All B-players have first={m}, second={m}")

# ============================================================
# ADDITIONAL: Verify the n=8 example from the problem for sanity
# ============================================================
print(f"\n{'=' * 70}")
print(f"BONUS: Verify the n=8 example from the original problem")
print(f"{'=' * 70}")

n8 = 8
m8 = 4

schedule_n8 = """
第1轮 A1-B1 B2-A2 A3-B3 B4-A4 A5-B5 B6-A6 A7-B7 B8-A8
第2轮 B3-A1 A2-B4 B5-A3 A4-B6 B7-A5 A6-B8 B1-A7 A8-B2
第3轮 A1-B5 B6-A2 A3-B7 B8-A4 A5-B1 B2-A6 A7-B3 B4-A8
第4轮 B7-A1 A2-B8 B1-A3 A4-B2 B3-A5 A6-B4 B5-A7 A8-B6
第5轮 A1-B2 B3-A2 A3-B4 B5-A4 A5-B6 B7-A6 A7-B8 B1-A8
第6轮 B4-A1 A2-B5 B6-A3 A4-B7 B8-A5 A6-B1 B2-A7 A8-B3
第7轮 A1-B6 B7-A2 A3-B8 B1-A4 A5-B2 B3-A6 A7-B4 B5-A8
第8轮 B8-A1 A2-B1 B2-A3 A4-B3 B4-A5 A6-B5 B6-A7 A8-B7
""".strip()

rounds8 = []
for line in schedule_n8.split('\n'):
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    matches = parts[1:]
    round_data = []
    for match_str in matches:
        a_idx, b_idx, a_first = parse_match(match_str)
        round_data.append((a_idx, b_idx, a_first))
    rounds8.append(round_data)

n8_errors = []

# Check pairs
pair8 = {}
for r_idx, rd in enumerate(rounds8):
    for a, b, f in rd:
        pair = (a, b)
        pair8[pair] = pair8.get(pair, 0) + 1
for i in range(n8):
    for j in range(n8):
        if pair8.get((i, j), 0) != 1:
            n8_errors.append(f"Pair (A{i+1},B{j+1}) count={pair8.get((i,j),0)}")

# Round balance
for r_idx, rd in enumerate(rounds8):
    af = sum(1 for a, b, f in rd if f)
    if af != m8:
        n8_errors.append(f"Round {r_idx+1} A-first={af}")

# A balance
for i in range(n8):
    fc = sum(1 for r in rounds8 for a, b, f in r if a == i and f)
    if fc != m8:
        n8_errors.append(f"A{i+1} first={fc}")

# B balance
for j in range(n8):
    fc = sum(1 for r in rounds8 for a, b, f in r if b == j and not f)
    if fc != m8:
        n8_errors.append(f"B{j+1} first={fc}")

if n8_errors:
    print(f"  n=8 example has issues: {n8_errors}")
else:
    print(f"  PASS: The n=8 example from the problem also passes all constraints")

# ============================================================
# FINAL VERDICT
# ============================================================
print(f"\n{'=' * 70}")
if all_pass:
    print(f"FINAL VERDICT: ALL {total_checks} CHECKS PASSED")
    print(f"The n=10 solution satisfies ALL original problem constraints.")
else:
    print(f"FINAL VERDICT: SOME CHECKS FAILED")
    print(f"The solution has errors that need to be fixed.")
print(f"{'=' * 70}")
