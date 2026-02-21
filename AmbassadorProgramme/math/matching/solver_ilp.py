#!/usr/bin/env python3
"""
ILP solver for n=10 team tournament scheduling.
Uses PuLP to find exact solutions.
"""
from pulp import *
import sys

n = 10
m = 5

def try_with_shifts(shifts, verbose=True):
    """Try to find color matrix F for given shift ordering."""
    if verbose:
        print(f"Trying shifts: {shifts}", flush=True)
    
    prob = LpProblem("tournament", LpMinimize)
    
    # Binary variables: F[r][i] = 1 iff A_i goes first in round r
    F = [[LpVariable(f"F_{r}_{i}", 0, 1, cat='Binary') for i in range(n)] for r in range(n)]
    
    # Dummy objective
    prob += 0
    
    # Row sums = m
    for r in range(n):
        prob += lpSum(F[r][i] for i in range(n)) == m
    
    # Column sums = m
    for i in range(n):
        prob += lpSum(F[r][i] for r in range(n)) == m
    
    # B-player balance: for each B_j, goes second exactly m times
    # B_j goes second in round r iff F[r][sigma_r^{-1}(j)] = 1
    # sigma_r(i) = (i + shifts[r]) % n, so sigma_r^{-1}(j) = (j - shifts[r]) % n
    for j in range(n):
        prob += lpSum(F[r][(j - shifts[r]) % n] for r in range(n)) == m
    
    # Solve
    prob.solve(PULP_CBC_CMD(msg=0))
    
    if prob.status == 1:
        result = [[int(value(F[r][i])) for i in range(n)] for r in range(n)]
        if verbose:
            print("  SOLUTION FOUND!", flush=True)
        return result
    else:
        if verbose:
            print(f"  No solution (status={prob.status})", flush=True)
        return None


def verify_full(F, shifts):
    """Full verification of all constraints."""
    errors = []
    
    # Each pair plays exactly once
    played = [[False]*n for _ in range(n)]
    for r in range(n):
        s = shifts[r]
        for i in range(n):
            j = (i + s) % n
            if played[i][j]:
                errors.append(f"Duplicate: A{i+1}-B{j+1}")
            played[i][j] = True
    for i in range(n):
        for j in range(n):
            if not played[i][j]:
                errors.append(f"Missing: A{i+1}-B{j+1}")
    
    # Row sums
    for r in range(n):
        s = sum(F[r])
        if s != m:
            errors.append(f"Row {r}: sum={s}")
    
    # Column sums
    for i in range(n):
        s = sum(F[r][i] for r in range(n))
        if s != m:
            errors.append(f"Col {i}: sum={s}")
    
    # B balance
    for j in range(n):
        first_count = 0
        second_count = 0
        for r in range(n):
            sh = shifts[r]
            i = (j - sh) % n
            if F[r][i] == 1:
                second_count += 1
            else:
                first_count += 1
        if first_count != m:
            errors.append(f"B{j+1}: first={first_count}")
    
    # Per-round B balance
    for r in range(n):
        b_first = sum(1 for i in range(n) if F[r][i] == 0)
        if b_first != m:
            errors.append(f"Round {r+1}: B_first={b_first}")
    
    return errors


def format_schedule(F, shifts):
    """Format in Chinese chess tournament notation."""
    lines = []
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
        lines.append(f"第{r+1}轮 {' '.join(matches)}")
    return '\n'.join(lines)


def main():
    print("=" * 60, flush=True)
    print("ILP Solver for n=10 Tournament Schedule", flush=True)
    print("=" * 60, flush=True)
    
    # Try 1: Simple cyclic shifts s_r = r
    print("\n--- Attempt 1: shifts = [0,1,2,...,9] ---", flush=True)
    shifts = list(range(n))
    F = try_with_shifts(shifts)
    
    if F is None:
        # Try 2: Shifts like n=8 example (evens first, then odds)
        print("\n--- Attempt 2: shifts = [0,2,4,6,8,1,3,5,7,9] ---", flush=True)
        shifts = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        F = try_with_shifts(shifts)
    
    if F is None:
        # Try 3: Other orderings
        orderings = [
            [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],
            [0, 5, 1, 6, 2, 7, 3, 8, 4, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 4, 8, 2, 6, 1, 5, 9, 3, 7],
            [0, 7, 4, 1, 8, 5, 2, 9, 6, 3],
            [0, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            [0, 6, 2, 8, 4, 1, 7, 3, 9, 5],
        ]
        for idx, shifts in enumerate(orderings):
            print(f"\n--- Attempt {idx+3}: shifts = {shifts} ---", flush=True)
            F = try_with_shifts(shifts)
            if F is not None:
                break
    
    if F is None:
        # Try 4: General approach - optimize over shifts too
        # Use a different Latin square (not cyclic shifts)
        print("\n--- Attempt: General Latin square approach ---", flush=True)
        F, shifts = solve_general()
    
    if F is not None:
        print("\n" + "=" * 60, flush=True)
        print("SOLUTION FOUND!", flush=True)
        print("=" * 60, flush=True)
        
        print(f"\nShifts used: {shifts}", flush=True)
        print("\nColor matrix F:", flush=True)
        for r in range(n):
            print(f"  Row {r}: {F[r]}")
        
        errors = verify_full(F, shifts)
        if errors:
            print("\nVERIFICATION ERRORS:", flush=True)
            for e in errors:
                print(f"  X {e}")
        else:
            print("\nAll conditions VERIFIED OK!", flush=True)
        
        print("\nSchedule:", flush=True)
        print(format_schedule(F, shifts))
    else:
        print("\nNO SOLUTION FOUND with any approach!", flush=True)
        sys.exit(1)
    
    return F, shifts


def solve_general():
    """
    General ILP: optimize over both pairings (Latin square) and colors.
    Variables: P[r][i][j] = 1 iff A_i plays B_j in round r
               F[r][i] = 1 iff A_i goes first in round r
    """
    print("Setting up general ILP (may be slow)...", flush=True)
    
    prob = LpProblem("tournament_general", LpMinimize)
    prob += 0  # dummy objective
    
    # Pairing variables
    P = [[[LpVariable(f"P_{r}_{i}_{j}", 0, 1, cat='Binary') 
            for j in range(n)] for i in range(n)] for r in range(n)]
    
    # Color variables
    # C[r][i][j] = 1 iff A_i plays B_j in round r AND A_i goes first
    C = [[[LpVariable(f"C_{r}_{i}_{j}", 0, 1, cat='Binary')
            for j in range(n)] for i in range(n)] for r in range(n)]
    
    # C[r][i][j] <= P[r][i][j]
    for r in range(n):
        for i in range(n):
            for j in range(n):
                prob += C[r][i][j] <= P[r][i][j]
    
    # Latin square constraints for P
    # Each A_i plays exactly one B in each round
    for r in range(n):
        for i in range(n):
            prob += lpSum(P[r][i][j] for j in range(n)) == 1
    
    # Each B_j plays exactly one A in each round  
    for r in range(n):
        for j in range(n):
            prob += lpSum(P[r][i][j] for i in range(n)) == 1
    
    # Each pair (A_i, B_j) plays exactly once
    for i in range(n):
        for j in range(n):
            prob += lpSum(P[r][i][j] for r in range(n)) == 1
    
    # F[r][i] = sum_j C[r][i][j] (A_i goes first = sum of C over all possible B opponents)
    # Row sums: each round has m A-players going first
    for r in range(n):
        prob += lpSum(C[r][i][j] for i in range(n) for j in range(n)) == m
    
    # Column sums: each A_i goes first m times
    for i in range(n):
        prob += lpSum(C[r][i][j] for r in range(n) for j in range(n)) == m
    
    # B balance: each B_j is second m times (equivalently, first m times)
    # B_j goes second when C[r][i][j] = 1 (meaning A_i goes first against B_j)
    for j in range(n):
        prob += lpSum(C[r][i][j] for r in range(n) for i in range(n)) == m
    
    # Per-round B balance: each round has m B going first
    # B goes first = P[r][i][j] - C[r][i][j] = 1
    for r in range(n):
        b_first = lpSum(P[r][i][j] - C[r][i][j] for i in range(n) for j in range(n))
        prob += b_first == m
    
    print("Solving general ILP...", flush=True)
    prob.solve(PULP_CBC_CMD(msg=1, timeLimit=300))
    
    if prob.status == 1:
        # Extract solution
        # Find shifts
        shifts = []
        F_matrix = []
        for r in range(n):
            shift_val = None
            f_row = [0]*n
            for i in range(n):
                for j in range(n):
                    if value(P[r][i][j]) > 0.5:
                        if i == 0:
                            shift_val = j
                        if value(C[r][i][j]) > 0.5:
                            f_row[i] = 1
            shifts.append(shift_val)
            F_matrix.append(f_row)
        
        print(f"  General ILP found solution! Shifts: {shifts}", flush=True)
        return F_matrix, shifts
    else:
        print(f"  General ILP: no solution (status={prob.status})", flush=True)
        return None, None


if __name__ == '__main__':
    main()
