#!/usr/bin/env python3
"""
Fast solver using simulated annealing with non-cyclic Latin squares.
Key insight: cyclic Latin squares are provably infeasible for n=10.
We need non-cyclic pairings.
"""
import random
import time
import sys

n = 10
m = 5

def make_shift_swap_ls():
    """Shift+swap Latin square: even rounds=shift, odd rounds=shift+adjacent swap."""
    L = [[0]*n for _ in range(n)]
    for r in range(n):
        shift = 2 * (r // 2)
        for i in range(n):
            val = (i + shift) % n
            if r % 2 == 1:
                if val % 2 == 0:
                    val = (val + 1) % n
                else:
                    val = (val - 1) % n
            L[r][i] = val
    return L

def make_d5_ls():
    """D5 (dihedral group) Cayley table."""
    L = [[0]*n for _ in range(n)]
    for a in range(n):
        ar, af = a % 5, a >= 5
        for b in range(n):
            br, bf = b % 5, b >= 5
            if not af:
                cr = (ar + br) % 5 if not bf else (ar + br) % 5
                cf = bf
            else:
                cr = (ar - br) % 5
                cf = not bf
            L[a][b] = cr + (5 if cf else 0)
    return L

def make_mixed_ls():
    """5 shifts + 5 reflections."""
    L = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            if r < 5:
                L[r][i] = (i + 2*r) % n
            else:
                L[r][i] = (2*(r-5) + 1 - i) % n
    return L

def make_random_ls(seed):
    """Generate a random Latin square using sequential row construction."""
    rng = random.Random(seed)
    L = [[0]*n for _ in range(n)]
    
    # Available values for each cell: start with all
    col_avail = [set(range(n)) for _ in range(n)]  # available values per column
    pair_used = [[False]*n for _ in range(n)]  # pair (i,j) used
    
    for r in range(n):
        # Build permutation for row r
        perm = [None]*n
        order = list(range(n))
        rng.shuffle(order)
        
        for i in order:
            candidates = [j for j in col_avail[i] if not pair_used[i][j]]
            if not candidates:
                return None  # Failed, retry
            j = rng.choice(candidates)
            perm[i] = j
        
        # Check it's actually a permutation
        if len(set(perm)) != n:
            return None
        
        L[r] = perm
        for i in range(n):
            j = perm[i]
            col_avail[i].discard(j)
            pair_used[i][j] = True
    
    return L

def verify_ls(L):
    for r in range(n):
        if sorted(L[r]) != list(range(n)):
            return False
    for i in range(n):
        if sorted(L[r][i] for r in range(n)) != list(range(n)):
            return False
    return True

def compute_b_transversals(L):
    """Compute B-transversals: for each B_j, which cells (r, i) affect its balance."""
    L_inv = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            L_inv[r][L[r][i]] = i
    
    trans = []
    for j in range(n):
        t = [L_inv[r][j] for r in range(n)]  # column index for each row
        trans.append(t)
    return trans


def solve_sa(L, max_attempts=500, max_steps=200000):
    """Simulated annealing to find color matrix for given Latin square."""
    trans = compute_b_transversals(L)
    
    for attempt in range(max_attempts):
        rng = random.Random(attempt * 137 + 42)
        
        # Random matrix with row sums = m
        F = []
        for r in range(n):
            row = [1]*m + [0]*(n-m)
            rng.shuffle(row)
            F.append(row)
        
        # Compute column sums and B-transversal sums
        col_sum = [sum(F[r][i] for r in range(n)) for i in range(n)]
        bt_sum = [sum(F[r][trans[j][r]] for r in range(n)) for j in range(n)]
        
        energy = sum((c - m)**2 for c in col_sum) + sum((b - m)**2 for b in bt_sum)
        
        if energy == 0:
            return F
        
        best_energy = energy
        temp = 3.0
        cool = 1.0 - 5.0 / max_steps
        
        for step in range(max_steps):
            # Random swap in a random row
            r = rng.randint(0, n-1)
            ones = [i for i in range(n) if F[r][i] == 1]
            zeros = [i for i in range(n) if F[r][i] == 0]
            i1 = rng.choice(ones)
            i0 = rng.choice(zeros)
            
            # Compute delta for column sums
            d_col = ((col_sum[i1]-1-m)**2 - (col_sum[i1]-m)**2 +
                     (col_sum[i0]+1-m)**2 - (col_sum[i0]-m)**2)
            
            # Compute delta for B-transversal sums
            # Which B_j's are affected? Those where trans[j][r] == i1 or i0
            d_bt = 0
            for j in range(n):
                if trans[j][r] == i1:
                    d_bt += (bt_sum[j]-1-m)**2 - (bt_sum[j]-m)**2
                elif trans[j][r] == i0:
                    d_bt += (bt_sum[j]+1-m)**2 - (bt_sum[j]-m)**2
            
            delta = d_col + d_bt
            
            if delta < 0 or (delta == 0 and rng.random() < 0.3) or (delta > 0 and temp > 0.001 and rng.random() < 2.718**(-delta/temp)):
                F[r][i1] = 0
                F[r][i0] = 1
                col_sum[i1] -= 1
                col_sum[i0] += 1
                for j in range(n):
                    if trans[j][r] == i1:
                        bt_sum[j] -= 1
                    elif trans[j][r] == i0:
                        bt_sum[j] += 1
                energy += delta
                
                if energy == 0:
                    return F
                if energy < best_energy:
                    best_energy = energy
            
            temp *= cool
        
        if attempt % 50 == 0:
            print(f"    Attempt {attempt}: best_energy={best_energy}", flush=True)
    
    return None


def verify_and_format(F, L):
    """Verify and format the schedule."""
    errors = []
    
    # Check Latin square
    pairs = set()
    for r in range(n):
        for i in range(n):
            pair = (i, L[r][i])
            if pair in pairs:
                errors.append(f"Dup pair {pair}")
            pairs.add(pair)
    
    # Row sums
    for r in range(n):
        if sum(F[r]) != m:
            errors.append(f"Row {r} sum={sum(F[r])}")
    
    # Col sums
    for i in range(n):
        s = sum(F[r][i] for r in range(n))
        if s != m:
            errors.append(f"A{i+1} first={s}")
    
    # B balance
    for j in range(n):
        second = 0
        for r in range(n):
            for i in range(n):
                if L[r][i] == j and F[r][i] == 1:
                    second += 1
        if second != m:
            errors.append(f"B{j+1} second={second}")
    
    # Round B balance
    for r in range(n):
        b_first = sum(1 for i in range(n) if F[r][i] == 0)
        if b_first != m:
            errors.append(f"Round {r+1} B_first={b_first}")
    
    # Format schedule
    lines = []
    for r in range(n):
        matches = []
        for i in range(n):
            j = L[r][i]
            if F[r][i] == 1:
                matches.append(f"A{i+1}-B{j+1}")
            else:
                matches.append(f"B{j+1}-A{i+1}")
        lines.append(f"第{r+1}轮 {' '.join(matches)}")
    
    return errors, '\n'.join(lines)


def main():
    start = time.time()
    
    named_ls = [
        ("Shift+Swap", make_shift_swap_ls()),
        ("D5 Cayley", make_d5_ls()),
        ("Mixed shift/ref", make_mixed_ls()),
    ]
    
    for name, L in named_ls:
        if not verify_ls(L):
            print(f"{name}: Invalid LS, skipping", flush=True)
            continue
        
        print(f"\n{'='*50}", flush=True)
        print(f"Trying {name}...", flush=True)
        print(f"{'='*50}", flush=True)
        
        F = solve_sa(L, max_attempts=200, max_steps=300000)
        if F is not None:
            errors, schedule = verify_and_format(F, L)
            if not errors:
                print(f"\nSOLUTION FOUND with {name}!", flush=True)
                print(f"\nColor matrix:", flush=True)
                for r in range(n):
                    print(f"  {F[r]}")
                print(f"\nSchedule:", flush=True)
                print(schedule)
                print(f"\nTotal time: {time.time()-start:.1f}s", flush=True)
                return F, L, schedule
            else:
                print(f"  Found but verification failed: {errors}", flush=True)
        else:
            print(f"  No solution found.", flush=True)
    
    # Try random Latin squares
    print(f"\n{'='*50}", flush=True)
    print(f"Trying random Latin squares...", flush=True)
    print(f"{'='*50}", flush=True)
    
    for seed in range(1000):
        L = make_random_ls(seed)
        if L is None or not verify_ls(L):
            continue
        
        F = solve_sa(L, max_attempts=20, max_steps=100000)
        if F is not None:
            errors, schedule = verify_and_format(F, L)
            if not errors:
                print(f"\nSOLUTION FOUND with random LS (seed={seed})!", flush=True)
                print(f"\nColor matrix:", flush=True)
                for r in range(n):
                    print(f"  {F[r]}")
                print(f"\nSchedule:", flush=True)
                print(schedule)
                print(f"\nTotal time: {time.time()-start:.1f}s", flush=True)
                return F, L, schedule
        
        if seed % 50 == 0:
            print(f"  Tried {seed+1} random LS...", flush=True)
    
    print("No solution found!", flush=True)
    return None, None, None


if __name__ == '__main__':
    main()
