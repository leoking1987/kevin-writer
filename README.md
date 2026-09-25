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
| 对话对象 | 一位具体客户；通篇使用“您” |
| 开场 | 前 10 秒点名目标观众并给判断，前 30 秒兑现冲突与问题承诺 |
| 主线 | 一个问题、一个主要受众、一个核心观点 |
| 句子 | 按气口写，不用连续碎短句，不把脚本写成一句一行 |
| 数据 | 先说数字说明什么，每段最多两组核心数字，来源实名 |
| 判断 | 明确建议、适用范围、具体例外和改判信号 |
| CTA | 每期一个主 CTA，最多一个轻量辅助动作 |
| 事实纪律 | 不编客户、成交、内部消息和一线观察；缺失内容使用 `【待补：需要什么】` |
| 交付门槛 | 18 项自检低于 29/36，不进入拍摄 |

完整语言规则以 [`65-口播稿语言风格规范_团队版_2026-09-24.md`](references/65-口播稿语言风格规范_团队版_2026-09-24.md) 为唯一标准。历史热门视频只提供主题、结构和专业判断证据，不参与语言定调。

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

如果稿件仍含 `【待补：…】`，Skill 会将其标为“待补稿”，不会冒充可直接拍摄的成稿。

## 项目结构

```text
kevin-writer/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── 65-口播稿语言风格规范_团队版_2026-09-24.md
    ├── content-playbook.md
    └── persona.md
```

- [`SKILL.md`](SKILL.md)：触发范围、工作流、事实门与交付标准。
- [`persona.md`](references/persona.md)：Kevin 的人物定位、可信度来源和事实边界。
- [`content-playbook.md`](references/content-playbook.md)：内容类型、结构、节奏与平台适配。
- [`65-口播稿语言风格规范_团队版_2026-09-24.md`](references/65-口播稿语言风格规范_团队版_2026-09-24.md)：语言规则的最高优先级来源。

## 规则优先级

发生冲突时，按以下顺序执行：

1. 用户在当前任务中的明确要求
2. `65-口播稿语言风格规范_团队版_2026-09-24.md`
3. `SKILL.md`
4. `content-playbook.md` 与历史视频样本

语言规范与旧样本冲突时，直接删除旧写法，不兼容、不折中。

## 其他智能体

这个仓库采用 Codex Skill 结构。其他智能体如果不支持 Skill 自动发现，仍可读取 `SKILL.md` 和 `references/` 作为项目级写作规范，但能否自动调用取决于具体客户端。

## 更新

在 Skill 目录执行：

```bash
git pull origin main
```

仓库地址：<https://github.com/leoking1987/kevin-writer>
