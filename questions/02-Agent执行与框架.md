# 02-Agent执行与框架

> 共 14 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q013 [P0]** 什么是 Agent Loop？定义最小的模型决策、工具执行、观察回填与退出条件。  （[S01](../sources/INDEX.md#S01)、[S03](../sources/INDEX.md#S03)、[S08](../sources/INDEX.md#S08)）
- [ ] **Q014 [P0]** ReAct、Plan-and-Execute、Reflection 的区别是什么？怎么根据任务选择？  （[S05](../sources/INDEX.md#S05)、[S09](../sources/INDEX.md#S09)、[S10](../sources/INDEX.md#S10)、[S19](../sources/INDEX.md#S19)）
- [ ] **Q015 [P0]** 没有 LangChain/LangGraph，使用原生 Python 怎样实现最小 Agent？  （[S01](../sources/INDEX.md#S01)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q016 [P0]** Agent 为什么会反复调用同一工具？怎样设计 max_steps、超时和预算停止条件？  （[S01](../sources/INDEX.md#S01)、[S03](../sources/INDEX.md#S03)、[S04](../sources/INDEX.md#S04)）
- [ ] **Q017 [P0]** Agent Harness 是什么，和具体的 Agent 业务编排有什么区别？  （[S03](../sources/INDEX.md#S03)、[S04](../sources/INDEX.md#S04)、[S11](../sources/INDEX.md#S11)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q018 [P0]** 用户问题模糊时，如何设计澄清问题与意图识别？  （[S01](../sources/INDEX.md#S01)、[S04](../sources/INDEX.md#S04)、[S19](../sources/INDEX.md#S19)）
- [ ] **Q019 [P0]** 意图识别采用规则、Embedding 还是 LLM？如何比较成本、可解释性和效果？  （[S04](../sources/INDEX.md#S04)、[S05](../sources/INDEX.md#S05)、[S24](../sources/INDEX.md#S24)）
- [ ] **Q020 [P1]** 为什么 Agent 会出现执行路径震荡，如何使用进展检测和结构化状态避免？  （[S04](../sources/INDEX.md#S04)、[S11](../sources/INDEX.md#S11)）
- [ ] **Q021 [P1]** Agent 状态如何表达当前目标、已完成步骤、待执行工具和错误？  （[S03](../sources/INDEX.md#S03)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q022 [P1]** 如何判断 Agent 真正完成任务，而不是只生成“已完成”的回复？  （[S01](../sources/INDEX.md#S01)、[S08](../sources/INDEX.md#S08)、[S22](../sources/INDEX.md#S22)）
- [ ] **Q023 [P1]** Coding Agent 如何完成仓库检索、修改文件、测试和变更审查？  （[S02](../sources/INDEX.md#S02)、[S29](../sources/INDEX.md#S29)）
- [ ] **Q024 [P1]** 不同模型的输出格式不同，Agent Runtime 如何适配？  （[S02](../sources/INDEX.md#S02)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q025 [P1]** 什么时候需要规划器和执行器分离，什么时候直接单循环就够？  （[S04](../sources/INDEX.md#S04)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q026 [P2]** LangGraph 与手写状态机的可维护性、可恢复性和调试成本如何比较？  （[S05](../sources/INDEX.md#S05)、[S25](../sources/INDEX.md#S25)）