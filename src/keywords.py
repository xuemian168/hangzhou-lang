# -*- coding: utf-8 -*-
"""
杭州话编程语言关键字定义
Hangzhou Dialect Programming Language Keywords Definition
"""

# 杭州话关键字到Python关键字的映射
HANGZHOU_KEYWORDS = {
    # 变量和赋值
    '老倌': 'var',
    '装': '=',
    '摆': '=',      # 放置、摆放
    '安': '=',      # 安放  
    '搁': '=',      # 搁置
    
    # 输出语句
    '话说': 'print',
    
    # 条件判断
    '特为': 'if',
    '要是': 'if',
    '不然': 'else',
    '还有': 'elif',
    
    # 循环
    '一息息': 'while',    # 一会儿
    '直到': 'until',
    
    # 函数
    '会做事': 'def',      # 会做事情
    '做事体': 'def',      # 干活儿
    '介个套': 'def',      # 怎么办 → 定义一个办法
    '有数': 'return',     # 懂了、明白了
    '晓得': 'return',     # 知道
    
    # 逻辑运算
    '大过': '>',
    '小过': '<',
    '等于': '==',
    '不等': '!=',
    '大等于': '>=',
    '小等于': '<=',
    
    # 算术运算
    '加': '+',
    '减': '-',
    '乘': '*',
    '除': '/',
    
    # 逻辑连接
    '还有': 'and',
    '要么': 'or',
    '不是': 'not',
    
    # 常用值
    '真的': 'True',
    '假的': 'False',
    '空的': 'None',
    '造话': 'False',      # 假话
    
    # 数据结构
    '一摊': 'list',       # 列表
    '一套': 'dict',       # 字典
    
    # 流程控制
    '跳出': 'break',
    '继续': 'continue',
    '歇力': 'break',      # 休息

    # 系统函数
    '撒宽': 'sleep',      # 随意放松 → 休眠
    '撒子儿': 'random',   # 玩耍 → 随机数

    # 模块导入
    '进来': 'import',
    '从': 'from',
    
    # 其他动作
    '寻事儿': 'find',     # 找茬、查找
    '耍子': 'run',        # 玩儿、执行
    '记牢': 'save',       # 记住
    '粘牢': 'attach',     # 粘住
    '拎起来': 'raise',    # 提起来
}

# 杭州话数字映射
HANGZHOU_NUMBERS = {
    '零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
    '五': '5', '六': '6', '七': '7', '八': '8', '九': '9',
    '十': '10', '百': '100', '千': '1000', '万': '10000'
}

# 杭州话时间表达
HANGZHOU_TIME = {
    '早上': 'morning',
    '早半日': 'morning',     # 上午
    '日里': 'day',           # 白天
    '日中': 'noon',          # 中午
    '晚快边儿': 'evening',   # 傍晚
    '夜里头': 'night',       # 夜晚
    '晚上头': 'night',       # 夜晚
    '头毛': 'just_now',      # 刚才
    '葛毛': 'now',           # 现在
    '格毛': 'now',           # 现在（另一种写法）
    '上毛': 'before',        # 前回
    '上毛子': 'before',      # 前回
    '旧年子': 'last_year',   # 去年
    '辰光': 'time',          # 时候
    '时光': 'time',          # 时候
}

# 杭州话家庭称谓
HANGZHOU_FAMILY = {
    '男人家': 'man',         # 男人
    '女人家': 'woman',       # 女人
    '小伢儿': 'child',       # 小孩子
    '男伢儿': 'boy',         # 男孩子
    '女伢儿': 'girl',        # 女孩子
    '阿爸': 'father',        # 父亲
    '姆妈': 'mother',        # 母亲
    '爹爹': 'grandfather',   # 祖父
    '奶奶': 'grandmother',   # 祖母
    '阿哥': 'brother',       # 兄
    '阿弟': 'brother',       # 弟
    '阿姐': 'sister',        # 姐
    '阿妹': 'sister',        # 妹
    '老公': 'husband',       # 丈夫
    '老婆': 'wife',          # 妻子
}

# 杭州话程度副词
HANGZHOU_DEGREE = {
    '尽该': 'very',          # 很
    '蛮蛮': 'very',          # 很
    '木佬佬': 'very',        # 很
    '蹩脚': 'bad',           # 差
    '起泡': 'bad',           # 差
    '推板': 'bad',           # 差
    '一滴滴': 'little',      # 一点儿
    '一息息': 'while',       # 一会儿
    '慢慢交': 'slowly',      # 慢慢地
    '好好交': 'well',        # 好好地
}

# 杭州话动作词汇
HANGZHOU_ACTIONS = {
    '做事体': 'work',        # 干活儿
    '吃酒': 'drink',         # 喝酒
    '吃烟': 'smoke',         # 抽烟
    '吃茶': 'tea',           # 喝茶
    '洗浴': 'bath',          # 洗澡
    '汏浴': 'bath',          # 洗澡
    '睏觉': 'sleep',         # 睡觉
    '歇力': 'rest',          # 休息
    '耍子': 'play',          # 玩儿
    '闹架儿': 'argue',       # 吵架
    '寻事儿': 'trouble',     # 找茬
    '看病': 'doctor',        # 看医生
    '讨老婆': 'marry',       # 娶媳妇
    '嫁老公': 'marry',       # 出嫁
}

# 杭州话形容词
HANGZHOU_ADJECTIVES = {
    '好看': 'beautiful',     # 美
    '难看': 'ugly',          # 丑
    '发靥': 'funny',         # 可笑、好笑
    '难为情': 'shy',         # 害臊
    '滥滥湿': 'wet',         # 很湿
    '冰冰瀴': 'cold',        # 很凉
    '墨墨黑': 'dark',        # 漆黑
    '糊达达': 'sticky',      # 粘粘糊糊
    '糊里达喇': 'sticky',    # 粘粘糊糊
    '不乖': 'naughty',       # 顽皮
    '吃力': 'tired',         # 累
}

# 杭州话疑问词
HANGZHOU_QUESTIONS = {
    '啥时光': 'when',        # 什么时候
    '啥地方': 'where',       # 什么地方
    '啥花头': 'what',        # 什么花样，什么东西
    '做啥': 'what_do',       # 做什么
}

# 杭州话量词
HANGZHOU_MEASURE = {
    '一毛': 'once',          # 一次
    '两毛': 'twice',         # 两次
    '一道': 'together',      # 一块儿
    '一床被': 'one_quilt',   # 一条被
    '一部车': 'one_car',     # 一辆车
    '一桄鱼': 'one_fish',    # 一条鱼
}

# 杭州话常用短语
HANGZHOU_PHRASES = {
    '格毛': 'now',           # 现在
    '头毛': 'just',          # 刚才
    '日里': 'day',           # 白天
    '夜到头': 'night',       # 夜晚
    '蛮蛮': 'very',          # 很
    '木老老': 'very',        # 很
    '尽该': 'very',          # 很
    '蹩脚': 'bad',           # 差
    '起泡': 'bad',           # 差
    '推板': 'bad',           # 差
    '晏歇会': 'see_later',   # 等会儿见
    '葛个老倌': 'this_person', # 这个人
    '那个老倌': 'that_person', # 那个人
}

# 合并所有词汇表
ALL_HANGZHOU_WORDS = {
    **HANGZHOU_KEYWORDS,
    **HANGZHOU_TIME,
    **HANGZHOU_FAMILY,
    **HANGZHOU_DEGREE,
    **HANGZHOU_ACTIONS,
    **HANGZHOU_ADJECTIVES,
    **HANGZHOU_QUESTIONS,
    **HANGZHOU_MEASURE,
    **HANGZHOU_PHRASES
}

# 获取Python对应的关键字
def get_python_keyword(hangzhou_word):
    """将杭州话关键字转换为Python关键字"""
    return HANGZHOU_KEYWORDS.get(hangzhou_word, hangzhou_word)

# 检查是否为杭州话关键字
def is_hangzhou_keyword(word):
    """检查是否为杭州话关键字"""
    return word in HANGZHOU_KEYWORDS

# 检查是否为杭州话词汇
def is_hangzhou_word(word):
    """检查是否为杭州话词汇"""
    return word in ALL_HANGZHOU_WORDS

# 获取所有杭州话关键字
def get_all_keywords():
    """获取所有杭州话关键字列表"""
    return list(HANGZHOU_KEYWORDS.keys())

# 获取杭州话词汇释义
def get_hangzhou_meaning(word):
    """获取杭州话词汇的含义"""
    return ALL_HANGZHOU_WORDS.get(word, word)

# 搜索杭州话词汇
def search_hangzhou_words(pattern):
    """搜索包含特定模式的杭州话词汇"""
    results = []
    for word, meaning in ALL_HANGZHOU_WORDS.items():
        if pattern in word or pattern in meaning:
            results.append((word, meaning))
    return results

# 获取词汇分类信息
def get_word_category(word):
    """获取词汇所属的分类"""
    if word in HANGZHOU_KEYWORDS:
        return "关键字"
    elif word in HANGZHOU_TIME:
        return "时间表达"
    elif word in HANGZHOU_FAMILY:
        return "家庭称谓"
    elif word in HANGZHOU_DEGREE:
        return "程度副词"
    elif word in HANGZHOU_ACTIONS:
        return "动作词汇"
    elif word in HANGZHOU_ADJECTIVES:
        return "形容词"
    elif word in HANGZHOU_QUESTIONS:
        return "疑问词"
    elif word in HANGZHOU_MEASURE:
        return "量词"
    elif word in HANGZHOU_PHRASES:
        return "常用短语"
    else:
        return "未分类" 