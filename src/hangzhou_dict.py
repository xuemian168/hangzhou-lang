# -*- coding: utf-8 -*-
"""
杭州话词典查询工具
Hangzhou Dialect Dictionary Tool
"""

import sys
import argparse
from keywords import (
    ALL_HANGZHOU_WORDS, 
    HANGZHOU_KEYWORDS,
    HANGZHOU_TIME,
    HANGZHOU_FAMILY,
    HANGZHOU_DEGREE,
    HANGZHOU_ACTIONS,
    HANGZHOU_ADJECTIVES,
    HANGZHOU_QUESTIONS,
    HANGZHOU_MEASURE,
    HANGZHOU_PHRASES,
    search_hangzhou_words,
    get_hangzhou_meaning,
    get_word_category
)

SPECIAL_WORDS = {
    "62": {
        "meaning": "盒子/笨蛋",
        "type": "俚语",
        "usage": [
            "这个62，啥都不懂！",
            "别像个62一样思考问题。",
            "一个62大的盒子。"
        ],
        "origin": "数字谐音",
        "humor_level": "高",
        "fun_fact": "在杭州话中，62既可以指盒子，也可以调侃某人笨。"
    }
}

class HangzhouDict:
    """杭州话词典类"""
    
    def __init__(self):
        self.categories = {
            "关键字": HANGZHOU_KEYWORDS,
            "时间表达": HANGZHOU_TIME,
            "家庭称谓": HANGZHOU_FAMILY,
            "程度副词": HANGZHOU_DEGREE,
            "动作词汇": HANGZHOU_ACTIONS,
            "形容词": HANGZHOU_ADJECTIVES,
            "疑问词": HANGZHOU_QUESTIONS,
            "量词": HANGZHOU_MEASURE,
            "常用短语": HANGZHOU_PHRASES
        }
    
    def search_word(self, word):
        """搜索特定词汇"""
        if word in ALL_HANGZHOU_WORDS:
            meaning = get_hangzhou_meaning(word)
            category = get_word_category(word)
            return {
                'word': word,
                'meaning': meaning,
                'category': category,
                'found': True
            }
        else:
            return {'found': False}
    
    def search_pattern(self, pattern):
        """模糊搜索"""
        results = search_hangzhou_words(pattern)
        return results
    
    def list_category(self, category_name):
        """列出指定分类的所有词汇"""
        if category_name in self.categories:
            return self.categories[category_name]
        else:
            return None
    
    def get_all_categories(self):
        """获取所有分类名称"""
        return list(self.categories.keys())
    
    def get_statistics(self):
        """获取词典统计信息"""
        stats = {}
        total = 0
        for name, words in self.categories.items():
            count = len(words)
            stats[name] = count
            total += count
        stats['总计'] = total
        return stats
    
    def print_word_info(self, word_info):
        """格式化输出词汇信息"""
        if word_info['found']:
            print(f"词汇: {word_info['word']}")
            print(f"含义: {word_info['meaning']}")
            print(f"分类: {word_info['category']}")
        else:
            print("未找到该词汇")
    
    def print_search_results(self, results):
        """格式化输出搜索结果"""
        if not results:
            print("没有找到匹配的词汇")
            return
        
        print(f"找到 {len(results)} 个匹配的词汇：")
        print("-" * 40)
        for word, meaning in results:
            category = get_word_category(word)
            print(f"{word} - {meaning} ({category})")
    
    def print_category_words(self, category_name):
        """输出指定分类的所有词汇"""
        words = self.list_category(category_name)
        if words is None:
            print(f"分类 '{category_name}' 不存在")
            return
        
        print(f"\n=== {category_name} ===")
        print(f"共 {len(words)} 个词汇：")
        print("-" * 40)
        
        for word, meaning in words.items():
            print(f"{word} - {meaning}")
    
    def print_all_categories(self):
        """输出所有分类的词汇"""
        for category_name in self.categories:
            self.print_category_words(category_name)
            print()
    
    def print_statistics(self):
        """输出统计信息"""
        stats = self.get_statistics()
        print("=== 杭州话词典统计 ===")
        for category, count in stats.items():
            print(f"{category}: {count} 个词汇")

def get_special_word_info(word):
    """获取特殊词汇信息"""
    return SPECIAL_WORDS.get(word, None)

def is_special_word(word):
    """判断是否为特殊词汇"""
    return word in SPECIAL_WORDS

def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='杭州话词典查询工具')
    parser.add_argument('-s', '--search', help='搜索词汇')
    parser.add_argument('-p', '--pattern', help='模糊搜索')
    parser.add_argument('-c', '--category', help='列出指定分类的词汇')
    parser.add_argument('-l', '--list', action='store_true', help='列出所有分类')
    parser.add_argument('-a', '--all', action='store_true', help='显示所有词汇')
    parser.add_argument('--stats', action='store_true', help='显示统计信息')
    parser.add_argument('-i', '--interactive', action='store_true', help='交互模式')
    
    args = parser.parse_args()
    
    dict_tool = HangzhouDict()
    
    if args.search:
        # 精确搜索
        result = dict_tool.search_word(args.search)
        dict_tool.print_word_info(result)
        
    elif args.pattern:
        # 模糊搜索
        results = dict_tool.search_pattern(args.pattern)
        dict_tool.print_search_results(results)
        
    elif args.category:
        # 显示分类词汇
        dict_tool.print_category_words(args.category)
        
    elif args.list:
        # 列出所有分类
        categories = dict_tool.get_all_categories()
        print("可用的词汇分类：")
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
    
    elif args.all:
        # 显示所有词汇
        dict_tool.print_all_categories()
        
    elif args.stats:
        # 显示统计信息
        dict_tool.print_statistics()
        
    elif args.interactive:
        # 交互模式
        interactive_mode(dict_tool)
        
    else:
        # 默认显示帮助
        parser.print_help()

def interactive_mode(dict_tool):
    """交互模式"""
    print("欢迎使用杭州话词典查询工具！")
    print("输入 'help' 查看帮助，输入 'quit' 退出")
    
    while True:
        try:
            command = input("\n杭州话词典> ").strip()
            
            if command == 'quit' or command == 'exit':
                print("晏歇会再见！")
                break
                
            elif command == 'help':
                print_help()
                
            elif command == 'stats':
                dict_tool.print_statistics()
                
            elif command == 'categories':
                categories = dict_tool.get_all_categories()
                print("可用的词汇分类：")
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                    
            elif command.startswith('search '):
                word = command[7:]
                result = dict_tool.search_word(word)
                dict_tool.print_word_info(result)
                
            elif command.startswith('pattern '):
                pattern = command[8:]
                results = dict_tool.search_pattern(pattern)
                dict_tool.print_search_results(results)
                
            elif command.startswith('category '):
                category = command[9:]
                dict_tool.print_category_words(category)
                
            else:
                # 默认作为搜索词汇处理
                if command:
                    result = dict_tool.search_word(command)
                    if result['found']:
                        dict_tool.print_word_info(result)
                    else:
                        # 尝试模糊搜索
                        results = dict_tool.search_pattern(command)
                        if results:
                            print(f"未找到精确匹配，以下是相关词汇：")
                            dict_tool.print_search_results(results)
                        else:
                            print("未找到相关词汇")
                            
        except KeyboardInterrupt:
            print("\n晏歇会再见！")
            break
        except Exception as e:
            print(f"出错了：{e}")

def print_help():
    """打印帮助信息"""
    help_text = """
杭州话词典查询工具使用说明：

基本命令：
  help          - 显示此帮助信息
  quit/exit     - 退出程序
  stats         - 显示词典统计信息
  categories    - 列出所有词汇分类

搜索命令：
  search <词汇>  - 精确搜索词汇
  pattern <模式> - 模糊搜索
  category <分类> - 显示指定分类的所有词汇
  
  也可以直接输入词汇进行搜索

示例：
  search 老倌
  pattern 时间
  category 家庭称谓
  老倌
"""
    print(help_text)

if __name__ == '__main__':
    main() 