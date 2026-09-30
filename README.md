# Kevin Writer

> 为 Kevin Mo 打造的中文个人品牌写作 Skill：把复杂的湾区房产问题，写成专业、直接、可信、能帮助客户做决定的口播内容。

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Language](https://img.shields.io/badge/language-简体中文-dc2626)
![Voice Standard](https://img.shields.io/badge/voice_standard-2026--09--24-2563eb)

## 它能做什么

`kevin-writer` 用于创作、改写和审核 Kevin Mo 的中文内容，包括：

- YouTube 长视频与短视频口播稿
- 湾区城市、社区和不同价位比较
- 房地产市场、政策、科技与购买力解读
- 买家、卖家与换房家庭的决策内容
- 高净值房产、隐私和复杂交易框架
- 豪宅社区、生活成本与资产规划内容

它不是把资料整理成一篇“看起来很专业”的文章，而是让 Kevin 像面对一位聪明、有购买力、但没时间研究全部数据的客户，直接给判断、解释原因、说明例外和下一步。

## 核心写作标准

| 维度 | 标准 |
|---|---|
| 出品优先级 | 逻辑清楚、信息密、说得顺；高于固定时长、内容比例、模板节奏和品牌植入 |
| 对话对象 | 一位具体客户；通篇使用“您” |
| 开场 | 尽快交代具体决策与初步判断，及时兑现标题；不为卡秒数硬造悬念 |
| 主线 | 一个问题、一个主要受众、一个核心观点 |
| 长稿 | 默认完整口播；按主次与决策顺序讲透，不注水、不擅自压成短视频 |
| 写法选择 | 未指定写法的房产决策口播先展示 2–4 张预览卡，选定骨架后成稿 |
| 句子 | 按气口写，不用连续碎短句，不把脚本写成一句一行 |
| 数据 | 先说数字说明什么，每段最多两组核心数字，来源实名 |
| 判断 | 明确建议、适用范围、具体例外和改判信号 |
| CTA | 有真实服务承接时最多一个主 CTA，可加一个轻量动作；没有就用可执行判断收口 |
| 事实纪律 | 不编客户、成交、内部消息和一线观察；缺失内容使用 `【待补：需要什么】` |
| 成交证据 | 31 笔逐笔成交价与团队汇总均可独立引用；五笔另有完整过程细节，按地区、价位、房型或交易问题调用 |
| 交付门槛 | 先过逻辑、信息密度与口述检查，再做 18 项自检；评分不能抵消前三项失败 |

称呼、气口、数字表达和禁语以 [`65-口播稿语言风格规范_团队版_2026-09-24.md`](references/65-口播稿语言风格规范_团队版_2026-09-24.md) 为语言标准；其模板与节奏建议不能覆盖上述出品优先级。情境稿按事件发生顺序推进，不把已经完成的决定重新当作待决问题。历史热门视频只提供主题、结构和专业判断证据，不参与语言定调。

写法选择流程、十一种方法卡、判断力方法论和预估规则已内置，无需另装 `script-angle`。已指定写法、局部润色、审核或非房产内容会跳过选择流程。预览中的留存预估是结构判断，不是实测保证；示例数字不能充当真实业绩。

## 安装

### 让 Codex 安装

把仓库地址发给 Codex，并告诉它：

```text
请从 https://github.com/leoking1987/kevin-writer 安装这个 Skill。
```

### 手动安装

macOS / Linux：

```bash
git clone https://github.com/leoking1987/kevin-writer.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/kevin-writer"
```

Windows PowerShell：

```powershell
git clone https://github.com/leoking1987/kevin-writer.git `
  "$env:USERPROFILE\.codex\skills\kevin-writer"
```

安装完成后，在支持 Skills 的 Codex 环境中通过 `$kevin-writer` 调用。

## 使用示例

安装后可以直接调用：

```text
使用 $kevin-writer，写一条 10 分钟口播稿。
受众是 Palo Alto 600 万到 800 万美元房产的卖家，
核心判断是：没有明确搬迁或资金需求时，不要急着卖。
```

```text
使用 $kevin-writer 审核这篇稿子。
重点检查：是不是通篇用“您”、有没有连续碎短句、
数据有没有翻译成人话、是否出现两个重 CTA。
```

```text
使用 $kevin-writer，把这篇市场分析改成 Kevin 能直接录的口播稿。
不要新增事实；缺少数据、案例和服务入口时，使用规范占位符。
```

```text
使用 $kevin-writer，写一条 Newark 独栋价格分层口播。
从 transaction-cases.md 的逐笔索引选取当地成交价作团队样本，
不要只引用“31 套、1.21 亿美元”的汇总，也不要补造面积或房况。
```

如果稿件仍含 `【待补：…】`，Skill 会将其标为“待补稿”，不会冒充可直接拍摄的成稿。

## 项目结构

```text
kevin-writer/
├── AGENTS.md
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── 65-口播稿语言风格规范_团队版_2026-09-24.md
    ├── content-playbook.md
    ├── persona.md
    ├── script-angle/
    │   ├── guide.md
    │   ├── conversion-score.md
    │   ├── ledger-template.md
    │   ├── method-cards.md
    │   └── methodology.md
    └── transaction-cases.md
```

- [`SKILL.md`](SKILL.md)：触发范围、工作流、事实门与交付标准。
- [`AGENTS.md`](AGENTS.md)：仓库维护规则，以及 README 强制同步要求。
- [`persona.md`](references/persona.md)：Kevin 的人物定位、可信度来源和事实边界。
- [`content-playbook.md`](references/content-playbook.md)：内容类型、结构、节奏与平台适配。
- [`transaction-cases.md`](references/transaction-cases.md)：31 笔去地址成交价格索引、团队业绩汇总，以及五笔可按主题展开的完整交易案例。
- [`65-口播稿语言风格规范_团队版_2026-09-24.md`](references/65-口播稿语言风格规范_团队版_2026-09-24.md)：当前团队语言标准；固定模板服从出品优先级。
- [`script-angle/guide.md`](references/script-angle/guide.md)：动笔前的写法筛选、预览卡和用户选择流程；配套资料按需读取。

## 规则优先级

发生冲突时，按以下顺序执行：

1. 用户在当前任务中的明确要求
2. 事实核验与隐私边界（不能用风格或模板豁免）
3. `SKILL.md` 的出品最高优先级：逻辑清楚、信息密、说得顺
4. 团队语言标准的其余规则与 `SKILL.md` 工作流
5. 用户选定的写法骨架，再由内容结构手册补充包装；历史样本不决定语言

语言规范与旧样本冲突时，直接删除旧写法，不兼容、不折中。

## 维护约定

`README.md` 必须与 Skill 同步维护。凡是修改 `SKILL.md`、`agents/`、`references/`、`scripts/` 或 `assets/`，都必须在同一轮工作、同一个提交中：

1. 更新 README 中受影响的能力说明、规则、目录和使用示例；
2. 清理失效链接、过期路径和与当前 Skill 冲突的旧描述；
3. 运行 Skill 校验并检查 README 的本地链接；
4. 即使 README 正文无需改写，也要更新下方同步日期，留下已复核的记录。

详细执行规则见 [`AGENTS.md`](AGENTS.md)。

**最近同步：2026-09-30（出品优先级、内置写法选择与 31 笔成交引用规则已复核）**

## 其他智能体

这个仓库采用 Codex Skill 结构。其他智能体如果不支持 Skill 自动发现，仍可读取 `SKILL.md` 和 `references/` 作为项目级写作规范，但能否自动调用取决于具体客户端。

## 更新

在 Skill 目录执行：

```bash
git pull origin main
```

仓库地址：<https://github.com/leoking1987/kevin-writer>
