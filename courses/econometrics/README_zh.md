# 计量经济学 Claude Code 工作流：本地复现说明

本文档说明如何基于 Pedro Sant'Anna 开源的 Claude Code 学术工作流，在 Cursor / VS Code 环境下复现并用于计量经济学科研与教学。原始介绍见 [wechatPost.md](./wechatPost.md)，任务来源见 [fetchGitHub.md](./fetchGitHub.md)。

---

## 一、背景与来源

- **作者**：Pedro Sant'Anna（Emory 大学经济学教授，Journal of Econometrics / JBES 副主编）
- **代表作**：Callaway & Sant'Anna (2021, JoE) 交错 DID，Google Scholar 引用超 1 万次
- **产出**：Econ 730: Causal Panel Data 博士课——6 套讲义、800+ 页幻灯片、配套 R 代码
- **许可**：MIT，可直接 fork 使用

**核心引用**（来自 [wechatPost.md](./wechatPost.md)）：

> 他不是给它一个个小指令，而是描述你要什么结果，然后它自己完成从规划到实施到质检的全过程。  
> … 每个文件最终会得到一个 0 到 100 的质量分数，80 分以下不允许提交到版本库。

---

## 二、本仓库中的复现内容

| 内容 | 位置 | 说明 |
|------|------|------|
| 微信文章解读 | [wechatPost.md](./wechatPost.md) | 工作流解读与借鉴要点 |
| 上游模板仓库（完整克隆） | [claude-code-my-workflow/](./claude-code-my-workflow/) | [pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) 的本地克隆，含 `.claude/`、规则、技能、Agent 等 |
| 工作流图示与操作说明 | [ideas.html](./ideas.html) | 端到端流程、在 Cursor/VS Code 中的用法、链接与摘录 |
| 本说明 | README_zh.md | 整体流程与复现步骤（中文） |

---

## 三、整体流程概览

1. **获取模板**  
   - 使用本仓库中已克隆的 `claude-code-my-workflow/`，或自行 fork 并 clone 上游：[https://github.com/pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)。

2. **环境**  
   - 安装 [Claude Code](https://code.claude.com/docs/en/overview)（`npm install -g @anthropic-ai/claude-code`）。  
   - 可选：XeLaTeX、Quarto、R、pdf2svg、gh CLI（按需安装，见上游 [README](https://github.com/pedrohcgs/claude-code-my-workflow#prerequisites)）。

3. **在 Cursor / VS Code 中使用**  
   - **Cursor**：在项目根目录打开 `claude-code-my-workflow`（或你 fork 的项目），用 Cursor 的 AI 助手 + 项目内 `.claude` 规则/技能，实现“描述任务 → 规划 → 执行 → 多 Agent 审查 → 质量门控”的流程。  
   - **VS Code + Claude Code 插件**：在 VS Code 中打开同一项目，使用 Claude Code 面板；流程与 CLI 类似，部分高级功能（如 agent teams）可能仍以 CLI 为完整。  
   - 详细步骤、提示词与链接见 [ideas.html](./ideas.html)。

4. **适配自己的项目**  
   - 复制或 fork 模板后，按上游 [Quick Start](https://github.com/pedrohcgs/claude-code-my-workflow#quick-start-5-minutes) 的“粘贴提示词”步骤，让 Claude 根据你的项目名、机构、工具链填写 `CLAUDE.md` 等占位符。  
   - 根据需要修改 `.claude/rules`、`.claude/agents`、`.claude/skills`（参见上游 [Adapting for Your Field](https://github.com/pedrohcgs/claude-code-my-workflow#adapting-for-your-field)）。

5. **单一真相源与复现协议**  
   - 论文/幻灯中的表格、数字只在一处定义（如 R 输出），其余从该处派生。  
   - 扩展模型前先自动复现原始结果，并设数值容差（点估计、标准误、覆盖率等），未通过则提示。

6. **探索与正式分离**  
   - 试探性分析放在 `explorations/`，质量门槛 60 分、流程简化；正式代码 80 分才可提交，PR 90 分等（见 [ideas.html](./ideas.html) 与上游 [Quality Gates](https://github.com/pedrohcgs/claude-code-my-workflow#quality-gates)）。

---

## 四、参考链接（与 ideas.html 一致）

- [Pedro Sant'Anna - Claude Code: My Workflow (Blog)](https://psantanna.com/claude-code-my-workflow/)
- [GitHub: pedrohcgs/claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow)
- [Pedro Sant'Anna - Emory University Faculty](https://economics.emory.edu/people/faculty/biography/sant-anna-pedro.html)
- [Callaway & Sant'Anna (2021), Journal of Econometrics](https://doi.org/10.1016/j.jeconom.2020.12.001)
- [Pedro Sant'Anna - Google Scholar](https://scholar.google.com/citations?user=BVWmSY4AAAAJ&hl=en)
- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Full workflow guide (Quarto)](https://psantanna.com/claude-code-my-workflow/workflow-guide.html)

---

## 五、在 Cursor 中“复现”的含义

- **复现**：在本机或 Cursor 工作区内使用与 Sant'Anna 相同的**工作流设计**（规划优先、承包商模式、多 Agent 审查、质量门控、探索/正式分离、单一真相源、复现协议）。  
- **实现方式**：  
  - 使用本仓库中已克隆的 `claude-code-my-workflow` 作为项目模板，在 Cursor 中打开该项目；或  
  - 在 Cursor 中打开你自己 fork 的同一仓库。  
- Cursor 的 AI 可读写项目内文件、执行命令，与 Claude Code CLI 类似；你可以通过项目内的 `CLAUDE.md`、`.claude/rules`、`.claude/skills` 等约束与引导行为，使“规划 → 实施 → 审查 → 打分”的流程在 Cursor 中可复现。  
- 更细的提示词、质量分数含义、以及“能在 Cursor / VS Code 做到什么程度”的说明，见 [ideas.html](./ideas.html)。

---

## 六、发布 ideas.html 到 GitHub Pages

- 若仓库已启用 GitHub Pages（来源：`main` 分支的 `docs/` 目录）：  
  - 将 [ideas.html](./ideas.html) 复制到仓库根目录下的 `docs/` 中（例如 `docs/ideas.html`），提交并推送后，页面地址一般为：  
    `https://<你的用户名>.github.io/genAI2026/ideas.html`  
  - 具体以仓库的 **Settings → Pages** 中配置为准。  
- 若尚未启用：在 GitHub 仓库 **Settings → Pages** 中选择 Source 为 **main**、文件夹为 **/docs**，保存后等待生成即可。

---

*本 README 与 ideas.html 由 [fetchGitHub.md](./fetchGitHub.md) 中的任务生成，旨在便于在 Cursor/VS Code 中复现并理解 Sant'Anna 的 Claude Code 学术工作流。*
