# AI 应用开发 / Agent 开发：2026 年 7—10 月面经增补 82 题

> 整理截至：2026-10-13。延续此前 45 道基础题；本文件为新增的 82 道进阶/项目追问题，合计可作为约 127 题复习池。原先 2026-07-10 的小红书报告（224 条目）并不是 224 道“7 月新增真题”，勿混淆。
>
> 来源说明：优先取有可查面试日期的个人面经原帖，并补充牛客及二次整理站。小红书笔记存在登录与索引限制，因此**不能声称下列问题全部出自小红书原帖**。部分网站仅标注月份；记为该网站的月份分类而非独立核实的面试日期。题目是根据来源提炼的复习问法，不是逐字引用。来源所标公司和面试经历均为发帖人自述，未获企业确认。
>
> 优先级：**P0** 核心必讲、**P1** 二轮追问、**P2** 深水区。建议答题顺序：原理 → 实际流程/源码 → 为什么选这种方案 → 替代方案与代价 → 如何测量。

## 7 月：12 题（接在原有基础题之后）

- [ ] **46. [P0]** 为什么一个客服项目要拆成多个 Agent？如何证明单 Agent 不够用？（[J1]）
- [ ] **47. [P1]** Skill 如何实现热插拔？为什么选进程池、RPC、注册中心？（[J1]）
- [ ] **48. [P1]** 用对象存储托管 Skill 文件能否替代注册中心？何种能力仍缺失？（[J1]）
- [ ] **49. [P1]** Agent 会话中的临时文件如何隔离、存储、过期清理？（[J1]）
- [ ] **50. [P0]** 单机 Agent Demo 升级为可用业务服务，首先补哪些工程能力？（[J1]）
- [ ] **51. [P0]** 大流量下模型调用的慢请求怎样排队、限流、超时和降级？（[J1]）
- [ ] **52. [P0]** BM25 与向量检索结果如何融合、如何验证带来的增益？（[J2]）
- [ ] **53. [P1]** PDF 扫描件、OCR 与表格结构化的错误如何定位、衡量？（[J2]）
- [ ] **54. [P1]** LangGraph State、Checkpoint 如何应对多个 Agent 的并发写入？（[J2]）
- [ ] **55. [P0]** Skill、Memory、RAG 各解决什么问题？为何不能混成一个模块？（[J1]）
- [ ] **56. [P1]** 长期记忆中重复记录和互相矛盾的经验如何更新、合并、遗忘？（[J1]）
- [ ] **57. [P0]** 单次 LLM 评分与带循环工具调用的 Agent 有何区别？（[J1]）

## 8 月：22 题

- [ ] **58. [P0]** 解释 Agent Harness 的边界；它与业务 Agent、模型 SDK、LangGraph 的区别是什么？（[A1]）
- [ ] **59. [P0]** 你如何组织 Agent 的路由/编排层？一个用户 Query 模糊与否如何判定？（[A1]）
- [ ] **60. [P0]** Tool、Skill 分别承担什么职责？Skill 什么时候加载才不会让上下文膨胀？（[A1]）
- [ ] **61. [P1]** 系统为何自研编排而不是直接使用 LangGraph？哪些部分不值得自研？（[A1]）
- [ ] **62. [P1]** 在服务提供商变化时，如何控制多个大模型的输出格式与业务表现差异？（[A1]）
- [ ] **63. [P1]** 服务 5000—6000 用户、日调用十余万次，容量如何估算、按哪层扩容？（[A1]）
- [ ] **64. [P0]** Agent 写入数据库/文件前，如何定义最小权限与人工确认边界？（[A1]）
- [ ] **65. [P1]** BGE-M3 的多路检索如何理解？与普通双塔 embedding 检索有什么差异？（[A2]）
- [ ] **66. [P1]** BM25 为何有词频饱和；关键词和向量得分能直接加权吗？（[A2]）
- [ ] **67. [P0]** 为什么模型 API 本身无状态，AI 客户端却能支持多轮记忆？（[A3]）
- [ ] **68. [P0]** 什么样的任务适合 A2A/多 Agent 协作，而非一个 Agent 顺序调用工具？（[A3]）
- [ ] **69. [P0]** 代码 Agent 读项目、修改文件、运行测试、提交 Git 的完整闭环如何控制？（[A3]）
- [ ] **70. [P1]** 当用户需求不断变化，工作流与自主 Agent 如何取舍？（[A3]）
- [ ] **71. [P0]** 如何确认 AI Coding 生成的代码具备可合并质量？（[A4]）
- [ ] **72. [P1]** 事实性幻觉与忠实度错误有哪些区别，如何验证模型答案？（[A4]）
- [ ] **73. [P0]** Python 装饰器如何编写一个打印耗时和日志的通用包装器？（[A4]）
- [ ] **74. [P1]** MCP 工具粒度该如何定义，工具列表过多时怎么发现和选择？（[A5]）
- [ ] **75. [P0]** 知识库文档变更后，采用全量更新还是增量索引？如何防止读取旧版本？（[A5]）
- [ ] **76. [P0]** 多 Agent 分派错误如何发现并纠正？主 Agent 根据什么信息派任务？（[A5]）
- [ ] **77. [P0]** 如何阻止 Agent 越权查询数据库或读取其他用户资料？（[A5]）
- [ ] **78. [P1]** 用哪些指标评价工具链与 Agent 的整体执行质量？如何构建测试集？（[A5]）
- [ ] **79. [P1]** 单接口瞬时涌入大于处理能力的请求、实时 Top-10 业务榜单怎么设计？（[A6]）

## 9 月：24 题

- [ ] **80. [P0]** 为什么采用主 Agent、编排层、子 Agent 三级架构？单层加工具为何不够？（[S1]）
- [ ] **81. [P0]** 子 Agent 上下文怎么裁剪传递，确保不会丢失任务必需信息？（[S1]）
- [ ] **82. [P1]** 多个 Agent 的执行状态和工具权限如何隔离，防止跨用户/跨任务串扰？（[S1]）
- [ ] **83. [P0]** LangGraph State、Node、Edge 与 Checkpoint 在真实项目里分别承担什么责任？（[S2]）
- [ ] **84. [P1]** 知识图谱相比普通向量 RAG 增加了哪些能力？怎样做对照实验？（[S2]）
- [ ] **85. [P0]** 离线评测集从哪来？是否使用线上 Trace、人工标注、合成样本？（[S2]）
- [ ] **86. [P0]** 如何证明 RAG/Agent 改进有效，防止只优化少量展示案例？（[S2]）
- [ ] **87. [P0]** Agent 调用外部工具，如何保证幂等并处理“超时但操作已成功”？（[S3]）
- [ ] **88. [P0]** SSE 断开、用户重连时，如何继续订阅正确的运行事件？（[S3]）
- [ ] **89. [P0]** Agent Trace 应该记录哪些信息，如何用它定位 Badcase？（[S3]）
- [ ] **90. [P1]** 哪些指标能用确定性程序算，哪些要用模型评审器或人工判分？（[S3]）
- [ ] **91. [P1]** 如何把线上低分 Case 回流为回归评测集，不断更新评测基线？（[S3]）
- [ ] **92. [P0]** 用户以为 Agent 已完成真实操作，但工具根本没有执行，如何检测并避免？（[S4]）
- [ ] **93. [P0]** Agent 需求变更后，如何设计回滚、验证和重新执行机制？（[S4]）
- [ ] **94. [P1]** 工作流节点失败是否导致整条链路中断？如何做局部重试与补偿？（[S4]）
- [ ] **95. [P1]** 按标题切块导致尺寸极不均匀，如何兼顾完整性与检索质量？（[S5]）
- [ ] **96. [P1]** 检索召回较差，如何区分召回阶段、融合阶段与重排阶段的问题？（[S5]）
- [ ] **97. [P1]** 多工具 Plan 流程中人工确认应放在哪些节点，如何减少不必要确认？（[S5]）
- [ ] **98. [P1]** Agent 长任务进程崩溃，如何通过 Lease、Checkpoint 或持久状态恢复？（[S6]）
- [ ] **99. [P2]** Fencing Token 解决什么问题？为什么仅凭分布式锁还不足以保护写操作？（[S6]）
- [ ] **100. [P0]** 明明换了更强的大模型，业务完成率反而下降，如何定位和证明原因？（[S7]）
- [ ] **101. [P0]** 模型生成的工具参数符合 JSON Schema，为什么仍可能不能执行？（[S7]）
- [ ] **102. [P0]** 在文档中嵌入恶意提示时，为什么只靠系统提示词不足以防御？（[S7]）
- [ ] **103. [P1]** LangGraph 与纯 Python 自定义 Loop 的取舍依据是什么？（[S8]）

## 10 月（截至 10 月 13 日）：24 题

- [ ] **104. [P0]** MCP 的 stdio、旧版 SSE 与 Streamable HTTP 如何区分，适用场景是什么？（[O1]）
- [ ] **105. [P1]** MCP 客户端、服务端初始化与工具发现流程是什么？版本兼容怎么保证？（[O1]）
- [ ] **106. [P0]** 有 100 个 MCP 工具时如何减少 Token、缩小候选集、提升路由准确性？（[O1]）
- [ ] **107. [P0]** 如何为对话 Agent 设计会话表、消息表与运行状态表？（[O1]）
- [ ] **108. [P0]** 短期、长期记忆发生冲突时，如何确定可信信息并避免用户画像污染？（[O1]）
- [ ] **109. [P1]** Redis 缓存穿透/击穿/雪崩有哪些区别？哪些适用于 Agent 场景？（[O1]）
- [ ] **110. [P0]** Skill、MCP 和 Function Calling 为什么不能相互替代？（[O2]）
- [ ] **111. [P1]** 大量 Skill 如何渐进式发现和加载？怎样定义输入输出契约？（[O2]）
- [ ] **112. [P0]** Agent Loop 的规划、执行、检查和终止条件怎么实现？（[O3]）
- [ ] **113. [P1]** Agent 多次重复选择相同工具或路由摇摆，如何识别并中止？（[O3]）
- [ ] **114. [P0]** 某 Agent 平常执行 5 分钟，突然耗时 20 分钟，该分层排查什么？（[O3]）
- [ ] **115. [P1]** 同一文件被多个 Agent 修改时，如何防止覆盖、并发冲突和脏状态？（[O4]）
- [ ] **116. [P0]** 长任务运行期间服务重启，断点恢复依赖哪些状态和持久化边界？（[O4]）
- [ ] **117. [P0]** Markdown 文档没有标题，应该怎样切片？如何为短 Query 检索长 Chunk？（[O5]）
- [ ] **118. [P1]** 旅行 Agent 遇到天气、行程天数改变，应该重规划还是局部修补？（[O5]）
- [ ] **119. [P0]** 对模型生成的不规范 JSON，如何做解析、校验、重试和失败兜底？（[O6]）
- [ ] **120. [P1]** PDF 中图片和公式如何提取、结构化、切分及检索？（[O6]）
- [ ] **121. [P0]** NL2SQL 检索信息超过模型上下文时怎么控制？SQL 如何只读、鉴权？（[O6]）
- [ ] **122. [P0]** 如何判断模型生成的代码是否允许上线？怎样安排测试、人工 Review 与回滚？（[O7]）
- [ ] **123. [P0]** 一次 Agent 执行包含多个工具，怎样证明每一步真实完成而非模型宣称完成？（[O7]）
- [ ] **124. [P1]** 业务 Skill 没有历史测试用例，新功能上线前怎么构建有覆盖率的测试集？（[O7]）
- [ ] **125. [P1]** 上下文摘要压缩如何保住任务目标、约束、已执行动作与工具结果？（[O3]）
- [ ] **126. [P1]** 引入 Agent 与固定 Workflow 的收益如何量化，不只看主观体验？（[O7]）
- [ ] **127. [P0]** 项目所谓“效率提升 10 倍”，基线、样本量、瓶颈变化和评测口径分别是什么？（[O7]）

## 来源索引（按月份，原帖优先）

### 7 月
- **J1** 淘天 Agent 面经合集（含 7/18、7/22、7/23）：https://www.nowcoder.com/discuss/928330146736537600
- **J2** 淘天 7/23 原帖：https://www.nowcoder.com/feed/main/detail/d875cc5d4d6e47608bc2ede695df438b
- **补充** 7/24 法本信息 Coding Agent 项目面经：https://www.nowcoder.com/feed/main/detail/d8f5de441b7a4f7ba32164ef37cce1fc

### 8 月
- **A1** 8/6 小红书大模型平台 Agentic 全栈岗（牛客原帖）：https://www.nowcoder.com/feed/main/detail/e5e9311a623940eead6ec98c65e7f9e8
- **A2** 8/7 拼多多 Agent 面经合集：https://api-cdn.nowcoder.com/discuss/929182786928279552
- **A3** 8/18 淘天 AI 一面原帖：https://api-cdn.nowcoder.com/feed/main/detail/8e5fb9efdc154b9e913a2c8bde2a2a0b
- **A4** 8/1 米哈游 Agent 开发提前批原帖：https://api-cdn.nowcoder.com/feed/main/detail/7b13b3c9e42745819ad822397a115812
- **A5** 8/28 深信服 Agent 开发一面原帖：https://api-cdn.nowcoder.com/feed/main/detail/45b40914f438434b88b60a21e3d5ec1e
- **A6** 8/26 淘天 Agent 面经汇总：https://api-cdn.nowcoder.com/discuss/931372614759481344

### 9 月
- **S1** 字节 Agent 三级编排面经（聚合，标注 2026-09）：https://mj.mianlingai.com/interview/bytedance-ai-agent-first-round-932407145864130560/
- **S2** 9/23 携程 Agent 开发原帖：https://www.nowcoder.com/feed/main/detail/0d590f82f4f243b180ee923860010b94
- **S3** 9/23 作业帮 Agent 开发原帖：https://www.nowcoder.com/feed/main/detail/3742d4aa5a50419d94aa02d549d6aab6
- **S4** 9/8 阿里控股 AI 全栈开发二面原帖：https://api-cdn.nowcoder.com/feed/main/detail/a11a3a9e0d824969b44db5bb2149ef9f
- **S5** 9/24 九方智投 Agent 开发面经（聚合）：https://mj.mianlingai.com/interview/jiufangzhitou-agent-dev-first-round-2916834/
- **S6** 快手 Agent 恢复/Lease 面经（聚合，标注 2026-09）：https://mj.mianlingai.com/interview/kuaishou-agent-dev-first-round-932315325276618752/
- **S7** vivo Agent 故障场景相关面经索引：https://mj.mianlingai.com/position/Agent%E5%BC%80%E5%8F%91/
- **S8** 9/16 美团 Agent 开发一面原帖：https://www.nowcoder.com/feed/main/detail/50bcdc47e7754aa7be59b6318fea514b

### 10 月（截至 10/13）
- **O1** 网易 Agent MCP、记忆面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/netease-agent-development-938914958287306752/
- **O2** 阿里巴巴 Agent、MCP、Skills 面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/alibaba-ai-agent-938174747332956160/
- **O3** 字节 Agent Harness/长任务面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/bytedance-agent-development-first-round-938539037059567616/
- **O4** 米哈游 Agent 代码生成/断点恢复面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/mihoyo-ai-agent-938914757099130880/
- **O5** 美团 RAG Markdown 切分与规划场景面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/meituan-agent-development-938539937836683264/
- **O6** 小厂智能体 PDF/JSON/NL2SQL（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/unknown-company-ai-agent-application-2923282/
- **O7** 美团 Agent 开发工程/Skill 面经（牛客二次聚合，标注 2026-10）：https://mj.mianlingai.com/interview/meituan-agent-development-first-round-2924661/

## 用 EchoMind 做面试准备：先准备这 12 道

- 46 多 Agent 与单 Agent 的依据：读 `backend/agents/agent_orchestrator.py`。
- 50 Agent Demo 如何工程化：读 `backend/api/main.py`、`backend/core/concurrency.py`。
- 52 RAG 混合检索及评估：读 `backend/tooling/knowledge_base.py`（先确认现有实现，不可虚构已有 BM25）。
- 55 Skill/Memory/RAG 边界：读 `backend/core/skill_loader.py`、`backend/memory/conversation_memory.py`。
- 58 Harness 与 Agent Runtime：对照 Yuxi/Octop 的架构文档，不要声称 EchoMind 已实现完整 Harness。
- 67 LLM 无状态与多轮记忆：读 `backend/memory/conversation_memory.py`。
- 75 文档增量更新：作为 EchoMind 的候选改造，不要说已经实现了生产级增量索引。
- 77 工具权限控制：读 `backend/agents/tools.py`、`backend/tooling/tool_manager.py`。
- 87 工具幂等：区分 API 对话幂等和**外部有副作用工具**的幂等。
- 89 Trace 定位：读 `/trace/tool/{request_id}` 与评测链路。
- 101 JSON Schema 与授权：区分格式正确、业务合法和可执行权限。
- 119 结构化输出失败：用 Pydantic 校验、重试与显式报错做一个可验证实验。

> **面试表述纪律：** 把“我研究过 EchoMind 的实现”“我独立改造并验证了 X”“我建议后续优化 Y”分开表述。未经测试的改进不能说成已上线效果，也不要捏造 QPS、延迟和准确率。