INTRO_TEMPLATE = """[返回完整规则目录](/cr/)

# 前言

{content}

[第一章 - 游戏概念 Game Concepts](/cr/1/)"""

MAIN_TEMPLATE = """[返回完整规则目录](/cr/) | {prev_next_chapter}

{content}

[返回完整规则目录](/cr/) | {prev_next_chapter}"""

GLOSSARY_PINYIN_TEMPLATE = """[返回完整规则目录](/cr/)
# 词汇表（按拼音首字母排序）

{content}"""

GLOSSARY_ALPHABET_TEMPLATE = """[返回完整规则目录](/cr/)
# 词汇表（按英文首字母排序） 

{content}"""

CREDITS_TEMPLATE = """[返回完整规则目录](/cr/)

# 版权信息 
{content}"""

CATALOG_TEMPLATE = """# 目录

此中文版《万智牌完整规则》是大中华区裁判社群志愿者的翻译成果，并非官方译本。

如果您对某条规则的翻译发现错误、或有改进的建议，亦或有意帮助翻译，请通过下列方式联系维护者：

- [Github Issue](https://github.com/HeliumOctahelide/magic-comp-rules-zh-cn)
- [大学院废墟用户反馈](https://mtgch.com/feedback)

中文版翻译负责人：李思扬

中文版翻译维护者：金汉宁、简单

历史版本负责人及贡献者：杜昊、张天启、许兆本、杨俊杰、刘清源等。

*{effective_time}*

[前言](/cr/intro/)

{content}

词汇表 Glossary - [按英文首字母排序](/cr/glossary/) | [按拼音首字母排序](/cr/glossarycn/)

[暂译名称列表](/cr/translatedterms/)

[版权信息](/cr/credits/)
"""