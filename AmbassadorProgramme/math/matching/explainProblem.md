# Problem Explanation: Balanced Inter-Team Round-Robin Tournament Scheduling

## Setup

- Two teams: **Team A** and **Team B**.
- Each team has **n = 2m** players.
  - Team A players: $A_1, A_2, \ldots, A_n$
  - Team B players: $B_1, B_2, \ldots, B_n$

## Objective

Construct a tournament schedule (pairing table) satisfying all constraints below. The specific task is to find a valid schedule for **n = 10** (i.e., m = 5).

## Constraints

The schedule must satisfy the following four conditions simultaneously:

### (1) Complete Round-Robin Between Teams
- There are exactly **n rounds** of play.
- Every player from Team A plays against every player from Team B **exactly once** across all rounds.
- This means each round consists of **n matchups** (one-to-one pairings between A and B players), and over n rounds, every possible A-B pair is covered exactly once (an n x n Latin square structure).

### (2) Distinct Opponents Per Round + First/Second Assignment
- In each round, every player faces a **different opponent** than in any other round.
- In each matchup, one player is designated as **"first" (先手)** and the other as **"second" (后手)**. The notation `X-Y` means X goes first and Y goes second.

### (3) Per-Round Balance of First/Second
- In **every single round**, each team has exactly **m players going first** and **m players going second**.
- That is, in each round, exactly half of Team A's players go first (and the other half go second), and similarly for Team B.

### (4) Overall Balance of First/Second
- After all n rounds are completed, **every individual player** has gone first exactly **m times** and gone second exactly **m times**.

## Summary of the Combinatorial Challenge

This is not just a standard round-robin scheduling problem. The difficulty lies in simultaneously satisfying:

- **Completeness**: every A-B pair plays exactly once (Latin square / complete bipartite matching across rounds).
- **Per-round balance**: each team contributes exactly m first-players and m second-players in every round.
- **Per-player balance**: each player is first exactly m times and second exactly m times across all rounds.

The problem is essentially asking for a **balanced orthogonal Latin square** or equivalently a **doubly balanced** complete bipartite tournament schedule.

## Known Example (n = 8)

A valid solution for n = 8 (m = 4) is provided in the problem statement, demonstrating that such schedules exist. The task is to extend this to n = 10 (m = 5).

## Mathematical Context

This problem relates to several areas of combinatorial mathematics:

- **Balanced tournament design**: scheduling tournaments with fairness constraints on home/away or first/second assignments.
- **Latin squares with balance properties**: the pairing structure forms a Latin square, with additional signing (first/second) constraints.
- **Kirkman-type scheduling problems**: named after Thomas Kirkman, who studied combinatorial scheduling with balance constraints.
- **Room squares and signed Latin squares**: a Room square is a combinatorial design closely related to balanced round-robin scheduling with home/away constraints.

The challenge increases with n because the constraints interact—satisfying one constraint may conflict with another, making brute-force search impractical for large n.
