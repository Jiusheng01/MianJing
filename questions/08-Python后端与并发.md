# 08-Python后端与并发

> 共 14 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q091 [P0]** FastAPI、Uvicorn 与 Pydantic 分别承担什么职责？  （[S02](../sources/INDEX.md#S02)、[S08](../sources/INDEX.md#S08)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q092 [P0]** Python 的 async、await、asyncio.gather 适合什么类型任务？  （[S07](../sources/INDEX.md#S07)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q093 [P0]** 协程、线程与进程的区别是什么？GIL 对 I/O 与 CPU 密集任务的影响如何？  （[S07](../sources/INDEX.md#S07)、[S27](../sources/INDEX.md#S27)）
- [ ] **Q094 [P0]** 长时间执行的 Agent 为什么不能直接完全依附单次 HTTP 请求？  （[S03](../sources/INDEX.md#S03)、[S07](../sources/INDEX.md#S07)）
- [ ] **Q095 [P0]** 如何实现单会话顺序执行和多会话并发执行？  （[S07](../sources/INDEX.md#S07)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q096 [P0]** 如何设计 client_request_id 与去重回执，避免重试重复保存消息？  （[S07](../sources/INDEX.md#S07)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q097 [P0]** LLM 接口超时后，用户重试该怎样判断原请求是否实际完成？  （[S07](../sources/INDEX.md#S07)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q098 [P0]** SSE 和 WebSocket 有何区别，如何实现断线重连和事件续传？  （[S07](../sources/INDEX.md#S07)、[S08](../sources/INDEX.md#S08)）
- [ ] **Q099 [P0]** 工具执行为什么需要限流、熔断、重试退避和超时隔离？  （[S02](../sources/INDEX.md#S02)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q100 [P1]** Redis Pipeline 与事务区别是什么，事务能提供哪类原子操作？  （[S05](../sources/INDEX.md#S05)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q101 [P1]** 数据库保存运行状态、Redis 保存事件与缓存，各有什么取舍？  （[S04](../sources/INDEX.md#S04)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q102 [P1]** 如何设计 AgentRun 表、Message 表、Conversation 表的关联？  （[S07](../sources/INDEX.md#S07)、[S30](../sources/INDEX.md#S30)）
- [ ] **Q103 [P1]** 如何实现 Mock LLM 和 Mock Tool 做不联网的单元测试？  （[S02](../sources/INDEX.md#S02)、[S20](../sources/INDEX.md#S20)）
- [ ] **Q104 [P2]** 如何给带外部 API 的异步系统做负载测试，并区分模型瓶颈和应用瓶颈？  （[S05](../sources/INDEX.md#S05)、[S30](../sources/INDEX.md#S30)）