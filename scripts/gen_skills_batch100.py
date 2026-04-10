#!/usr/bin/env python3
"""Generate 100 human-skill packs + patch README.md markers. Run from repo root."""
from __future__ import annotations

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(ROOT, "README.md")

# slug, category, zh name, trigger hint, domain tag, one_line blurb, guard note
REAL: list[tuple[str, str, str, str, str, str, str]] = [
    ("wangfei-skill", "real-people", "王菲", "红豆、如愿", "歌手 / 气质", "疏离气声、去技巧叙事、情爱作修养不作表演", "非医疗；不编造访谈"),
    ("zhaobenshan-skill", "real-people", "赵本山", "春晚小品、刘老根", "喜剧 / 乡土", "东北伦理误会链、乡土人物一口立住、反转包袱", "净版；忌荤段模板"),
    ("fanwei-skill", "real-people", "范伟", "马大帅、耳朵大有福", "演员 / 喜剧", "木讷外壳下的精算与善良、慢节奏包袱", "角色与本人区分"),
    ("songdandan-skill", "real-people", "宋丹丹", "我爱我家、白云", "喜剧 / 综艺", "嘴快心软、生活段子高密度、代际戏剧化", "忌人身攻击"),
    ("geyou-skill", "real-people", "葛优", "甲方乙方、活着", "演员", "蔫坏冷面、话少留白、小人物体面与大谎", "虚构创作谈"),
    ("liangchaowei-skill", "real-people", "梁朝伟", "无间道、花样年华", "演员", "眼神叙事、内向克制、沉默里爆发", "非替本人发言"),
    ("naying-skill", "real-people", "那英", "好声音、直给导师", "歌手 / 综艺", "东北大姐直球、舞台 Diva、综艺金句", "忌侮辱参与者"),
    ("wangfeng-skill", "real-people", "汪峰", "鲍家街、怒放", "摇滚 / 创作", "宏大质问句、理想高音、公共发言硬壳", "非煽动对立"),
    ("lijian-singer-skill", "real-people", "李健", "贝加尔湖畔", "歌手", "知识分子浪漫、隐喻洁癖、慢语速金句", "非人生导师保证"),
    ("maobuyi-skill", "real-people", "毛不易", "消愁、像我这样的人", "唱作人", "庸常卑微里的诗意、口语入歌、反鸡汤温柔", "不消费抑郁"),
    ("xuezhiqian-skill", "real-people", "薛之谦", "演员、综艺怪咖", "流行 / 综艺", "情歌与综艺自解构、反差人设", "忌造谣式营销叙事"),
    ("dazhangwei-skill", "real-people", "大张伟", "花儿、碎嘴综艺", "音乐人 / 综艺", "段子密度、解构崇高、丧燃一句落地", "净版；非教唆"),
    ("shenteng-skill", "real-people", "沈腾", "夏洛特烦恼、麻花", "喜剧演员", "小人物逆袭、伏笔 callback、悲情喜剧底", "虚构喜剧结构"),
    ("jialing-skill", "real-people", "贾玲", "你好李焕英", "导演 / 喜剧", "亲情债喜剧壳、女性叙事与真诚收束", "非消费逝者"),
    ("chenpeisi-skill", "real-people", "陈佩斯", "吃面条、主角配角", "小品", "肢体语言主导、形体喜剧精密", "致敬经典结构非抄袭"),
    ("douwentao-skill", "real-people", "窦文涛", "锵锵、圆桌派", "谈话节目", "圆桌松弛毒舌、文化八卦软化、夹枪不伤脸", "非新闻定论"),
    ("madong-skill", "real-people", "马东", "奇葩说、乐夏", "综艺制作人", "赛制叙事、金句剪枝、辩论产品化", "非操纵舆论教程"),
    ("caikangyong-skill", "real-people", "蔡康永", "康熙、情商书", "主持 / 作家", "温柔刀提问、高情商收束、留面子的讽刺", "非 PUA"),
    ("jinxing-skill", "real-people", "金星", "金星秀、舞蹈", "舞蹈家 / 主持", "毒舌正义人设、身体隐喻、价值观直球", "忌跨性别与身份羞辱"),
    ("yanglan-skill", "real-people", "杨澜", "杨澜访谈录", "主持", "精英访谈节奏、知性骨架、点题收束", "非官方背书"),
    ("dongqing-skill", "real-people", "董卿", "诗词大会、朗读者", "主持 / 文化节目", "诗意串场、仪式感停顿、宏大题词私人化", "非替机构发言"),
    ("jackie-chan-skill", "real-people", "成龙", "警察故事、我是谁", "动作明星", "搏命喜剧动作、民族品牌叙事、自嘲大哥", "禁止危险模仿；非武术教程"),
    ("lilianjie-skill", "real-people", "李连杰", "黄飞鸿、少林寺", "动作 / 公益", "武僧正气壳、后期佛系叙事转向", "禁止搏击教程"),
    ("donnie-yen-skill", "real-people", "甄子丹", "叶问", "动作", "咏春架势与家国叙事节奏、快剪爽点", "禁止暴力教唆"),
    ("wujing-skill", "real-people", "吴京", "战狼、流浪地球", "演员 / 导演", "主旋律英雄壳、直男效能叙事", "非煽动仇恨"),
    ("huangbo-skill", "real-people", "黄渤", "疯狂的石头", "演员", "高情商自嘲、市井小聪明、大时代夹缝", "非替本人编造隐私"),
    ("xuzheng-skill", "real-people", "徐峥", "囧途、药神", "导演 / 演员", "荒诞公路喜剧、社会切口通俗悲剧", "非医药建议"),
    ("ninghao-skill", "real-people", "宁浩", "石头、无人区", "导演", "多线咬合、黑色幽默、小人物链条反应", "禁止犯罪教唆"),
    ("fengxiaogang-skill", "real-people", "冯小刚", "甲方乙方、芳华", "导演", "京味贺岁群像、怀旧滤镜与集体记忆", "虚构创作"),
    ("chenkaige-skill", "real-people", "陈凯歌", "霸王别姬", "导演", "宏大史观与个体命运、仪式感镜头", "非片场八卦"),
    ("liangwendao-skill", "real-people", "梁文道", "开卷八分钟", "文化评论", "书店体温和左倾、引书搭桥、慢炖结论", "非学术代写"),
    ("chendanqing-skill", "real-people", "陈丹青", "局部、退步集", "美术评论", "反教条美育、直言与骄傲、纽约往事对照", "忌侮辱性人身攻击"),
    ("beidao-skill", "real-people", "北岛", "回答、朦胧诗", "诗人", "冷意象、否定句诗学、流亡与记忆", "不伪造诗句"),
    ("yangjiang-skill", "real-people", "杨绛", "我们仨", "作家 / 翻译", "克制温吞里的锋利、知识分子家常回忆", "已故；尊重"),
    ("wangxiaobo-skill", "real-people", "王小波", "沉默的大多数", "作家", "理性狂欢、反愚蠢、自由隐喻", "成人语境；净版改写"),
    ("moyan-skill", "real-people", "莫言", "红高粱、诺奖演说", "作家", "魔幻乡土、感官暴力与民间口语", "虚构；非煽动"),
    ("qiongyao-skill", "real-people", "琼瑶", "庭院深深、还珠", "言情作家", "强情绪对白、三角伦理、眼泪经济", "虚构模板；忌情感操控教程"),
    ("gulong-skill", "real-people", "古龙", "小李飞刀", "武侠作家", "短句蒙太奇、浪子孤独、酒友女人", "已故；非搏击教程"),
    ("cailan-skill", "real-people", "蔡澜", "食神专栏", "美食 / 生活家", "享乐主义正当化、旅行搭子叙事", "非过量饮酒医疗建议"),
    ("xuzidong-skill", "real-people", "许子东", "圆桌派、细读张爱玲", "学者 / 评论", "材料与梗混搭、人物册页式短评", "非伪造文献"),
]

FIC: list[tuple[str, str, str, str, str, str, str]] = [
    ("zhizunbao-skill", "fiction-tv", "至尊宝", "大话西游", "喜剧武侠虚构", "月光宝盒时间循环、痞子真心、延迟满足的悲剧", "虚构；忌低俗骚扰话术"),
    ("zixia-skill", "fiction-tv", "紫霞", "大话西游", "喜剧武侠虚构", "一剑定情、眼泪经济、理想主义恋爱壳", "虚构"),
    ("xusanduo-skill", "fiction-tv", "许三多", "士兵突击", "军旅剧虚构", "钝感坚持、不抛弃不放弃、草根成长", "禁止军事违法教程"),
    ("yuanlang-skill", "fiction-tv", "袁朗", "士兵突击", "军旅剧虚构", "老 A 冷血人设、试探与打磨、精英残酷浪漫", "虚构"),
    ("andi-huanlesong-skill", "fiction-tv", "安迪", "欢乐颂", "都市剧虚构", "海归理性、职场风控、精英孤独", "虚构"),
    ("quxiaoxiao-skill", "fiction-tv", "曲筱绡", "欢乐颂", "都市剧虚构", "精怪富二代、嘴毒心软、关系网打法", "虚构；忌现实霸凌"),
    ("fanshengmei-skill", "fiction-tv", "樊胜美", "欢乐颂", "都市剧虚构", "原生家庭吸血、面子与里子撕裂", "虚构；防抑郁消费"),
    ("minglou-skill", "fiction-tv", "明楼", "伪装者", "谍战虚构", "三面间谍、辞令层叠、亲情作人质", "禁止间谍违法教程"),
    ("mingtai-skill", "fiction-tv", "明台", "伪装者", "谍战虚构", "公子成长、技能蒙太奇、信仰落地", "禁止间谍违法教程"),
    ("wangmanchun-skill", "fiction-tv", "汪曼春", "伪装者", "反派虚构", "痴情反派、权力与占有欲、悲剧性疯批", "反面教材"),
    ("meichangsu-skill", "fiction-tv", "梅长苏", "琅琊榜", "古装权谋虚构", "病弱智囊、雪冤叙事、棋子与棋手", "虚构；禁止现实陷害"),
    ("jingwang-skill", "fiction-tv", "靖王", "琅琊榜", "古装权谋虚构", "耿直宗室、信任成本、笨办法正义", "虚构"),
    ("fanxian-skill", "fiction-tv", "范闲", "庆余年", "古装穿越虚构", "嬉笑权谋、现代梗古代壳、父子棋局", "虚构"),
    ("chenpingping-skill", "fiction-tv", "陈萍萍", "庆余年", "古装权谋虚构", "轮椅上的权、隐忍复仇、体制内的暗线", "虚构"),
    ("wangqinian-skill", "fiction-tv", "王启年", "庆余年", "古装喜剧虚构", "碎嘴忠诚、贪小便宜大节、情报贩子喜剧", "虚构"),
    ("siteng-skill", "fiction-tv", "司藤", "司藤", "奇幻剧虚构", "女王傲娇、藤系依赖、民国线悬疑", "虚构"),
    ("baiqian-skill", "fiction-tv", "白浅", "三生三世", "仙侠虚构", "神族恋、失忆与劫数、上神松弛感", "虚构"),
    ("weiwuxian-skill", "fiction-tv", "魏无羡", "陈情令", "仙侠虚构", "不羁侠气、群嘲护短、悲剧性背负", "虚构"),
    ("lanwangji-skill", "fiction-tv", "蓝忘机", "陈情令", "仙侠虚构", "端方克制、问灵十三载、规则内深情", "虚构"),
    ("gujia-skill", "fiction-tv", "顾佳", "三十而已", "都市剧虚构", "精英妈妈、婚姻风险对冲、体面崩塌", "虚构"),
    ("zhongxiaoqin-skill", "fiction-tv", "钟晓芹", "三十而已", "都市剧虚构", "普通人复位、婚姻试错、写作治愈", "虚构"),
    ("hanshangyan-skill", "fiction-tv", "韩商言", "亲爱的热爱的", "都市剧虚构", "电竞冷面、团队爹系、恋爱直球破冰", "虚构"),
    ("tongnian-skill", "fiction-tv", "佟年", "亲爱的热爱的", "都市剧虚构", "甜妹直球、学霸恋爱、软萌坚持", "虚构"),
    ("zhoushengchen-skill", "fiction-tv", "周生辰", "周生如故", "古装虚构", "克制宿命、家国大于私情、悲剧美学", "虚构"),
    ("shiyi-skill", "fiction-tv", "时宜", "周生如故", "古装虚构", "现代转世叙事、记忆与仪式、柔中带刚", "虚构"),
    ("dongfangqingcang-skill", "fiction-tv", "东方青苍", "苍兰诀", "仙侠虚构", "魔尊情感觉醒、强弱反转、业火壳", "虚构"),
    ("xiaolanhua-skill", "fiction-tv", "小兰花", "苍兰诀", "仙侠虚构", "软萌治愈、神女内核、误会甜虐", "虚构"),
    ("lingbuyi-skill", "fiction-tv", "凌不疑", "星汉灿烂", "古装虚构", "复仇将军、疯批克制、家族血债", "虚构；禁止暴力教唆"),
    ("chengshaoshang-skill", "fiction-tv", "程少商", "星汉灿烂", "古装虚构", "倔强成长、原生家庭拉扯、自我选择", "虚构"),
    ("shenmo-skill", "fiction-tv", "沈墨", "漫长的季节", "悬疑剧虚构", "创伤反杀叙事、时代灰雾、钢琴意象", "虚构；禁止犯罪模仿"),
    ("wangyang-mcz-skill", "fiction-tv", "王阳", "漫长的季节", "悬疑剧虚构", "诗意青年、理想主义陨落、父辈对照", "虚构"),
    ("gaoqisheng-skill", "fiction-tv", "高启盛", "狂飙", "反派虚构", "疯批高智、亲情捆绑、暴力升级链", "反面教材；禁止涉黑教唆"),
    ("houliangping-skill", "fiction-tv", "侯亮平", "人民的名义", "廉政虚构", "程序正义脸、家庭戏减压、反腐话术", "虚构"),
    ("lidakang-skill", "fiction-tv", "李达康", "人民的名义", "廉政虚构", "GDP 执念、窗口服务梗、政绩与人情张力", "虚构"),
    ("huyifei-skill", "fiction-tv", "胡一菲", "爱情公寓", "情景喜剧虚构", "公寓女王、武力梗喜剧化、嘴硬心软", "虚构；忌暴力模仿"),
]

ANI: list[tuple[str, str, str, str, str, str, str]] = [
    ("feiyangyang-skill", "animation", "沸羊羊", "喜羊羊", "子供向", "暴躁直男式热心、竞争心、反差喜剧", "全年龄；勿抄版权对白"),
    ("nuanyangyang-skill", "animation", "暖羊羊", "喜羊羊", "子供向", "班长型温柔、治愈担当、群体粘合", "全年龄"),
    ("xiyangyang-skill", "animation", "喜羊羊", "喜羊羊", "子供向", "机智破局、冷笑话、团队主心骨", "全年龄；勿抄对白"),
    ("hongtailang-skill", "animation", "红太狼", "喜羊羊", "子供向", "平底锅梗、家庭权力喜剧、反派妻", "安全喜剧"),
    ("xiaohuihui-skill", "animation", "小灰灰", "喜羊羊", "子供向", "萌系第三方、狼羊模糊、童言破局", "儿童安全"),
    ("huluwa-erwa-skill", "animation", "二娃", "葫芦兄弟", "子供向", "千里眼顺风耳、侦查与辅助", "非危险模仿"),
    ("huluwa-sanwa-skill", "animation", "三娃", "葫芦兄弟", "子供向", "铜头铁臂、硬扛前锋", "非危险模仿"),
    ("huluwa-siwa-skill", "animation", "四娃", "葫芦兄弟", "子供向", "火攻输出、急躁莽撞", "非危险模仿"),
    ("huluwa-wuwa-skill", "animation", "五娃", "葫芦兄弟", "子供向", "水攻控场、吞吐喜剧", "非危险模仿"),
    ("huluwa-liuwa-skill", "animation", "六娃", "葫芦兄弟", "子供向", "隐身偷袭、信息差喜剧", "非危险模仿"),
    ("huluwa-qiwa-skill", "animation", "七娃", "葫芦兄弟", "子供向", "宝葫芦收一切、被洗脑反转", "非危险模仿"),
    ("rukawa-skill", "animation", "流川枫", "灌篮高手", "少年漫", "面瘫球痴、单打美学、成长暗线", "虚构"),
    ("akagi-skill", "animation", "赤木刚宪", "灌篮高手", "少年漫", "队长脊梁、篮板信仰、大猩猩梗自嘲", "虚构"),
    ("mitsui-skill", "animation", "三井寿", "灌篮高手", "少年漫", "浪子回头、体力槽与三分救赎", "虚构"),
    ("miyagi-skill", "animation", "宫城良田", "灌篮高手", "少年漫", "小个子速度、耳钉人设、电光第一步", "虚构"),
    ("luffy-skill", "animation", "路飞", "海贼王", "少年漫", "自由宣言、橡胶脑洞战、伙伴羁绊", "虚构；非暴力教唆"),
    ("zoro-skill", "animation", "索隆", "海贼王", "少年漫", "路痴反差、三刀流执念、副船长担当", "虚构；非暴力教唆"),
    ("nami-skill", "animation", "娜美", "海贼王", "少年漫", "航海图天才、财迷喜剧壳、气候战", "虚构"),
    ("tanjiro-skill", "animation", "灶门炭治郎", "鬼灭之刃", "少年漫", "温柔斩杀、嗅觉战、家族债", "虚构；非暴力细节"),
    ("nezuko-skill", "animation", "灶门祢豆子", "鬼灭之刃", "少年漫", "竹筒萌点、鬼化反差、兄妹羁绊", "虚构"),
    ("saitama-skill", "animation", "琦玉", "一拳超人", "少年漫", "无敌无聊、一拳解构热血、超市券日常", "虚构"),
    ("genos-skill", "animation", "杰诺斯", "一拳超人", "少年漫", "改造人认真、战损美学、师徒忠犬", "虚构"),
    ("shinchan-skill", "animation", "野原新之助", "蜡笔小新", "子供向", "五岁黄腔净版化、想象力、家庭温情", "全年龄净版"),
    ("maruko-skill", "animation", "小丸子", "樱桃小丸子", "子供向", "懒散可爱、家族群像、童年微小确幸", "全年龄"),
    ("doraemon-skill", "animation", "哆啦A梦", "机器猫", "子供向", "道具脑洞、大雄成长线、温柔科幻", "勿逐字抄录版权对白"),
]

SKILLS100 = REAL + FIC + ANI

MARKER_REAL = (
    "| [黄健翔.skill](./real-people/huangjianxiang-skill/README.md) "
    "| 体育解说 | 爆发式观点、节奏陡升、立场鲜明；非地域攻击；合规表达 |\n"
)
MARKER_FIC = (
    "| [余则成.skill](./fiction-tv/yuzecheng-skill/README.md) "
    "| 谍战虚构 | 《潜伏》双面生活、冷幽默减压；**禁止**间谍违法教程 |\n"
)
MARKER_ANI = (
    "| [坂田银时.skill](./animation/gintoki-skill/README.md) "
    "| 少年漫 | 《银魂》废柴壳武士芯、吐槽 meta；**虚构**；全年龄净版 |\n"
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
    ins_r = "".join(readme_row(*t) for t in REAL)
    ins_f = "".join(readme_row(*t) for t in FIC)
    ins_a = "".join(readme_row(*t) for t in ANI)
    if MARKER_REAL not in content:
        raise SystemExit("README marker (黄健翔) not found")
    if MARKER_FIC not in content:
        raise SystemExit("README marker (余则成) not found")
    if MARKER_ANI not in content:
        raise SystemExit("README marker (坂田银时) not found")
    content = content.replace(MARKER_REAL, MARKER_REAL + ins_r, 1)
    content = content.replace(MARKER_FIC, MARKER_FIC + ins_f, 1)
    content = content.replace(MARKER_ANI, MARKER_ANI + ins_a, 1)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    assert len(SKILLS100) == 100, len(SKILLS100)
    for row in SKILLS100:
        write_skill(*row)
    patch_readme()
    print("OK: wrote", len(SKILLS100), "skills + README patch")


if __name__ == "__main__":
    main()
