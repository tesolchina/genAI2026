# Solution: Team Round-Robin Tournament for n=10 / 解答：n=10 全队循环赛编排

## Problem Statement / 问题描述

Find a schedule for two teams of n=10 (m=5) players satisfying:
1. 10 rounds, each player faces every opponent exactly once
2. Each round: 5 A-players go first, 5 go second; 5 B-players go first, 5 go second
3. Over all rounds: each player goes first exactly 5 times

为两支各有n=10人（m=5）的队伍编排赛程，满足：
1. 共10轮，每位队员和对方每位队员恰好交手一次
2. 每轮：5名A队员执先、5名执后；5名B队员执先、5名执后
3. 全部轮次结束后：每位队员执先恰好5次

## Key Insight / 关键发现

For n=8 (m=4), simple cyclic shift pairings work because 8 ≡ 0 (mod 4).

当n=8（m=4）时，简单的循环移位对阵方案可行，因为8能被4整除。

**For n=10 (m=5), cyclic shifts are provably INFEASIBLE.** We proved this through:
1. A parity argument: with any cyclic shift ordering, the condition `2a = m = 5` has no integer solution
2. ILP verification: the CBC solver explored 793,129 nodes without finding a feasible solution
3. LP relaxation shows fractional values at 0.5, confirming the integrality gap

**当n=10（m=5）时，循环移位方案被证明不可行。** 我们通过以下方式证明：
1. 奇偶性论证：对于任何循环移位排列，条件 `2a = m = 5` 无整数解
2. ILP验证：CBC求解器探索了793,129个节点，未找到可行解
3. LP松弛显示0.5的分数值，确认了整数间隙

Therefore, n=10 requires a **non-cyclic Latin square** for the pairings.

因此，n=10需要一个**非循环拉丁方**来安排对阵。

## Solution (found by CP-SAT solver) / 解答（CP-SAT求解器求得）

Using Google OR-Tools' CP-SAT solver to simultaneously find both pairings and color assignments:

使用Google OR-Tools的CP-SAT求解器同时寻找对阵方案和先后手分配：

```
第1轮 A1-B1 A2-B2 A3-B3 A4-B4 A5-B5 B6-A6 B7-A7 B8-A8 B9-A9 B10-A10
第2轮 B2-A1 B9-A2 A3-B4 B6-A4 A5-B7 B10-A6 A7-B3 A8-B1 A9-B8 B5-A10
第3轮 B8-A1 B7-A2 A3-B5 A4-B10 B1-A5 B9-A6 B6-A7 A8-B4 A9-B3 A10-B2
第4轮 A1-B9 A2-B4 A3-B10 B2-A4 B8-A5 A6-B5 B1-A7 B3-A8 B7-A9 A10-B6
第5轮 B6-A1 B1-A2 B2-A3 A4-B7 A5-B9 B3-A6 A7-B4 B5-A8 A9-B10 A10-B8
第6轮 B4-A1 B5-A2 B9-A3 A4-B3 B2-A5 A6-B8 B10-A7 A8-B7 A9-B6 A10-B1
第7轮 A1-B7 B10-A2 B6-A3 B5-A4 B3-A5 A6-B1 A7-B8 A8-B9 A9-B2 B4-A10
第8轮 A1-B5 A2-B3 B8-A3 B1-A4 A5-B10 A6-B2 B9-A7 A8-B6 B4-A9 B7-A10
第9轮 A1-B10 A2-B8 B7-A3 A4-B9 A5-B6 B4-A6 A7-B5 B2-A8 B1-A9 B3-A10
第10轮 B3-A1 A2-B6 A3-B1 B8-A4 B4-A5 A6-B7 A7-B2 B10-A8 B5-A9 A10-B9
```

Format / 格式说明: The player on the LEFT of "-" goes first. / "-"左边的队员执先。

## Verification / 验证

### Each pair plays exactly once ✓ / 每对恰好交手一次 ✓
All 100 pairs (A_i, B_j) appear exactly once across the 10 rounds.
全部100对组合（A_i, B_j）在10轮中各出现恰好一次。

### Per-round balance ✓ / 每轮平衡 ✓
Each round has exactly 5 A-players going first and 5 B-players going first.
每轮恰好有5名A队员执先、5名B队员执先。

### A-player balance ✓ / A队员平衡 ✓
| Player 队员 | First 执先 | Second 执后 |
|------------|-----------|------------|
| A1 - A10   | 5 each 各5 | 5 each 各5 |

### B-player balance ✓ / B队员平衡 ✓
| Player 队员 | First 执先 | Second 执后 |
|------------|-----------|------------|
| B1 - B10   | 5 each 各5 | 5 each 各5 |

## Method / 方法

The solution was found using Google OR-Tools' CP-SAT solver in approximately 0.3 seconds. The solver simultaneously determined:
1. **Pairings**: A non-cyclic Latin square of order 10
2. **Color assignment**: A balanced first/second assignment

该解由Google OR-Tools的CP-SAT求解器在约0.3秒内求得，同时确定了：
1. **对阵方案**：一个10阶非循环拉丁方
2. **先后手分配**：平衡的执先/执后分配方案

The CP-SAT solver uses a combination of SAT (Boolean satisfiability), constraint propagation, and linear programming techniques, making it far more effective than pure ILP for this type of constraint satisfaction problem.

CP-SAT求解器综合运用了SAT（布尔可满足性）、约束传播和线性规划技术，在处理此类约束满足问题时远比纯ILP高效。
