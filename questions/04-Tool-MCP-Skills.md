# 04-Tool-MCP-Skills

> 共 14 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q039 [P0]** Function Calling 完整链路是什么，谁执行工具，工具结果如何回到模型？  （[S01](../sources/INDEX.md#S01)、[S02](../sources/INDEX.md#S02)、[S22](../sources/INDEX.md#S22)）
- [ ] **Q040 [P0]** 工具 Schema 包含哪些字段？模型产生了无效参数时怎么处理？  （[S02](../sources/INDEX.md#S02)、[S05](../sources/INDEX.md#S05)、[S22](../sources/INDEX.md#S22)）
- [ ] **Q041 [P0]** MCP 与 Function Calling 的区别是什么？它们可以一起使用吗？  （[S05](../sources/INDEX.md#S05)、[S09](../sources/INDEX.md#S09)、[S15](../sources/INDEX.md#S15)）
- [ ] **Q042 [P0]** Tool、MCP、Skill 各有什么边界，为什么不能互相替代？  （[S06](../sources/INDEX.md#S06)、[S15](../sources/INDEX.md#S15)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q043 [P0]** 工具调用超时或返回业务错误，如何重试、降级和向模型反馈？  （[S02](../sources/INDEX.md#S02)、[S05](../sources/INDEX.md#S05)、[S22](../sources/INDEX.md#S22)）
- [ ] **Q044 [P0]** 有副作用的工具如何处理幂等，防止重试导致重复下单或退款？  （[S07](../sources/INDEX.md#S07)、[S01](../sources/INDEX.md#S01)）
- [ ] **Q045 [P0]** 如何避免模型伪造工具参数或访问未授权资源？  （[S01](../sources/INDEX.md#S01)、[S05](../sources/INDEX.md#S05)、[S07](../sources/INDEX.md#S07)）
- [ ] **Q046 [P0]** 工具注册、发现、权限检查、执行、审计的生命周期是什么？  （[S02](../sources/INDEX.md#S02)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q047 [P1]** Skill 热插拔有哪些方案？进程隔离、RPC 和注册中心分别解决什么问题？  （[S06](../sources/INDEX.md#S06)）
- [ ] **Q048 [P1]** 当 MCP 工具数量达到上百个时，怎样做发现、过滤和动态描述加载？  （[S04](../sources/INDEX.md#S04)、[S15](../sources/INDEX.md#S15)）
- [ ] **Q049 [P1]** MCP 的 stdio 与 Streamable HTTP 如何选择？旧 SSE 传输的边界是什么？  （[S15](../sources/INDEX.md#S15)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q050 [P1]** Tool Calling 过程怎样控制最大轮次、速率、预算和外部 API 配额？  （[S03](../sources/INDEX.md#S03)、[S22](../sources/INDEX.md#S22)）
- [ ] **Q051 [P1]** Tool 返回数据含外部指令时，如何区分数据与指令？  （[S05](../sources/INDEX.md#S05)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q052 [P2]** 一个 Skill 的配置发生版本升级后，如何灰度、回退和兼容执行中的任务？  （[S06](../sources/INDEX.md#S06)、[S25](../sources/INDEX.md#S25)）