# Kevin Writer

> Kevin Mo（MK GROUP）湾区/硅谷房产频道的高认知真诚客观型脚本创作与深度改稿 Skill（v2）。

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Language](https://img.shields.io/badge/language-简体中文-dc2626)
![Version](https://img.shields.io/badge/version-v2-2563eb)

## 它能做什么

`kevin-writer` 用于 Kevin Mo 湾区/硅谷房产频道的脚本从零撰写、初稿逐段精修、全文顺稿润色、口播去废话、行动建议 / CTA 重构，以及产出原稿与改写版左右对照 Word（`.docx`）文档。

面向**硅谷高认知、习惯 1.5 倍速看内容的理性决策者**，围绕四项核心原则：

1. **立场真诚（敢先劝退）**：打破“双面劝买”的常规中介话术，先明确说出哪几类人当下最好什么都不做，肯定租房与继续持有低息房的理性价值。
2. **完全客观（不恐吓唱衰）**：绝不对观众个人房产扣“会跌价 / 卖不掉 / 没人接手”的恐吓句，所有下行压力与流动性变化均落回客观盘面、细分区域与房型。
3. **数据硬核（反差贴脸放 + 因果桥）**：对立数据紧挨输出，跨层级指标补齐因果过渡，用真实一线实盘替代虚构假设；严禁编造数据，缺口显式标出 `【待补：...】`。
4. **表达精炼（尊重智商与时间）**：删尽基础算术、常识鸡汤与 AI 套话，每段只做「核心判断 → 硬数据对比 → 机制与推论」单线推进；CTA 定位为「决策体检」而非催成交。

## 两种标准工作流

- **流程 A（全文改稿 + 左右对照 `.docx`）**：还原左栏原稿 → 按核心规范重构右栏（保留 100% 硬数据并标出 `【待补】`）→ 调用 [`scripts/render_comparison_docx.py`](scripts/render_comparison_docx.py) 生成 US Letter 横向三列对照 Word 文档（含顶部摘要卡、跨页表头、行不截断与 `【待补】` 高亮）。
- **流程 B（单段改写 / 从零起稿）**：单段改写直接给干净正文；从零起稿按五幕骨架输出（反差开场 → 盘面数据拆解 → 机制与分化证据 → 关键时间节点/观测信号 → 先劝退再分层建议 + 决策体检 CTA + 客观收口）。

完整规则见 [`SKILL.md`](SKILL.md)，改前改后范例与交稿自检见 [`references/style-checklist.md`](references/style-checklist.md)。

## 事实与合规边界

- **严禁编造**：不杜撰未核实的百分比、劝退次数或客户故事；缺数显式标注 `【待补：具体缺什么数据】`。
- **守住证据等级**：不把“可能 / 不一定 / 相对看好”拔高为绝对预测，明确区分整体中位数据与个体房源表现。
- **合规红线**：严格遵守 Fair Housing（只讲地段、供给、设施与数据，不按族裔/国籍/宗教/家庭状况刻画社区）；涉税、法、保险只做客观事实提醒，不替代专业顾问意见。

## 安装

### 让 Codex 安装

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

安装完成后通过 `$kevin-writer` 调用。如需运行左右对照 Word 生成脚本，请确保 Python 环境已安装 `python-docx`。

## 调用示例

```text
使用 $kevin-writer，把这份湾区市场视频初稿逐段精修，
并生成原稿 vs 改写版左右对照 .docx 文档。
要求保留全部硬数据、先劝退再给方案、清零 AI 套话和恐吓句。
```

```text
使用 $kevin-writer，从零起稿一条硅谷湾区房市分析脚本。
按五幕骨架输出：反差开场、盘面数据拆解、机制与分化证据、
关键观测信号、先劝退再分层建议与决策体检 CTA。
```

## 项目结构

```text
kevin-writer/
├── AGENTS.md
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── style-checklist.md
└── scripts/
    └── render_comparison_docx.py
```

- [`SKILL.md`](SKILL.md)：核心观众立场、数据叙事纪律、行动建议与 CTA 范式、禁用词与双工作流。
- [`references/style-checklist.md`](references/style-checklist.md)：5 组改前 vs 改后实战范例与 6 项交稿前硬自检清单。
- [`scripts/render_comparison_docx.py`](scripts/render_comparison_docx.py)：可复用的横向三列左右对照 `.docx` 渲染脚本。
- [`agents/openai.yaml`](agents/openai.yaml)：界面描述与默认调用提示。
- [`AGENTS.md`](AGENTS.md)：仓库维护与 README 同步规则。

## 规则优先级

1. 用户当前明确要求
2. 事实核验、证据等级与 Fair Housing 合规红线
3. [`SKILL.md`](SKILL.md) 核心规范与工作流
4. [`references/style-checklist.md`](references/style-checklist.md) 改稿对照与自检清单

## 维护约定

`README.md` 必须与 Skill 同步维护，详细规则见 [`AGENTS.md`](AGENTS.md)。

**最近同步：2026-11-26（整体替换为 `kevin-script-v2` 高认知真诚客观型脚本工作流，精简为 `SKILL.md` + `references/style-checklist.md` + `scripts/render_comparison_docx.py`，彻底清理旧版冗余参考文件）**

仓库地址：<https://github.com/leoking1987/kevin-writer>
