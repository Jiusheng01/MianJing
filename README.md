# Agent Interview Handbook | AI 应用开发面经资料库

> 多平台 AI Agent / Python AI 应用开发面经与高频追问整理。整理截至 **2026-10-13**，根据公开网页独立归纳，并为每一道题保留来源编号与可访问 URL。

**当前版本：120 道去重的学习题、33 个不同公开来源 URL、10 个知识主题。** 来源平台覆盖牛客、小红书、掘金、知乎、B站、V2EX、SegmentFault、GitHub。

**重要：这不是“全网穷尽”，不是“已核验企业内部真题”，也不是官方题库。** 公司、岗位、面试日期通常来自发帖人自述或整理者转述；部分小红书链接通过二级报告间接索引，不能直接验证原帖内容。题目均为主题改写，未复制原帖长篇回答。

## 入口

- [全部题库 · Markdown 勾选](ALL_QUESTIONS.md)
- [分主题题库](questions/)
- [来源索引：平台 / 日期 / 链接 / 可信度](sources/INDEX.md)
- [面经整理方法与验证级别](METHODOLOGY.md)
- [七天冲刺计划](SPRINT_7_DAYS.md)
- [历史增补稿（82 题，未逐条复核）](archive/2026-07_to_10_questions_82.md)
- [结构化题库 JSON](data/questions.json) / [来源 JSON](data/sources.json)

## 分类与题量

| 主题 | 题数 | 学习入口 |
|---|---:|---|
| 01-项目与技术选型 | 12 | [开始复习](questions/01-项目与技术选型.md) |
| 02-Agent执行与框架 | 14 | [开始复习](questions/02-Agent执行与框架.md) |
| 03-多Agent与LangGraph | 12 | [开始复习](questions/03-多Agent与LangGraph.md) |
| 04-Tool-MCP-Skills | 14 | [开始复习](questions/04-Tool-MCP-Skills.md) |
| 05-RAG与知识库 | 16 | [开始复习](questions/05-RAG与知识库.md) |
| 06-Memory与上下文 | 11 | [开始复习](questions/06-Memory与上下文.md) |
| 07-评测与观测 | 11 | [开始复习](questions/07-评测与观测.md) |
| 08-Python后端与并发 | 14 | [开始复习](questions/08-Python后端与并发.md) |
| 09-安全与故障恢复 | 9 | [开始复习](questions/09-安全与故障恢复.md) |
| 10-LLM模型基础 | 7 | [开始复习](questions/10-LLM模型基础.md) |

## 使用说明

1. 先刷 P0 题。每题试着回答：“业务问题 → 实现流程 → 为什么这么设计 → 替代方案 → 如何验证”。
2. 想知道“哪来的”，点击题目后的 `[Sxx]` 跳转来源，检查来源类型和日期口径。
3. 二手转载或教程中的问题只作为备考线索，不写成“某公司面试官确实问过”。
4. 用真实个人项目/开源改造做可验证实践；不要编造“上线”“准确率提升”“并发量”。
5. 通过 `python scripts/validate.py` 校验源 ID、重复问题、数量和 URL 格式。

## 版权和使用边界

只摘录/归纳问题主题与标题，链接原作者页面，不批量转载参考答案、付费内容、评论及图片。所有原帖版权归各自作者。若来源不可访问、撤稿或需更正，可修改 `data/sources.json` 并重新生成索引。

## 说明

仓库初始内容独立于任何用户的业务项目；不会修改 EchoMind。本仓库独立于 EchoMind 项目，用于集中维护可溯源的 AI 应用开发面经与复习资料。