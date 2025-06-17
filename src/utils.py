# -*- coding: utf-8 -*-
"""
杭州话编程语言工具函数
Hangzhou Dialect Programming Language Utilities
"""

import sys
from typing import List, Optional, Any, Dict
from keywords import HANGZHOU_KEYWORDS, HANGZHOU_PHRASES

class HangzhouError(Exception):
    """杭州话编程语言错误基类"""
    def __init__(self, message: str, line: Optional[int] = None, column: Optional[int] = None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.format_message())
    
    def format_message(self) -> str:
        """格式化错误消息"""
        if self.line is not None:
            if self.column is not None:
                return f"第{self.line}行第{self.column}列: {self.message}"
            else:
                return f"第{self.line}行: {self.message}"
        return self.message

class LexerError(HangzhouError):
    """词法分析错误"""
    pass

class ParserError(HangzhouError):
    """语法分析错误"""
    pass

class RuntimeError(HangzhouError):
    """运行时错误"""
    pass

def format_hangzhou_error(error: Exception, source_code: str = "") -> str:
    """格式化杭州话风格的错误消息"""
    error_messages = {
        'SyntaxError': '语法错误',
        'NameError': '变量名错误',
        'TypeError': '类型错误',
        'ValueError': '值错误',
        'ZeroDivisionError': '除零错误',
        'IndexError': '索引错误',
        'KeyError': '键错误',
        'AttributeError': '属性错误',
        'RuntimeError': '运行时错误'
    }
    
    error_type = type(error).__name__
    hangzhou_error_type = error_messages.get(error_type, '未知错误')
    
    # 杭州话风格的错误描述
    hangzhou_descriptions = {
        'SyntaxError': [
            "这语法不对啊老倌！",
            "写得乱七八糟的，看不懂啊！",
            "这句话说得不对啊！"
        ],
        'NameError': [
            "这个老倌我不认识啊！",
            "没有这个东西啊！",
            "你说的这个我不知道啊！"
        ],
        'TypeError': [
            "这两个东西不能这么搞啊！",
            "类型不对啊老倌！",
            "这个不能这么用啊！"
        ],
        'ZeroDivisionError': [
            "不能除以零啊老倌！",
            "这样除没有意义啊！"
        ],
        'ValueError': [
            "这个值不对啊！",
            "给的东西不合适啊！"
        ]
    }
    
    import random
    descriptions = hangzhou_descriptions.get(error_type, ["出错了！"])
    description = random.choice(descriptions)
    
    return f"{hangzhou_error_type}: {description}\n详细信息: {str(error)}"

def debug_tokens(text: str) -> None:
    """调试模式：显示词法分析结果"""
    from lexer import tokenize
    
    print("词法分析结果:")
    print("-" * 40)
    
    try:
        tokens = tokenize(text)
        for i, token in enumerate(tokens):
            print(f"{i:3d}: {token.type.name:15} | {token.value:20} | {token.line}:{token.column}")
    except Exception as e:
        print(f"词法分析错误: {e}")
    
    print("-" * 40)

def debug_ast(text: str) -> None:
    """调试模式：显示语法分析结果"""
    from parser import parse_text
    
    print("语法分析结果:")
    print("-" * 40)
    
    try:
        ast = parse_text(text)
        print_ast(ast)
    except Exception as e:
        print(f"语法分析错误: {e}")
    
    print("-" * 40)

def print_ast(node: Any, indent: int = 0) -> None:
    """打印抽象语法树"""
    prefix = "  " * indent
    node_name = type(node).__name__
    
    print(f"{prefix}{node_name}")
    
    # 打印节点属性
    if hasattr(node, '__dict__'):
        for attr_name, attr_value in node.__dict__.items():
            if attr_name.startswith('_'):
                continue
            
            print(f"{prefix}  {attr_name}:", end="")
            
            if isinstance(attr_value, list):
                if attr_value:
                    print()
                    for item in attr_value:
                        if hasattr(item, '__dict__'):
                            print_ast(item, indent + 2)
                        else:
                            print(f"{prefix}    {item}")
                else:
                    print(" []")
            elif hasattr(attr_value, '__dict__'):
                print()
                print_ast(attr_value, indent + 2)
            else:
                print(f" {attr_value}")

def translate_to_python(hangzhou_code: str) -> str:
    """将杭州话代码翻译为Python代码（简单版本）"""
    lines = hangzhou_code.split('\n')
    python_lines = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            python_lines.append(line)
            continue
        
        # 简单的关键字替换
        python_line = line
        for hangzhou_keyword, python_keyword in HANGZHOU_KEYWORDS.items():
            if python_keyword in ['var', 'print']:
                continue  # 这些需要特殊处理
            python_line = python_line.replace(hangzhou_keyword, python_keyword)
        
        # 特殊处理
        if '老倌' in python_line and '装' in python_line:
            # 变量声明：老倌 name 装 value -> name = value
            parts = python_line.split()
            if len(parts) >= 4 and parts[0] == '老倌' and parts[2] == '装':
                var_name = parts[1]
                value_part = ' '.join(parts[3:])
                python_line = f"{var_name} = {value_part}"
        
        if python_line.startswith('话说'):
            # 输出语句：话说 value -> print(value)
            content = python_line[2:].strip()
            if content.startswith('：'):
                content = content[1:].strip()
            python_line = f"print({content})"
        
        python_lines.append(python_line)
    
    return '\n'.join(python_lines)

def get_keyword_suggestions(partial_word: str) -> List[str]:
    """获取关键字建议（用于自动补全）"""
    suggestions = []
    
    for keyword in HANGZHOU_KEYWORDS.keys():
        if keyword.startswith(partial_word):
            suggestions.append(keyword)
    
    for phrase in HANGZHOU_PHRASES.keys():
        if phrase.startswith(partial_word):
            suggestions.append(phrase)
    
    return sorted(suggestions)

def validate_syntax_simple(code: str) -> List[str]:
    """简单的语法验证，返回警告列表"""
    warnings = []
    lines = code.split('\n')
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # 检查常见错误
        if '老倌' in line and '装' not in line:
            warnings.append(f"第{i}行: 变量声明可能缺少'装'关键字")
        
        if line.startswith('特为') and not line.endswith('：'):
            warnings.append(f"第{i}行: 条件语句可能缺少冒号")
        
        if line.startswith('会做事') and '：' not in line:
            warnings.append(f"第{i}行: 函数定义可能缺少冒号")
        
        # 检查括号匹配
        open_parens = line.count('（') + line.count('(')
        close_parens = line.count('）') + line.count(')')
        if open_parens != close_parens:
            warnings.append(f"第{i}行: 括号不匹配")
    
    return warnings

def format_code(code: str) -> str:
    """格式化杭州话代码"""
    lines = code.split('\n')
    formatted_lines = []
    indent_level = 0
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            formatted_lines.append('')
            continue
        
        # 减少缩进
        if stripped.startswith('不然') or stripped == '':
            indent_level = max(0, indent_level - 1)
        
        # 添加缩进
        formatted_line = '    ' * indent_level + stripped
        formatted_lines.append(formatted_line)
        
        # 增加缩进
        if stripped.endswith('：'):
            indent_level += 1
    
    return '\n'.join(formatted_lines)

def get_version_info() -> Dict[str, str]:
    """获取版本信息"""
    return {
        'version': '1.0.0',
        'name': '杭州话编程语言',
        'english_name': 'Hangzhou Dialect Programming Language',
        'author': 'Hangzhou Lang Team',
        'description': '基于杭州方言的编程语言，让编程更有地方特色',
        'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    }

def print_welcome() -> None:
    """打印欢迎信息"""
    version_info = get_version_info()
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    {version_info['name']} v{version_info['version']}                    ║
║              {version_info['english_name']}               ║
║                                                              ║
║  让编程说杭州话！Make Programming Speak Hangzhou Dialect!    ║
║                                                              ║
║  基于Python {version_info['python_version']} 开发                                        ║
╚══════════════════════════════════════════════════════════════╝
""")

if __name__ == '__main__':
    # 测试代码
    test_code = '''
老倌 张三 装 25
话说："你好，杭州！"
特为 张三 大过 18：
    话说："成年了"
'''
    
    print("测试词法分析:")
    debug_tokens(test_code)
    
    print("\n测试语法分析:")
    debug_ast(test_code)
    
    print("\n语法验证:")
    warnings = validate_syntax_simple(test_code)
    for warning in warnings:
        print(warning)
    
    print("\n格式化代码:")
    print(format_code(test_code)) 