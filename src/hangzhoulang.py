#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
杭州话编程语言主程序
Hangzhou Dialect Programming Language Main Program
"""

import sys
import os
import argparse
from typing import List, Optional
from interpreter import interpret_text, HangzhouInterpreter
from lexer import tokenize, HangzhouLexer
from parser import parse_text

class HangzhouREPL:
    """杭州话交互式解释器（摆话模式）"""
    
    def __init__(self):
        self.interpreter = HangzhouInterpreter()
        self.history = []
    
    def run(self) -> None:
        """启动交互模式"""
        print("欢迎使用杭州话编程语言！")
        print("你要跟 hangzhoulang 话啊？开始好嘞！要是一句话太长的话你就用\\拆开来说。")
        print("输入'拜拜'或'完了'退出。")
        print()
        
        while True:
            try:
                # 获取用户输入
                line = self._get_input()
                
                if not line.strip():
                    continue
                
                # 检查退出命令
                if line.strip() in ['拜拜', '完了', '再会', 'exit', 'quit']:
                    print("高场了！再会！")
                    break
                
                # 特殊命令
                if line.strip() == '历史':
                    self._show_history()
                    continue
                elif line.strip() == '清空':
                    self.history.clear()
                    print("历史记录已清空。")
                    continue
                elif line.strip() == '帮助':
                    self._show_help()
                    continue
                
                # 执行代码
                self._execute_line(line)
                self.history.append(line)
                
            except KeyboardInterrupt:
                print("\n高场了！")
                break
            except EOFError:
                print("\n高场了！")
                break
            except Exception as e:
                print(f"出错了: {e}")
    
    def _get_input(self) -> str:
        """获取用户输入，支持多行输入"""
        line = input("你要话啥？ ")
        
        # 处理多行输入
        while line.endswith('\\'):
            line = line[:-1]  # 移除反斜杠
            continuation = input("你还要话啥？ ")
            line += continuation
        
        return line
    
    def _execute_line(self, line: str) -> None:
        """执行一行代码"""
        try:
            # 解析并执行
            program = parse_text(line)
            self.interpreter.output_buffer = []
            
            for statement in program.statements:
                self.interpreter.execute_statement(statement)
            
            # 如果没有输出，尝试作为表达式求值
            if not self.interpreter.output_buffer and program.statements:
                from parser import Expression
                stmt = program.statements[-1]
                # 简单处理：如果最后一个语句看起来像表达式，尝试求值
                # 这里简化处理，实际应该改进语法分析器
        
        except Exception as e:
            print(f"错误: {e}")
    
    def _show_history(self) -> None:
        """显示历史记录"""
        if not self.history:
            print("还没有历史记录。")
            return
        
        print("历史记录:")
        for i, line in enumerate(self.history, 1):
            print(f"{i:3d}: {line}")
    
    def _show_help(self) -> None:
        """显示帮助信息"""
        print("杭州话编程语言帮助:")
        print("  拜拜/完了     - 退出程序")
        print("  历史         - 显示命令历史")
        print("  清空         - 清空命令历史")
        print("  帮助         - 显示此帮助信息")
        print()
        print("语法示例:")
        print("  老倌 张三 装 25              # 变量声明")
        print("  话说：\"格毛天气蛮蛮好！\"     # 输出语句")
        print("  特为 张三 大过 20：           # 条件判断")
        print("      话说：\"张三年纪大\"")
        print("  会做事 算账（老倌 甲，老倌 乙）：  # 函数定义")
        print("      有数 甲 加 乙")

def run_file(filename: str, debug: bool = False) -> None:
    """运行杭州话程序文件"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if debug:
            print(f"正在执行文件: {filename}")
            print("=" * 50)
            print(content)
            print("=" * 50)
            
            # 显示词法分析结果
            print("词法分析结果:")
            tokens = tokenize(content)
            for token in tokens:
                print(f"  {token}")
            print()
        
        # 执行程序
        results = interpret_text(content)
        
        if debug and results:
            print("执行结果:")
            for result in results:
                print(result)
    
    except FileNotFoundError:
        print(f"错误: 找不到文件 '{filename}'")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"错误: 无法读取文件 '{filename}'，请确保文件是UTF-8编码")
        sys.exit(1)
    except Exception as e:
        print(f"执行错误: {e}")
        sys.exit(1)

def run_example(example_name: str) -> None:
    """运行内置示例"""
    examples = {
        'hello': '''
# 这是一个简单的Hello World程序
话说 "你好，杭州！"
话说 "Welcome to Hangzhou Dialect Programming!"
''',
        'calculator': '''
# 简单计算器示例
老倌 甲 装 10
老倌 乙 装 5

话说 "甲 = "
话说 甲
话说 "乙 = "
话说 乙

老倌 结果 装 甲 加 乙
话说 "甲 + 乙 = "
话说 结果

老倌 结果 装 甲 减 乙
话说 "甲 - 乙 = "
话说 结果

老倌 结果 装 甲 乘 乙
话说 "甲 * 乙 = "
话说 结果
''',
        'life': '''
# 杭州生活场景示例
话说 "欢迎来到杭州话生活场景演示！"

# 时间相关
老倌 现在时光 装 "葛毛"
话说 "现在是" 加 现在时光 加 "，正好做点事体。"

老倌 早上时间 装 "早半日"
老倌 白天时间 装 "日里" 
老倌 夜晚时间 装 "夜里头"

话说 "杭州人一天的时光："
话说 早上时间 加 "起床，" 加 白天时间 加 "做事体，" 加 夜晚时间 加 "睏觉。"

# 家庭成员介绍
话说 "\\n杭州人的家庭称谓："
老倌 爸爸 装 "阿爸"
老倌 妈妈 装 "姆妈" 
老倌 爷爷 装 "爹爹"
老倌 奶奶 装 "奶奶"

话说 "家里有" 加 爸爸 加 "、" 加 妈妈 加 "、" 加 爷爷 加 "、" 加 奶奶

# 杭州话程度表达
老倌 程度1 装 "蛮蛮"
老倌 程度2 装 "尽该" 

话说 "\\n杭州话的程度表达："
话说 "今天天气" 加 程度1 加 "好看！"
话说 "这道菜" 加 程度2 加 "好吃！"

话说 "\\n晏歇会再见！欢迎多来杭州耍子！"
''',
        'condition': '''
# 条件判断示例
老倌 年龄 装 25

特为 年龄 大过 18：
    话说 "这个老倌成年了"
不然：
    话说 "这个老倌还小"

特为 年龄 大过 60：
    话说 "这个老倌是老人家"
不然：
    话说 "这个老倌还年轻"
''',
        'function': '''
# 函数定义示例
会做事 打招呼（老倌 名字）：
    话说 "你好，"
    话说 名字
    话说 "！"

会做事 计算（老倌 甲，老倌 乙）：
    老倌 和 装 甲 加 乙
    有数 和

# 调用函数
打招呼（"小明"）
老倌 结果 装 计算（3，4）
话说 "3 + 4 = "
话说 结果
'''
    }
    
    if example_name not in examples:
        print(f"未知的示例: {example_name}")
        print(f"可用示例: {', '.join(examples.keys())}")
        return
    
    print(f"运行示例: {example_name}")
    print("=" * 50)
    print(examples[example_name])
    print("=" * 50)
    print("执行结果:")
    
    try:
        interpret_text(examples[example_name])
    except Exception as e:
        print(f"执行错误: {e}")

def main() -> None:
    """主函数"""
    parser = argparse.ArgumentParser(
        description='杭州话编程语言解释器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用示例:
  hangzhoulang                    # 启动交互模式
  hangzhoulang hello.hz           # 运行程序文件
  hangzhoulang --example hello    # 运行内置示例
  hangzhoulang --debug hello.hz   # 调试模式运行
        '''
    )
    
    parser.add_argument('file', nargs='?', help='要执行的杭州话程序文件')
    parser.add_argument('--debug', '-d', action='store_true', help='启用调试模式')
    parser.add_argument('--example', '-e', help='运行内置示例')
    parser.add_argument('--version', '-v', action='version', version='杭州话编程语言 v1.0.0')
    
    args = parser.parse_args()
    
    # 运行示例
    if args.example:
        run_example(args.example)
        return
    
    # 运行文件
    if args.file:
        run_file(args.file, args.debug)
        return
    
    # 交互模式
    repl = HangzhouREPL()
    repl.run()

if __name__ == '__main__':
    main() 