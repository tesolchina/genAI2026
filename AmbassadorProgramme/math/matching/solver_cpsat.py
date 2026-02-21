#!/usr/bin/env python3
"""
Solve using Google OR-Tools CP-SAT solver.
This solver simultaneously finds both the pairings (Latin square) and 
the color assignment (first/second).
"""
from ortools.sat.python import cp_model
import time

n = 10
m = 5

def solve_full():
    """Full problem: find both pairings and colors."""
    print("Setting up CP-SAT model...", flush=True)
    t0 = time.time()
    
    model = cp_model.CpModel()
    
    # y[r][i][j] = 1 if A_i plays B_j in round r
    y = [[[model.NewBoolVar(f'y_{r}_{i}_{j}') for j in range(n)] 
          for i in range(n)] for r in range(n)]
    
    # f[r][i] = 1 if A_i goes first in round r
    f = [[model.NewBoolVar(f'f_{r}_{i}') for i in range(n)] for r in range(n)]
    
    # w[r][i][j] = y[r][i][j] AND f[r][i] (A_i goes first against B_j in round r)
    w = [[[model.NewBoolVar(f'w_{r}_{i}_{j}') for j in range(n)]
          for i in range(n)] for r in range(n)]
    
    # Linking w = y AND f
    for r in range(n):
        for i in range(n):
            for j in range(n):
                # w <= y, w <= f, w >= y + f - 1
                model.Add(w[r][i][j] <= y[r][i][j])
                model.Add(w[r][i][j] <= f[r][i])
                model.Add(w[r][i][j] >= y[r][i][j] + f[r][i] - 1)
    
    # Latin square constraints
    # Each A_i plays exactly one B per round
    for r in range(n):
        for i in range(n):
            model.Add(sum(y[r][i][j] for j in range(n)) == 1)
    
    # Each B_j plays exactly one A per round
    for r in range(n):
        for j in range(n):
            model.Add(sum(y[r][i][j] for i in range(n)) == 1)
    
    # Each pair plays exactly once
    for i in range(n):
        for j in range(n):
            model.Add(sum(y[r][i][j] for r in range(n)) == 1)
    
    # f[r][i] can only be 1 if A_i plays in round r (which is always true)
    # But f[r][i] should be 0 or 1 regardless
    
    # Row sums: each round has m A going first
    for r in range(n):
        model.Add(sum(f[r][i] for i in range(n)) == m)
    
    # Column sums: each A_i goes first m times
    for i in range(n):
        model.Add(sum(f[r][i] for r in range(n)) == m)
    
    # B balance: each B_j goes second exactly m times
    # B_j goes second when w[r][i][j] = 1 for some i
    for j in range(n):
        model.Add(sum(w[r][i][j] for r in range(n) for i in range(n)) == m)
    
    # Symmetry breaking: fix round 0 to identity pairing
    for i in range(n):
        model.Add(y[0][i][i] == 1)
    
    # Fix round 0 colors: first 5 A go first
    for i in range(m):
        model.Add(f[0][i] == 1)
    for i in range(m, n):
        model.Add(f[0][i] == 0)
    
    print(f"Model setup: {time.time()-t0:.1f}s", flush=True)
    print(f"Variables: {model.Proto().variables.__len__()}", flush=True)
    
    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300
    solver.parameters.num_search_workers = 4
    solver.parameters.log_search_progress = True
    
    print("Solving...", flush=True)
    status = solver.Solve(model)
    
    print(f"\nStatus: {solver.StatusName(status)}", flush=True)
    print(f"Time: {solver.WallTime():.1f}s", flush=True)
    
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        # Extract solution
        L = [[0]*n for _ in range(n)]
        F = [[0]*n for _ in range(n)]
        
        for r in range(n):
            for i in range(n):
                F[r][i] = solver.Value(f[r][i])
                for j in range(n):
                    if solver.Value(y[r][i][j]) == 1:
                        L[r][i] = j
        
        return L, F
    
    return None, None


def verify_and_print(L, F):
    """Verify and print the schedule."""
    errors = []
    
    # Latin square check
    for r in range(n):
        if sorted(L[r]) != list(range(n)):
            errors.append(f"Row {r} not a permutation")
    for i in range(n):
        col = [L[r][i] for r in range(n)]
        if sorted(col) != list(range(n)):
            errors.append(f"Col {i} not a permutation")
    
    # Row sums
    for r in range(n):
        if sum(F[r]) != m:
            errors.append(f"Row {r} sum = {sum(F[r])}")
    
    # Col sums
    for i in range(n):
        s = sum(F[r][i] for r in range(n))
        if s != m:
            errors.append(f"A{i+1} first = {s}")
    
    # B balance
    for j in range(n):
        second = 0
        for r in range(n):
            for i in range(n):
                if L[r][i] == j and F[r][i] == 1:
                    second += 1
        if second != m:
            errors.append(f"B{j+1} second = {second}")
    
    # Round B balance
    for r in range(n):
        b_first = sum(1 for i in range(n) if F[r][i] == 0)
        if b_first != m:
            errors.append(f"Round {r+1} B_first = {b_first}")
    
    if errors:
        print("\nVERIFICATION ERRORS:")
        for e in errors:
            print(f"  {e}")
        return False
    
    print("\nAll conditions VERIFIED!", flush=True)
    
    # Print Latin square
    print("\nPairings (Latin square):")
    for r in range(n):
        print(f"  Round {r+1}: {L[r]}")
    
    # Print color matrix
    print("\nColor matrix:")
    for r in range(n):
        print(f"  Round {r+1}: {F[r]}")
    
    # Print schedule
    print("\nSchedule:")
    for r in range(n):
        matches = []
        for i in range(n):
            j = L[r][i]
            if F[r][i] == 1:
                matches.append(f"A{i+1}-B{j+1}")
            else:
                matches.append(f"B{j+1}-A{i+1}")
        print(f"第{r+1}轮 {' '.join(matches)}")
    
    return True


if __name__ == '__main__':
    L, F = solve_full()
    if L is not None:
        verify_and_print(L, F)
    else:
        print("No solution found!")
