# Online Search Results: Balanced Inter-Team Round-Robin Tournament Scheduling

## Search Summary

**Problem**: Given two teams A and B each with n=2m players, construct a schedule of n rounds where:
1. Every A-player plays every B-player exactly once
2. Each round is a perfect matching between teams (distinct opponents per round)
3. Each round has exactly m players from each team going first and m going second
4. Each individual player goes first exactly m times and second exactly m times overall

**Target**: Find a solution for **n = 10** (m = 5).

---

## Verdict: No Direct Solution Found Online

After extensive searching across ArXiv, MathOverflow, Math StackExchange, combinatorics journals, Chinese math/Go forums, and tournament scheduling resources, **no exact online solution was found for this specific problem with n=10**. The problem appears to be a niche variant that combines several well-studied constraints in a way that hasn't been explicitly addressed in the literature we found.

However, several closely related mathematical frameworks and papers provide **ideas and methods** that can be used to construct or find a solution. These are detailed below.

---

## Closely Related Mathematical Concepts

### 1. Balanced Tournament Designs (BTD)

**Relevance**: HIGH — BTDs are the closest standard combinatorial design to this problem.

A BTD(n) is an n × (2n−1) array on 2n elements where each cell contains a pair, every pair appears once, each element appears once per column, and no element appears more than twice per row. BTDs exist for all n except n=2.

- **Paper**: E. R. Lamken, S. A. Vanstone. *Balanced Tournament Designs and Related Topics*. Discrete Mathematics, Vol. 77, 1989.
  - [https://www.sciencedirect.com/science/article/pii/0012365X89903580](https://www.sciencedirect.com/science/article/pii/0012365X89903580)

- **Thesis**: *The Existence of Balanced Tournament Designs and Partitioned Balanced Tournament Designs*. University of Waterloo.
  - [https://uwspace.uwaterloo.ca/handle/10012/1178](https://uwspace.uwaterloo.ca/handle/10012/1178)

- **Paper**: *Balanced tournament designs with almost orthogonal resolutions*. Journal of the Australian Mathematical Society.
  - [https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/balanced-tournament-designs-with-almost-orthogonal-resolutions/4015BAF76A4BD3CC399FF665CF74C87B](https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/balanced-tournament-designs-with-almost-orthogonal-resolutions/4015BAF76A4BD3CC399FF665CF74C87B)

**Note**: BTDs address "all-play-all" within a single pool of 2n players, not the bipartite (Team A vs Team B) variant in our problem. However, the mathematical techniques (Latin squares, resolutions) are directly applicable.

---

### 2. Fair Schedules for Round Robin Tournaments (ArXiv 2025)

**Relevance**: MEDIUM-HIGH — Addresses fairness of home/away (first/second) scheduling.

A recent paper introduces "ranking-fair schedules" for single round robin tournaments, proving existence when the number of participants is a multiple of 4. Shows that the standard Circle Method fails for n > 8.

- **Paper**: Sten Wessel, Cor Hurkens, Frits Spieksma. *Fair Schedules for Single Round Robin Tournaments with Ranked Participants*. arXiv:2502.04159, February 2025.
  - [https://arxiv.org/abs/2502.04159](https://arxiv.org/abs/2502.04159)
  - [PDF](https://arxiv.org/pdf/2502.04159)

**Key insight**: The standard Circle Method (the most common scheduling algorithm) cannot produce ranking-fair schedules for more than 8 teams. This may explain why simple cyclic constructions fail for n=10 in our problem.

---

### 3. Room Squares and Howell Designs

**Relevance**: MEDIUM — Related balanced designs with pairing and signing constraints.

A Room square is an n×n array filled with n+1 symbols, used in bridge tournament scheduling. Room squares exist only for odd n (except n=3,5), so they don't directly apply to n=10. Howell designs H(s,2n) generalize Room squares and have been completely characterized.

- **Wikipedia**: Room square
  - [https://en.wikipedia.org/wiki/Room_square](https://en.wikipedia.org/wiki/Room_square)

- **Encyclopedia of Mathematics**: Howell design
  - [https://encyclopediaofmath.org/wiki/Howell_design](https://encyclopediaofmath.org/wiki/Howell_design)

- **Paper**: *Complete balanced Howell rotations for 8k+5 teams*. Discrete Mathematics.
  - [https://www.sciencedirect.com/science/article/pii/0012365X82901376](https://www.sciencedirect.com/science/article/pii/0012365X82901376)

---

### 4. Latin Square Constructions for Tournament Scheduling

**Relevance**: HIGH — The pairing structure of our problem IS a Latin square.

In our problem, the assignment of who plays whom across rounds forms a Latin square (each A-player plays each B-player exactly once). The "signing" (first/second) is an additional constraint on top of this Latin square. Construction methods using modular arithmetic are standard.

- **Cut-the-Knot**: Latin Squares - Simple Construction
  - [http://cut-the-knot.org/arithmetic/latin2.shtml](http://cut-the-knot.org/arithmetic/latin2.shtml)

- **Wikipedia**: Mutually Orthogonal Latin Squares
  - [https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares](https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares)

**Key idea**: For our problem, the pairing can be described by cyclic shifts: in round r, player A_i plays B_{(i + s_r) mod n}, where s_0, s_1, ..., s_{n-1} are a permutation of {0, 1, ..., n-1}. The challenge is finding a "signing matrix" F (n×n binary matrix with row sums = column sums = m) that also satisfies the B-player balance constraint.

---

### 5. Home/Away Pattern Scheduling

**Relevance**: MEDIUM — Addresses the first/second (home/away) assignment problem in round-robin tournaments.

- **Paper**: *Scheduling Partial Round Robin Tournaments Subject to Home Away Pattern Sets*. Electronic Journal of Combinatorics.
  - [https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r55/pdf](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r55/pdf)

- **Paper**: *Constructing fair round robin tournaments with a minimum number of breaks*. Operations Research Letters.
  - [https://www.sciencedirect.com/science/article/abs/pii/S0167637710001124](https://www.sciencedirect.com/science/article/abs/pii/S0167637710001124)

- **Tutorial PDF**: Pim van 't Hof. *Round Robin Scheduling*.
  - [https://pimvanthof.github.io/rr.pdf](https://pimvanthof.github.io/rr.pdf)

- **Paper**: *The flexibility of home away pattern sets*. Journal of Scheduling, 2022.
  - [https://link.springer.com/content/pdf/10.1007/s10951-022-00734-w.pdf](https://link.springer.com/content/pdf/10.1007/s10951-022-00734-w.pdf)

---

### 6. Complete Mixed Doubles Round Robin Tournaments (ArXiv)

**Relevance**: MEDIUM — Involves balanced scheduling between two groups with crossing constraints.

- **Paper**: D. R. Berman, M. Wakeling. *Complete Mixed Doubles Round Robin Tournaments*. arXiv:1310.5240, 2013.
  - [https://arxiv.org/abs/1310.5240](https://arxiv.org/abs/1310.5240)
  - [PDF](https://arxiv.org/pdf/1310.5240)

---

### 7. All-Play-All Tournament Designs (Practical Schedules)

**Relevance**: LOW-MEDIUM — Provides practical tournament designs with left/right balance for 10 players (but single-pool, not bipartite).

Julian D. A. Wiseman provides concrete tournament designs for 10 players with venue and left-right balance optimization. While this is for all-play-all (not two-team), the left-right balancing techniques are informative.

- **10-player design**: [https://jdawiseman.com/papers/tournaments/all-play-all/apa_10.html](https://jdawiseman.com/papers/tournaments/all-play-all/apa_10.html)
- **Main explanation**: [https://jdawiseman.com/papers/tournaments/all-play-all/all-play-all.html](https://jdawiseman.com/papers/tournaments/all-play-all/all-play-all.html)

---

### 8. Bipartite Traveling Tournament Problem (ArXiv 2025)

**Relevance**: LOW — Addresses bipartite inter-league scheduling but focuses on travel distance, not first/second balance.

- **Paper**: *An Improved Algorithm for a Bipartite Traveling Tournament in Interleague Sports Scheduling*. arXiv:2505.06828.
  - [https://arxiv.org/abs/2505.06828](https://arxiv.org/abs/2505.06828)

---

### 9. A Variant of the Round-Robin Scheduling Problem

**Relevance**: LOW — Different variant (team reshuffling, not fixed teams).

- **Paper**: Chris Busenhart, Norbert Hungerbühler, William Xu. *A Variant of the Round-Robin Scheduling Problem*. Ars Combinatoria, Volume 158, 2024.
  - [https://combinatorialpress.com/ars-articles/volume-158/a-variant-of-the-round-robin-scheduling-problem/](https://combinatorialpress.com/ars-articles/volume-158/a-variant-of-the-round-robin-scheduling-problem/)

---

### 10. Chinese-Language Resources on Go Tournament Scheduling

**Relevance**: MEDIUM — Practical scheduling rules for Go (围棋) tournaments with first/second hand (先后手) balance.

- **101围棋网 — 积分编排制**: Describes the practical principles for balancing black/white (first/second) assignments in Go tournament pairing.
  - [https://doc.101weiqi.com/room/jifenbianpai/](https://doc.101weiqi.com/room/jifenbianpai/)

- **Wikipedia 循环赛**: Standard round-robin tournament scheduling in Chinese.
  - [https://zh.wikipedia.org/wiki/循环赛](https://zh.wikipedia.org/wiki/%E5%BE%AA%E7%8E%AF%E8%B5%9B)

- **秋雨夜象棋网 — 赛制简介循环制**: Chinese chess round-robin scheduling conventions, including the rule that the team listed first plays first on odd-numbered boards and second on even-numbered boards.
  - [https://blog.sina.com.cn/s/blog_3f19d0c20101f7qw.html](https://blog.sina.com.cn/s/blog_3f19d0c20101f7qw.html)

**Note**: These resources describe practical tournament conventions but do not provide a mathematical construction for the specific 4-constraint problem we are solving.

---

## Summary of Ideas for Solving the Problem

Based on the literature search, the most promising approaches for finding an n=10 solution are:

1. **ILP / Constraint Programming** (already implemented in `solver_ilp.py`): Model the full problem as an integer linear program. The general ILP formulation with pairing variables P[r][i][j] and color variables C[r][i][j] is correct and should find a solution if one exists, though it has O(n^3) binary variables.

2. **Cyclic Latin square + balanced signing matrix**: Fix the pairing structure as cyclic shifts (A_i plays B_{(i+s_r) mod n}), then search for a {0,1}-signing matrix F with doubly balanced row/column sums AND B-player balance. The key insight from the ArXiv 2025 paper is that standard cyclic methods may not work for n=10.

3. **Non-cyclic Latin square constructions**: Consider non-cyclic pairings (e.g., based on finite field constructions or other algebraic methods) that may admit balanced signings more naturally.

4. **Decomposition approach**: Treat the problem as decomposing the complete bipartite graph K_{10,10} into 10 directed perfect matchings, where each matching has 5 edges oriented in each direction, and the in-degree and out-degree of every vertex across all matchings equals 5.

---

*Search conducted: February 16, 2026*
*Sources searched: ArXiv, Google Scholar, MathOverflow, Math StackExchange, ScienceDirect, Springer, Cambridge Core, Wikipedia, Chinese math/Go forums, combinatorial press journals*
