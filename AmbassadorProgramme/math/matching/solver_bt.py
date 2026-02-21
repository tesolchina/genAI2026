#!/usr/bin/env python3
"""
Backtracking solver for n=10 team tournament with non-cyclic Latin squares.
"""
from itertools import combinations
import sys
import time

n = 10
m = 5

def d5_cayley_table():
    """Cayley table of D5 (dihedral group of order 10).
    Elements: 0=e, 1=r, 2=r^2, 3=r^3, 4=r^4, 5=s, 6=rs, 7=r^2s, 8=r^3s, 9=r^4s
    """
    L = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            a_rot = a % 5 if a < 5 else a % 5
            a_ref = a >= 5
            b_rot = b % 5 if b < 5 else b % 5
            b_ref = b >= 5
            if not a_ref and not b_ref:
                c_rot = (a_rot + b_rot) % 5
                c_ref = False
            elif not a_ref and b_ref:
                c_rot = (a_rot + b_rot) % 5
                c_ref = True
            elif a_ref and not b_ref:
                c_rot = (a_rot - b_rot) % 5
                c_ref = True
            else:
                c_rot = (a_rot - b_rot) % 5
                c_ref = False
            L[a][b] = c_rot + (5 if c_ref else 0)
    return L

def mixed_latin_square():
    """Latin square using shifts for first 5 rounds, reflections for last 5."""
    L = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            if r < 5:
                L[r][i] = (i + 2*r) % n
            else:
                L[r][i] = (2*(r-5) + 1 - i) % n
    return L

def custom_latin_square_1():
    """Another non-cyclic Latin square."""
    L = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            if r % 2 == 0:
                L[r][i] = (i + r) % n
            else:
                L[r][i] = (r - i) % n
    return L

def custom_latin_square_2():
    """Latin square mixing different multipliers."""
    L = [[0]*n for _ in range(n)]
    mults = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
    shifts = [0, 0, 2, 2, 4, 4, 6, 6, 8, 8]
    for r in range(n):
        for i in range(n):
            L[r][i] = (mults[r] * i + shifts[r]) % n
    return L

def custom_latin_square_3():
    """Try yet another construction."""
    # Use the structure: round r sends i to (i*a_r + b_r) mod 10
    # where a_r alternates between 1 and 3, and b_r ensures Latin property
    perms = [
        [0,1,2,3,4,5,6,7,8,9],  # identity
        [1,0,3,2,5,4,7,6,9,8],  # swap adjacent
        [2,3,4,5,6,7,8,9,0,1],  # shift 2
        [3,2,5,4,7,6,9,8,1,0],  # shift 2 + swap
        [4,5,6,7,8,9,0,1,2,3],  # shift 4
        [5,4,7,6,9,8,1,0,3,2],  # shift 4 + swap
        [6,7,8,9,0,1,2,3,4,5],  # shift 6
        [7,6,9,8,1,0,3,2,5,4],  # shift 6 + swap
        [8,9,0,1,2,3,4,5,6,7],  # shift 8
        [9,8,1,0,3,2,5,4,7,6],  # shift 8 + swap
    ]
    L = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            L[r][i] = perms[r][i]
    return L


def verify_latin_square(L):
    """Check if L is a valid Latin square."""
    for r in range(n):
        if sorted(L[r]) != list(range(n)):
            return False, f"Row {r} not a permutation: {L[r]}"
    for i in range(n):
        col = [L[r][i] for r in range(n)]
        if sorted(col) != list(range(n)):
            return False, f"Col {i} not a permutation: {col}"
    # Check all pairs
    pairs = set()
    for r in range(n):
        for i in range(n):
            pair = (i, L[r][i])
            if pair in pairs:
                return False, f"Duplicate pair {pair} in round {r}"
            pairs.add(pair)
    return True, "OK"


def solve_backtrack(L, verbose=True):
    """Given a Latin square L, find color matrix F using backtracking."""
    # Compute inverse permutations
    L_inv = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            L_inv[r][L[r][i]] = i
    
    # B-transversals: for each j, the set of cells that affect B_j's balance
    # B_j goes second when F[r][L_inv[r][j]] = 1
    b_trans = []
    for j in range(n):
        trans = [(r, L_inv[r][j]) for r in range(n)]
        b_trans.append(trans)
    
    # Backtracking: build F row by row
    col_count = [0] * n
    b_count = [0] * n  # B_j second count
    
    nodes = [0]
    start_time = time.time()
    
    def backtrack(r, solution):
        nodes[0] += 1
        if nodes[0] % 1000000 == 0 and verbose:
            elapsed = time.time() - start_time
            print(f"  Nodes: {nodes[0]:,}, row {r}, elapsed: {elapsed:.1f}s", flush=True)
        
        if r == n:
            return all(c == m for c in col_count) and all(c == m for c in b_count)
        
        remain = n - r - 1  # rows after this one
        
        # Determine forced and forbidden columns
        forced = set()
        forbidden = set()
        
        for i in range(n):
            if col_count[i] >= m:
                forbidden.add(i)
            elif col_count[i] + remain + 1 < m:
                return False  # can't reach m even including this row
            elif col_count[i] + remain < m:
                forced.add(i)  # must include this row
        
        # Check B-transversal constraints
        for j in range(n):
            b_r, b_i = b_trans[j][r]  # cell (r, b_i) affects B_j
            assert b_r == r
            
            if b_count[j] >= m:
                forbidden.add(b_i)  # B_j already has enough seconds
            elif b_count[j] + remain < m:
                forced.add(b_i)  # must give B_j a second here
        
        if forced & forbidden:
            return False
        
        if len(forced) > m:
            return False
        if n - len(forbidden) < m:
            return False
        
        free = [i for i in range(n) if i not in forced and i not in forbidden]
        need = m - len(forced)
        
        if need < 0 or need > len(free):
            return False
        
        for extra in combinations(free, need):
            chosen = sorted(list(forced) + list(extra))
            
            # Apply
            for i in chosen:
                col_count[i] += 1
            for j in range(n):
                _, b_i = b_trans[j][r]
                if b_i in chosen:
                    b_count[j] += 1
            
            # Check feasibility
            ok = True
            for i in range(n):
                if col_count[i] > m or col_count[i] + remain < m:
                    ok = False
                    break
            if ok:
                for j in range(n):
                    if b_count[j] > m or b_count[j] + remain < m:
                        ok = False
                        break
            
            if ok:
                solution.append(chosen)
                if backtrack(r + 1, solution):
                    return True
                solution.pop()
            
            # Undo
            for i in chosen:
                col_count[i] -= 1
            for j in range(n):
                _, b_i = b_trans[j][r]
                if b_i in chosen:
                    b_count[j] -= 1
        
        return False
    
    solution = []
    result = backtrack(0, solution)
    elapsed = time.time() - start_time
    
    if verbose:
        print(f"  Total nodes: {nodes[0]:,}, time: {elapsed:.1f}s", flush=True)
    
    if result:
        F = [[0]*n for _ in range(n)]
        for r, chosen in enumerate(solution):
            for i in chosen:
                F[r][i] = 1
        return F
    return None


def verify_full(F, L):
    """Full verification."""
    errors = []
    
    # Latin square = each pair once
    for i in range(n):
        for j in range(n):
            count = sum(1 for r in range(n) if L[r][i] == j)
            if count != 1:
                errors.append(f"Pair A{i+1}-B{j+1} count={count}")
    
    # Row sums
    for r in range(n):
        s = sum(F[r])
        if s != m:
            errors.append(f"Row {r}: sum={s}")
    
    # Col sums
    for i in range(n):
        s = sum(F[r][i] for r in range(n))
        if s != m:
            errors.append(f"Col {i}: sum={s}")
    
    # B balance
    for j in range(n):
        second = 0
        for r in range(n):
            i_match = None
            for i in range(n):
                if L[r][i] == j:
                    i_match = i
                    break
            if F[r][i_match] == 1:
                second += 1
        if second != m:
            errors.append(f"B{j+1}: second={second}")
    
    # Round B balance
    for r in range(n):
        b_first = sum(1 for i in range(n) if F[r][i] == 0)
        if b_first != m:
            errors.append(f"Round {r+1}: B first={b_first}")
    
    return errors


def format_schedule(F, L):
    """Format schedule."""
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
    return '\n'.join(lines)


def main():
    latin_squares = [
        ("D5 Cayley table", d5_cayley_table),
        ("Mixed shift/reflection", mixed_latin_square),
        ("Alternating shift/reflection", custom_latin_square_1),
        ("Shift+swap pairs", custom_latin_square_3),
    ]
    
    for name, gen_func in latin_squares:
        print(f"\n{'='*60}", flush=True)
        print(f"Trying: {name}", flush=True)
        print(f"{'='*60}", flush=True)
        
        L = gen_func()
        ok, msg = verify_latin_square(L)
        if not ok:
            print(f"  Invalid Latin square: {msg}", flush=True)
            continue
        print(f"  Latin square verified: {msg}", flush=True)
        
        print(f"  Running backtracking solver...", flush=True)
        F = solve_backtrack(L, verbose=True)
        
        if F is not None:
            print(f"\n  SOLUTION FOUND!", flush=True)
            print(f"\n  Color matrix:", flush=True)
            for r in range(n):
                print(f"    Row {r}: {F[r]}")
            
            errors = verify_full(F, L)
            if errors:
                print(f"\n  VERIFICATION ERRORS:", flush=True)
                for e in errors:
                    print(f"    {e}")
            else:
                print(f"\n  All conditions VERIFIED!", flush=True)
                print(f"\n  Schedule:", flush=True)
                print(format_schedule(F, L))
            return F, L
        else:
            print(f"  No solution with this Latin square.", flush=True)
    
    print("\nNo solution found with any Latin square!", flush=True)
    return None, None


if __name__ == '__main__':
    main()
