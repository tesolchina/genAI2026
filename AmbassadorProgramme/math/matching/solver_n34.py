#!/usr/bin/env python3
"""
Solve the team round-robin tournament for n=34, m=17.
Uses CP-SAT with an efficient formulation:
- IntVar for pairings (n^2 vars) + inverse permutations
- Element constraints for B-balance (avoids n^3 booleans)
Total ~4n^2 ≈ 4600 variables instead of ~2n^3 ≈ 78000.
"""
from ortools.sat.python import cp_model
import time
import sys

n = 34
m = 17

def solve():
    print(f"=== Efficient CP-SAT solver for n={n}, m={m} ===", flush=True)
    t0 = time.time()
    
    model = cp_model.CpModel()
    
    # L[r][i]: which B_j does A_i face in round r
    print("  Creating L (pairing) IntVars...", flush=True)
    L = [[model.NewIntVar(0, n-1, f'L_{r}_{i}') for i in range(n)] for r in range(n)]
    
    # P[r][j]: which A_i does B_j face in round r (inverse of L[r])
    print("  Creating P (inverse) IntVars...", flush=True)
    P = [[model.NewIntVar(0, n-1, f'P_{r}_{j}') for j in range(n)] for r in range(n)]
    
    # f[r][i]: 1 if A_i goes first in round r
    print("  Creating f (color) BoolVars...", flush=True)
    f = [[model.NewBoolVar(f'f_{r}_{i}') for i in range(n)] for r in range(n)]
    
    # g[r][j]: 1 if B_j goes second in round r (= f[r][P[r][j]])
    print("  Creating g (B-second) BoolVars...", flush=True)
    g = [[model.NewBoolVar(f'g_{r}_{j}') for j in range(n)] for r in range(n)]
    
    print(f"  Variables created: {4*n*n} total ({time.time()-t0:.1f}s)", flush=True)
    
    # L[r] is a permutation, P[r] is its inverse
    print("  Adding inverse permutation constraints...", flush=True)
    for r in range(n):
        model.AddInverse(L[r], P[r])
    print(f"  Inverse done ({time.time()-t0:.1f}s)", flush=True)
    
    # Each A_i faces each B_j exactly once (column AllDifferent)
    print("  Adding column AllDifferent...", flush=True)
    for i in range(n):
        model.AddAllDifferent([L[r][i] for r in range(n)])
    print(f"  Col AllDiff done ({time.time()-t0:.1f}s)", flush=True)
    
    # Element constraint: g[r][j] = f[r][ P[r][j] ]
    # B_j goes second when the A-player facing B_j goes first
    print("  Adding element constraints for g...", flush=True)
    for r in range(n):
        for j in range(n):
            model.AddElement(P[r][j], f[r], g[r][j])
    print(f"  Element done ({time.time()-t0:.1f}s)", flush=True)
    
    # Row sum: each round has m A-players going first
    print("  Adding balance constraints...", flush=True)
    for r in range(n):
        model.Add(sum(f[r][i] for i in range(n)) == m)
    
    # Column sum: each A_i goes first m times
    for i in range(n):
        model.Add(sum(f[r][i] for r in range(n)) == m)
    
    # B-balance: each B_j goes second m times
    for j in range(n):
        model.Add(sum(g[r][j] for r in range(n)) == m)
    
    print(f"  Balance done ({time.time()-t0:.1f}s)", flush=True)
    
    # Symmetry breaking
    print("  Adding symmetry breaking...", flush=True)
    # Round 0: identity pairing
    for i in range(n):
        model.Add(L[0][i] == i)
    # Round 0: first m A-players go first
    for i in range(m):
        model.Add(f[0][i] == 1)
    for i in range(m, n):
        model.Add(f[0][i] == 0)
    
    # Round 1: A_0 plays B_1 (break rotational symmetry)
    model.Add(L[1][0] == 1)
    
    setup_time = time.time() - t0
    print(f"\nModel setup: {setup_time:.1f}s", flush=True)
    
    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 600
    solver.parameters.num_search_workers = 8
    solver.parameters.log_search_progress = True
    
    # Search strategy hints
    print("Solving...", flush=True)
    status = solver.Solve(model)
    
    print(f"\nStatus: {solver.StatusName(status)}", flush=True)
    print(f"Wall time: {solver.WallTime():.1f}s", flush=True)
    
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
    return errors


def write_solution(L, F, solve_time, filename="solution_34.txt"):
    with open(filename, 'w') as out:
        out.write(f"# Team Round-Robin Tournament Solution for n={n}, m={m}\n")
        out.write(f"# 全队循环赛编排方案 n={n}, m={m}\n")
        out.write(f"# Solved by CP-SAT in {solve_time:.1f}s\n")
        out.write("# Format: player LEFT of '-' goes first / \"-\"左边的队员执先\n\n")
        
        for r in range(n):
            matches = []
            for i in range(n):
                j = L[r][i]
                if F[r][i] == 1:
                    matches.append(f"A{i+1}-B{j+1}")
                else:
                    matches.append(f"B{j+1}-A{i+1}")
            out.write(f"第{r+1}轮 {' '.join(matches)}\n")
        
        out.write(f"\n# Verification 验证\n")
        errors = verify(L, F)
        if errors:
            out.write(f"# ERRORS: {len(errors)}\n")
            for e in errors:
                out.write(f"#   {e}\n")
        else:
            out.write(f"# ALL CHECKS PASSED 全部检查通过\n")
            out.write(f"# - All {n*n} pairs exactly once / 全部{n*n}对各一次\n")
            out.write(f"# - Each round: {m} A-first, {m} B-first / 每轮{m}名A执先{m}名B执先\n")
            out.write(f"# - Each player: first={m}, second={m} / 每位队员执先{m}次执后{m}次\n")
    
    print(f"\nSolution written to {filename}", flush=True)


if __name__ == '__main__':
    L, F, solve_time = solve()
    if L is not None:
        errors = verify(L, F)
        if errors:
            print(f"\nVERIFICATION FAILED: {len(errors)} errors", flush=True)
            for e in errors[:10]:
                print(f"  {e}", flush=True)
        else:
            print(f"\nALL CHECKS PASSED!", flush=True)
        write_solution(L, F, solve_time)
    else:
        print("\nNo solution found within time limit!", flush=True)
        sys.exit(1)
