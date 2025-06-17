# 杭州话编程语言 (Hangzhou Dialect Programming Language)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

> 让编程说杭州话！基于杭州方言的编程语言，让代码更有地方特色。

本项目受到[东北话编程语言](https://github.com/zhanyong-wan/dongbei)的启发

## 特色功能

- 🗣️ **纯杭州话语法** - 使用地道的杭州方言关键字
- 🎯 **简单易学** - 基于Python，语法简洁明了  
- 🎮 **交互模式** - 支持"摆话"模式，实时交互编程
- 📱 **跨平台** - 支持 Windows、macOS、Linux
- 🔧 **调试友好** - 完整的错误提示和调试功能
- 📚 **丰富示例** - 内置多个示例程序

## 快速开始

### 安装要求

- Python 3
- UTF-8 编码支持

### 克隆项目

```bash
git clone https://github.com/xuemian168/hangzhou-lang.git
cd hangzhou-lang
```

### 运行示例

```bash
# 进入src目录
cd src

# 交互模式（摆话模式）
python hangzhoulang.py

# 运行示例程序
python hangzhoulang.py --example hello

# 运行程序文件
python hangzhoulang.py ../test/examples/hello_world.hz

# 调试模式
python hangzhoulang.py --debug ../test/examples/calculator.hz
```

## 语法介绍

### 基础语法

#### 变量声明和赋值
```hangzhoulang
# 声明变量
老倌 张三 装 25
老倌 姓名 装 "小明"
老倌 成绩 装 88.5

# 赋值
张三 装 30
```

#### 输出语句
```hangzhoulang
话说："你好，杭州！"
话说：张三
话说："格毛天气蛮蛮好！"
```

#### 条件判断
```hangzhoulang
特为 张三 大过 18：
    话说："这个老倌成年了"
不然：
    话说："这个老倌还小"
```

#### 循环
```hangzhoulang
老倌 i 装 0
一息息 i 小过 10：
    话说：i
    i 装 i 加 1
```

#### 函数定义
```hangzhoulang
会做事 打招呼（老倌 名字）：
    话说："你好，"
    话说：名字
    话说："！"
    
会做事 计算（老倌 甲，老倌 乙）：
    老倌 结果 装 甲 加 乙
    有数 结果

# 调用函数
打招呼（"小王"）
老倌 和 装 计算（3，5）
```

### 关键字对照表

| 杭州话 | 含义 | 对应功能 |
|--------|------|----------|
| 老倌 | 变量 | 变量声明 |
| 装 | 赋值 | = |
| 话说 | 输出 | print |
| 特为 | 条件 | if |
| 要是 | 条件 | if |
| 不然 | 否则 | else |
| 一息息 | 循环 | while |
| 会做事 | 函数 | def |
| 有数 | 返回 | return |
| 大过 | 大于 | > |
| 小过 | 小于 | < |
| 等于 | 等于 | == |
| 加 | 加法 | + |
| 减 | 减法 | - |
| 乘 | 乘法 | * |
| 除 | 除法 | / |

### 杭州话特色词汇

#### 时间表达
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 早上/早半日 | 上午 | 时间 |
| 日里 | 白天 | 时间 |
| 日中 | 中午 | 时间 |
| 晚快边儿 | 傍晚 | 时间 |
| 夜里头/晚上头 | 夜晚 | 时间 |
| 头毛 | 刚才 | 时间 |
| 葛毛/格毛 | 现在 | 时间 |
| 上毛/上毛子 | 前回 | 时间 |
| 旧年子 | 去年 | 时间 |
| 辰光/时光 | 时候 | 时间 |

#### 家庭称谓
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 男人家 | 男人 | 称谓 |
| 女人家 | 女人 | 称谓 |
| 小伢儿 | 小孩子 | 称谓 |
| 男伢儿 | 男孩子 | 称谓 |
| 女伢儿 | 女孩子 | 称谓 |
| 阿爸 | 父亲 | 称谓 |
| 姆妈 | 母亲 | 称谓 |
| 爹爹 | 祖父 | 称谓 |
| 奶奶 | 祖母 | 称谓 |

#### 程度副词
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 尽该 | 很 | 程度 |
| 蛮蛮 | 很 | 程度 |
| 木佬佬 | 很 | 程度 |
| 蹩脚 | 差 | 程度 |
| 起泡 | 差 | 程度 |
| 推板 | 差 | 程度 |
| 一滴滴 | 一点儿 | 程度 |
| 慢慢交 | 慢慢地 | 程度 |
| 好好交 | 好好地 | 程度 |

#### 动作词汇
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 做事体 | 干活儿 | 动作 |
| 吃酒 | 喝酒 | 动作 |
| 吃烟 | 抽烟 | 动作 |
| 吃茶 | 喝茶 | 动作 |
| 洗浴/汏浴 | 洗澡 | 动作 |
| 睏觉 | 睡觉 | 动作 |
| 歇力 | 休息 | 动作 |
| 耍子 | 玩儿 | 动作 |
| 寻事儿 | 找茬 | 动作 |
| 闹架儿 | 吵架 | 动作 |

#### 形容词
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 好看 | 美 | 形容词 |
| 难看 | 丑 | 形容词 |
| 发靥 | 可笑、好笑 | 形容词 |
| 难为情 | 害臊 | 形容词 |
| 滥滥湿 | 很湿 | 形容词 |
| 冰冰瀴 | 很凉 | 形容词 |
| 墨墨黑 | 漆黑 | 形容词 |
| 不乖 | 顽皮 | 形容词 |
| 吃力 | 累 | 形容词 |

#### 疑问词
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 啥时光 | 什么时候 | 疑问词 |
| 啥地方 | 什么地方 | 疑问词 |
| 啥花头 | 什么花样/东西 | 疑问词 |
| 做啥 | 做什么 | 疑问词 |

#### 量词
| 杭州话 | 普通话 | 说明 |
|--------|--------|------|
| 一毛 | 一次 | 量词 |
| 两毛 | 两次 | 量词 |
| 一道 | 一块儿 | 量词 |
| 一床被 | 一条被 | 量词 |
| 一部车 | 一辆车 | 量词 |
| 一桄鱼 | 一条鱼 | 量词 |

## 内置函数

```hangzhoulang
# 数学函数
老倌 结果 装 绝对值（-5）      # 5
老倌 结果 装 求根（16）        # 4.0
老倌 结果 装 向上取整（3.2）   # 4
老倌 结果 装 向下取整（3.8）   # 3

# 字符串函数
老倌 长度 装 长度（"杭州"）    # 2
老倌 大写 装 大写（"hello"）   # "HELLO"
老倌 小写 装 小写（"WORLD"）   # "world"

# 类型检查
老倌 检查 装 是数字（123）     # 真的
老倌 检查 装 是字符串（"abc"） # 真的
```

## 示例程序

### Hello World
```hangzhoulang
# Hello World 示例
话说："你好，杭州！"
话说："格毛天气蛮蛮好！"

老倌 城市 装 "杭州"
话说："欢迎来到"
话说：城市
```

### 计算器
```hangzhoulang
# 简单计算器
老倌 甲 装 10
老倌 乙 装 5

老倌 和 装 甲 加 乙
老倌 差 装 甲 减 乙
老倌 积 装 甲 乘 乙
老倌 商 装 甲 除 乙

话说："加法结果："
话说：和
话说："减法结果："
话说：差
```

### 斐波那契数列
```hangzhoulang
# 斐波那契数列
会做事 斐波那契（老倌 n）：
    特为 n 小等于 1：
        有数 n
    不然：
        有数 斐波那契（n 减 1） 加 斐波那契（n 减 2）

# 计算前10项
老倌 i 装 0
一息息 i 小过 10：
    老倌 结果 装 斐波那契（i）
    话说：结果
    i 装 i 加 1
```

## 交互模式（摆话模式）

启动交互模式：
```bash
python hangzhoulang.py
```

交互示例：
```
欢迎使用杭州话编程语言！
你要跟 hangzhoulang 摆话啊？开始吧！要是一句话太长的话你就用\拆开来说。

你要话啥？ 老倌 张三 装 25
你要话啥？ 话说：张三
25
你要话啥？ 话说："格毛天气蛮蛮好！"
格毛天气蛮蛮好！
你要话啥？ 拜拜
高场了！再会！
```

### 交互模式命令

- `拜拜` / `完了` - 退出程序
- `历史` - 显示命令历史
- `清空` - 清空命令历史  
- `帮助` - 显示帮助信息

## 命令行选项

```bash
python hangzhoulang.py [选项] [文件]

选项:
  -h, --help              显示帮助信息
  -v, --version           显示版本信息
  -d, --debug             启用调试模式
  -e, --example 示例名     运行内置示例

示例:
  python hangzhoulang.py                    # 交互模式
  python hangzhoulang.py hello.hz           # 运行文件
  python hangzhoulang.py --example hello    # 运行示例
  python hangzhoulang.py --debug test.hz    # 调试模式
```

## 内置示例

| 示例名 | 描述 |
|--------|------|
| hello | Hello World 程序 |
| calculator | 计算器示例 |
| life | 杭州生活场景示例（展示杭州话词汇） |
| condition | 条件判断示例 |
| function | 函数定义示例 |

运行示例：
```bash
python hangzhoulang.py --example hello
python hangzhoulang.py --example calculator
python hangzhoulang.py --example life
```

## 杭州话词典工具

项目包含一个专门的杭州话词典查询工具，帮助学习和查找杭州话词汇：

### 基本用法
```bash
# 统计词汇信息
python hangzhou_dict.py --stats

# 搜索特定词汇
python hangzhou_dict.py -s 老倌

# 模糊搜索
python hangzhou_dict.py -p time

# 查看分类词汇
python hangzhou_dict.py -c 家庭称谓

# 列出所有分类
python hangzhou_dict.py -l

# 显示所有词汇
python hangzhou_dict.py -a

# 交互模式
python hangzhou_dict.py -i
```

### 交互模式示例
```
杭州话词典> 老倌
词汇: 老倌
含义: var
分类: 关键字

杭州话词典> category 时间表达
=== 时间表达 ===
共 15 个词汇：
----------------------------------------
早上 - morning
早半日 - morning
...

杭州话词典> pattern 家庭
找到 15 个匹配的词汇：
----------------------------------------
男人家 - man (家庭称谓)
女人家 - woman (家庭称谓)
...
```

### 词汇统计
当前版本包含：
- 关键字: 44 个词汇
- 时间表达: 15 个词汇  
- 家庭称谓: 15 个词汇
- 程度副词: 10 个词汇
- 动作词汇: 14 个词汇
- 形容词: 11 个词汇
- 疑问词: 4 个词汇
- 量词: 6 个词汇
- 常用短语: 13 个词汇
- **总计: 132 个词汇**

## 文件结构

```
hangzhoulang/
├── src/
│   ├── hangzhoulang.py    # 主程序入口
│   ├── hangzhou_dict.py   # 杭州话词典工具
│   ├── lexer.py           # 词法分析器
│   ├── parser.py          # 语法分析器
│   ├── interpreter.py     # 解释器核心
│   ├── keywords.py        # 关键字定义
│   └── utils.py           # 工具函数
├── test/
│   └── examples/
│       ├── hello_world.hz # Hello World示例
│       ├── calculator.hz  # 计算器示例
│       ├── hangzhou_life.hz # 杭州生活场景示例
│       └── fibonacci.hz   # 斐波那契示例
├── docs/
│   ├── README.md          # 项目文档
│   └── 词汇扩展更新.md    # 词汇扩展说明
└── README.md              # 主说明文件
```

## 开发指南

### 添加新关键字

1. 在 `src/keywords.py` 中的 `HANGZHOU_KEYWORDS` 字典添加映射
2. 在词法分析器中添加识别逻辑（如需要）
3. 在语法分析器中添加解析逻辑（如需要）
4. 在解释器中添加执行逻辑（如需要）

### 调试技巧

```bash
# 显示词法分析结果
python hangzhoulang.py --debug your_file.hz

# 在代码中添加调试信息
from utils import debug_tokens, debug_ast
debug_tokens("老倌 张三 装 25")
debug_ast("话说：'你好'")
```

## 错误处理

杭州话编程语言提供友好的错误提示：

```
语法错误: 这语法不对啊老倌！
详细信息: 期望 ':', 但得到 'NEWLINE'

变量名错误: 这个老倌我不认识啊！
详细信息: 未定义的变量: 李四

除零错误: 不能除以零啊老倌！
详细信息: 运行时错误: 除零错误
```

## 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/新功能`)
3. 提交更改 (`git commit -am '添加新功能'`)
4. 推送到分支 (`git push origin feature/新功能`)
5. 创建 Pull Request

### 贡献内容

- 🐛 Bug 修复
- ✨ 新功能
- 📚 文档改进
- 🎯 性能优化
- 🌍 多语言支持
- 📝 示例程序

## 版本历史

### v1.0.0 (2025-06-17)
- ✨ 初始版本发布
- 🎯 基础语法支持
- 🗣️ 交互模式
- 📚 示例程序
- 🔧 调试功能

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

- 感谢 [东北话编程语言](https://github.com/zhanyong-wan/dongbei) 项目的启发
- 感谢所有为杭州方言文化传承做出贡献的人们
- 感谢开源社区的支持

## 联系方式

- 项目主页：https://github.com/xuemian168/hangzhou-lang
- 问题反馈：https://github.com/xuemian168/hangzhou-lang/issues
- 邮箱：xuemian888@gmail.com

---

## 参考资料
1. [Wikipedia](https://zh.wikipedia.org/zh-hans/%E6%9D%AD%E5%B7%9E%E8%AF%9D#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)
2. [Chazidian](https://www.chazidian.com/fangyan1787/)
3. [杭州话与普通话拼音对照表](https://z.hangzhou.com.cn/2014/hzh/content/2014-10/14/content_5482920.htm)
4. [杭州方言词典]（https://z.hangzhou.com.cn/2014/hzh/content/2014-10/14/content_5483005_2.htm）

**让编程说杭州话，让代码更有温度！**

*Make Programming Speak Hangzhou Dialect, Make Code More Warm!* 