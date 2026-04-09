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

[目录分类](#目录分类) · [已收录人物](#已收录人物) · [安装](#安装) · [怎么调用](#怎么调用) · [五层蒸馏](#这个仓库蒸馏了什么) · [人物示例](#人物示例) · [仓库约定](#仓库约定) · [重做标准](#重做标准) · [赞助](#赞助)

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
| [薛兆丰.skill](./real-people/xuezhaofeng-skill/README.md) | 经济学通识 / 综艺向科普 | 成本与选择、边际、激励；**非**伪造数据与学术代写 |
| [鲁豫.skill](./real-people/luyu-skill/README.md) | 电视访谈 / 播客 | 人生节点切片、短句接话、轻质疑推进；**非**恶搞羞辱 |
| [鲁迅.skill](./real-people/luxun-skill/README.md) | 杂文 / 公共议论 | 揭弊与反讽、韧性行动；**已故**；**禁止**伪造引文 |
| [余秀华.skill](./real-people/yuxiuhua-skill/README.md) | 当代诗 / 自述表达 | 身体与土地意象、反矫情；**禁止**残障侮辱与玩梗消费痛苦 |

<a id="收录-影视虚构"></a>

### 影视虚构（`fiction-tv/`）

| 人物 | 领域 | 快速说明 |
| --- | --- | --- |
| [范德彪.skill](./fiction-tv/fandebiao-skill/README.md) | 影视喜剧 / 方言梗 | 《马大帅》彪哥，头衔膨胀与豪迈兜底（虚构角色） |
| [苏大强.skill](./fiction-tv/sudaqiang-skill/README.md) | 家庭剧 / 反面沟通 | 《都挺好》作系家长话术；**反面教材**，非操纵教程 |
| [祁同伟.skill](./fiction-tv/qitongwei-skill/README.md) | 廉政叙事 / 反派弧光 | 《人民的名义》自怜式合理化；**禁止**腐败教唆 |
| [高育良.skill](./fiction-tv/gaoyuliang-skill/README.md) | 廉政叙事 / 学者型反派 | 《人民的名义》辞令包装；**禁止**违法指导 |
| [李云龙.skill](./fiction-tv/liyunlong-skill/README.md) | 战争剧 / 士气叙事 | 《亮剑》粗粝动员与义气；**禁止**军事教唆与暴力细节 |
| [甄嬛.skill](./fiction-tv/zhenhuan-skill/README.md) | 古装权谋剧 / 潜台词 | 《甄嬛传》隐忍与双层听者；**虚构**；**禁止**现实陷害教唆 |

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

其余人物的适用场景与更多示例见 [已收录人物](#已收录人物) 表格中的链接，打开对应 `*-skill/README.md` 即可。下面仅举一例：

### 雷军.skill

> 适用于创业方法论、产品定义、爆品策略、用户口碑、效率优化、商业演讲与管理复盘等问题。  
> 详见 [`leijun-skill/README.md`](./real-people/leijun-skill/README.md)。

#### 使用示例

```text
用七字诀看我们团队现在缺的是口碑还是快
三大铁律里我们最虚的是哪一条
用复盘三问拆这次发布为什么没打透
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
