# human-skill

> 把人物语气蒸馏成 prompt 很容易。把人物的认知框架蒸馏成可运行的 `.skill`，才更有价值。

`human-skill` 是一个人物认知框架仓库。

每个人物对应一个独立 `*-skill/` 目录，按**语料性质**归在 [`real-people/`](./real-people/README.md)、[`fiction-tv/`](./fiction-tv/README.md) 或 [`animation/`](./animation/README.md) 下；内含 `SKILL.md`、`README.md`，并推荐附带 `references/research/nuwa-phase1-synthesis.md`（公开语料摘录，便于追溯）。**人物 skill 的编写曾参考开源项目 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill) 的多源调研思路**；除根目录本说明外，子目录正文不再重复提及该工具。

目标不是复读名人语录，也不是做表层角色扮演，而是尽量提炼这个人物在公开材料里反复出现的：

- 怎么说话
- 怎么想问题
- 怎么做判断
- 什么会反对
- 什么边界不会越过

## 导航

| 区块 | 说明 |
| --- | --- |
| [目录分类](#目录分类) | 真实 / 影视 / 动画三类目录说明 |
| [已收录人物](#已收录人物) | 全部 skill 索引表（含分段锚点） |
| [安装](#安装) | `npx skills add` 与引用方式 |
| [怎么调用](#怎么调用) | 自然语言触发示例 |
| [这个仓库蒸馏了什么](#这个仓库蒸馏了什么) | 五层蒸馏框架 |
| [人物示例](#人物示例) | 按人物的使用示例合集 |
| [仓库约定](#仓库约定) | 目录结构与文件要求 |
| [重做标准](#重做标准) | 新增/重写原则 |
| [赞助](#赞助) | 微信 / 支付宝 |

## 目录分类

| 分类 | 目录 | 说明 |
| --- | --- | --- |
| **真实人物** | [`real-people/`](./real-people/README.md) | 基于现实中公众人物的公开言论、履历与活动 |
| **影视虚构** | [`fiction-tv/`](./fiction-tv/README.md) | 真人影视剧中的虚构角色 |
| **动画虚构** | [`animation/`](./animation/README.md) | 动画 / 系列片中的虚构角色 |

## 已收录人物

**分段跳转：** [真实人物](#收录-真实人物) · [影视虚构](#收录-影视虚构) · [动画虚构](#收录-动画虚构)

<a id="收录-真实人物"></a>

### 真实人物（`real-people/`）

| 人物 | 领域 | 快速说明 |
| --- | --- | --- |
| [张雪峰.skill](./real-people/zhangxuefeng-skill/README.md) | 教育 / 职业路径 | 就业倒推、家庭分流、Agentic 检索协议；**已故说明见 README** |
| [蔡徐坤.skill](./real-people/caixukun-skill/README.md) | 音乐 / 舞台 / 审美 | 内部真实、双速创作、极简×细节 |
| [周杰伦.skill](./real-people/zhoujielun-skill/README.md) | 流行音乐 / 创作 | 改变品味、中国风作概念、混搭统一 |
| [马保国.skill](./real-people/mabaoguo-skill/README.md) | 网络梗体 / 模因 | 保国体叙事结构（非武术背书） |
| [雷军.skill](./real-people/leijun-skill/README.md) | 创业 / 产品 / 商业 | 七字诀、三大铁律、复盘与长期叙事 |
| [罗永浩.skill](./real-people/luoyonghao-skill/README.md) | 产品 / 创业 / 表达 | 理想主义张力、表达克制与访谈伦理 |
| [六小龄童.skill](./real-people/liuxiaolingtong-skill/README.md) | 经典 IP / 表演 / 文化演讲 | 改编底线、西游传播、孙悟空三重性、择一事终一生 |
| [卢本伟.skill](./real-people/lubenwei-skill/README.md) | 电竞 / 游戏直播（清洁版） | 前 LOL 职业/主播表达节奏；**禁止**辱骂教唆、开挂、冲人；合规红线见 README |
| [罗翔.skill](./real-people/luoxiang-skill/README.md) | 法理科普 / 法哲学 | 案例—规范—价值、罪刑法定、圆圈正义；**非**法律意见 |
| [李诞.skill](./real-people/lidan-skill/README.md) | 脱口秀 / 综艺表达 | 消解崇高、丧系清醒、圆场递台阶；**非** PUA |
| [郭德纲.skill](./real-people/guodegang-skill/README.md) | 相声 / 喜剧节奏 | 三番四抖、捧逗尺寸；净版结构，**非**荤段模板 |
| [余华.skill](./real-people/yuhua-skill/README.md) | 文学访谈 / 叙事语气 | 冷幽默、反励志、轻语气重细节 |
| [马斯克.skill](./real-people/mashike-skill/README.md) | 创新叙事 / 工程乐观（公开言论轴） | 第一性原理、垂直整合；**非**投资建议、非造谣 |
| [Naval Ravikant.skill](./real-people/naval-ravikant-skill/README.md) | 财富观 / 创作者战略（公开论述） | specific knowledge、杠杆、长期主义；**非**荐股 |

<a id="收录-影视虚构"></a>

### 影视虚构（`fiction-tv/`）

| 人物 | 领域 | 快速说明 |
| --- | --- | --- |
| [范德彪.skill](./fiction-tv/fandebiao-skill/README.md) | 影视喜剧 / 方言梗 | 《马大帅》彪哥，头衔膨胀与豪迈兜底（虚构角色） |
| [苏大强.skill](./fiction-tv/sudaqiang-skill/README.md) | 家庭剧 / 反面沟通 | 《都挺好》作系家长话术；**反面教材**，非操纵教程 |
| [祁同伟.skill](./fiction-tv/qitongwei-skill/README.md) | 廉政叙事 / 反派弧光 | 《人民的名义》自怜式合理化；**禁止**腐败教唆 |
| [高育良.skill](./fiction-tv/gaoyuliang-skill/README.md) | 廉政叙事 / 学者型反派 | 《人民的名义》辞令包装；**禁止**违法指导 |
| [李云龙.skill](./fiction-tv/liyunlong-skill/README.md) | 战争剧 / 士气叙事 | 《亮剑》粗粝动员与义气；**禁止**军事教唆与暴力细节 |

<a id="收录-动画虚构"></a>

### 动画虚构（`animation/`）

| 人物 | 领域 | 快速说明 |
| --- | --- | --- |
| [懒羊羊.skill](./animation/lanyangyang-skill/README.md) | 子供向动画 / 喜剧人设 | 《喜羊羊与灰太狼》懒羊羊，低能耗动机与反差喜剧（虚构角色） |
| [灰太狼.skill](./animation/huitailang-skill/README.md) | 子供向动画 / 反派萌 | 《喜羊羊与灰太狼》失败循环与执念喜剧；全年龄安全 |
| [光头强.skill](./animation/guangtouqiang-skill/README.md) | 子供向动画 / 打工人母题 | 《熊出没》KPI 周旋与追逐喜剧；全年龄安全 |

## 安装

安装整个仓库：

```bash
npx skills add lucian55/human-skill
```

安装后，在支持 `.skill` 的环境里直接引用人物名字即可触发对应视角。

## 怎么调用

通用写法：

```text
用 XXX 的视角回答这个问题
切换到 XXX，帮我分析一下
模仿 XXX 的思考方式，不要只学语气
```

## 这个仓库蒸馏了什么

参考人物蒸馏类 skill 的组织方式，这个仓库默认会尽量提炼五层：

| 层次 | 说明 |
| --- | --- |
| **怎么说话** | 表达 DNA：语气、节奏、常用句式、锋利度 |
| **怎么想** | 心智模型：这个人看问题时最稳定的框架 |
| **怎么判断** | 决策启发式：面对模糊问题时会先问什么、先看什么 |
| **什么不做** | 反模式：他通常反对什么做法、会警惕什么错误 |
| **边界在哪** | 诚实边界：哪些内容不能伪装成“本人会这么说” |

这也是每个人物 skill 重写时默认遵守的标准。

## 人物示例

### 张雪峰.skill

> 适用于高考志愿、考研、专业选择、职业方向、普通家庭决策等问题。  
> **张雪峰老师已于 2026-03-24 逝世**，详见 [`zhangxuefeng-skill/README.md`](./real-people/zhangxuefeng-skill/README.md)；skill 为其公开方法论遗产。

#### 使用示例

```text
按张雪峰式框架，结合检索数据谈这个专业中位数去向
普通家庭选金融前先过哪几道资源关？
用就业倒推法拆考研是不是在逃避就业
```

### 蔡徐坤.skill

> 适用于音乐创作、舞台表达、偶像发展、审美把控、作品打磨、公众表达等问题。  
> 详见 [`caixukun-skill/README.md`](./real-people/caixukun-skill/README.md)。

#### 使用示例

```text
用蔡徐坤式创作者框架帮我想一个极简高完成度舞台
内部真实和外部期待冲突时怎么排优先级
这首歌该深磨还是趁热收尾？用双速创作逻辑帮我判断
```

### 周杰伦.skill

> 适用于流行音乐创作、旋律与编曲、概念专辑、舞台与视觉表达、跨艺术融合、个人风格建立等问题。  
> 详见 [`zhoujielun-skill/README.md`](./real-people/zhoujielun-skill/README.md)。

#### 使用示例

```text
用周杰伦式作者框架看副歌够不够「一站住」
中国风按「创作概念」而不是古风模板怎么下手
概念专辑先画情绪地图还是先做主打
```

### 马保国.skill

> 适用于夸张叙事、反差幽默、互联网梗体表达、自我辩护式发言、短视频人物口播风格等问题（**戏仿模因，非纪实**）。  
> 详见 [`mabaoguo-skill/README.md`](./real-people/mabaoguo-skill/README.md)。

#### 使用示例

```text
写一段保国体口播吐槽需求方偷袭排期
30 秒短视频开场：大意了没有闪 + 好自为之
把线上 bug 甩锅改成「年轻人不讲测试」荒诞版（勿映射真人）
```

### 范德彪.skill

> 适用于《马大帅》范德彪（彪哥）式**喜剧台词**、东北市井江湖梗、吹牛打脸短视频脚本等；**虚构角色**，非范伟本人。  
> 详见 [`fandebiao-skill/README.md`](./fiction-tv/fandebiao-skill/README.md)。

#### 使用示例

```text
用范德彪视角写：项目黄了但辽北著名狠人不能输嘴
把周报被怼改成「按套路打」「欧了」混搭的荒诞独白
论成败人生豪迈版：相亲失败后的彪哥式自我解围
```

### 懒羊羊.skill

> 适用于《喜羊羊与灰太狼》懒羊羊式**全年龄安全**台词、推脱—反转节奏、与靠谱队友反差、儿童向「小懒惰→小成长」弧光等；**虚构动画角色**，非配音演员本人。  
> 详见 [`lanyangyang-skill/README.md`](./animation/lanyangyang-skill/README.md)。

#### 使用示例

```text
用懒羊羊式节奏写被催任务但只想再睡五分钟（幽默、无教唆怠工）
喜羊羊拉懒羊羊去训练：写一段内心戏与推脱三段论
儿童向：遇到困难先想躲，靠朋友鼓励迈一小步，不要危险模仿
把「低能耗哲学」写成先冠冕堂皇再被打脸的小剧场
```

### 雷军.skill

> 适用于创业方法论、产品定义、爆品策略、用户口碑、效率优化、商业演讲与管理复盘等问题。  
> 详见 [`leijun-skill/README.md`](./real-people/leijun-skill/README.md)。

#### 使用示例

```text
用七字诀看我们团队现在缺的是口碑还是快
三大铁律里我们最虚的是哪一条
用复盘三问拆这次发布为什么没打透
```

### 罗永浩.skill

> 适用于产品经理视角、创业复盘、品牌表达、公众发言分寸、理想主义与商业现实的平衡等问题。  
> 详见 [`luoyonghao-skill/README.md`](./real-people/luoyonghao-skill/README.md)。

#### 使用示例

```text
用老罗式结构 critique 这个 onboarding（判断→例证→改法）
如果按「不要做什么」收敛我的公开发言
创业复盘怎么写低级错误才不像卖惨
```

### 六小龄童.skill

> 适用于名著改编伦理、西游 IP 与传统文化传播、孙悟空角色塑造、校园/公益演讲结构等问题（基于**公开言论**框架，非恶搞专用）。  
> 详见 [`liuxiaolingtong-skill/README.md`](./real-people/liuxiaolingtong-skill/README.md)。

#### 使用示例

```text
用「改编不是乱编」公开主张里的底线思维审这个西游改编梗概
按三重性 checklist 看这个孙悟空角色缺了哪一层
写一篇「苦练七十二变笑对八十一难」主题的演讲提纲（第三人称，不冒充本人）
```

### 卢本伟.skill

> 适用于**合规**游戏解说口播、直播式叙事节奏、退役选手视角复盘、主播影响力与红线讨论；基于前《英雄联盟》职业选手与主播的**公开形象**抽象，**不**鼓励辱骂教唆、开挂或规避封禁。  
> 详见 [`lubenwei-skill/README.md`](./real-people/lubenwei-skill/README.md)。

#### 使用示例

```text
用清洁版「铺垫—反转」节奏写一段 LOL 团战前瞻，全年龄无脏字
把电竞自信的叙事写成先抬势、再接得住结果的复盘口播
给新人讲主播为什么不能教唆粉丝骂人（结合公开报道事实）
```

### 罗翔.skill

> 适用于普法叙事、议论文、伦理两难讨论、程序正义与民意关系等问题；**非**个案法律咨询。  
> 详见 [`luoxiang-skill/README.md`](./real-people/luoxiang-skill/README.md)。

#### 使用示例

```text
用罗翔式三层结构拆网络暴力：事实、法律、道德
用圆圈正义隐喻写「理想司法」作文结尾，不要煽动
张三式课堂案例：虚构去识别化 + 构成要件讨论
```

### 李诞.skill

> 适用于轻松演讲开场、冲突软化、脱口秀/综艺节奏、预期违背式段子；**非** PUA、非推卸责任。  
> 详见 [`lidan-skill/README.md`](./real-people/lidan-skill/README.md)。

#### 使用示例

```text
复盘会太僵，用李诞式先消解再落地写开场
给冷场嘉宾写三句递台阶串词
加班主题段子要反转，但不要侮辱同事
```

### 郭德纲.skill

> 适用于对口/单口喜剧骨架、演讲包袱、三番四抖教学；**净版**，非荤段与人身攻击模板。  
> 详见 [`guodegang-skill/README.md`](./real-people/guodegang-skill/README.md)。

#### 使用示例

```text
用三番四抖写「甲方改需求」净版段子骨架
解释捧逗各自负责什么，给极简对白 demo
演讲里嵌一个自我调侃包袱再落回论点
```

### 余华.skill

> 适用于访谈体回答、叙事语气、反励志创作谈、文学概念降维比喻。  
> 详见 [`yuhua-skill/README.md`](./real-people/yuhua-skill/README.md)。

#### 使用示例

```text
用余华式冷静细节写小说开头，少形容词
访谈答年轻人焦虑：降维比喻，不要鸡汤
把叙事视角用吃饭走路讲给非文学读者
```

### 马斯克.skill（公开言论轴）

> 适用于创新拆解、硬科技路演语气、第一性原理思考练习；**非**投资建议、非伪造产品/推文。  
> 详见 [`mashike-skill/README.md`](./real-people/mashike-skill/README.md)。

#### 使用示例

```text
用第一性原理拆是否自研某模块，不要编造数据
愿景开场 + 可验证里程碑 + 风险一句 + 免责声明
解释垂直整合叙事何时成立、何时是组织负担
```

### Naval Ravikant.skill

> 适用于职业战略、创作者杠杆思维、specific knowledge 自检；**非**荐股、非伪造语录。  
> 详见 [`naval-ravikant-skill/README.md`](./real-people/naval-ravikant-skill/README.md)。

#### 使用示例

```text
用 Naval 框架列三个可能的 specific knowledge 方向（假设性）
给高中生解释劳动力杠杆 vs 代码/媒体杠杆，不要荐股
写一段长期主义短文，可保留 leverage 等英文关键词
```

### 苏大强.skill

> 适用于家庭剧剧本、沟通课反面案例、讽刺段子；**虚构**，《都挺好》；**非**操纵家人教程。  
> 详见 [`sudaqiang-skill/README.md`](./fiction-tv/sudaqiang-skill/README.md)。

#### 使用示例

```text
写三场戏：试探→道德绑架→子女反击（虚构）
沟通课：一句作爹式甩锅为何伤人，给健康改写对比
```

### 祁同伟.skill

> 适用于反派独白、廉政案例话术分析、《人民的名义》人物弧讨论；**禁止**腐败教唆。  
> 详见 [`qitongwei-skill/README.md`](./fiction-tv/qitongwei-skill/README.md)。

#### 使用示例

```text
话剧课反派独白骨架，要有代价收束，不要违法细节
分析「自怜外包责任」话术，对照依法履职
```

### 高育良.skill

> 适用于学者型反派对白、廉政话术识辩；**禁止**违法操作指导。  
> 详见 [`gaoyuliang-skill/README.md`](./fiction-tv/gaoyuliang-skill/README.md)。

#### 使用示例

```text
书房戏：大局辞令三段 + 被事实戳穿，不要违法细节
培训：什么叫概念升格甩责，给合规沟通对照
```

### 李云龙.skill

> 适用于战争剧士气台词骨架、团队动员的安全比喻、管理课反面案例；**禁止**军事教唆与暴力细节。  
> 详见 [`liyunlong-skill/README.md`](./fiction-tv/liyunlong-skill/README.md)。

#### 使用示例

```text
写净版攻坚动员广播稿，抗战剧风，不要武器细节
用亮剑精神比喻创业冷启动，补合规边界提醒
```

### 灰太狼.skill

> 适用于《喜羊羊与灰太狼》全年龄喜剧脚本、与懒羊羊动机对照；**非**暴力写实、非逐字抄录版权对白。  
> 详见 [`huitailang-skill/README.md`](./animation/huitailang-skill/README.md)。

#### 使用示例

```text
写发明翻车小剧场，退场用原创「再来」句式变体
对比灰太狼主动执念 vs 懒羊羊被动节能
```

### 光头强.skill

> 适用于《熊出没》式打工人母题、儿童追逐喜剧；全年龄安全，**非**危险劳作教唆。  
> 详见 [`guangtouqiang-skill/README.md`](./animation/guangtouqiang-skill/README.md)。

#### 使用示例

```text
接到李老板电话后的儿童向内心戏，结尾诚实或合作
把周报压力写成熊出没式追逐喜剧，不映射真人
```

## 仓库约定

每个名人 skill 目录（位于 `real-people/`、`fiction-tv/` 或 `animation/` 下）至少包含：

- `SKILL.md`：给 Agent 使用的技能文件
- `README.md`：给人看的说明文档

推荐结构：

```text
real-people/                    # 或 fiction-tv/、animation/
└── person-skill/
    ├── SKILL.md
    ├── README.md
    └── references/research/nuwa-phase1-synthesis.md   # 公开语料调研摘要（推荐）
```

## 重做标准

后续新增或重做人物时，默认遵循这些原则：

1. **归类**：真实公众人物 → `real-people/`；真人剧影虚构角色 → `fiction-tv/`；动画虚构角色 → `animation/`。  
2. 不做简单口头禅模仿，优先提炼认知框架。
3. 不把未经证实的私生活、争议和传言写成事实。
4. 每个人物都要有“表达 DNA”也要有“诚实边界”。
5. README 要能回答“这个人物适合解决什么问题”和“怎么触发”。  
6. SKILL.md 要能回答“先问什么、怎么判断、什么不做”。

## 赞助

如果这个项目对你有帮助，欢迎请我喝杯咖啡。

| 微信 | 支付宝 |
| --- | --- |
| <img src="images/wechat.jpg" alt="微信收款码" height="240" /> | <img src="images/alipay.jpg" alt="支付宝收款码" height="240" /> |

打开微信/支付宝扫一扫即可赞助，感谢支持。
