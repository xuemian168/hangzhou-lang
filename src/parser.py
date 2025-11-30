# -*- coding: utf-8 -*-
"""
杭州话编程语言语法分析器
Hangzhou Dialect Programming Language Parser
"""

from typing import List, Optional, Union, Any
from lexer import Token, TokenType, tokenize
from keywords import get_python_keyword, HANGZHOU_KEYWORDS

class ASTNode:
    """抽象语法树节点基类"""
    pass

class Program(ASTNode):
    """程序根节点"""
    def __init__(self, statements: List[ASTNode]):
        self.statements = statements

class Statement(ASTNode):
    """语句基类"""
    pass

class Expression(ASTNode):
    """表达式基类"""
    pass

class VarDeclaration(Statement):
    """变量声明语句"""
    def __init__(self, name: str, value: Optional[Expression] = None):
        self.name = name
        self.value = value

class Assignment(Statement):
    """赋值语句"""
    def __init__(self, name: str, value: Expression):
        self.name = name
        self.value = value

class PrintStatement(Statement):
    """输出语句"""
    def __init__(self, expression: Expression):
        self.expression = expression

class IfStatement(Statement):
    """条件语句"""
    def __init__(self, condition: Expression, then_branch: List[Statement], 
                 else_branch: Optional[List[Statement]] = None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileStatement(Statement):
    """循环语句"""
    def __init__(self, condition: Expression, body: List[Statement]):
        self.condition = condition
        self.body = body

class FunctionDef(Statement):
    """函数定义语句"""
    def __init__(self, name: str, params: List[str], body: List[Statement]):
        self.name = name
        self.params = params
        self.body = body

class ReturnStatement(Statement):
    """返回语句"""
    def __init__(self, value: Optional[Expression] = None):
        self.value = value

class BinaryOp(Expression):
    """二元运算表达式"""
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

class UnaryOp(Expression):
    """一元运算表达式"""
    def __init__(self, operator: str, operand: Expression):
        self.operator = operator
        self.operand = operand

class Literal(Expression):
    """字面量表达式"""
    def __init__(self, value: Union[str, int, float, bool]):
        self.value = value

class Identifier(Expression):
    """标识符表达式"""
    def __init__(self, name: str):
        self.name = name

class FunctionCall(Expression):
    """函数调用表达式"""
    def __init__(self, name: str, args: List[Expression]):
        self.name = name
        self.args = args

class HangzhouParser:
    """杭州话语法分析器"""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def error(self, message: str) -> None:
        """抛出语法分析错误"""
        if self.current_token:
            raise SyntaxError(f"语法分析错误 第{self.current_token.line}行: {message}")
        else:
            raise SyntaxError(f"语法分析错误: {message}")
    
    def advance(self) -> None:
        """移动到下一个token"""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None
    
    def match(self, token_type: TokenType) -> bool:
        """检查当前token是否匹配指定类型"""
        return self.current_token and self.current_token.type == token_type
    
    def consume(self, token_type: TokenType, message: str = "") -> Token:
        """消费指定类型的token"""
        if self.match(token_type):
            token = self.current_token
            self.advance()
            return token
        else:
            self.error(message or f"期望 {token_type}, 但得到 {self.current_token.type if self.current_token else 'EOF'}")
    
    def skip_newlines(self) -> None:
        """跳过换行符"""
        while self.match(TokenType.NEWLINE):
            self.advance()
    
    def parse(self) -> Program:
        """解析整个程序"""
        statements = []
        self.skip_newlines()
        
        while self.current_token and not self.match(TokenType.EOF):
            if self.match(TokenType.COMMENT):
                self.advance()
                continue
            
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
            self.skip_newlines()
        
        return Program(statements)
    
    def parse_statement(self) -> Optional[Statement]:
        """解析语句"""
        if not self.current_token:
            return None
        
        # 变量声明：老倌 name 装 value
        if self.match(TokenType.KEYWORD) and self.current_token.value == '老倌':
            return self.parse_var_declaration()
        
        # 输出语句：话说 expression
        elif self.match(TokenType.KEYWORD) and self.current_token.value == '话说':
            return self.parse_print_statement()
        
        # 条件语句：特为/要是 condition
        elif self.match(TokenType.KEYWORD) and self.current_token.value in ['特为', '要是']:
            return self.parse_if_statement()
        
        # 循环语句：一息息 condition
        elif self.match(TokenType.KEYWORD) and self.current_token.value == '一息息':
            return self.parse_while_statement()
        
        # 函数定义：会做事/做事体/介个套 name(params)
        elif self.match(TokenType.KEYWORD) and self.current_token.value in ['会做事', '做事体', '介个套']:
            return self.parse_function_def()
        
        # 返回语句：有数 expression
        elif self.match(TokenType.KEYWORD) and self.current_token.value == '有数':
            return self.parse_return_statement()
        
        # 赋值语句：identifier 装 value
        elif self.match(TokenType.IDENTIFIER):
            return self.parse_assignment_or_expression()
        
        else:
            # 跳过未知token
            self.advance()
            return None
    
    def parse_var_declaration(self) -> VarDeclaration:
        """解析变量声明"""
        self.consume(TokenType.KEYWORD)  # 消费 '老倌'
        name_token = self.consume(TokenType.IDENTIFIER, "期望变量名")
        
        value = None
        if self.match(TokenType.KEYWORD) and self.current_token.value == '装':
            self.advance()  # 消费 '装'
            value = self.parse_expression()
        
        return VarDeclaration(name_token.value, value)
    
    def parse_assignment_or_expression(self) -> Statement:
        """解析赋值语句或表达式语句"""
        name_token = self.consume(TokenType.IDENTIFIER)
        
        if self.match(TokenType.KEYWORD) and self.current_token.value == '装':
            self.advance()  # 消费 '装'
            value = self.parse_expression()
            return Assignment(name_token.value, value)
        else:
            # 这是一个表达式语句，暂时忽略
            return None
    
    def parse_print_statement(self) -> PrintStatement:
        """解析输出语句"""
        self.consume(TokenType.KEYWORD)  # 消费 '话说'
        
        # 可选的冒号
        if self.match(TokenType.COLON):
            self.advance()
        
        expression = self.parse_expression()
        return PrintStatement(expression)
    
    def parse_if_statement(self) -> IfStatement:
        """解析条件语句"""
        self.consume(TokenType.KEYWORD)  # 消费 '特为' 或 '要是'
        condition = self.parse_expression()
        
        self.consume(TokenType.COLON, "期望 ':'")
        self.skip_newlines()
        
        then_branch = []
        while (self.current_token and 
               not (self.match(TokenType.KEYWORD) and self.current_token.value in ['不然', 'EOF'])):
            stmt = self.parse_statement()
            if stmt:
                then_branch.append(stmt)
            self.skip_newlines()
        
        else_branch = None
        if self.match(TokenType.KEYWORD) and self.current_token.value == '不然':
            self.advance()  # 消费 '不然'
            self.consume(TokenType.COLON, "期望 ':'")
            self.skip_newlines()
            
            else_branch = []
            while (self.current_token and 
                   not self.match(TokenType.EOF)):
                stmt = self.parse_statement()
                if stmt:
                    else_branch.append(stmt)
                self.skip_newlines()
        
        return IfStatement(condition, then_branch, else_branch)
    
    def parse_while_statement(self) -> WhileStatement:
        """解析循环语句"""
        self.consume(TokenType.KEYWORD)  # 消费 '一息息'
        condition = self.parse_expression()
        
        self.consume(TokenType.COLON, "期望 ':'")
        self.skip_newlines()
        
        body = []
        while (self.current_token and not self.match(TokenType.EOF)):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
            self.skip_newlines()
        
        return WhileStatement(condition, body)
    
    def parse_function_def(self) -> FunctionDef:
        """解析函数定义"""
        self.consume(TokenType.KEYWORD)  # 消费 '会做事'
        name_token = self.consume(TokenType.IDENTIFIER, "期望函数名")
        
        self.consume(TokenType.LPAREN, "期望 '('")
        
        params = []
        while not self.match(TokenType.RPAREN):
            if self.match(TokenType.KEYWORD) and self.current_token.value == '老倌':
                self.advance()  # 消费 '老倌'
            
            param_token = self.consume(TokenType.IDENTIFIER, "期望参数名")
            params.append(param_token.value)
            
            if self.match(TokenType.COMMA):
                self.advance()
        
        self.consume(TokenType.RPAREN, "期望 ')'")
        self.consume(TokenType.COLON, "期望 ':'")
        self.skip_newlines()
        
        body = []
        while (self.current_token and not self.match(TokenType.EOF)):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
            self.skip_newlines()
        
        return FunctionDef(name_token.value, params, body)
    
    def parse_return_statement(self) -> ReturnStatement:
        """解析返回语句"""
        self.consume(TokenType.KEYWORD)  # 消费 '有数'
        
        value = None
        if not self.match(TokenType.NEWLINE) and not self.match(TokenType.EOF):
            value = self.parse_expression()
        
        return ReturnStatement(value)
    
    def parse_expression(self) -> Expression:
        """解析表达式"""
        return self.parse_logical_or()
    
    def parse_logical_or(self) -> Expression:
        """解析逻辑或表达式"""
        expr = self.parse_logical_and()
        
        while (self.match(TokenType.KEYWORD) and 
               self.current_token.value == '要么'):
            operator = self.current_token.value
            self.advance()
            right = self.parse_logical_and()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_logical_and(self) -> Expression:
        """解析逻辑与表达式"""
        expr = self.parse_equality()
        
        while (self.match(TokenType.KEYWORD) and 
               self.current_token.value == '还有'):
            operator = self.current_token.value
            self.advance()
            right = self.parse_equality()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_equality(self) -> Expression:
        """解析等式表达式"""
        expr = self.parse_comparison()
        
        while self.match(TokenType.EQUAL) or self.match(TokenType.NOT_EQUAL):
            operator = self.current_token.value
            self.advance()
            right = self.parse_comparison()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_comparison(self) -> Expression:
        """解析比较表达式"""
        expr = self.parse_addition()
        
        while (self.match(TokenType.GREATER) or self.match(TokenType.LESS) or
               self.match(TokenType.GREATER_EQUAL) or self.match(TokenType.LESS_EQUAL) or
               (self.match(TokenType.KEYWORD) and self.current_token.value in ['大过', '小过', '大等于', '小等于'])):
            operator = self.current_token.value
            self.advance()
            right = self.parse_addition()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_addition(self) -> Expression:
        """解析加减表达式"""
        expr = self.parse_multiplication()
        
        while (self.match(TokenType.PLUS) or self.match(TokenType.MINUS) or
               (self.match(TokenType.KEYWORD) and self.current_token.value in ['加', '减'])):
            operator = self.current_token.value
            self.advance()
            right = self.parse_multiplication()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_multiplication(self) -> Expression:
        """解析乘除表达式"""
        expr = self.parse_unary()
        
        while (self.match(TokenType.MULTIPLY) or self.match(TokenType.DIVIDE) or
               (self.match(TokenType.KEYWORD) and self.current_token.value in ['乘', '除'])):
            operator = self.current_token.value
            self.advance()
            right = self.parse_unary()
            expr = BinaryOp(expr, operator, right)
        
        return expr
    
    def parse_unary(self) -> Expression:
        """解析一元表达式"""
        if (self.match(TokenType.MINUS) or
            (self.match(TokenType.KEYWORD) and self.current_token.value == '不是')):
            operator = self.current_token.value
            self.advance()
            expr = self.parse_unary()
            return UnaryOp(operator, expr)
        
        return self.parse_primary()
    
    def parse_primary(self) -> Expression:
        """解析基本表达式"""
        # 数字字面量
        if self.match(TokenType.NUMBER):
            value = float(self.current_token.value) if '.' in self.current_token.value else int(self.current_token.value)
            self.advance()
            return Literal(value)
        
        # 字符串字面量
        if self.match(TokenType.STRING):
            value = self.current_token.value
            self.advance()
            return Literal(value)
        
        # 布尔值
        if self.match(TokenType.KEYWORD) and self.current_token.value in ['真的', '假的']:
            value = self.current_token.value == '真的'
            self.advance()
            return Literal(value)
        
        # None值
        if self.match(TokenType.KEYWORD) and self.current_token.value == '空的':
            self.advance()
            return Literal(None)
        
        # 标识符或函数调用
        if self.match(TokenType.IDENTIFIER):
            name = self.current_token.value
            self.advance()
            
            # 函数调用
            if self.match(TokenType.LPAREN):
                self.advance()  # 消费 '('
                
                args = []
                while not self.match(TokenType.RPAREN):
                    args.append(self.parse_expression())
                    if self.match(TokenType.COMMA):
                        self.advance()
                
                self.consume(TokenType.RPAREN, "期望 ')'")
                return FunctionCall(name, args)
            else:
                return Identifier(name)
        
        # 括号表达式
        if self.match(TokenType.LPAREN):
            self.advance()  # 消费 '('
            expr = self.parse_expression()
            self.consume(TokenType.RPAREN, "期望 ')'")
            return expr
        
        self.error("期望表达式")

def parse(tokens: List[Token]) -> Program:
    """便捷函数：将token列表解析为AST"""
    parser = HangzhouParser(tokens)
    return parser.parse()

def parse_text(text: str) -> Program:
    """便捷函数：将文本解析为AST"""
    tokens = tokenize(text)
    return parse(tokens) 