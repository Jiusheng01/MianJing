# 03-多Agent与LangGraph

> 共 12 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q027 [P0]** 主 Agent、辅助 Agent 各承担什么职责，路由依据是什么？  （[S04](../sources/INDEX.md#S04)、[S05](../sources/INDEX.md#S05)、[S06](../sources/INDEX.md#S06)）
- [ ] **Q028 [P0]** 用户同时咨询技术故障与退款，怎么支持多个领域而非只选单一意图？  （[S05](../sources/INDEX.md#S05)、[S06](../sources/INDEX.md#S06)、[S19](../sources/INDEX.md#S19)）
- [ ] **Q029 [P0]** LangGraph 的 State、Node、Edge、条件边分别是什么？  （[S05](../sources/INDEX.md#S05)、[S09](../sources/INDEX.md#S09)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q030 [P0]** 多 Agent 并行和串行的选择依据是什么，如何合成结果？  （[S04](../sources/INDEX.md#S04)、[S06](../sources/INDEX.md#S06)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q031 [P0]** 多 Agent 之间要共享什么上下文？哪些信息必须隔离？  （[S05](../sources/INDEX.md#S05)、[S07](../sources/INDEX.md#S07)）
- [ ] **Q032 [P0]** 多 Agent 任务失败一个分支，系统应该全部失败还是允许部分完成？  （[S04](../sources/INDEX.md#S04)、[S07](../sources/INDEX.md#S07)）
- [ ] **Q033 [P1]** LangGraph 的 Checkpoint、interrupt、resume 适合解决什么类型的问题？  （[S05](../sources/INDEX.md#S05)、[S11](../sources/INDEX.md#S11)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q034 [P1]** 如何为每个 Agent 配置工具白名单与最小权限？  （[S07](../sources/INDEX.md#S07)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q035 [P1]** 当多个 Agent 同时修改文件或共享数据时，如何避免互相覆盖？  （[S04](../sources/INDEX.md#S04)、[S07](../sources/INDEX.md#S07)）
- [ ] **Q036 [P1]** 子 Agent 结果与主 Agent 判断不一致，谁有最终决策权？  （[S04](../sources/INDEX.md#S04)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q037 [P1]** 如何证明多 Agent 相比单 Agent 的质量收益超过了额外延迟和 Token 成本？  （[S06](../sources/INDEX.md#S06)、[S05](../sources/INDEX.md#S05)）
- [ ] **Q038 [P2]** LangGraph 运行中的长任务和 HTTP 请求生命周期该怎样解耦？  （[S03](../sources/INDEX.md#S03)、[S25](../sources/INDEX.md#S25)）