#!/usr/bin/env python3
"""Independent verification of solution_34_plus.txt with extra constraint."""

n = 34
m = 17

def parse_match(s):
    parts = s.split('-')
    left, right = parts[0], parts[1]
    if left.startswith('A'):
        return int(left[1:])-1, int(right[1:])-1, True
    else:
        return int(right[1:])-1, int(left[1:])-1, False

rounds = []
with open('solution_34_plus.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('第'):
            parts = line.split()
            rounds.append([parse_match(m) for m in parts[1:]])

print("=" * 70)
print(f"VERIFICATION: n={n} with no-3-consecutive constraint")
print("=" * 70)

all_pass = True
checks = 0

# Structure
checks += 1
assert len(rounds) == n, f"Expected {n} rounds, got {len(rounds)}"
print(f"PASS: {n} rounds, {n} matches each")

# Pairs
checks += 1
pc = {}
for rd in rounds:
    for a, b, f in rd:
        pc[(a,b)] = pc.get((a,b), 0) + 1
ok = all(pc.get((i,j),0) == 1 for i in range(n) for j in range(n))
print(f"{'PASS' if ok else 'FAIL'}: All {n*n} pairs exactly once")
all_pass &= ok

# Per-round permutation
checks += 1
ok = all(sorted([a for a,b,f in rd]) == list(range(n)) and
         sorted([b for a,b,f in rd]) == list(range(n)) for rd in rounds)
print(f"{'PASS' if ok else 'FAIL'}: Each player plays once per round")
all_pass &= ok

# Per-round balance
checks += 1
ok = all(sum(1 for a,b,f in rd if f) == m for rd in rounds)
print(f"{'PASS' if ok else 'FAIL'}: Each round {m} A-first, {m} B-first")
all_pass &= ok

# A-player balance
checks += 1
ok = True
for i in range(n):
    fc = sum(1 for rd in rounds for a,b,f in rd if a==i and f)
    if fc != m:
        print(f"  FAIL: A{i+1} first={fc}")
        ok = False
print(f"{'PASS' if ok else 'FAIL'}: All A-players first={m}, second={m}")
all_pass &= ok

# B-player balance
checks += 1
ok = True
for j in range(n):
    fc = sum(1 for rd in rounds for a,b,f in rd if b==j and not f)
    if fc != m:
        print(f"  FAIL: B{j+1} first={fc}")
        ok = False
print(f"{'PASS' if ok else 'FAIL'}: All B-players first={m}, second={m}")
all_pass &= ok

# === EXTRA: No 3 consecutive first/second ===
print(f"\n--- Extra constraint: no 3 consecutive ---")

# A-players
checks += 1
ok = True
violations = 0
for i in range(n):
    seq = [0]*n
    for r_idx, rd in enumerate(rounds):
        for a,b,f in rd:
            if a == i:
                seq[r_idx] = 1 if f else 0
    for r in range(n-2):
        s = seq[r] + seq[r+1] + seq[r+2]
        if s == 3:
            violations += 1
            if violations <= 3:
                print(f"  FAIL: A{i+1} 3 consecutive FIRST rounds {r+1}-{r+3}")
            ok = False
        if s == 0:
            violations += 1
            if violations <= 3:
                print(f"  FAIL: A{i+1} 3 consecutive SECOND rounds {r+1}-{r+3}")
            ok = False
if violations > 3:
    print(f"  ... and {violations-3} more violations")
print(f"{'PASS' if ok else 'FAIL'}: No A-player has 3 consecutive first/second")
all_pass &= ok

# B-players
checks += 1
ok = True
violations = 0
for j in range(n):
    seq = [0]*n
    for r_idx, rd in enumerate(rounds):
        for a,b,f in rd:
            if b == j:
                seq[r_idx] = 1 if not f else 0  # B goes first when A goes second
    for r in range(n-2):
        s = seq[r] + seq[r+1] + seq[r+2]
        if s == 3:
            violations += 1
            if violations <= 3:
                print(f"  FAIL: B{j+1} 3 consecutive FIRST rounds {r+1}-{r+3}")
            ok = False
        if s == 0:
            violations += 1
            if violations <= 3:
                print(f"  FAIL: B{j+1} 3 consecutive SECOND rounds {r+1}-{r+3}")
            ok = False
if violations > 3:
    print(f"  ... and {violations-3} more violations")
print(f"{'PASS' if ok else 'FAIL'}: No B-player has 3 consecutive first/second")
all_pass &= ok

# Print sample A-player pattern
print(f"\nSample first/second patterns (1=first, 0=second):")
for i in range(3):
    seq = []
    for rd in rounds:
        for a,b,f in rd:
            if a == i:
                seq.append('1' if f else '0')
    print(f"  A{i+1}: {''.join(seq)}")
for j in range(3):
    seq = []
    for rd in rounds:
        for a,b,f in rd:
            if b == j:
                seq.append('0' if f else '1')  # B first when A second
    print(f"  B{j+1}: {''.join(seq)}")

print(f"\n{'=' * 70}")
if all_pass:
    print(f"FINAL: ALL {checks} CHECKS PASSED")
else:
    print(f"FINAL: SOME CHECKS FAILED")
print(f"{'=' * 70}")
