# 所有题目（按主题分类）

> 共 **129** 道去重后的归纳题，关联 **40** 个不同 URL（索引中 42 条来源记录，包括少量指向同一原文的不同标签）。截至 2026-10-13。

> P0 = 面试冲刺必备；P1 = 常见追问；P2 = 进阶。每道题后的来源是内容/考点线索，**不表示该题被对应公司逐字问过**。

## [01-项目与技术选型](questions/01-项目与技术选型.md)

- [ ] **Q001 [P0]** 用 90 秒介绍一个真实 AI Agent 项目，说明需求、技术架构和个人负责边界。 （[S01](sources/INDEX.md#S01)、[S02](sources/INDEX.md#S02)、[S05](sources/INDEX.md#S05)、[S29](sources/INDEX.md#S29)）
- [ ] **Q002 [P0]** 你为什么把当前系统做成 Agent，而不是普通 LLM API 或固定 Workflow？ （[S05](sources/INDEX.md#S05)、[S06](sources/INDEX.md#S06)、[S20](sources/INDEX.md#S20)）
- [ ] **Q003 [P0]** 介绍一次用户请求从 HTTP 接入到最终回复的完整数据流。 （[S01](sources/INDEX.md#S01)、[S02](sources/INDEX.md#S02)、[S09](sources/INDEX.md#S09)）
- [ ] **Q004 [P0]** 项目中最复杂的问题是什么，你如何定位和解决，做过哪些可复现的验证？ （[S02](sources/INDEX.md#S02)、[S05](sources/INDEX.md#S05)、[S30](sources/INDEX.md#S30)）
- [ ] **Q005 [P0]** 你使用了 LangGraph 还是自研 Loop，为什么这样选？ （[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)、[S05](sources/INDEX.md#S05)）
- [ ] **Q006 [P0]** 为什么使用多 Agent？改成单 Agent + Tools 会发生什么变化？ （[S05](sources/INDEX.md#S05)、[S06](sources/INDEX.md#S06)、[S09](sources/INDEX.md#S09)）
- [ ] **Q007 [P0]** 哪些改进是你亲手完成的，哪些来自开源项目或团队其他成员？ （[S01](sources/INDEX.md#S01)、[S02](sources/INDEX.md#S02)、[S05](sources/INDEX.md#S05)、[S29](sources/INDEX.md#S29)）
- [ ] **Q008 [P0]** 如何定义项目效果指标？如何避免没有数据却声称提效 10 倍？ （[S05](sources/INDEX.md#S05)、[S27](sources/INDEX.md#S27)、[S30](sources/INDEX.md#S30)）
- [ ] **Q009 [P1]** 如果重新设计现有系统，你会先改哪些模块？为什么？ （[S04](sources/INDEX.md#S04)、[S05](sources/INDEX.md#S05)、[S30](sources/INDEX.md#S30)）
- [ ] **Q010 [P1]** 如何从演示 Demo 过渡为支持真实用户的应用服务？ （[S20](sources/INDEX.md#S20)、[S30](sources/INDEX.md#S30)）
- [ ] **Q011 [P1]** 需求变化时，如何设计模块边界以避免一个 main.py 包揽全部业务？ （[S02](sources/INDEX.md#S02)、[S30](sources/INDEX.md#S30)）
- [ ] **Q012 [P1]** 项目选用的模型、向量库、缓存为什么适合场景，替代方案是什么？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)、[S30](sources/INDEX.md#S30)）

## [02-Agent执行与框架](questions/02-Agent执行与框架.md)

- [ ] **Q013 [P0]** 什么是 Agent Loop？定义最小的模型决策、工具执行、观察回填与退出条件。 （[S01](sources/INDEX.md#S01)、[S03](sources/INDEX.md#S03)、[S08](sources/INDEX.md#S08)）
- [ ] **Q014 [P0]** ReAct、Plan-and-Execute、Reflection 的区别是什么？怎么根据任务选择？ （[S05](sources/INDEX.md#S05)、[S09](sources/INDEX.md#S09)、[S10](sources/INDEX.md#S10)、[S19](sources/INDEX.md#S19)）
- [ ] **Q015 [P0]** 没有 LangChain/LangGraph，使用原生 Python 怎样实现最小 Agent？ （[S01](sources/INDEX.md#S01)、[S20](sources/INDEX.md#S20)）
- [ ] **Q016 [P0]** Agent 为什么会反复调用同一工具？怎样设计 max_steps、超时和预算停止条件？ （[S01](sources/INDEX.md#S01)、[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)）
- [ ] **Q017 [P0]** Agent Harness 是什么，和具体的 Agent 业务编排有什么区别？ （[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)、[S11](sources/INDEX.md#S11)、[S25](sources/INDEX.md#S25)）
- [ ] **Q018 [P0]** 用户问题模糊时，如何设计澄清问题与意图识别？ （[S01](sources/INDEX.md#S01)、[S04](sources/INDEX.md#S04)、[S19](sources/INDEX.md#S19)）
- [ ] **Q019 [P0]** 意图识别采用规则、Embedding 还是 LLM？如何比较成本、可解释性和效果？ （[S04](sources/INDEX.md#S04)、[S05](sources/INDEX.md#S05)、[S24](sources/INDEX.md#S24)）
- [ ] **Q020 [P1]** 为什么 Agent 会出现执行路径震荡，如何使用进展检测和结构化状态避免？ （[S04](sources/INDEX.md#S04)、[S11](sources/INDEX.md#S11)）
- [ ] **Q021 [P1]** Agent 状态如何表达当前目标、已完成步骤、待执行工具和错误？ （[S03](sources/INDEX.md#S03)、[S20](sources/INDEX.md#S20)）
- [ ] **Q022 [P1]** 如何判断 Agent 真正完成任务，而不是只生成“已完成”的回复？ （[S01](sources/INDEX.md#S01)、[S08](sources/INDEX.md#S08)、[S22](sources/INDEX.md#S22)）
- [ ] **Q023 [P1]** Coding Agent 如何完成仓库检索、修改文件、测试和变更审查？ （[S02](sources/INDEX.md#S02)、[S29](sources/INDEX.md#S29)）
- [ ] **Q024 [P1]** 不同模型的输出格式不同，Agent Runtime 如何适配？ （[S02](sources/INDEX.md#S02)、[S20](sources/INDEX.md#S20)）
- [ ] **Q025 [P1]** 什么时候需要规划器和执行器分离，什么时候直接单循环就够？ （[S04](sources/INDEX.md#S04)、[S20](sources/INDEX.md#S20)）
- [ ] **Q026 [P2]** LangGraph 与手写状态机的可维护性、可恢复性和调试成本如何比较？ （[S05](sources/INDEX.md#S05)、[S25](sources/INDEX.md#S25)）

## [03-多Agent与LangGraph](questions/03-多Agent与LangGraph.md)

- [ ] **Q027 [P0]** 主 Agent、辅助 Agent 各承担什么职责，路由依据是什么？ （[S04](sources/INDEX.md#S04)、[S05](sources/INDEX.md#S05)、[S06](sources/INDEX.md#S06)）
- [ ] **Q028 [P0]** 用户同时咨询技术故障与退款，怎么支持多个领域而非只选单一意图？ （[S05](sources/INDEX.md#S05)、[S06](sources/INDEX.md#S06)、[S19](sources/INDEX.md#S19)）
- [ ] **Q029 [P0]** LangGraph 的 State、Node、Edge、条件边分别是什么？ （[S05](sources/INDEX.md#S05)、[S09](sources/INDEX.md#S09)、[S25](sources/INDEX.md#S25)）
- [ ] **Q030 [P0]** 多 Agent 并行和串行的选择依据是什么，如何合成结果？ （[S04](sources/INDEX.md#S04)、[S06](sources/INDEX.md#S06)、[S20](sources/INDEX.md#S20)）
- [ ] **Q031 [P0]** 多 Agent 之间要共享什么上下文？哪些信息必须隔离？ （[S05](sources/INDEX.md#S05)、[S07](sources/INDEX.md#S07)）
- [ ] **Q032 [P0]** 多 Agent 任务失败一个分支，系统应该全部失败还是允许部分完成？ （[S04](sources/INDEX.md#S04)、[S07](sources/INDEX.md#S07)）
- [ ] **Q033 [P1]** LangGraph 的 Checkpoint、interrupt、resume 适合解决什么类型的问题？ （[S05](sources/INDEX.md#S05)、[S11](sources/INDEX.md#S11)、[S25](sources/INDEX.md#S25)）
- [ ] **Q034 [P1]** 如何为每个 Agent 配置工具白名单与最小权限？ （[S07](sources/INDEX.md#S07)、[S20](sources/INDEX.md#S20)）
- [ ] **Q035 [P1]** 当多个 Agent 同时修改文件或共享数据时，如何避免互相覆盖？ （[S04](sources/INDEX.md#S04)、[S07](sources/INDEX.md#S07)）
- [ ] **Q036 [P1]** 子 Agent 结果与主 Agent 判断不一致，谁有最终决策权？ （[S04](sources/INDEX.md#S04)、[S20](sources/INDEX.md#S20)）
- [ ] **Q037 [P1]** 如何证明多 Agent 相比单 Agent 的质量收益超过了额外延迟和 Token 成本？ （[S06](sources/INDEX.md#S06)、[S05](sources/INDEX.md#S05)）
- [ ] **Q038 [P2]** LangGraph 运行中的长任务和 HTTP 请求生命周期该怎样解耦？ （[S03](sources/INDEX.md#S03)、[S25](sources/INDEX.md#S25)）

## [04-Tool-MCP-Skills](questions/04-Tool-MCP-Skills.md)

- [ ] **Q039 [P0]** Function Calling 完整链路是什么，谁执行工具，工具结果如何回到模型？ （[S01](sources/INDEX.md#S01)、[S02](sources/INDEX.md#S02)、[S22](sources/INDEX.md#S22)）
- [ ] **Q040 [P0]** 工具 Schema 包含哪些字段？模型产生了无效参数时怎么处理？ （[S02](sources/INDEX.md#S02)、[S05](sources/INDEX.md#S05)、[S22](sources/INDEX.md#S22)）
- [ ] **Q041 [P0]** MCP 与 Function Calling 的区别是什么？它们可以一起使用吗？ （[S05](sources/INDEX.md#S05)、[S09](sources/INDEX.md#S09)、[S15](sources/INDEX.md#S15)）
- [ ] **Q042 [P0]** Tool、MCP、Skill 各有什么边界，为什么不能互相替代？ （[S06](sources/INDEX.md#S06)、[S15](sources/INDEX.md#S15)、[S25](sources/INDEX.md#S25)）
- [ ] **Q043 [P0]** 工具调用超时或返回业务错误，如何重试、降级和向模型反馈？ （[S02](sources/INDEX.md#S02)、[S05](sources/INDEX.md#S05)、[S22](sources/INDEX.md#S22)）
- [ ] **Q044 [P0]** 有副作用的工具如何处理幂等，防止重试导致重复下单或退款？ （[S07](sources/INDEX.md#S07)、[S01](sources/INDEX.md#S01)）
- [ ] **Q045 [P0]** 如何避免模型伪造工具参数或访问未授权资源？ （[S01](sources/INDEX.md#S01)、[S05](sources/INDEX.md#S05)、[S07](sources/INDEX.md#S07)）
- [ ] **Q046 [P0]** 工具注册、发现、权限检查、执行、审计的生命周期是什么？ （[S02](sources/INDEX.md#S02)、[S25](sources/INDEX.md#S25)）
- [ ] **Q047 [P1]** Skill 热插拔有哪些方案？进程隔离、RPC 和注册中心分别解决什么问题？ （[S06](sources/INDEX.md#S06)）
- [ ] **Q048 [P1]** 当 MCP 工具数量达到上百个时，怎样做发现、过滤和动态描述加载？ （[S04](sources/INDEX.md#S04)、[S15](sources/INDEX.md#S15)）
- [ ] **Q049 [P1]** MCP 的 stdio 与 Streamable HTTP 如何选择？旧 SSE 传输的边界是什么？ （[S15](sources/INDEX.md#S15)、[S20](sources/INDEX.md#S20)）
- [ ] **Q050 [P1]** Tool Calling 过程怎样控制最大轮次、速率、预算和外部 API 配额？ （[S03](sources/INDEX.md#S03)、[S22](sources/INDEX.md#S22)）
- [ ] **Q051 [P1]** Tool 返回数据含外部指令时，如何区分数据与指令？ （[S05](sources/INDEX.md#S05)、[S20](sources/INDEX.md#S20)）
- [ ] **Q052 [P2]** 一个 Skill 的配置发生版本升级后，如何灰度、回退和兼容执行中的任务？ （[S06](sources/INDEX.md#S06)、[S25](sources/INDEX.md#S25)）

## [05-RAG与知识库](questions/05-RAG与知识库.md)

- [ ] **Q053 [P0]** 说出 RAG 离线建库和在线问答的完整链路。 （[S01](sources/INDEX.md#S01)、[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q054 [P0]** 为什么要 Chunk？固定长度、递归切分、按标题和语义切分怎样取舍？ （[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q055 [P0]** 为什么纯向量检索会漏掉错误码、产品型号和精确专有词？ （[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)）
- [ ] **Q056 [P0]** BM25、向量检索与混合检索分别适用于哪些查询？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q057 [P0]** 什么是 Rerank？为什么需要先粗召回再精排？ （[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q058 [P0]** RAG 出现错误答案，如何判别是检索错误还是生成错误？ （[S01](sources/INDEX.md#S01)、[S21](sources/INDEX.md#S21)）
- [ ] **Q059 [P0]** 检索召回率低，按 Query 改写、Chunk、Embedding、索引、TopK 如何逐项排查？ （[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)、[S24](sources/INDEX.md#S24)）
- [ ] **Q060 [P0]** 为什么有些 Agent 不需要每次查询知识库？与固定 RAG 链路相比有什么代价？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)）
- [ ] **Q061 [P1]** PDF 表格、扫描件、OCR 错误、图片与公式如何影响知识检索？ （[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)）
- [ ] **Q062 [P1]** RRF 如何融合稀疏和稠密检索排序结果？ （[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q063 [P1]** Embedding 模型如何选型，离线建库与在线查询的向量空间为何要一致？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)）
- [ ] **Q064 [P1]** 文档更新时如何做增量索引、版本切换和旧向量删除？ （[S03](sources/INDEX.md#S03)、[S21](sources/INDEX.md#S21)）
- [ ] **Q065 [P1]** RAG 与微调的边界是什么，什么情况组合使用？ （[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q066 [P1]** 构建万级文档知识库如何处理任务调度、批量 embedding 与失败重试？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)）
- [ ] **Q067 [P2]** GraphRAG 和普通向量 RAG 的适用场景有何不同？ （[S04](sources/INDEX.md#S04)、[S21](sources/INDEX.md#S21)）
- [ ] **Q068 [P2]** Agentic RAG 如何决定继续检索还是停下来，如何控制成本？ （[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）

## [06-Memory与上下文](questions/06-Memory与上下文.md)

- [ ] **Q069 [P0]** 模型 API 通常无状态，AI 对话中的多轮记忆是谁实现的？ （[S05](sources/INDEX.md#S05)、[S08](sources/INDEX.md#S08)、[S19](sources/INDEX.md#S19)）
- [ ] **Q070 [P0]** Working Memory、短期历史、长期记忆、用户画像分别保存什么？ （[S09](sources/INDEX.md#S09)、[S15](sources/INDEX.md#S15)、[S25](sources/INDEX.md#S25)）
- [ ] **Q071 [P0]** 为什么要区分 Redis 中的近期会话与向量库中的可检索长期记忆？ （[S05](sources/INDEX.md#S05)、[S15](sources/INDEX.md#S15)）
- [ ] **Q072 [P0]** 什么时候应使用滑动窗口，什么时候应使用摘要压缩？ （[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)）
- [ ] **Q073 [P0]** 上下文超出模型窗口时，如何保留约束、目标、工具结果和未完成步骤？ （[S02](sources/INDEX.md#S02)、[S04](sources/INDEX.md#S04)）
- [ ] **Q074 [P0]** 长期记忆保存哪些信息才有价值，哪些个人信息不应该存储？ （[S09](sources/INDEX.md#S09)、[S15](sources/INDEX.md#S15)）
- [ ] **Q075 [P1]** 摘要发生事实遗漏时如何检测？怎么保留原始消息供追溯？ （[S02](sources/INDEX.md#S02)、[S03](sources/INDEX.md#S03)）
- [ ] **Q076 [P1]** 如何解决长期记忆中内容矛盾、过期和误写问题？ （[S15](sources/INDEX.md#S15)、[S25](sources/INDEX.md#S25)）
- [ ] **Q077 [P1]** 用户说“上次那个订单”，如何做指代消解和相关历史检索？ （[S15](sources/INDEX.md#S15)、[S21](sources/INDEX.md#S21)）
- [ ] **Q078 [P1]** 为什么不把所有上下文直接塞进 Prompt，成本和安全问题是什么？ （[S04](sources/INDEX.md#S04)、[S15](sources/INDEX.md#S15)）
- [ ] **Q079 [P2]** 跨会话的 Memory 更新在并发执行时怎么避免覆盖或时序混乱？ （[S07](sources/INDEX.md#S07)、[S25](sources/INDEX.md#S25)）

## [07-评测与观测](questions/07-评测与观测.md)

- [ ] **Q080 [P0]** Agent 不同于普通分类模型，最终任务成功率怎么定义？ （[S05](sources/INDEX.md#S05)、[S09](sources/INDEX.md#S09)、[S19](sources/INDEX.md#S19)）
- [ ] **Q081 [P0]** 如何构建覆盖正常路径、异常路径、越权请求的 Agent 评测集？ （[S05](sources/INDEX.md#S05)、[S08](sources/INDEX.md#S08)、[S25](sources/INDEX.md#S25)）
- [ ] **Q082 [P0]** 如何用 Trace 定位问题属于意图识别、路由、检索、工具还是生成阶段？ （[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)、[S25](sources/INDEX.md#S25)）
- [ ] **Q083 [P0]** 如何区分 RAG 检索评测（Recall@K 等）和最终答案评测？ （[S21](sources/INDEX.md#S21)、[S23](sources/INDEX.md#S23)）
- [ ] **Q084 [P0]** 模型升级后怎样建立同数据集回归测试和对照实验？ （[S05](sources/INDEX.md#S05)、[S25](sources/INDEX.md#S25)）
- [ ] **Q085 [P0]** 发现一个 Badcase 后怎样生成稳定复现样本，并评估修复是否引入新问题？ （[S05](sources/INDEX.md#S05)、[S25](sources/INDEX.md#S25)）
- [ ] **Q086 [P1]** 如何统计模型调用 Token、工具成功率、P95 延迟、超时率和平均成本？ （[S04](sources/INDEX.md#S04)、[S25](sources/INDEX.md#S25)）
- [ ] **Q087 [P1]** LLM-as-Judge 有哪些偏见和不稳定性，如何结合确定性规则与人工抽检？ （[S05](sources/INDEX.md#S05)、[S20](sources/INDEX.md#S20)）
- [ ] **Q088 [P1]** 线上没有显式反馈时怎样构建评测样本？ （[S15](sources/INDEX.md#S15)、[S25](sources/INDEX.md#S25)）
- [ ] **Q089 [P1]** A/B 测试中如何排除提示词、检索数据和模型版本同时改变带来的干扰？ （[S05](sources/INDEX.md#S05)、[S25](sources/INDEX.md#S25)）
- [ ] **Q090 [P2]** 工具描述更新后怎样检测工具选择准确率回退？ （[S02](sources/INDEX.md#S02)、[S25](sources/INDEX.md#S25)）

## [08-Python后端与并发](questions/08-Python后端与并发.md)

- [ ] **Q091 [P0]** FastAPI、Uvicorn 与 Pydantic 分别承担什么职责？ （[S02](sources/INDEX.md#S02)、[S08](sources/INDEX.md#S08)、[S20](sources/INDEX.md#S20)）
- [ ] **Q092 [P0]** Python 的 async、await、asyncio.gather 适合什么类型任务？ （[S07](sources/INDEX.md#S07)、[S20](sources/INDEX.md#S20)）
- [ ] **Q093 [P0]** 协程、线程与进程的区别是什么？GIL 对 I/O 与 CPU 密集任务的影响如何？ （[S07](sources/INDEX.md#S07)、[S27](sources/INDEX.md#S27)）
- [ ] **Q094 [P0]** 长时间执行的 Agent 为什么不能直接完全依附单次 HTTP 请求？ （[S03](sources/INDEX.md#S03)、[S07](sources/INDEX.md#S07)）
- [ ] **Q095 [P0]** 如何实现单会话顺序执行和多会话并发执行？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q096 [P0]** 如何设计 client_request_id 与去重回执，避免重试重复保存消息？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q097 [P0]** LLM 接口超时后，用户重试该怎样判断原请求是否实际完成？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q098 [P0]** SSE 和 WebSocket 有何区别，如何实现断线重连和事件续传？ （[S07](sources/INDEX.md#S07)、[S08](sources/INDEX.md#S08)）
- [ ] **Q099 [P0]** 工具执行为什么需要限流、熔断、重试退避和超时隔离？ （[S02](sources/INDEX.md#S02)、[S30](sources/INDEX.md#S30)）
- [ ] **Q100 [P1]** Redis Pipeline 与事务区别是什么，事务能提供哪类原子操作？ （[S05](sources/INDEX.md#S05)、[S30](sources/INDEX.md#S30)）
- [ ] **Q101 [P1]** 数据库保存运行状态、Redis 保存事件与缓存，各有什么取舍？ （[S04](sources/INDEX.md#S04)、[S30](sources/INDEX.md#S30)）
- [ ] **Q102 [P1]** 如何设计 AgentRun 表、Message 表、Conversation 表的关联？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q103 [P1]** 如何实现 Mock LLM 和 Mock Tool 做不联网的单元测试？ （[S02](sources/INDEX.md#S02)、[S20](sources/INDEX.md#S20)）
- [ ] **Q104 [P2]** 如何给带外部 API 的异步系统做负载测试，并区分模型瓶颈和应用瓶颈？ （[S05](sources/INDEX.md#S05)、[S30](sources/INDEX.md#S30)）

## [09-安全与故障恢复](questions/09-安全与故障恢复.md)

- [ ] **Q105 [P0]** Prompt Injection 与普通用户指令有什么区别，RAG 文档里的指令怎么隔离？ （[S04](sources/INDEX.md#S04)、[S20](sources/INDEX.md#S20)）
- [ ] **Q106 [P0]** 调用 SQL 工具为什么不能只信任模型输出“SELECT”？如何限制真实数据库权限？ （[S01](sources/INDEX.md#S01)、[S20](sources/INDEX.md#S20)）
- [ ] **Q107 [P0]** 订单查询工具如何校验用户身份、订单归属和可访问字段？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q108 [P0]** 人工审批节点如何设计？哪些高风险行为不应由模型自动执行？ （[S05](sources/INDEX.md#S05)、[S20](sources/INDEX.md#S20)）
- [ ] **Q109 [P0]** Agent 进程崩溃后如何判断任务需要重试还是恢复，如何处理外部副作用？ （[S03](sources/INDEX.md#S03)、[S04](sources/INDEX.md#S04)）
- [ ] **Q110 [P1]** Lease、锁与请求幂等分别解决什么问题？为什么不能相互替代？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q111 [P1]** 多租户环境如何隔离 Prompt、Memory、工具权限和 Trace？ （[S07](sources/INDEX.md#S07)、[S25](sources/INDEX.md#S25)）
- [ ] **Q112 [P1]** 当一条工具链执行部分成功时，如何设计补偿、审核与用户提示？ （[S07](sources/INDEX.md#S07)、[S30](sources/INDEX.md#S30)）
- [ ] **Q113 [P2]** 流式输出中途客户端断开，怎样避免将半截结果误认为完整任务？ （[S02](sources/INDEX.md#S02)、[S07](sources/INDEX.md#S07)）

## [10-LLM模型基础](questions/10-LLM模型基础.md)

- [ ] **Q114 [P0]** Temperature、Top-p 与 Max Tokens 各控制什么？Temperature=0 是否保证完全确定？ （[S15](sources/INDEX.md#S15)、[S19](sources/INDEX.md#S19)、[S26](sources/INDEX.md#S26)）
- [ ] **Q115 [P0]** Transformer 的 Attention 机制是什么？Q、K、V 分别承担什么角色？ （[S15](sources/INDEX.md#S15)、[S20](sources/INDEX.md#S20)）
- [ ] **Q116 [P0]** Token 与上下文窗口有什么关系，长上下文为什么仍然有成本？ （[S03](sources/INDEX.md#S03)、[S15](sources/INDEX.md#S15)）
- [ ] **Q117 [P1]** 大模型输出格式不符合 JSON Schema 时如何校验、重试和提供兜底？ （[S05](sources/INDEX.md#S05)、[S26](sources/INDEX.md#S26)）
- [ ] **Q118 [P1]** 什么时候选择更小的分类模型而不是通用大模型完成意图识别？ （[S04](sources/INDEX.md#S04)、[S24](sources/INDEX.md#S24)）
- [ ] **Q119 [P1]** 什么是 Embedding？它与生成模型有什么不同？ （[S05](sources/INDEX.md#S05)、[S21](sources/INDEX.md#S21)）
- [ ] **Q120 [P2]** vLLM、KV Cache、Continuous Batching 与应用层并发的边界是什么？ （[S19](sources/INDEX.md#S19)、[S20](sources/INDEX.md#S20)）

## [新增：小红书快手 / 理想实战追问](interviews/xiaohongshu/)

- [ ] **Q121 [P0]** 三路意图识别结果冲突，怎样融合分数并验证收益？ （[S36](sources/INDEX.md#S36)、[S38](sources/INDEX.md#S38)）
- [ ] **Q122 [P0]** Query 改写出现“退货/退款”歧义、效果变差怎么办？ （[S36](sources/INDEX.md#S36)）
- [ ] **Q123 [P1]** 一次性 Workflow 和自主 Agent Loop 如何取舍？怎样衡量一次修复率？ （[S38](sources/INDEX.md#S38)）
- [ ] **Q124 [P1]** Skill 与 System Prompt 的边界是什么，何时独立成 Agent？ （[S36](sources/INDEX.md#S36)、[S38](sources/INDEX.md#S38)）
- [ ] **Q125 [P0]** 动态 Skill 注入如何实现渐进式加载？ （[S36](sources/INDEX.md#S36)、[S38](sources/INDEX.md#S38)）
- [ ] **Q126 [P1]** Codex + Skill 与独立 Traceback 分析产品如何比较？ （[S36](sources/INDEX.md#S36)、[S38](sources/INDEX.md#S38)）
- [ ] **Q127 [P1]** 超长终端日志的错误不在尾部，如何定位并分配上下文预算？ （[S38](sources/INDEX.md#S38)）
- [ ] **Q128 [P1]** 前端竞态治理：AbortController、watch、请求版本号怎样使用？ （[S37](sources/INDEX.md#S37)、[S38](sources/INDEX.md#S38)）
- [ ] **Q129 [P0]** 多 Agent 系统如何多机部署，保证会话状态一致、幂等与工具执行安全？ （[S37](sources/INDEX.md#S37)）
