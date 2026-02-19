# AI maths breakthrough shows the real value lies in the creative loop

I refer to your report on the Chinese team's use of AI to advance the "kissing number" problem ("Romance between scientists and AI," 19 February).

The kissing number asks how many identical balls can touch one central ball without overlapping—a question Newton posed in 1694, still unsolved in most dimensions. PackingStar's record-breaking results, including the first advance in 13 dimensions since 1971, deserve celebration.

Your headline calls this a "romance," and the metaphor runs deeper than it might seem. A key design idea—a second AI agent that removes flawed choices—came from watching a mathematician delete bad entries by hand: the team taught their machine to mimic human instinct. But the machine returned the favour, discovering sphere arrangements that overturned assumptions held for decades. Their hardest task was "interpreting the data from the AI black box"—reading meaning into surprises neither side could have produced alone.

That is what makes this a genuine romance, not mere human oversight of a fast calculator: each partner transforms the other. If we want AI-driven research to bear fruit, we should invest not just in algorithms, but in the human expertise to question, interpret, and build on what AI reveals.

---

**Word count:** ~194 words.

---

## Notes: how this revision strengthens the argument

### What changed from the previous draft

1. **Echoes the SCMP "romance" metaphor**  
   The previous draft introduced "creative loop" as a standalone concept. This revision picks up the SCMP's own word—"romance"—and shows it is not just poetic language but structurally accurate. A romance is bidirectional: both partners change each other. That framing makes the argument immediately intuitive to readers of the original report.

2. **Two-way transformation made explicit**  
   - *Human → AI:* The Corrector agent was literally designed to simulate what a mathematician did by hand—deleting "bad balls" during the 14D problem. Human instinct was encoded into the AI's architecture.  
   - *AI → Human:* PackingStar discovered configurations that "fundamentally challenge long-held antipodal paradigms." The AI did not confirm what mathematicians expected; it showed them they were wrong, inspiring new construction principles.  
   - This bidirectional exchange is what elevates the partnership beyond the familiar "AI as tool" narrative.

3. **"Returned the favour" as pivot**  
   The sentence "But the machine returned the favour" is the rhetorical turn. It moves from the expected (humans design AI) to the surprising (AI teaches humans something new). This is the non-obvious claim that prevents readers from thinking "of course humans matter."

4. **Closing ties back to "romance"**  
   "That is what makes this a genuine romance, not mere human oversight of a fast calculator" — the closing now directly echoes and reinterprets the headline, giving readers a richer understanding of the word they already read.

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
