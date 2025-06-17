# -*- coding: utf-8 -*-
"""
杭州话编程语言词法分析器
Hangzhou Dialect Programming Language Lexer
"""

import re
import enum
from typing import List, NamedTuple, Optional
from keywords import HANGZHOU_KEYWORDS, HANGZHOU_NUMBERS, is_hangzhou_keyword

class TokenType(enum.Enum):
    """Token类型枚举"""
    # 基本类型
    KEYWORD = "KEYWORD"        # 关键字
    IDENTIFIER = "IDENTIFIER"  # 标识符
    NUMBER = "NUMBER"          # 数字
    STRING = "STRING"          # 字符串
    
    # 运算符
    PLUS = "PLUS"              # +
    MINUS = "MINUS"            # -
    MULTIPLY = "MULTIPLY"      # *
    DIVIDE = "DIVIDE"          # /
    ASSIGN = "ASSIGN"          # =
    
    # 比较运算符
    EQUAL = "EQUAL"            # ==
    NOT_EQUAL = "NOT_EQUAL"    # !=
    GREATER = "GREATER"        # >
    LESS = "LESS"              # <
    GREATER_EQUAL = "GREATER_EQUAL"  # >=
    LESS_EQUAL = "LESS_EQUAL"  # <=
    
    # 分隔符
    LPAREN = "LPAREN"          # (
    RPAREN = "RPAREN"          # )
    LBRACE = "LBRACE"          # {
    RBRACE = "RBRACE"          # }
    LBRACKET = "LBRACKET"      # [
    RBRACKET = "RBRACKET"      # ]
    COMMA = "COMMA"            # ,
    COLON = "COLON"            # :
    SEMICOLON = "SEMICOLON"    # ;
    
    # 特殊
    NEWLINE = "NEWLINE"        # 换行
    EOF = "EOF"                # 文件结束
    COMMENT = "COMMENT"        # 注释

class Token(NamedTuple):
    """Token数据结构"""
    type: TokenType
    value: str
    line: int
    column: int

class HangzhouLexer:
    """杭州话词法分析器"""
    
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def error(self, message: str) -> None:
        """抛出词法分析错误"""
        raise SyntaxError(f"词法分析错误 第{self.line}行第{self.column}列: {message}")
    
    def current_char(self) -> Optional[str]:
        """获取当前字符"""
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]
    
    def peek_char(self, offset: int = 1) -> Optional[str]:
        """向前查看字符"""
        peek_pos = self.pos + offset
        if peek_pos >= len(self.text):
            return None
        return self.text[peek_pos]
    
    def advance(self) -> None:
        """移动到下一个字符"""
        if self.pos < len(self.text):
            if self.text[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self) -> None:
        """跳过空白字符（除换行符外）"""
        while self.current_char() and self.current_char() in ' \t\r':
            self.advance()
    
    def read_string(self) -> str:
        """读取字符串字面量"""
        quote_char = self.current_char()  # " 或 '
        self.advance()  # 跳过开始的引号
        
        value = ""
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char():
                    # 处理转义字符
                    escape_chars = {
                        'n': '\n', 't': '\t', 'r': '\r', 
                        '\\': '\\', '"': '"', "'": "'"
                    }
                    value += escape_chars.get(self.current_char(), self.current_char())
                    self.advance()
            else:
                value += self.current_char()
                self.advance()
        
        if not self.current_char():
            self.error("字符串未正确结束")
        
        self.advance()  # 跳过结束的引号
        return value
    
    def read_number(self) -> str:
        """读取数字"""
        value = ""
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
            value += self.current_char()
            self.advance()
        
        return value
    
    def read_chinese_number(self) -> str:
        """读取中文数字"""
        value = ""
        while self.current_char() and self.current_char() in HANGZHOU_NUMBERS:
            value += self.current_char()
            self.advance()
        
        # 转换为阿拉伯数字
        result = ""
        for char in value:
            result += HANGZHOU_NUMBERS.get(char, char)
        
        return result
    
    def read_identifier(self) -> str:
        """读取标识符或关键字"""
        value = ""
        while (self.current_char() and 
               (self.current_char().isalnum() or 
                self.current_char() in '_' or 
                ord(self.current_char()) > 127)):  # 支持中文字符
            value += self.current_char()
            self.advance()
        
        return value
    
    def read_comment(self) -> str:
        """读取注释"""
        value = ""
        self.advance()  # 跳过 #
        
        while self.current_char() and self.current_char() != '\n':
            value += self.current_char()
            self.advance()
        
        return value.strip()
    
    def tokenize(self) -> List[Token]:
        """将输入文本转换为token列表"""
        while self.current_char():
            # 跳过空白字符
            if self.current_char() in ' \t\r':
                self.skip_whitespace()
                continue
            
            # 换行符
            if self.current_char() == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\n', self.line, self.column))
                self.advance()
                continue
            
            # 注释
            if self.current_char() == '#':
                comment = self.read_comment()
                self.tokens.append(Token(TokenType.COMMENT, comment, self.line, self.column))
                continue
            
            # 字符串
            if self.current_char() in '"\'':
                string_value = self.read_string()
                self.tokens.append(Token(TokenType.STRING, string_value, self.line, self.column))
                continue
            
            # 数字
            if self.current_char().isdigit():
                number = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, number, self.line, self.column))
                continue
            
            # 中文数字
            if self.current_char() in HANGZHOU_NUMBERS:
                chinese_number = self.read_chinese_number()
                self.tokens.append(Token(TokenType.NUMBER, chinese_number, self.line, self.column))
                continue
            
            # 双字符运算符
            two_char = self.current_char() + (self.peek_char() or '')
            if two_char == '==':
                self.tokens.append(Token(TokenType.EQUAL, '==', self.line, self.column))
                self.advance()
                self.advance()
                continue
            elif two_char == '!=':
                self.tokens.append(Token(TokenType.NOT_EQUAL, '!=', self.line, self.column))
                self.advance()
                self.advance()
                continue
            elif two_char == '>=':
                self.tokens.append(Token(TokenType.GREATER_EQUAL, '>=', self.line, self.column))
                self.advance()
                self.advance()
                continue
            elif two_char == '<=':
                self.tokens.append(Token(TokenType.LESS_EQUAL, '<=', self.line, self.column))
                self.advance()
                self.advance()
                continue
            
            # 单字符运算符和分隔符
            single_char_tokens = {
                '+': TokenType.PLUS,
                '-': TokenType.MINUS,
                '*': TokenType.MULTIPLY,
                '/': TokenType.DIVIDE,
                '=': TokenType.ASSIGN,
                '>': TokenType.GREATER,
                '<': TokenType.LESS,
                '(': TokenType.LPAREN,
                ')': TokenType.RPAREN,
                '{': TokenType.LBRACE,
                '}': TokenType.RBRACE,
                '[': TokenType.LBRACKET,
                ']': TokenType.RBRACKET,
                ',': TokenType.COMMA,
                ':': TokenType.COLON,
                '：': TokenType.COLON,  # 中文冒号
                ';': TokenType.SEMICOLON,
            }
            
            if self.current_char() in single_char_tokens:
                token_type = single_char_tokens[self.current_char()]
                self.tokens.append(Token(token_type, self.current_char(), self.line, self.column))
                self.advance()
                continue
            
            # 标识符和关键字（包括中文）
            if (self.current_char().isalpha() or 
                self.current_char() == '_' or 
                ord(self.current_char()) > 127):
                identifier = self.read_identifier()
                
                # 检查是否为杭州话关键字
                if is_hangzhou_keyword(identifier):
                    self.tokens.append(Token(TokenType.KEYWORD, identifier, self.line, self.column))
                else:
                    self.tokens.append(Token(TokenType.IDENTIFIER, identifier, self.line, self.column))
                continue
            
            # 未知字符
            self.error(f"未知字符: '{self.current_char()}'")
        
        # 添加EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens

def tokenize(text: str) -> List[Token]:
    """便捷函数：将文本转换为token列表"""
    lexer = HangzhouLexer(text)
    return lexer.tokenize() 