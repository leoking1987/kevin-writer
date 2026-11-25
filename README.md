# Kevin Writer

> 为 Kevin Mo 打造的中文个人品牌社媒写作 Skill：写出逻辑锋利、口语自然、贴合社媒完播节奏、按主题原生定制的硅谷局内人表达。

![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Language](https://img.shields.io/badge/language-简体中文-dc2626)
![Version](https://img.shields.io/badge/architecture-v2_Social_Retention-2563eb)

## 它能做什么

`kevin-writer` 用于创作、改写和审核 Kevin Mo 的中文个人品牌内容，覆盖：

- YouTube 长 / 中 / 短视频口播（Shorts / Reels / 视频号）
- 小红书与社交媒体干货图文
- 湾区市场异动、科技/AI 与政策传导链解读
- 城市与社区真实生活对比、买卖与换房摊牌算账
- 高净值复杂交易框架与湾区生活成本内容

它不是把资料整理成一份四平八稳的免责报告，而是让 Kevin 像坐在观众对面，拿一支笔把最容易算错的那笔账圈出来——专业但不学术、干脆但不浮夸、有锋芒但不训人。

## 四条核心写作铁律

1. **活人说话，去合规报告腔与端水腔**：通篇用“您”但不客套；先亮观点、再一句划清例外，禁止每段自我找补（如“但这也不能证明 / 也不能这么说 / 未必”），把抽象名词换成看得见的动作和账单。
2. **脱离旧案与旧模板，一题一味**：默认不读历史 Top5 全文、不强塞团队成交案例库，按题材切换原生口感（侦探剥洋葱 / 多米诺传导链 / 摊牌算账 / 生活切片对撞 / 松弛账本吐槽），彻底告别所有主题一个味道。
3. **一根主骨，单向推进，绝不啰嗦**：每篇只打穿 1 个主矛盾，走完 3–4 个单向递进大拍；同一观点只打一次，交稿前瘦身砍掉 15%–25% 废话铺垫，绝不为凑 10 分钟注水。
4. **社媒完播引擎**：前 3–5 秒冷开场（反常事实 / 二选一站队 / 戳破盲区 / 账单直切，严禁复读标题），中段靠 Re-Hook 钩子接力拉完播，结尾 1–2 句干脆收束并自然引导互动或单个轻 CTA。

## 按需参考与默认交付

- **按需读取（Lazy Loading）**：核心规则收拢在 [`SKILL.md`](SKILL.md)，参考文件仅按需查阅；[`transaction-cases.md`](references/transaction-cases.md) 与 [`youtube-top5/`](references/youtube-top5/index.md) 默认不自动注入，防止旧案污染新题材。
- **默认交付**：3–5 个高点击标题候选 + 可直接录/发的干净成稿。
- **按需制作包**：仅当用户明确要求分镜/B-roll 或先看多种写法方案时，再分别触发 [`broll-annotation.md`](references/broll-annotation.md) 或 [`script-angle/guide.md`](references/script-angle/guide.md)。

## 事实与隐私红线

- **零编造**：不虚构客户、成交、对话、数据、房源状态、内幕或 Kevin 亲历；缺失关键事实用 `【待补：需要什么】` 并标注 `状态：待补稿`。
- **时效与口径**：时效数据核验可靠来源，口播顺口带出日期范围，精确口径放文末备注或字卡。
- **归属与合规**：团队做的说“我们”，本人亲历才说“我”；客户去标识化，遵守 Fair Housing，法律/税务/贷款只讲决策框架、不做收益保证。

## 安装

### 让 Codex 安装

```text
请从 https://github.com/leoking1987/kevin-writer 安装这个 Skill。
```

### 手动安装

```powershell
git clone https://github.com/leoking1987/kevin-writer.git `
  "$env:USERPROFILE\.codex\skills\kevin-writer"
```

安装完成后在支持 Skills 的环境中通过 `$kevin-writer` 调用。

## 调用示例

```text
使用 $kevin-writer，写一条 60 秒短视频口播。
主题：为什么湾区千万豪宅里，50 年老房反而比新房卖得更快？
要求：3 秒冷开场、单线剥洋葱、不念报表、不端水，结尾留互动问题。
```

```text
使用 $kevin-writer，写一篇 8 分钟 YouTube 长视频口播。
主题：AI 大厂裁员潮下，硅谷房价为什么没按大家想的往下掉？
要求：走多米诺传导链，3–4 个大拍推进，中段带 Re-Hook，不硬塞成交案例。
```

```text
使用 $kevin-writer 审核并重写这篇旧稿。
重点干掉里面的端水免责句、兜圈子段落和慢热开头，保留真实数据与口径。
```

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
    ├── broll-annotation.md
    ├── content-playbook.md
    ├── humanization-pass.md
    ├── persona.md
    ├── platform-register.md
    ├── title-patterns-maggie.md
    ├── transaction-cases.md
    ├── writing-dna.md
    ├── script-angle/
    │   ├── conversion-score.md
    │   ├── guide.md
    │   ├── ledger-template.md
    │   ├── method-cards.md
    │   └── methodology.md
    └── youtube-top5/
        ├── 01-JpKYltxiqps.md
        ├── 02--ctQstVxw84.md
        ├── 03-zapfE7XlWF8.md
        ├── 04-ZVgXT3JoRJw.md
        ├── 05-UZn3x7YcksE.md
        ├── calibration.md
        ├── index.md
        ├── manifest.json
        └── voice-evidence.md
```

- [`SKILL.md`](SKILL.md)：核心铁律、事实红线、极简写作流与按需参考索引。
- [`agents/openai.yaml`](agents/openai.yaml)：界面描述与默认调用提示。
- [`AGENTS.md`](AGENTS.md)：仓库维护与 README 同步规则。
- [`writing-dna.md`](references/writing-dna.md)：Kevin 的 6 层声纹基线及与 Marie 的差异定位。
- [`content-playbook.md`](references/content-playbook.md)：社媒完播引擎（Cold Open / Re-Hook）与五大题材原生结构。
- [`humanization-pass.md`](references/humanization-pass.md)：去机械腔、去端水免责与事实保真润色清单。
- [`platform-register.md`](references/platform-register.md)：短视频、YouTube 中长视频、小红书与正式材料语域。
- [`title-patterns-maggie.md`](references/title-patterns-maggie.md)：高点击标题规律与 Kevin 本地化公式。
- [`persona.md`](references/persona.md)：人物底盘与传记边界。
- [`65-口播稿语言风格规范_团队版_2026-09-24.md`](references/65-口播稿语言风格规范_团队版_2026-09-24.md)：团队称呼、气口、数字口语化与禁语补充参考。
- [`transaction-cases.md`](references/transaction-cases.md)：可选成交证据库（31 笔价格索引 + 5 笔细节），仅在主题需要时按需调用。
- [`broll-annotation.md`](references/broll-annotation.md)：按需触发的定稿后 A/B-roll 画面分析与策划规范。
- [`script-angle/guide.md`](references/script-angle/guide.md)：按需触发的多写法方案预览与选择流程。
- [`youtube-top5/calibration.md`](references/youtube-top5/calibration.md)：可选历史声纹档案使用边界（防旧案与 2020 年播报腔污染）。

## 规则优先级

1. 用户当前明确要求
2. 事实核验、去标识化隐私与 Fair Housing 红线
3. [`SKILL.md`](SKILL.md) 的四条核心铁律（活人口语、一题一味、单向逻辑、社媒完播）
4. [`writing-dna.md`](references/writing-dna.md)、[`content-playbook.md`](references/content-playbook.md) 与 [`humanization-pass.md`](references/humanization-pass.md)
5. 其他按需调用的参考文件与可选档案

## 维护约定

`README.md` 必须与 Skill 同步维护，详细规则见 [`AGENTS.md`](AGENTS.md)。

**最近同步：2026-11-25（重构 v2 架构：大幅精简 SKILL.md 解除规则僵化、根治端水报告腔、取消历史 Top5 与旧案例强制绑定防止同质化、建立单向 3–4 拍主骨逻辑与社媒 Cold Open / Re-Hook 完播引擎）**

仓库地址：<https://github.com/leoking1987/kevin-writer>
