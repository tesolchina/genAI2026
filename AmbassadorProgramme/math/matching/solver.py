#!/usr/bin/env python3
"""
Solve the n=10 team tournament scheduling problem using fast local search.
"""
import random
import sys

n = 10
m = 5

def solve():
    """Find 10x10 binary matrix with row/col/anti-diag sums = 5."""
    best_ever = float('inf')
    
    for seed in range(10000):
        rng = random.Random(seed)
        
        # Random matrix with row sums = m
        F = []
        for r in range(n):
            row = [1]*m + [0]*(n-m)
            rng.shuffle(row)
            F.append(row)
        
        col_sum = [sum(F[r][i] for r in range(n)) for i in range(n)]
        ad_sum = [0]*n
        for r in range(n):
            for i in range(n):
                if F[r][i]:
                    ad_sum[(r+i) % n] += 1
        
        energy = sum((c - m)**2 for c in col_sum) + sum((a - m)**2 for a in ad_sum)
        
        if energy == 0:
            print(f"Found at seed {seed}, step 0!", flush=True)
            return F
        
        # Fast local search with occasional random restarts
        for step in range(100000):
            r = rng.randint(0, n-1)
            ones = [i for i in range(n) if F[r][i] == 1]
            zeros = [i for i in range(n) if F[r][i] == 0]
            i1 = rng.choice(ones)
            i0 = rng.choice(zeros)
            
            ad_k1 = (r + i1) % n
            ad_k0 = (r + i0) % n
            
            # Compute delta
            d_col = ((col_sum[i1]-1-m)**2 - (col_sum[i1]-m)**2 +
                     (col_sum[i0]+1-m)**2 - (col_sum[i0]-m)**2)
            
            if ad_k1 == ad_k0:
                d_ad = 0
            else:
                d_ad = ((ad_sum[ad_k1]-1-m)**2 - (ad_sum[ad_k1]-m)**2 +
                        (ad_sum[ad_k0]+1-m)**2 - (ad_sum[ad_k0]-m)**2)
            
            delta = d_col + d_ad
            
            # Accept improving or equal moves; occasionally accept worse
            temp = max(0.001, 2.0 * (1.0 - step / 100000))
            if delta < 0 or (delta == 0 and rng.random() < 0.5) or (delta > 0 and rng.random() < 0.01 * (2.718 ** (-delta / temp))):
                F[r][i1] = 0
                F[r][i0] = 1
                col_sum[i1] -= 1
                col_sum[i0] += 1
                ad_sum[ad_k1] -= 1
                ad_sum[ad_k0] += 1
                energy += delta
                
                if energy == 0:
                    print(f"Found at seed {seed}, step {step}!", flush=True)
                    return F
        
        if energy < best_ever:
            best_ever = energy
            if seed % 100 == 0:
                print(f"Seed {seed}: energy={energy} (best={best_ever})", flush=True)
        elif seed % 500 == 0:
            print(f"Seed {seed}: energy={energy} (best={best_ever})", flush=True)
    
    return None


def verify_and_print(F):
    shifts = list(range(n))
    
    print("\nColor matrix F:", flush=True)
    for r in range(n):
        print(f"  Row {r}: {F[r]}")
    
    row_sums = [sum(F[r]) for r in range(n)]
    col_sums = [sum(F[r][i] for r in range(n)) for i in range(n)]
    ad_sums = [0]*n
    for r in range(n):
        for i in range(n):
            if F[r][i]:
                ad_sums[(r+i) % n] += 1
    
    print(f"\nRow sums: {row_sums}")
    print(f"Col sums: {col_sums}")
    print(f"Anti-diag sums: {ad_sums}")
    
    # Full verification
    errors = []
    
    # Each pair plays exactly once
    played = [[False]*n for _ in range(n)]
    for r in range(n):
        s = shifts[r]
        for i in range(n):
            j = (i + s) % n
            if played[i][j]:
                errors.append(f"A{i+1}-B{j+1} duplicate!")
            played[i][j] = True
    for i in range(n):
        for j in range(n):
            if not played[i][j]:
                errors.append(f"A{i+1}-B{j+1} never played!")
    
    # B player balance
    for j in range(n):
        b_first = 0
        for r in range(n):
            s = shifts[r]
            i = (j - s) % n
            if F[r][i] == 0:
                b_first += 1
        if b_first != m:
            errors.append(f"B{j+1} first {b_first} times (need {m})")
    
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  X {e}")
    else:
        print("\nAll conditions verified! OK")
    
    # Print schedule
    print("\nSchedule:")
    for r in range(n):
        s = shifts[r]
        matches = []
        for i in range(n):
            j = (i + s) % n
            a_name = f"A{i+1}"
            b_name = f"B{j+1}"
            if F[r][i] == 1:
                matches.append(f"{a_name}-{b_name}")
            else:
                matches.append(f"{b_name}-{a_name}")
        print(f"第{r+1}轮 {' '.join(matches)}")
    
    return len(errors) == 0


if __name__ == '__main__':
    print("Searching...", flush=True)
    F = solve()
    if F:
        verify_and_print(F)
    else:
        print("No solution found!")
        sys.exit(1)
