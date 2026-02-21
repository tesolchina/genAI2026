#!/usr/bin/env python3
"""
Solve n=34 with extra constraint: no 3 consecutive first or second.
Strategy: two-phase approach.
  Phase 1: Try coloring the existing Latin square from solution_34.txt
  Phase 2: If that fails, solve full problem with relaxed symmetry breaking.
"""
from ortools.sat.python import cp_model
import time
import sys

n = 34
m = 17

def read_existing_latin_square(filename="solution_34.txt"):
    """Read the Latin square from the existing solution."""
    L = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if not line.startswith('第'):
                continue
            parts = line.split()
            row = []
            for match_str in parts[1:]:
                p = match_str.split('-')
                left, right = p[0], p[1]
                if left.startswith('A'):
                    a_idx = int(left[1:]) - 1
                    b_idx = int(right[1:]) - 1
                else:
                    b_idx = int(left[1:]) - 1
                    a_idx = int(right[1:]) - 1
                row.append((a_idx, b_idx))
            perm = [0] * n
            for a_idx, b_idx in row:
                perm[a_idx] = b_idx
            L.append(perm)
    return L


def solve_coloring_only(L_fixed):
    """Phase 1: Given Latin square, find coloring with no-3-consecutive."""
    print(f"=== Phase 1: Coloring only (n={n}, m={m}) ===", flush=True)
    t0 = time.time()
    
    model = cp_model.CpModel()
    
    f = [[model.NewBoolVar(f'f_{r}_{i}') for i in range(n)] for r in range(n)]
    
    # Row sums
    for r in range(n):
        model.Add(sum(f[r][i] for i in range(n)) == m)
    
    # Column sums
    for i in range(n):
        model.Add(sum(f[r][i] for r in range(n)) == m)
    
    # B-balance using fixed L
    for j in range(n):
        terms = []
        for r in range(n):
            for i in range(n):
                if L_fixed[r][i] == j:
                    terms.append(f[r][i])
                    break
        model.Add(sum(terms) == m)
    
    # No 3 consecutive first/second for A-players
    for i in range(n):
        for r in range(n - 2):
            s = f[r][i] + f[r+1][i] + f[r+2][i]
            model.Add(s >= 1)
            model.Add(s <= 2)
    
    # No 3 consecutive for B-players
    # Build B_j's opponent map: in round r, B_j faces A_{inv[r][j]}
    inv = [[0]*n for _ in range(n)]
    for r in range(n):
        for i in range(n):
            inv[r][L_fixed[r][i]] = i
    
    for j in range(n):
        for r in range(n - 2):
            # B_j goes second = f[r][inv[r][j]] (A opponent goes first)
            s = f[r][inv[r][j]] + f[r+1][inv[r+1][j]] + f[r+2][inv[r+2][j]]
            model.Add(s >= 1)  # not 3 consecutive first for B_j
            model.Add(s <= 2)  # not 3 consecutive second for B_j
    
    print(f"  Model: {n*n} BoolVars, setup {time.time()-t0:.1f}s", flush=True)
    
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 120
    solver.parameters.num_search_workers = 8
    solver.parameters.log_search_progress = True
    
    print("  Solving...", flush=True)
    status = solver.Solve(model)
    print(f"  Status: {solver.StatusName(status)} ({solver.WallTime():.1f}s)", flush=True)
    
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        Fv = [[solver.Value(f[r][i]) for i in range(n)] for r in range(n)]
        return Fv, solver.WallTime()
    return None, solver.WallTime()


def solve_full():
    """Phase 2: Full solver with pairings + coloring + no-3-consecutive."""
    print(f"\n=== Phase 2: Full solver (n={n}, m={m}) ===", flush=True)
    t0 = time.time()
    
    model = cp_model.CpModel()
    
    L = [[model.NewIntVar(0, n-1, f'L_{r}_{i}') for i in range(n)] for r in range(n)]
    P = [[model.NewIntVar(0, n-1, f'P_{r}_{j}') for j in range(n)] for r in range(n)]
    f = [[model.NewBoolVar(f'f_{r}_{i}') for i in range(n)] for r in range(n)]
    g = [[model.NewBoolVar(f'g_{r}_{j}') for j in range(n)] for r in range(n)]
    
    for r in range(n):
        model.AddInverse(L[r], P[r])
    for i in range(n):
        model.AddAllDifferent([L[r][i] for r in range(n)])
    for r in range(n):
        for j in range(n):
            model.AddElement(P[r][j], f[r], g[r][j])
    
    for r in range(n):
        model.Add(sum(f[r][i] for i in range(n)) == m)
    for i in range(n):
        model.Add(sum(f[r][i] for r in range(n)) == m)
    for j in range(n):
        model.Add(sum(g[r][j] for r in range(n)) == m)
    
    # No 3 consecutive for A
    for i in range(n):
        for r in range(n - 2):
            s = f[r][i] + f[r+1][i] + f[r+2][i]
            model.Add(s >= 1)
            model.Add(s <= 2)
    # No 3 consecutive for B
    for j in range(n):
        for r in range(n - 2):
            s = g[r][j] + g[r+1][j] + g[r+2][j]
            model.Add(s >= 1)
            model.Add(s <= 2)
    
    # Lighter symmetry breaking (no fixing round 1 opponent)
    for i in range(n):
        model.Add(L[0][i] == i)
    for i in range(m):
        model.Add(f[0][i] == 1)
    for i in range(m, n):
        model.Add(f[0][i] == 0)
    
    print(f"  Model setup: {time.time()-t0:.1f}s", flush=True)
    
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 600
    solver.parameters.num_search_workers = 8
    solver.parameters.log_search_progress = True
    
    print("  Solving...", flush=True)
    status = solver.Solve(model)
    print(f"  Status: {solver.StatusName(status)} ({solver.WallTime():.1f}s)", flush=True)
    
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        Lv = [[solver.Value(L[r][i]) for i in range(n)] for r in range(n)]
        Fv = [[solver.Value(f[r][i]) for i in range(n)] for r in range(n)]
        return Lv, Fv, solver.WallTime()
    return None, None, solver.WallTime()


def verify(L, F):
    errors = []
    for r in range(n):
        if sorted(L[r]) != list(range(n)):
            errors.append(f"Round {r+1}: row not permutation")
    for i in range(n):
        col = [L[r][i] for r in range(n)]
        if sorted(col) != list(range(n)):
            errors.append(f"A{i+1}: col not permutation")
    for r in range(n):
        if sum(F[r]) != m:
            errors.append(f"Round {r+1}: A-first={sum(F[r])}")
    for i in range(n):
        s = sum(F[r][i] for r in range(n))
        if s != m:
            errors.append(f"A{i+1}: first={s}")
    for j in range(n):
        sec = sum(1 for r in range(n) for i in range(n) if L[r][i] == j and F[r][i] == 1)
        if sec != m:
            errors.append(f"B{j+1}: second={sec}")
    for r in range(n):
        bf = sum(1 for i in range(n) if F[r][i] == 0)
        if bf != m:
            errors.append(f"Round {r+1}: B-first={bf}")
    
    # Extra: A-players no 3 consecutive
    for i in range(n):
        for r in range(n - 2):
            s = F[r][i] + F[r+1][i] + F[r+2][i]
            if s == 0:
                errors.append(f"A{i+1}: 3 consec SECOND rounds {r+1}-{r+3}")
            if s == 3:
                errors.append(f"A{i+1}: 3 consec FIRST rounds {r+1}-{r+3}")
    
    # Extra: B-players no 3 consecutive
    for j in range(n):
        b_sec = []
        for r in range(n):
            for i in range(n):
                if L[r][i] == j:
                    b_sec.append(F[r][i])
                    break
        for r in range(n - 2):
            s = b_sec[r] + b_sec[r+1] + b_sec[r+2]
            if s == 0:
                errors.append(f"B{j+1}: 3 consec FIRST rounds {r+1}-{r+3}")
            if s == 3:
                errors.append(f"B{j+1}: 3 consec SECOND rounds {r+1}-{r+3}")
    
    return errors


def write_solution(L, F, solve_time, filename="solution_34_plus.txt"):
    with open(filename, 'w') as out:
        out.write(f"# Team Round-Robin Tournament Solution for n={n}, m={m}\n")
        out.write(f"# EXTRA: No player goes first/second 3 rounds in a row\n")
        out.write(f"# 额外约束：任何队员都不能连续三轮执先或连续三轮执后\n")
        out.write(f"# Solved by CP-SAT in {solve_time:.1f}s\n")
        out.write("# Format: player LEFT of '-' goes first\n\n")
        
        for r in range(n):
            matches = []
            for i in range(n):
                j = L[r][i]
                if F[r][i] == 1:
                    matches.append(f"A{i+1}-B{j+1}")
                else:
                    matches.append(f"B{j+1}-A{i+1}")
            out.write(f"第{r+1}轮 {' '.join(matches)}\n")
        
        out.write(f"\n# Verification\n")
        errors = verify(L, F)
        if errors:
            out.write(f"# ERRORS: {len(errors)}\n")
            for e in errors:
                out.write(f"#   {e}\n")
        else:
            out.write(f"# ALL CHECKS PASSED\n")
            out.write(f"# - All {n*n} pairs exactly once\n")
            out.write(f"# - Each round: {m} A-first, {m} B-first\n")
            out.write(f"# - Each player: first={m}, second={m}\n")
            out.write(f"# - No 3 consecutive first or second for any player\n")
    
    print(f"Solution written to {filename}", flush=True)


if __name__ == '__main__':
    # Phase 1: try existing Latin square
    try:
        L_fixed = read_existing_latin_square("solution_34.txt")
        print(f"Read Latin square from solution_34.txt ({len(L_fixed)} rounds)", flush=True)
        F, wt = solve_coloring_only(L_fixed)
        if F is not None:
            errors = verify(L_fixed, F)
            if errors:
                print(f"\nPhase 1 VERIFICATION FAILED: {len(errors)} errors", flush=True)
                for e in errors[:10]:
                    print(f"  {e}", flush=True)
                print("Falling back to Phase 2...", flush=True)
                F = None
            else:
                print(f"\nPhase 1: ALL CHECKS PASSED!", flush=True)
                write_solution(L_fixed, F, wt)
                sys.exit(0)
    except FileNotFoundError:
        print("solution_34.txt not found, skipping Phase 1", flush=True)
        F = None
    
    # Phase 2: full solver
    if F is None:
        L, F, wt = solve_full()
        if L is not None:
            errors = verify(L, F)
            if errors:
                print(f"\nPhase 2 VERIFICATION FAILED: {len(errors)} errors", flush=True)
                for e in errors[:20]:
                    print(f"  {e}", flush=True)
            else:
                print(f"\nPhase 2: ALL CHECKS PASSED!", flush=True)
            write_solution(L, F, wt)
        else:
            print("\nNo solution found!", flush=True)
            sys.exit(1)
