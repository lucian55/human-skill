#!/usr/bin/env python3
"""Batch +10: append after 马化腾 / 小燕子 / 奇犽 table rows. Run from repo root."""
from __future__ import annotations

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, "README.md")

REAL_4: list[tuple[str, str, str, str, str, str, str]] = [
    ("hanhong-skill", "real-people", "韩红", "天路、慈善", "歌手 / 公益", "高音情感爆发、救灾叙事、直球正义人设", "非替基金会官方发言"),
    ("linjunjie-skill", "real-people", "林俊杰", "江南、修炼爱情", "歌手 / 创作", "技术流情歌、游戏宅梗、自律创作人设", "非替本人编造"),
    ("zhengqinwen-skill", "real-people", "郑钦文", "法网、Queen Wen", "网球 / 体育", "攻击性底线、采访直球、新生代自信", "非煽动对立"),
    ("dongyuhui-skill", "real-people", "董宇辉", "东方甄选、直播讲书", "主播 / 知识带货", "小作文金句、共情带货、文化人壳", "非替东方甄选官方发言"),
]

FIC_3: list[tuple[str, str, str, str, str, str, str]] = [
    ("guofurong-skill", "fiction-tv", "郭芙蓉", "武林外传", "情景喜剧虚构", "排山倒海梗、侠女梦与现实抠门、成长嘴硬", "虚构；忌暴力模仿"),
    ("lvxiucai-skill", "fiction-tv", "吕秀才", "武林外传", "情景喜剧虚构", "子曰嘴炮、读书人迂阔与意外高光", "虚构"),
    ("baizhantang-skill", "fiction-tv", "白展堂", "武林外传", "情景喜剧虚构", "盗圣反差、胆小负责、葵花点穴梗", "虚构；忌暴力模仿"),
]

ANI_3: list[tuple[str, str, str, str, str, str, str]] = [
    ("kakashi-skill", "animation", "旗木卡卡西", "火影忍者", "少年漫", "迟到的老师、写轮眼悬念、慵懒靠谱", "虚构；非暴力教唆"),
    ("midoriya-skill", "animation", "绿谷出久", "我的英雄学院", "少年漫", "无个性起点、笔记英雄学、哭腔热血", "虚构；非暴力教唆"),
    ("tsukino-usagi-skill", "animation", "月野兔", "美少女战士", "少女漫", "爱哭变身、闺蜜线、代表月亮宣言", "虚构；勿抄版权对白"),
]

SKILLS10 = REAL_4 + FIC_3 + ANI_3

MARKER_REAL = (
    "| [马化腾.skill](./real-people/mahuateng-skill/README.md) "
    "| 互联网企业家 | 低调闷声、连接一切、抄与超越梗（解构用）；非替腾讯承诺；忌造谣 |\n"
)
MARKER_FIC = (
    "| [小燕子.skill](./fiction-tv/xiaoyanzi-skill/README.md) "
    "| 古装喜剧虚构 | 民间丫头闯宫、反规矩活力、闯祸成长；虚构 |\n"
)
MARKER_ANI = (
    "| [奇犽.skill](./animation/killua-skill/README.md) "
    "| 少年漫 | 刺客家族反差、甜食梗、友情的信任；虚构；非暴力教唆 |\n"
)


def write_skill(
    slug: str,
    cat: str,
    zh: str,
    trigger: str,
    domain: str,
    blurb: str,
    guard: str,
) -> None:
    base = os.path.join(ROOT, cat, slug)
    os.makedirs(os.path.join(base, "references", "research"), exist_ok=True)

    syn = f"""# {zh} · 公开/剧作语料摘要（压缩版）

> 本 skill 为**快速蒸馏包**：便于检索与触发；细化论证请补充权威来源并自行核对。

## 01 定位

- **人物/角色**：{zh}  
- **领域标签**：{domain}  
- **触发联想**：{trigger}

## 02 可迁移框架（归纳）

- {blurb}

## 03 诚实边界

- {guard}  
- 不冒充本人或版权方；不编造未公开言论与情节当事实。

## 04 使用建议

- 优先阅读同目录 [`SKILL.md`](./SKILL.md) 的 First Questions 与 Guardrails 再开写。
"""

    blurb_head = blurb[:78] + ("…" if len(blurb) > 78 else "")
    guard_head = guard[:58] + ("…" if len(guard) > 58 else "")
    skill_md = f"""---
name: {slug}
description: |
  {zh}（{domain}）认知与表达框架（压缩蒸馏）：{blurb_head}
  触发：{trigger} 等。{guard_head}
---

# {zh} · 思维操作系统（压缩版）

## 语料摘要

- 详见 [`references/research/nuwa-phase1-synthesis.md`](references/research/nuwa-phase1-synthesis.md)。

## 激活方式

- 默认：**第三人称顾问**，迁移框架不写侮辱与违法细节。  
- 用户越界请求 → 按 Guardrails 拒绝并给替代。

## First Questions

1. 场景：**写作 / 剧本 / 评论 / 演讲 / 复盘**？  
2. 受众与底线：**全年龄 / 成人 / 虚构反面教材**？  
3. 需要 **第一人称扮演** 还是 **结构抽取**？

## 核心心智模型（压缩）

### 模型 A：标签化入口

**一句话**：用公众最熟的**一个意象或一句功能**把人立住，再展开。

### 模型 B：矛盾驱动

**一句话**：写作张力来自**自我矛盾或环境错位**，先写矛盾再写台词。

### 模型 C：收束伦理

**一句话**：段末回到**可执行善意或虚构声明**，防误读教唆。

## 决策启发式

1. 这话会伤害**弱势群体**吗？  
2. 需要**来源脚注**吗？（真实人物/历史）  
3. 虚构反派是否标明**反面教材**？

## 反模式

- 伪造名言、伪造剧情当新闻。  
- 教唆违法、歧视、骚扰。  
- 把压缩包当**严谨传记**或**法律意见**。

## Guardrails

- {guard}  
- 见 synthesis 与同目录 README。

## Examples

**用户**：给我一个 80 字开场白骨架。  
**方向**：标签入口 + 矛盾一句 + 虚构声明（若适用）。
"""

    readme = f"""# {zh}.skill

{zh} 的**压缩蒸馏** skill：适合快速搭写作/评论/剧本结构。完整论证请自行查权威材料。

## 文档

- [`references/research/nuwa-phase1-synthesis.md`](references/research/nuwa-phase1-synthesis.md)  
- [`SKILL.md`](SKILL.md)

## 使用示例

```text
用 {zh} 式框架写一段 200 字评论骨架，不要伪造引语
按 {slug} 的 First Questions 先问清场景再写对白
```

## 安装

```bash
npx skills add lucian55/human-skill/{cat}/{slug}
```

"""

    for path, content in [
        (os.path.join(base, "references", "research", "nuwa-phase1-synthesis.md"), syn),
        (os.path.join(base, "SKILL.md"), textwrap.dedent(skill_md).strip() + "\n"),
        (os.path.join(base, "README.md"), readme),
    ]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def readme_row(slug: str, cat: str, zh: str, _: str, domain: str, blurb: str, guard: str) -> str:
    path = f"./{cat}/{slug}/README.md"
    short = blurb.replace("|", "｜")[:42] + ("…" if len(blurb) > 42 else "")
    gshort = guard.replace("|", "｜")[:24]
    return f"| [{zh}.skill]({path}) | {domain} | {short}；{gshort} |\n"


def patch_readme() -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    ins_r = "".join(readme_row(*t) for t in REAL_4)
    ins_f = "".join(readme_row(*t) for t in FIC_3)
    ins_a = "".join(readme_row(*t) for t in ANI_3)
    if MARKER_REAL not in content:
        raise SystemExit("README marker (马化腾) not found")
    if MARKER_FIC not in content:
        raise SystemExit("README marker (小燕子) not found")
    if MARKER_ANI not in content:
        raise SystemExit("README marker (奇犽) not found")
    content = content.replace(MARKER_REAL, MARKER_REAL + ins_r, 1)
    content = content.replace(MARKER_FIC, MARKER_FIC + ins_f, 1)
    content = content.replace(MARKER_ANI, MARKER_ANI + ins_a, 1)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    assert len(SKILLS10) == 10, len(SKILLS10)
    for row in SKILLS10:
        write_skill(*row)
    patch_readme()
    print("OK: +10 skills + README append")


if __name__ == "__main__":
    main()
