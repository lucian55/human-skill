#!/usr/bin/env python3
"""Generate 50 human-skill packs (SKILL.md, README.md, nuwa-phase1-synthesis.md). Run from repo root."""
from __future__ import annotations

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# slug, category dir, zh name, en/trigger hint, domain tag, one_line blurb, guard note
SKILLS: list[tuple[str, str, str, str, str, str, str]] = [
    # real-people (24)
    ("libai-skill", "real-people", "李白", "诗仙、将进酒", "古典诗人", "豪放与自我投射、酒与月意象、功名张力", "非历史定论；不伪造诗句"),
    ("dufu-skill", "real-people", "杜甫", "诗史、三吏三别", "古典诗人", "沉郁、家国与民生句法、律诗起承转合", "不伪造诗文；哀悼体尊重"),
    ("sushi-skill", "real-people", "苏轼", "东坡、赤壁", "古典诗人", "旷达与自嘲、儒释道混搭比喻、生活哲学化", "引文须核对版本"),
    ("yuqiuyu-skill", "real-people", "余秋雨", "文化苦旅", "文化散文", "宏大叙事与历史意象、游记式议论", "非史学代写；不编造田野"),
    ("yizhongtian-skill", "real-people", "易中天", "百家讲坛", "历史通俗", "悬念切片、现代类比、口语讲史", "区分戏说与学术结论"),
    ("baiyansong-skill", "real-people", "白岩松", "新闻1+1", "新闻评论", "克制提问、价值收束、公共理性口吻", "非官方代言；不造谣"),
    ("huangzhizhong-skill", "real-people", "黄执中", "奇葩说", "辩论", "重构议题、受身与升维、情绪命名", "非诡辩教唆；不人身攻击"),
    ("pujian-skill", "real-people", "朴树", "平凡之路", "音乐人", "内向真诚、少话多留白、生命与创作一体", "不消费抑郁；非医疗建议"),
    ("cuijian-skill", "real-people", "崔健", "一块红布", "摇滚", "地下与现场感、隐喻与直白并置", "非煽动违法"),
    ("zhouxingchi-skill", "real-people", "周星驰", "无厘头导演", "喜剧作者", "小人物逆袭节奏、夸张反差、悲情底", "虚构创作谈；非私生活八卦"),
    ("zheng-yuanjie-skill", "real-people", "郑渊洁", "皮皮鲁", "儿童文学", "童话寓言化社会规则、儿童视角正义", "儿童安全；非恐吓教育"),
    ("hanhan-skill", "real-people", "韩寒", "三重门赛车", "作家车手", "反套路叙事、冷幽默、公共发言锋利", "不伪造赛事实；尊重他人"),
    ("jiazhangke-skill", "real-people", "贾樟柯", "小武三峡好人", "电影作者", "县城美学、时间停滞感、底层尊严镜头伦理", "非纪实裁断"),
    ("wangjiawei-skill", "real-people", "王家卫", "2046花样年华", "电影作者", "时间错位、独白、暧昧与失落母题", "非片场八卦"),
    ("gongli-skill", "real-people", "巩俐", "红高粱霸王别姬", "表演作者", "身体与气场、沉默戏、角色距离感", "非替本人发言"),
    ("zhangyimou-skill", "real-people", "张艺谋", "色彩大场面", "电影导演", "集体仪式、色彩符号、群像调度", "非官方活动内幕"),
    ("jiangwen-skill", "real-people", "姜文", "让子弹飞", "电影作者", "寓言暴力美学、台词密度、黑色幽默", "禁止现实暴力教唆"),
    ("luozhenyu-skill", "real-people", "罗振宇", "得到跨年", "知识服务", "长期主义叙事、概念产品化、故事化论证", "非成功学保证；非荐股"),
    ("fandeng-skill", "real-people", "樊登", "樊登读书", "讲书人", "拆书三段论、行动号召、温和说服", "非替代原著阅读；非心理咨询"),
    ("yilijing-skill", "real-people", "易立竞", "人物采访", "尖锐访谈", "压迫式提问、沉默施压、事实钉刺", "非羞辱；征得同意语境"),
    ("xuzhisheng-skill", "real-people", "徐志胜", "脱口秀", "喜剧", "自嘲外貌与社会观察、节奏松、梗软着陆", "不歧视群体"),
    ("xuzhiyuan-skill", "real-people", "许知远", "十三邀", "知识分子访谈", "反流量提问、尴尬坚持、思想史钩沉", "不冒充节目"),
    ("chenming-skill", "real-people", "陈铭", "奇葩说", "辩论", "上价值与共情平衡、爱的话语、学院派收束", "非道德绑架"),
    ("hewei-skill", "real-people", "贺炜", "足球诗人解说", "体育解说", "文学比喻嵌入赛况、克制激情、终场金句", "非煽动球迷对立"),
    ("huangjianxiang-skill", "real-people", "黄健翔", "激情解说", "体育解说", "爆发式观点、节奏陡升、立场鲜明", "非地域攻击；合规表达"),
    # fiction-tv (16)
    ("lin-daiyu-skill", "fiction-tv", "林黛玉", "红楼梦", "古典虚构", "敏感多思、诗谶、自尊与脆弱", "虚构；防抑郁消费"),
    ("jiabaoyu-skill", "fiction-tv", "贾宝玉", "红楼梦", "古典虚构", "情不情、反仕途经济、女儿崇拜叙事", "虚构；非性别刻板侮辱"),
    ("luzhishen-skill", "fiction-tv", "鲁智深", "水浒传", "古典虚构", "粗中有细、义字当头、暴力喜剧化", "禁止可模仿暴力细节"),
    ("linchong-skill", "fiction-tv", "林冲", "水浒传", "古典虚构", "隐忍到爆发、体制内小人物悲剧", "虚构；非现实报复教程"),
    ("zhugeliang-skill", "fiction-tv", "诸葛亮", "三国演义", "历史剧虚构", "锦囊叙事、谨慎天才、话术与士气", "非真实军事参谋"),
    ("caocao-skill", "fiction-tv", "曹操", "三国演义", "历史剧虚构", "奸雄雄辩、诗才与权谋一体台词", "虚构反面教材边界"),
    ("yangguo-skill", "fiction-tv", "杨过", "神雕侠侣", "武侠虚构", "反叛与痴情、断臂隐喻、师徒伦理张力", "虚构；非现实伦理操作"),
    ("xiaolongnv-skill", "fiction-tv", "小龙女", "神雕侠侣", "武侠虚构", "冷感极简、出世与入世切换", "虚构"),
    ("guojing-skill", "fiction-tv", "郭靖", "射雕英雄传", "武侠虚构", "钝感大智、朴素正义、师徒传承", "虚构"),
    ("zhangwuji-skill", "fiction-tv", "张无忌", "倚天屠龙记", "武侠虚构", "优柔与仁心、多方势力夹缝", "虚构"),
    ("anxin-skill", "fiction-tv", "安欣", "狂飙", "刑侦剧虚构", "理想主义耗损、程序正义执念、白发象征", "禁止刑侦违法教程；虚构"),
    ("gaoqiqiang-skill", "fiction-tv", "高启强", "狂飙", "反派虚构", "底层爬升合理化链条、亲情绑架、权力腐蚀", "反面教材；禁止涉黑教唆"),
    ("shengminglan-skill", "fiction-tv", "盛明兰", "知否", "宅斗虚构", "藏锋、借势、家族政治中的生存理性", "虚构；禁止现实陷害"),
    ("sumingyu-skill", "fiction-tv", "苏明玉", "都挺好", "都市剧虚构", "原生家庭边界、职场硬壳与软芯", "虚构"),
    ("fanghongjian-skill", "fiction-tv", "方鸿渐", "围城", "文学虚构", "知识分子自嘲、文凭焦虑、婚姻讽喻", "虚构"),
    ("yuzecheng-skill", "fiction-tv", "余则成", "潜伏", "谍战虚构", "双面生活、冷幽默减压、信仰叙事", "禁止间谍违法教程"),
    # animation (10)
    ("meiyangyang-skill", "animation", "美羊羊", "喜羊羊", "子供向", "精致礼貌、偶发小脾气、闺蜜线", "全年龄；版权对白勿照抄"),
    ("xiongda-skill", "animation", "熊大", "熊出没", "子供向", "大哥责任、劝熊二、和光头强周旋", "安全喜剧"),
    ("xionger-skill", "animation", "熊二", "熊出没", "子供向", "贪吃憨厚、跟班喜剧、意外破局", "安全喜剧"),
    ("hututu-skill", "animation", "胡图图", "大耳朵图图", "子供向", "童问世界、家庭温情、想象力", "儿童安全"),
    ("zhubajie-skill", "animation", "猪八戒", "西游记动画", "喜剧虚构", "贪懒馋、关键时刻不掉链子", "非宗教教义"),
    ("shaseng-skill", "animation", "沙僧", "西游记动画", "喜剧虚构", "挑担沉默、和稀泥、团队粘合", "全年龄"),
    ("tangseng-skill", "animation", "唐僧", "西游记动画", "喜剧虚构", "戒律外壳、慈悲内核、唠叨节奏", "非传教"),
    ("huluwadawa-skill", "animation", "大娃", "葫芦兄弟", "子供向", "力大莽撞、先冲后学协作", "非危险模仿"),
    ("sakuragi-skill", "animation", "樱木花道", "灌篮高手", "少年漫", "自大与成长、搞笑训练蒙太奇、热血笨蛋", "虚构；非暴力教唆"),
    ("gintoki-skill", "animation", "坂田银时", "银魂", "少年漫", "废柴外壳武士芯、吐槽 meta、丧燃", "虚构；全年龄净版"),
]


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

    skill_md = f"""---
name: {slug}
description: |
  {zh}（{domain}）认知与表达框架（压缩蒸馏）：{blurb[:80]}…
  触发：{trigger} 等。{guard[:60]}
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


def main() -> None:
    for row in SKILLS:
        write_skill(*row)
    # print table rows for README append
    for slug, cat, zh, _, domain, blurb, guard in SKILLS:
        path = f"./{cat}/{slug}/README.md"
        short = blurb.replace("|", "｜")[:42] + ("…" if len(blurb) > 42 else "")
        gshort = guard.replace("|", "｜")[:24]
        print(
            f"| [{zh}.skill]({path}) | {domain} | {short}；{gshort} |"
        )


if __name__ == "__main__":
    main()
