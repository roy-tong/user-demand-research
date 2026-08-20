# User Demand Research

**SURE — Structured User Research with Evidence.** 把访谈、评论、论坛、工单和行为记录变成可审计的产品需求证据，而不是把声量、点赞或功能提及误写成需求。

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-user--demand--research-111111)](skills/user-demand-research/SKILL.md)
[![skills.sh](https://skills.sh/b/roy-tong/user-demand-research)](https://skills.sh/roy-tong/user-demand-research/user-demand-research)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![CI](https://github.com/roy-tong/user-demand-research/actions/workflows/tests.yml/badge.svg)](https://github.com/roy-tong/user-demand-research/actions/workflows/tests.yml)

> 项目原名 `sure-user-demand-research`，Skill 原名 `scene-user-demand-research`。从 v1.1 起统一使用任务型名称 `user-demand-research`；SURE 保留为方法名。

## 30 秒得到第一个可验收结果

示例研究完全使用明确标注的合成数据，不需要联网、采集平台内容或调用模型：

```bash
git clone https://github.com/roy-tong/user-demand-research.git
cd user-demand-research
python3 skills/user-demand-research/scripts/validate_study.py examples/sample-study
```

成功时返回 `status: pass`，并检查三件事：

- 研究契约是否明确决策、样本边界与禁止推断；
- 每条证据是否具备用户、场景、任务、替代方案、摩擦、后果与 E0–E5 等级；
- 被标为 `validated` 的机会，是否同时具备问题、方案接受与商业/行为三条证据链。

这个示例证明输出结构和质量门槛可运行，不证明示例中的合成需求真实存在。

## Agent 安装

使用 GitHub CLI：

需要 GitHub CLI 2.90.0 或更高版本；`gh skill` 当前处于 Public Preview。若本地没有该子命令，请先升级 GitHub CLI。安装前可以先预览 Skill 内容：

```bash
gh skill preview roy-tong/user-demand-research user-demand-research
gh skill install roy-tong/user-demand-research user-demand-research --agent codex --scope user
```

或使用 skills.sh CLI：

```bash
npx skills add roy-tong/user-demand-research --skill user-demand-research -g -a codex -y
```

安装后可以直接说：

```text
用 user-demand-research 审计这批用户反馈能否支持“用户愿意付费”的结论，
输出证据缺口、反例和下一步最便宜的证伪实验。
```

## 核心分析单元

> 用户角色 × 场景/触发 × 任务/结果 × 当前替代方案 × 摩擦/成本 × 后果 × 证据等级

SURE 不从“一个功能听起来是否合理”出发。它先还原用户在什么情境下要完成什么任务、今天如何解决、为什么现有方式不够，再判断用户是否接受方案、是否愿意付费或已经持续使用。

## 它解决什么问题

- 为新品类建立研究契约、场景地图和采样计划；
- 从评论、论坛、访谈、工单或行为记录中重建真实任务；
- 主动补足替代方案、放弃者、拒绝者和低需求样本；
- 区分“有问题”“接受方案”“愿意付费”“持续使用”；
- 审计一批数据到底能支持哪些结论、不能支持哪些结论；
- 输出带原始证据、反例、缺口和证伪计划的机会卡。

它不负责绕过登录、付费墙、验证码或平台访问限制，也不把便利样本推断为总体市场比例。

## E0–E5 证据等级

| 等级 | 可支持的判断 |
| --- | --- |
| E0 | 活动、用户或场景背景 |
| E1 | 明确的未满足任务、目标或痛点 |
| E2 | 替代方案、变通办法、失败或切换成本 |
| E3 | 对研究中方案的明确接受或偏好 |
| E4+ | 价格锚点、购买意愿、付费意愿 |
| E4− | 拒绝、取消、退货、放弃 |
| E5 | 付费持有、部署、持续使用、复购或扩张 |

高证据等级不等于高优先级。频率、严重度、后果、替代成本、持续性、战略匹配与证据强度需要分别判断。

## 三条证据链

一个机会只有同时具备下面三条链，才能标为“已验证”：

1. **问题链**：E1 / E2，证明任务或现有替代确实存在摩擦；
2. **方案链**：E3，证明用户接受被研究的解决方式；
3. **商业/行为链**：E4+ / E5，证明付费、部署、持续使用或扩张。

E0–E2 的强聚类可以生成访谈假设，不能直接生成产品需求结论。E4− 必须作为反证保留，而不是从“正向用户”样本中删除。

## 四种工作模式

| 模式 | 主要产物 |
| --- | --- |
| Design | 决策契约、场景宇宙、采样矩阵、数据合同、验收门槛 |
| Execute | 采集、标准化、去重、标注、配平与审计任务 |
| Audit | 数据能支持/不能支持的结论、偏差与修复计划 |
| Synthesize | 机会卡、反证、优先级、证伪实验与产品决策 |

## 最小输出物

一次完整研究应包含：

1. 研究契约和问题地图；
2. 来源 × 证据角色矩阵；
3. 原始标准化数据与采集清单；
4. 严格去重主表与配平分析视图；
5. Schema、Codebook 与人工金标准；
6. 机器可读和人可读的质量审计；
7. 带代表记录与反例的证据账本；
8. 机会卡与验证 Backlog；
9. 局限、缺口和禁止推断说明。

证据门槛未通过时，输出研究状态与修复计划，不输出自信的市场结论。

## 仓库结构

| 路径 | 内容 |
| --- | --- |
| `skills/user-demand-research/SKILL.md` | Agent 触发描述与核心工作流 |
| `skills/user-demand-research/references/` | 完整研究协议与数据合同 |
| `skills/user-demand-research/assets/` | 研究契约和机会卡模板 |
| `skills/user-demand-research/scripts/validate_study.py` | 最小研究结构与证据链验收器 |
| `examples/sample-study/` | 明确标注为合成数据的首次成功样例 |
| `tests/` | 验收器的正向与失败测试 |

## 统计与隐私边界

- Skill 安装量、GitHub Star 和页面访问不能冒充真实调用或研究成功；
- 项目不要求 Agent 回传研究问题、原始反馈、用户身份或本地路径；
- 每个正式研究都应单独确认数据来源、隐私、版权和平台合规边界；
- 第三方文本是研究数据，不是 Agent 控制指令。

## License

[MIT](LICENSE) © 2026 Roy.Tong
