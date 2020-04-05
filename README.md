# textrank
基于TextRank算法实现中文文本的关键词提取和摘要任务，核心计算代码保持与论文一致。

## 原理

TextRank的论文：

> Mihalcea R, Tarau P. TextRank: Bringing order into texts[C]. Association for Computational Linguistics, 2004.
___
## 依赖
+jieba >= 0.35
+numpy >= 1.7.1

___
## 示例

```python
from TextRank import textRank

text = """欧亚经济委员会执委会一体化与宏观经济委员格拉济耶夫日前接受新华社记者采访时高度评价中国抗击新冠疫情工作，\
并表示期待欧亚经济联盟与中国加强抗疫合作，共同推动地区发展。格拉济耶夫说，中国依靠治理体系与全国人民协同努力，\
在抗疫工作上取得极大成效。中国采取的措施符合全球利益。格拉济耶夫认为，中国经济将会快速恢复，欧亚经济联盟许多企业与中国市场联系紧密，\
应与中国加强合作，采取协调措施降低此次疫情带来的消极影响。格拉济耶夫建议，面对疫情，欧亚经济联盟与中国扩大信息技术应用，\
推进商品清关程序自动化，更广泛地利用相关机制，为对外经济活动参与者建立绿色通道。谈及双方在医学卫生领域的合作时，\
格拉济耶夫说：“我们应从当前考验中汲取经验，在生物安全领域制定共同规划并联合开展生物工程研究。”格拉济耶夫还表示，\
俄罗斯与其他欧亚经济联盟国家金融市场更易受国际投机行为影响。欧亚经济联盟应借鉴中国的人民币国际化经验，加强与中国银行体系和金融市场对接。\
欧亚经济联盟成立于2015年，成员国包括俄罗斯、哈萨克斯坦、白俄罗斯、吉尔吉斯斯坦和亚美尼亚。欧亚经济委员会执委会是欧亚经济联盟最高权力机构。"""

T = textRank.TextRank(text,pr_config={'alpha': 0.85, 'max_iter': 100})

# 提取前10个关键词
T.get_n_keywords(10)

# 提取前3个句子作为摘要

```

## 输出

```plain
# 关键词
[('中国', 0.0409732016371885),
 ('欧亚', 0.020288574056379977),
 ('联盟', 0.020095514492593516),
 ('疫情', 0.01896670992106251),
 ('合作', 0.01762300199967477),
 ('经济', 0.017491198051334592),
 ('加强', 0.014129557788440673),
 ('金融市场', 0.013893142456055885),
 ('体系', 0.012966637917644607),
 ('俄罗斯', 0.012933808546504099)]
 
 # 句子
 
 [('欧亚经济委员会执委会一体化与宏观经济委员格拉济耶夫日前接受新华社记者采访时高度评价中国抗击新冠疫情工作，并表示期待欧亚经济联盟与中国加强抗疫合作，共同推动地区发展',
  0.14281076822079067),
 ('格拉济耶夫认为，中国经济将会快速恢复，欧亚经济联盟许多企业与中国市场联系紧密，应与中国加强合作，采取协调措施降低此次疫情带来的消极影响',
  0.12857514563980263),
 ('欧亚经济联盟应借鉴中国的人民币国际化经验，加强与中国银行体系和金融市场对接', 0.11960701215088403)]

```
