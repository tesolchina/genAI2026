# Draft 02 — SCMP letter (kissing number / PackingStar)

I refer to your report on the Chinese team's use of AI to advance the "kissing number" problem ("Romance between scientists and AI," 19 February).

The kissing number asks how many identical balls can touch one central ball without overlapping—a question posed by Newton in 1694, still unsolved in most dimensions. PackingStar's record-breaking results, including the first advance in 13 dimensions since 1971, deserve celebration.

But the deeper lesson is that this breakthrough emerged from a genuine creative loop, not mere human supervision of AI. PackingStar discovered sphere arrangements that overturned assumptions mathematicians had held for decades. Mathematicians then interpreted those surprises and extracted new principles to push results further still. As the team said, the work they spent the most time on was "interpreting the data from the AI black box." Even a key design idea—a second agent that removes flawed choices—came from watching a mathematician delete bad entries by hand.

This is not the familiar story of AI as a faster calculator checked by humans. If we want AI-driven research to bear fruit, we should invest not just in algorithms, but in the human expertise to question, interpret, and build on what AI reveals.

---

**Word count:** ~186 words.

---

## Notes: how draft 02 addresses the "sounds trivial" problem

### Core problem with draft 01
Draft 01's thesis was "the importance of human input at every stage of AI-driven research." A reader could reasonably respond: *of course humans are important—why are you telling me this?* The argument listed human roles (posing questions, designing methods, checking meaning) but did not explain what was surprising or non-obvious about them.

### What changed

1. **From platitude to specific, non-obvious claim**  
   The new thesis is that the breakthrough **"emerged from a genuine creative loop, not mere human supervision of AI."** This immediately signals that the letter is not about the obvious need for oversight. It's about a two-way process: AI overturned human assumptions, and humans then built new theory from those surprises. That's a claim that could surprise a reader.

2. **Evidence chosen for surprise value**  
   - *AI overturned decades-old assumptions:* The paper reports that PackingStar's configurations "fundamentally challenge long-held antipodal paradigms." This is not AI doing what humans already expected—it's AI showing that humans were wrong. That inversion is what makes the loop interesting.  
   - *Human interpretation was the hardest part:* From the PKU video, the mathematician said his most time-consuming job was acting as "解释神" (interpreter)—reading meaning out of the AI's black-box outputs. This reframes the human role: not a supervisor pressing "approve," but an interpreter doing the hardest intellectual work.  
   - *Human instinct baked into AI design:* The second agent came from watching a mathematician manually delete bad entries during the "14D nightmare." Human intuition was not just applied after AI; it was encoded into the AI's own architecture.

3. **Closing reframed**  
   Draft 01 ended with "keep humans in the loop"—the very cliché we want to avoid. Draft 02 ends with a concrete ask: **invest in the human expertise to question, interpret, and build on what AI reveals.** This specifies the *kind* of human contribution (questioning, interpreting, building), not just human presence.

4. **What was cut from draft 01**  
   - "The problem itself was posed by generations of mathematicians" (true but obvious).  
   - "the team had to reproduce known results before claiming new ones" (good practice, not an argument).  
   - "Verification and interpretation… still rest with people" (too close to "of course").  
   - Quote "human and machine exploring the universe together" (poetic but vague; replaced with the more specific "interpreting the data from the AI black box").

### Sentence-by-sentence sources

**Sentence 1 — "PackingStar discovered sphere arrangements that overturned assumptions mathematicians had held for decades."**

> "several of the newly discovered configurations fundamentally challenge long-held antipodal paradigms. Rather than conforming to symmetry-driven constructions centered around antipodal pairing, these configurations exhibit asymmetric yet highly regular geometric patterns."  
> — *Paper, §Introduction ¶4 (line 183 of html)*

> "In multiple cases, they reveal deep algebraic correspondences with finite simple groups and previously unnoticed geometric relationships across dimensions."  
> — *Paper, same paragraph*

---

**Sentence 2 — "Mathematicians then interpreted those surprises and extracted new principles to push results further still."**

> "These structural insights have, in turn, inspired mathematicians to extract new and more general construction principles. Building on patterns uncovered by PackingStar, subsequent human-designed configurations have further improved existing lower bounds in several dimensions, including 22 dimensions, illustrating a productive feedback loop between AI-driven discovery and mathematical theory."  
> — *Paper, §Introduction ¶4 (line 183 of html)*

> (Abstract also): "Inspired by these patterns, humans devised further improved constructions."  
> — *Paper, Abstract (line 69 of html)*

---

**Sentence 3 — "As the team said, the work they spent the most time on was 'interpreting the data from the AI black box.'"**

> "我觉得我花了最多时间的工作，就是我去尝试解读 AI 这个黑箱带给我的这个数据。英文中有一个很好的词，可以描述我的工作……在古希腊里叫做解释神。AI 作为一个黑箱子，他就告诉你说，我比人类我比之前做到的所有值都更优，那么我们到底去怎么样去解读这个 AI 给我们这样子的灵感。"  
> Translation: "The work I spent the most time on was trying to interpret the data that the AI black box gave me. There's a good English word for my role… in ancient Greek it means 'interpreter of the gods.' The AI, as a black box, just tells you: I'm better than everything humans have achieved before. So how do we actually interpret the inspiration the AI gives us?"  
> — *PKU WeChat video, timestamp ~15:22*

---

**Sentence 4 — "Even a key design idea—a second agent that removes flawed choices—came from watching a mathematician delete bad entries by hand."**

> "复原14维到最后的时候，我需要手动的删掉一些球，它就可以复原。1932人类是有这样的能力，但是当时机器是没有的，有一些球它有点像一个老鼠害一锅汤那种感觉……那如果是这样的话，是否我们可以有一种修正的机制去识别一下这种加的不太好的球，也就是再用一个智能体来模拟人类手动修正的操作。"  
> Translation: "When recovering 14 dimensions, at the very end I needed to manually delete some balls for it to work. Humans had this ability, but the machine didn't. Some balls were like 'one bad apple spoils the barrel'—once added, they immediately destroyed the whole structure. So we thought: can we have a correction mechanism to identify badly placed balls? That is, use a second agent to simulate the human manual correction."  
> — *PKU WeChat video, timestamp ~09:35*

> (Paper's description of the resulting design): "the second agent performs delayed and selective corrections by leveraging a more global understanding of matrix, dynamically removing invalid or inconsistent entries and compressing the first agent's search space."  
> — *Paper, §Introduction ¶3 (line 171 of html)*
