#!/usr/bin/env python3
"""Batch 4: 50 human-skill packs + append README rows after 许子东 / 胡一菲 / 哆啦A梦. Run from repo root."""
from __future__ import annotations

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, "README.md")

# slug, category, zh, trigger, domain, blurb, guard
REAL_24: list[tuple[str, str, str, str, str, str, str]] = [
    ("hejiong-skill", "real-people", "何炅", "快乐大本营、向往", "主持 / 综艺", "零差评老好人壳、圆场与递台阶、少年感主持", "非替湖南卫视发言"),
    ("sabeining-skill", "real-people", "撒贝宁", "今日说法、明星大侦探", "主持 / 法制综艺", "法制梗与综艺反差、知识炫耀式幽默", "非法律意见"),
    ("wanghan-skill", "real-people", "汪涵", "天天向上", "主持", "大哥式控场、方言与文化包袱、慢语速权威", "非官方背书"),
    ("yaoming-skill", "real-people", "姚明", "NBA、篮协", "篮球 / 体育", "身高隐喻幽默、中美桥梁叙事、体制内转型话术", "非煽动球迷对立"),
    ("li-na-skill", "real-people", "李娜", "法网、直率采访", "网球 / 体育", "个性球员叙事、怼媒体金句、职业化独立", "非替本人编造"),
    ("liuxiang-skill", "real-people", "刘翔", "110 米栏、退赛舆论", "田径 / 体育", "巅峰与伤病叙事、民族情绪收束、运动员主体性", "不消费伤痛；尊重运动员"),
    ("guailing-skill", "real-people", "谷爱凌", "冬奥、双文化", "冰雪 / 体育", "学霸运动员、中美双文化话术、品牌亲和力", "非替本人编造"),
    ("subingtian-skill", "real-people", "苏炳添", "百米、亚洲纪录", "田径 / 体育", "大龄突破叙事、科学训练梗、低调激情", "非兴奋剂暗示"),
    ("langping-skill", "real-people", "郎平", "女排、铁榔头", "排球 / 教练", "集体主义与个人英雄平衡、暂停与换人话术", "非煽动对立"),
    ("zhangyiming-skill", "real-people", "张一鸣", "字节、推荐算法", "互联网创业", "延迟满足、Context not control、全球化叙事", "非内幕交易；非替公司发言"),
    ("renzhengfei-skill", "real-people", "任正非", "华为、内部信", "企业家", "危机讲话、灰度管理、家长式务实", "非替华为官方表态"),
    ("zhangxiaolong-skill", "real-people", "张小龙", "微信公开课", "产品经理", "克制功能、用完即走、工具哲学", "非替腾讯承诺功能"),
    ("wangxing-skill", "real-people", "王兴", "美团、饭否语录", "互联网创业", "极简刻薄金句、无限游戏叙事", "非荐股；非内幕"),
    ("dinglei-skill", "real-people", "丁磊", "网易、养猪梗", "互联网创业", "佛系老板、游戏与音乐品味人设", "非替网易发言"),
    ("liudehua-skill", "real-people", "刘德华", "天王、无间道", "歌手 / 演员", "勤奋劳模叙事、全民偶像亲和力、自律人设", "非替本人编造隐私"),
    ("zhangxueyou-skill", "real-people", "张学友", "歌神、逃犯克星梗", "歌手 / 演员", "情歌技术流、演唱会叙事、梗图二次传播", "忌违法玩梗越界"),
    ("zhouyunfa-skill", "real-people", "周润发", "英雄本色、赌神", "演员", "小马哥式兄弟情、潇洒与落魄反差", "虚构角色与本人区分"),
    ("shuqi-skill", "real-people", "舒淇", "文艺片、松弛感", "演员", "性感与文艺并置、自嘲大嘴、慢热真诚", "非替本人编造"),
    ("tangwei-skill", "real-people", "汤唯", "色戒、晚秋", "演员", "隐忍表演、语言切换、作者片气质", "非替本人编造"),
    ("zhangziyi-skill", "real-people", "章子怡", "一代宗师、野心脸", "演员", "狠劲与脆弱同框、国际章叙事、综艺真性情", "非替本人编造"),
    ("liuzhenyun-skill", "real-people", "刘震云", "一句顶一万句、茅奖", "作家", "乡土絮叨哲学、冷幽默绕弯、饭局话里有话", "不伪造引文"),
    ("wangshuo-skill", "real-people", "王朔", "动物凶猛、顽主", "作家 / 京味", "痞子真诚、反崇高、口语暴力美学", "净版改写；忌侮辱弱势群体"),
    ("liyanhong-skill", "real-people", "李彦宏", "百度、AI", "互联网企业家", "技术乐观、All in AI 叙事、公关危机话术", "非替百度官方发言"),
    ("mahuateng-skill", "real-people", "马化腾", "腾讯、产品经理", "互联网企业家", "低调闷声、连接一切、抄与超越梗（解构用）", "非替腾讯承诺；忌造谣"),
]

FIC_16: list[tuple[str, str, str, str, str, str, str]] = [
    ("sunwukong-tv-skill", "fiction-tv", "孙悟空", "86 西游、大话对比", "神话剧虚构", "闹天宫与取经成长、顽童与佛性张力", "虚构；非宗教教义"),
    ("wusong-skill", "fiction-tv", "武松", "水浒传", "古典虚构", "快意恩仇、醉打叙事、刚烈悲剧", "禁止可模仿暴力细节"),
    ("likui-skill", "fiction-tv", "李逵", "水浒传", "古典虚构", "黑旋风直球、忠诚与滥杀张力", "反面教材；禁止暴力教唆"),
    ("liubei-skill", "fiction-tv", "刘备", "三国演义", "历史剧虚构", "仁德话术、哭戏政治、桃园叙事", "虚构；非史学定论"),
    ("guanyu-skill", "fiction-tv", "关羽", "三国演义", "历史剧虚构", "义绝标签、红脸威严、骄傲败因", "虚构"),
    ("zhangfei-skill", "fiction-tv", "张飞", "三国演义", "历史剧虚构", "莽撞勇猛、敬君子慢小人", "虚构；忌可模仿暴力"),
    ("jixiaolan-skill", "fiction-tv", "纪晓岚", "铁齿铜牙", "古装喜剧虚构", "机智对联、讽和珅、文人痞气", "虚构"),
    ("heshen-skill", "fiction-tv", "和珅", "铁齿铜牙", "反派虚构", "贪官话术、媚上幽默、反面教材", "反面教材；禁止腐败教唆"),
    ("ziwei-huanzhu-skill", "fiction-tv", "紫薇", "还珠格格", "古装喜剧虚构", "柔弱才情、认亲线、眼泪正义", "虚构"),
    ("tangjing-skill", "fiction-tv", "唐晶", "我的前半生", "都市剧虚构", "闺蜜边界、职场精英冷感、理性分手", "虚构"),
    ("luozijun-skill", "fiction-tv", "罗子君", "我的前半生", "都市剧虚构", "全职太太 reboot、成长线与争议依赖", "虚构"),
    ("hehan-skill", "fiction-tv", "贺涵", "我的前半生", "都市剧虚构", "导师型男主、职场金句、情感争议", "虚构；忌情感操控教程"),
    ("bainiangzi-skill", "fiction-tv", "白娘子", "新白娘子传奇", "神话剧虚构", "报恩恋、法术壳、人间伦理", "虚构；非宗教教义"),
    ("xuxian-skill", "fiction-tv", "许仙", "新白娘子传奇", "神话剧虚构", "懦弱书生、凡俗与仙恋张力", "虚构"),
    ("rongma-skill", "fiction-tv", "容嬷嬷", "还珠格格", "反派虚构", "针刑符号、忠仆反派、童年阴影喜剧化", "反面教材；禁止暴力模仿"),
    ("xiaoyanzi-skill", "fiction-tv", "小燕子", "还珠格格", "古装喜剧虚构", "民间丫头闯宫、反规矩活力、闯祸成长", "虚构"),
]

ANI_10: list[tuple[str, str, str, str, str, str, str]] = [
    ("nobita-skill", "animation", "野比大雄", "哆啦A梦", "子供向", "废柴主角成长线、善良底、道具依赖喜剧", "勿逐字抄录版权对白"),
    ("naruto-skill", "animation", "漩涡鸣人", "火影忍者", "少年漫", "吊车尾逆袭、嘴遁与羁绊、不认输口号", "虚构；非暴力教唆"),
    ("sasuke-skill", "animation", "宇智波佐助", "火影忍者", "少年漫", "复仇者弧光、高冷战力、兄弟叙事", "虚构；非暴力教唆"),
    ("gojo-skill", "animation", "五条悟", "咒术回战", "少年漫", "无敌教师、眼罩梗、领域展开爽点", "虚构；非暴力细节"),
    ("haibara-skill", "animation", "灰原哀", "名侦探柯南", "少年推理漫", "冷静毒舌、科学家壳、少年身体隐喻", "虚构；禁止犯罪细节"),
    ("amuro-skill", "animation", "安室透", "名侦探柯南", "少年推理漫", "三重身份张力、波本梗、服务生伪装", "虚构；禁止犯罪教唆"),
    ("misaka-skill", "animation", "御坂美琴", "某科学的超电磁炮", "少年漫", "炮姐傲娇、正义感、学园都市梗", "虚构"),
    ("levi-skill", "animation", "利威尔", "进击的巨人", "少年漫", "兵长洁癖战力、矮个子反差、残酷抉择", "虚构；非仇恨教唆"),
    ("ichigo-skill", "animation", "黑崎一护", "BLEACH", "少年漫", "守护宣言、代打美学、成长型热血", "虚构；非暴力教唆"),
    ("killua-skill", "animation", "奇犽", "全职猎人", "少年漫", "刺客家族反差、甜食梗、友情的信任", "虚构；非暴力教唆"),
]

SKILLS50 = REAL_24 + FIC_16 + ANI_10

MARKER_REAL = (
    "| [许子东.skill](./real-people/xuzidong-skill/README.md) "
    "| 学者 / 评论 | 材料与梗混搭、人物册页式短评；非伪造文献 |\n"
)
MARKER_FIC = (
    "| [胡一菲.skill](./fiction-tv/huyifei-skill/README.md) "
    "| 情景喜剧虚构 | 公寓女王、武力梗喜剧化、嘴硬心软；虚构；忌暴力模仿 |\n"
)
MARKER_ANI = (
    "| [哆啦A梦.skill](./animation/doraemon-skill/README.md) "
    "| 子供向 | 道具脑洞、大雄成长线、温柔科幻；勿逐字抄录版权对白 |\n"
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
    ins_r = "".join(readme_row(*t) for t in REAL_24)
    ins_f = "".join(readme_row(*t) for t in FIC_16)
    ins_a = "".join(readme_row(*t) for t in ANI_10)
    if MARKER_REAL not in content:
        raise SystemExit("README marker (许子东) not found — table tail changed?")
    if MARKER_FIC not in content:
        raise SystemExit("README marker (胡一菲) not found — table tail changed?")
    if MARKER_ANI not in content:
        raise SystemExit("README marker (哆啦A梦) not found — table tail changed?")
    content = content.replace(MARKER_REAL, MARKER_REAL + ins_r, 1)
    content = content.replace(MARKER_FIC, MARKER_FIC + ins_f, 1)
    content = content.replace(MARKER_ANI, MARKER_ANI + ins_a, 1)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    assert len(SKILLS50) == 50, len(SKILLS50)
    for row in SKILLS50:
        write_skill(*row)
    patch_readme()
    print("OK: batch4 wrote", len(SKILLS50), "skills + README append")


if __name__ == "__main__":
    main()
