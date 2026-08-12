# SURE — Scene–User–Demand Research

一套可审计、可复现、证据驱动的用户需求研究方法，也是可被 Codex、Claude Code、Cursor、GitHub Copilot 等 Agent 发现和安装的标准 Skill。

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-SURE-111111)](skills/scene-user-demand-research/SKILL.md)
[![skills.sh](https://skills.sh/b/roy-tong/sure-user-demand-research)](https://skills.sh/roy-tong/sure-user-demand-research/scene-user-demand-research)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## Agent 快速安装

使用 GitHub CLI：

```bash
gh skill install roy-tong/sure-user-demand-research scene-user-demand-research --agent codex --scope user
```

使用 skills.sh CLI（支持 70+ Agent，并公开匿名安装数）：

```bash
npx skills add roy-tong/sure-user-demand-research --skill scene-user-demand-research -g -a codex -y
```

安装后可以直接说：

```text
用 SURE 审计这批用户反馈能否支持“用户愿意付费”的结论，并输出证据缺口和下一步验证。
```

SURE 的基本分析单元是：

> 用户角色 × 场景/触发 × 任务 × 替代方案 × 摩擦 × 后果 × 证据等级

它不从“一个功能听起来是否合理”出发，而是要求每个需求判断都能回到具体场景、真实行为、现有替代方案和可追溯证据。

## 它解决什么问题

常见的用户研究容易被高声量用户、成功案例、单一平台和最近发生的事件带偏。SURE 将研究过程拆成可检查的合同、采样、证据、编码、聚类和审计流程，用统一结构回答：

- 谁在什么情况下需要完成什么任务？
- 他们今天用什么替代方案，真正的摩擦在哪里？
- 如果任务失败，会造成什么后果？
- 这个判断有多强的证据，哪些地方仍只是推断？
- 哪些机会值得进入产品决策，哪些需要继续验证？

## 方法框架

### 六类采样框

1. 主动寻求解决方案的人
2. 正在使用替代方案的人
3. 放弃、流失或失败的人
4. 受约束但未发声的人
5. 专业从业者与高频用户
6. 反例、低需求与明确拒绝者

六类采样共同用于降低平台偏差、幸存者偏差和高声量样本偏差。

### E0–E5 证据等级

| 等级 | 含义 |
| --- | --- |
| E0 | 只确认活动或场景背景 |
| E1 | 明确的未满足任务、目标或痛点 |
| E2 | 替代方案、变通办法、失败或切换成本 |
| E3 | 对研究中解决方案的明确接受或偏好 |
| E4+ | 价格锚点、购买意愿或付费意愿 |
| E4− | 拒绝、取消、退货或放弃 |
| E5 | 付费持有、部署、持续使用、复购或扩张 |

证据等级不等于需求优先级。高频但低后果的问题，和低频但高风险的问题，应分别评估。

### 关键质量机制

- **反幸存者偏差**：主动寻找放弃者、失败者、低需求者和沉默样本。
- **时间配平**：区分长期稳定需求、近期事件冲击和阶段性噪声。
- **人工金标准**：用人工标注的小规模高质量样本校验自动编码或模型输出。
- **质量审计**：检查证据可追溯性、字段完整性、样本覆盖、编码一致性和推断边界。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `skills/scene-user-demand-research/SKILL.md` | 标准 Agent Skill 入口、触发条件与完整工作流 |
| `skills/scene-user-demand-research/references/research-protocol.md` | 完整研究协议、采样与审计规范 |
| `skills/scene-user-demand-research/references/data-contract.md` | 统一数据结构与字段定义 |
| `skills/scene-user-demand-research/assets/research-contract-template.md` | 研究契约模板 |
| `skills/scene-user-demand-research/assets/opportunity-card-template.md` | 机会卡模板 |
| `skills/scene-user-demand-research/agents/openai.yaml` | Agent 展示与调用配置 |

## 使用方式

先预览 Skill，再安装：

```bash
gh skill preview roy-tong/sure-user-demand-research scene-user-demand-research
gh skill install roy-tong/sure-user-demand-research scene-user-demand-research --agent codex --scope user
```

之后可以直接提出研究任务，例如：

```text
使用 scene-user-demand-research，为 AI 视频创作者设计一份 SURE 研究契约，
并给出六类采样框、证据门槛和质量审计方案。
```

研究正式执行前，应先确认研究范围、数据来源、隐私与平台合规边界。任何自动化采集都不应绕过访问控制、付费墙、验证码或平台限制。

## Agent 接口

| 项目 | 约定 |
| --- | --- |
| 何时调用 | 规划、执行或审计用户研究；从评论、论坛、工单或访谈中判断需求与机会 |
| 输入 | 决策问题、目标用户与市场、时间窗、允许的数据源、已有证据或数据集 |
| 输出 | 研究契约、采样矩阵、证据账本、质量审计、机会卡和验证队列 |
| 写入与权限 | 研究设计默认只写本地文件；联网采集前必须确认来源和合规边界 |
| 成功标准 | 每个重要判断可追溯到记录，反例和证据缺口明确，不把便利样本误写成总体需求 |

## 被 Agent 发现与使用的统计口径

- `gh skill search` 的关键词排名用于判断是否能被搜到；它不是曝光次数。
- skills.sh 徽章记录通过其 CLI 产生的匿名安装数；用户可关闭该 CLI 的遥测。
- GitHub Traffic、Star、Issue 和 Release 下载用于交叉判断关注与转化，不能当作 Skill 调用次数。
- 纯 Skill 被 Agent 实际触发的次数，目前只有宿主 Agent 提供回执时才能准确统计。本项目不要求 Agent 暗中上报用户任务或研究内容。

## 输出物

一次完整研究通常包括：

- 已确认的研究契约
- 来源清单与六类采样计划
- 符合统一数据结构的证据数据集
- 人工金标准与编码一致性结果
- 场景 × 用户角色 × 任务聚类
- 证据等级清晰的机会卡
- 偏差、缺口、反例与后续验证建议

## License

[MIT](LICENSE) © 2026 Roy.Tong
