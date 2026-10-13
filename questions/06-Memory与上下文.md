# 06-Memory与上下文

> 共 11 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q069 [P0]** 模型 API 通常无状态，AI 对话中的多轮记忆是谁实现的？  （[S05](../sources/INDEX.md#S05)、[S08](../sources/INDEX.md#S08)、[S19](../sources/INDEX.md#S19)）
- [ ] **Q070 [P0]** Working Memory、短期历史、长期记忆、用户画像分别保存什么？  （[S09](../sources/INDEX.md#S09)、[S15](../sources/INDEX.md#S15)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q071 [P0]** 为什么要区分 Redis 中的近期会话与向量库中的可检索长期记忆？  （[S05](../sources/INDEX.md#S05)、[S15](../sources/INDEX.md#S15)）
- [ ] **Q072 [P0]** 什么时候应使用滑动窗口，什么时候应使用摘要压缩？  （[S03](../sources/INDEX.md#S03)、[S04](../sources/INDEX.md#S04)）
- [ ] **Q073 [P0]** 上下文超出模型窗口时，如何保留约束、目标、工具结果和未完成步骤？  （[S02](../sources/INDEX.md#S02)、[S04](../sources/INDEX.md#S04)）
- [ ] **Q074 [P0]** 长期记忆保存哪些信息才有价值，哪些个人信息不应该存储？  （[S09](../sources/INDEX.md#S09)、[S15](../sources/INDEX.md#S15)）
- [ ] **Q075 [P1]** 摘要发生事实遗漏时如何检测？怎么保留原始消息供追溯？  （[S02](../sources/INDEX.md#S02)、[S03](../sources/INDEX.md#S03)）
- [ ] **Q076 [P1]** 如何解决长期记忆中内容矛盾、过期和误写问题？  （[S15](../sources/INDEX.md#S15)、[S25](../sources/INDEX.md#S25)）
- [ ] **Q077 [P1]** 用户说“上次那个订单”，如何做指代消解和相关历史检索？  （[S15](../sources/INDEX.md#S15)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q078 [P1]** 为什么不把所有上下文直接塞进 Prompt，成本和安全问题是什么？  （[S04](../sources/INDEX.md#S04)、[S15](../sources/INDEX.md#S15)）
- [ ] **Q079 [P2]** 跨会话的 Memory 更新在并发执行时怎么避免覆盖或时序混乱？  （[S07](../sources/INDEX.md#S07)、[S25](../sources/INDEX.md#S25)）