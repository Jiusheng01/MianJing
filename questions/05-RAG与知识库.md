# 05-RAG与知识库

> 共 16 题。根据公开来源归纳，题目不是原帖逐字转载。

- [ ] **Q053 [P0]** 说出 RAG 离线建库和在线问答的完整链路。  （[S01](../sources/INDEX.md#S01)、[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q054 [P0]** 为什么要 Chunk？固定长度、递归切分、按标题和语义切分怎样取舍？  （[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q055 [P0]** 为什么纯向量检索会漏掉错误码、产品型号和精确专有词？  （[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q056 [P0]** BM25、向量检索与混合检索分别适用于哪些查询？  （[S05](../sources/INDEX.md#S05)、[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q057 [P0]** 什么是 Rerank？为什么需要先粗召回再精排？  （[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q058 [P0]** RAG 出现错误答案，如何判别是检索错误还是生成错误？  （[S01](../sources/INDEX.md#S01)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q059 [P0]** 检索召回率低，按 Query 改写、Chunk、Embedding、索引、TopK 如何逐项排查？  （[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)、[S24](../sources/INDEX.md#S24)）
- [ ] **Q060 [P0]** 为什么有些 Agent 不需要每次查询知识库？与固定 RAG 链路相比有什么代价？  （[S05](../sources/INDEX.md#S05)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q061 [P1]** PDF 表格、扫描件、OCR 错误、图片与公式如何影响知识检索？  （[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q062 [P1]** RRF 如何融合稀疏和稠密检索排序结果？  （[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q063 [P1]** Embedding 模型如何选型，离线建库与在线查询的向量空间为何要一致？  （[S05](../sources/INDEX.md#S05)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q064 [P1]** 文档更新时如何做增量索引、版本切换和旧向量删除？  （[S03](../sources/INDEX.md#S03)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q065 [P1]** RAG 与微调的边界是什么，什么情况组合使用？  （[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）
- [ ] **Q066 [P1]** 构建万级文档知识库如何处理任务调度、批量 embedding 与失败重试？  （[S05](../sources/INDEX.md#S05)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q067 [P2]** GraphRAG 和普通向量 RAG 的适用场景有何不同？  （[S04](../sources/INDEX.md#S04)、[S21](../sources/INDEX.md#S21)）
- [ ] **Q068 [P2]** Agentic RAG 如何决定继续检索还是停下来，如何控制成本？  （[S21](../sources/INDEX.md#S21)、[S23](../sources/INDEX.md#S23)）