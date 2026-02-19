# More ideas for SCMP letter — from PKU/WeChat video (Ref/PKU_wechat)

**Source:** Ref/PKU_wechat.txt (transcript of PKU WeChat video, ~16 min). Processed with learnCoze pipeline (process_session.py from Knowledge-Hub/project/learnCoze).  
**Use:** Supplement work/ideas4letters.md with insights that only appear in the video, for a reader’s letter that feels closer to the team’s own story and language.

---

## Video-only insights (not in SCMP report or preprint in the same way)

### Story and emotion

- **“创造新的数字生命” / creating new digital life**  
  Speaker says that from the moment they saw “that pile of balls,” they felt able to imagine beyond 3D and to “create new digital life.” Good metaphor for letter: AI plus maths as *creating* new mathematical structures, not just optimising old ones.

- **Pomegranate (石榴子)**  
  Same image as Qi in the report: in 3D, imagine a pomegranate; replace seeds with unit spheres—how many can touch the centre? Accessible and vivid for readers.

- **14D as “梦魇” / nightmare**  
  For half a year they could not reproduce the known 1932 result in 14 dimensions; “thousands of experiments” failed. He dreamed of 1700-plus but “all hallucination.” If they couldn’t reach 1932, the AI would have had a “fatal flaw.” Shows how seriously they take *reproducing* human results before claiming new ones—strong angle for “AI suggests, humans verify.”

- **“射箭到月亮” / shooting an arrow to the moon**  
  “Until you actually shoot, you never know if the arrow will land.” “Everyone said our project would fail.” Like AlphaGo’s “divine move”—commentators called it a mistake; it turned out to be historic. You can use this to stress uncertainty and perseverance in discovery.

- **“又黑又长的路” / road long and dark**  
  “This past year, every day was algorithms, structures, numbers.” After the breakthrough, “the road ahead suddenly lit up; there seems a wider starry sky.” **PackingStar as 飞船 / spacecraft**—“not arrival, but a brand-new start.” Fits the “romance” and “new beginning” themes.

### How the two-agent idea was born

- **Human correction that the machine didn’t have**  
  To get 14D 1932, the mathematician had to *manually delete some balls*—“one bad ball ruins the whole soup.” So they asked: can a second agent simulate that “correction”? That’s the origin of the Filler–Corrector design. For the letter: the second agent came from *watching what the human did*—human intuition encoded into the system.

- **“陈栋把球问题转化成了博弈问题”**  
  “Chengdong turned the sphere problem into a game (博弈).” The second player acts like a regulariser on the huge search space. You can say: the “two players” are not a technical detail—they are the *clever idea* that made the rest possible, and they came from maths–AI collaboration.

### No training data vs “无中生有”

- **Unlike protein folding**  
  Maths has no big training set; it’s “无中生有” (creating from nothing). So this is discovery without massive labelled data—a different kind of AI for science. Good for a sentence on “AI that explores rather than interpolates.”

### Engineering and scale

- **“计算跟智能密不可分”**  
  “If you have a method that searches all answers fast, you are the smartest.” Speeding up search “turns three years into one.” So computation and intelligence are inseparable—useful for a line on why investment in both algorithms and infrastructure matters.

- **Maths + engineering team**  
  They stress working with “精兵强将” (strong engineers): GPU-native ops, mixed precision, checkpointing, parallelising every loop. Scale (15D, 20D, 30D+) and robustness (recover from crashes) came from that. Letter angle: breakthrough needed both mathematical imagination and serious engineering.

### Interpretation and “解释神”

- **“我花最多时间的工作：解读 AI 黑箱给我的数据”**  
  “The work I spent the most time on was interpreting the data from the AI black box.” He invokes the idea of 解释神 (hermeneutics / interpreting the divine): AI says “I’m better than before”—then *how* do we interpret that? For the letter: humans don’t just verify numbers; they *interpret* what the machine found.

### Young team and “浪漫”

- **“六个非常年轻的同学”**  
  “Six very young students”; “基础学科加人工智能.” “中国学者，尤其是年轻一代，真的特别厉害.” You can highlight that a small, young, cross-disciplinary team did this—and that AI’s role is to help such scientists “更高效地探索未知的宇宙,” which is “人类和机器共同探索科学的浪漫.”

### Fragments and “数字生命”

- **“碎片” / fragments**  
  After each round they decompose the matrix into geometric “fragments,” then reassemble and refill—“like cell division, constantly creating new digital life.” In the letter you could say: the system doesn’t only add spheres; it *decomposes and recombines* structures, like an exploratory life cycle.

### Counter-intuitive structures

- **No “对进球” but high symmetry**  
  Some beautiful structures have *no* antipodal pair yet very high symmetry—and they “架起引力通道” (build gravity channels) between “几何孤立星” in different dimensions, so mathematicians can see the problem in a more macro, systematic way. Ties to the preprint’s “antipodal paradigms” in plain language.

---

## Suggested new angles (from video)

1. **Human move that inspired the second agent**  
   The mathematician had to “delete bad balls” by hand to get 1932; the second agent was designed to automate that. So the architecture encodes human intuition—good for “collaboration, not replacement.”

2. **Discovery without big data**  
   Kissing number has no training set; progress is “无中生有.” Contrast with AlphaFold-style AI. One sentence can position this as a different kind of AI-for-science.

3. **Interpretation as the slow part**  
   “Most time spent interpreting the black box.” Use 解释神 lightly: machines propose, humans *interpret* and explain—science stays human at the core.

4. **Young team + PackingStar as spacecraft**  
   Six young people, maths + AI; “PackingStar is the spacecraft to explore the starry sky; not arrival, but a new start.” Fits SCMP’s “romance” and a forward-looking close.

5. **14D nightmare and verification**  
   Half a year failing to reproduce 1932; they treated that as a test of the AI. Use it to underline: before claiming new bounds, they insisted on matching known results—responsible use of AI in maths.

---

## How to combine with ideas4letters.md

- Use **ideas4letters.md** for: structure, preprint-only points, and general angles (collaboration, HK/region, trust, 1694→2025).
- Use **moreIdeas.md** for: quotes and metaphors from the video (“digital life,” “arrow to the moon,” “one bad ball,” “spacecraft,” “解释神”), the origin of the two-agent idea, the 14D story, and the young team / 浪漫 framing.
- In the letter: one or two short, vivid lines from the video (e.g. “not arrival, but a new beginning”; “human and machine exploring the universe together”) can make the piece feel closer to the people behind the result.

---

## Processing note

- **Scripts used:** `Knowledge-Hub/project/learnCoze/process_session.py` (with venv), on `Ref/PKU_wechat.mp4` and `Ref/PKU_wechat.txt`.
- **Outputs (when run completes):** `Ref/keyframes/`, `Ref/aligned_data.json`, `Ref/ChineseNotesCoze.md`.
- **This doc:** Built from the existing transcript `Ref/PKU_wechat.txt`; video processing was launched in parallel and may still be running (OCR is slow).
