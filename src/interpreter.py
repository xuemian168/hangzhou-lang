# -*- coding: utf-8 -*-
"""
杭州话编程语言解释器核心
Hangzhou Dialect Programming Language Interpreter
"""

from typing import Any, Dict, List, Optional, Union
from parser import (
    ASTNode, Program, Statement, Expression,
    VarDeclaration, Assignment, PrintStatement, IfStatement, WhileStatement,
    FunctionDef, ReturnStatement, BinaryOp, UnaryOp, Literal, Identifier, FunctionCall
)
from keywords import HANGZHOU_KEYWORDS
import random
import time

class ReturnException(Exception):
    """用于函数返回的异常"""
    def __init__(self, value: Any):
        self.value = value

class HangzhouFunction:
    """杭州话函数对象"""
    def __init__(self, name: str, params: List[str], body: List[Statement], closure: Dict[str, Any]):
        self.name = name
        self.params = params
        self.body = body
        self.closure = closure

class Environment:
    """变量环境"""
    def __init__(self, parent: Optional['Environment'] = None):
        self.variables: Dict[str, Any] = {}
        self.parent = parent
    
    def define(self, name: str, value: Any) -> None:
        """定义变量"""
        self.variables[name] = value
    
    def get(self, name: str) -> Any:
        """获取变量值"""
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f"未定义的变量: {name}")
    
    def set(self, name: str, value: Any) -> None:
        """设置变量值"""
        if name in self.variables:
            self.variables[name] = value
        elif self.parent and self.parent.has(name):
            self.parent.set(name, value)
        else:
            self.variables[name] = value
    
    def has(self, name: str) -> bool:
        """检查变量是否存在"""
        return name in self.variables or (self.parent and self.parent.has(name))

class HangzhouInterpreter:
    """杭州话解释器"""
    
    def __init__(self):
        self.global_env = Environment()
        self.current_env = self.global_env
        self.output_buffer = []  # 用于存储输出
        
        # 内置函数
        self._setup_builtins()
        
        self._easter_egg_counter = 0
        self._secret_62_messages = [
            "哎呀，你这个62！",
            "62不62啊？",
            "格毛是个62！",
            "别太62了！",
            "这代码咋这么62呢？"
        ]
        # 新增十三点彩蛋消息
        self._secret_13_messages = [
            "哎呀，这代码怕是十三点啊！",
            "十三点不十三点？",
            "格毛的逻辑咋这么十三点？",
            "嫑整这么十三点的代码！",
            "这代码咋这么不拎清？"
        ]
    
    def _setup_builtins(self) -> None:
        """设置内置函数"""
        # 数学函数
        self.global_env.define('求根', lambda x: x ** 0.5)
        self.global_env.define('绝对值', lambda x: abs(x))
        self.global_env.define('向上取整', lambda x: int(x) + (1 if x > int(x) else 0))
        self.global_env.define('向下取整', lambda x: int(x))
        
        # 字符串函数
        self.global_env.define('长度', lambda x: len(x))
        self.global_env.define('大写', lambda x: str(x).upper())
        self.global_env.define('小写', lambda x: str(x).lower())
        
        # 类型检查
        self.global_env.define('是数字', lambda x: isinstance(x, (int, float)))
        self.global_env.define('是字符串', lambda x: isinstance(x, str))
        self.global_env.define('是布尔', lambda x: isinstance(x, bool))

        # 系统函数
        self.global_env.define('撒宽', self._builtin_sleep)      # sleep - 随意放松
        self.global_env.define('撒子儿', self._builtin_random)   # random - 玩耍/随机
    
    def _builtin_sleep(self, ms: Union[int, float]) -> None:
        """
        撒宽 - 休眠函数
        参数: ms - 毫秒数
        """
        if not isinstance(ms, (int, float)):
            raise TypeError("撒宽的参数必须是数字（毫秒）")
        time.sleep(ms / 1000)

    def _builtin_random(self, *args) -> Union[int, float]:
        """
        撒子儿 - 随机数函数
        用法:
          撒子儿()        -> 0到1之间的随机小数
          撒子儿(max)     -> 0到max之间的随机整数
          撒子儿(min,max) -> min到max之间的随机整数
        """
        if len(args) == 0:
            return random.random()
        elif len(args) == 1:
            return random.randint(0, int(args[0]))
        elif len(args) == 2:
            return random.randint(int(args[0]), int(args[1]))
        else:
            raise TypeError("撒子儿最多接受两个参数")

    def error(self, message: str) -> None:
        """抛出运行时错误"""
        raise RuntimeError(f"运行时错误: {message}")
    
    def interpret(self, program: Program) -> List[str]:
        """解释执行程序"""
        self.output_buffer = []
        
        try:
            for statement in program.statements:
                self.execute_statement(statement)
        except ReturnException as e:
            # 在全局作用域遇到return，忽略
            pass
        except Exception as e:
            self.output_buffer.append(f"错误: {str(e)}")
        
        return self.output_buffer
    
    def execute_statement(self, stmt: Statement) -> None:
        """执行语句"""
        if isinstance(stmt, VarDeclaration):
            self.execute_var_declaration(stmt)
        elif isinstance(stmt, Assignment):
            self.execute_assignment(stmt)
        elif isinstance(stmt, PrintStatement):
            self.execute_print_statement(stmt)
        elif isinstance(stmt, IfStatement):
            self.execute_if_statement(stmt)
        elif isinstance(stmt, WhileStatement):
            self.execute_while_statement(stmt)
        elif isinstance(stmt, FunctionDef):
            self.execute_function_def(stmt)
        elif isinstance(stmt, ReturnStatement):
            self.execute_return_statement(stmt)
        else:
            self.error(f"未知的语句类型: {type(stmt)}")
    
    def execute_var_declaration(self, stmt: VarDeclaration) -> None:
        """执行变量声明"""
        value = None
        if stmt.value:
            value = self.evaluate_expression(stmt.value)
        self.current_env.define(stmt.name, value)
    
    def execute_assignment(self, stmt: Assignment) -> None:
        """执行赋值语句"""
        value = self.evaluate_expression(stmt.value)
        self.current_env.set(stmt.name, value)
    
    def execute_print_statement(self, stmt: PrintStatement) -> None:
        """执行输出语句"""
        value = self.evaluate_expression(stmt.expression)
        output = self.stringify(value)
        self.output_buffer.append(output)
        print(output)  # 同时输出到控制台
    
    def execute_if_statement(self, stmt: IfStatement) -> None:
        """执行条件语句"""
        condition_value = self.evaluate_expression(stmt.condition)
        
        if self.is_truthy(condition_value):
            for statement in stmt.then_branch:
                self.execute_statement(statement)
        elif stmt.else_branch:
            for statement in stmt.else_branch:
                self.execute_statement(statement)
    
    def execute_while_statement(self, stmt: WhileStatement) -> None:
        """执行循环语句"""
        while True:
            condition_value = self.evaluate_expression(stmt.condition)
            if not self.is_truthy(condition_value):
                break
            
            for statement in stmt.body:
                self.execute_statement(statement)
    
    def execute_function_def(self, stmt: FunctionDef) -> None:
        """执行函数定义"""
        function = HangzhouFunction(stmt.name, stmt.params, stmt.body, dict(self.current_env.variables))
        self.current_env.define(stmt.name, function)
    
    def execute_return_statement(self, stmt: ReturnStatement) -> None:
        """执行返回语句"""
        value = None
        if stmt.value:
            value = self.evaluate_expression(stmt.value)
        raise ReturnException(value)
    
    def evaluate_expression(self, expr: Expression) -> Any:
        """求值表达式"""
        if isinstance(expr, Literal):
            return expr.value
        elif isinstance(expr, Identifier):
            return self.current_env.get(expr.name)
        elif isinstance(expr, BinaryOp):
            return self.evaluate_binary_op(expr)
        elif isinstance(expr, UnaryOp):
            return self.evaluate_unary_op(expr)
        elif isinstance(expr, FunctionCall):
            return self.evaluate_function_call(expr)
        else:
            self.error(f"未知的表达式类型: {type(expr)}")
    
    def evaluate_binary_op(self, expr: BinaryOp) -> Any:
        """求值二元运算"""
        left = self.evaluate_expression(expr.left)
        
        # 短路求值
        if expr.operator in ['还有', 'and']:
            if not self.is_truthy(left):
                return left
            return self.evaluate_expression(expr.right)
        elif expr.operator in ['要么', 'or']:
            if self.is_truthy(left):
                return left
            return self.evaluate_expression(expr.right)
        
        right = self.evaluate_expression(expr.right)
        
        # 算术运算
        if expr.operator in ['+', '加']:
            return left + right
        elif expr.operator in ['-', '减']:
            return left - right
        elif expr.operator in ['*', '乘']:
            return left * right
        elif expr.operator in ['/', '除']:
            if right == 0:
                self.error("除零错误")
            return left / right
        
        # 比较运算
        elif expr.operator in ['>', '大过']:
            return left > right
        elif expr.operator in ['<', '小过']:
            return left < right
        elif expr.operator in ['>=', '大等于']:
            return left >= right
        elif expr.operator in ['<=', '小等于']:
            return left <= right
        elif expr.operator in ['==', '等于']:
            return left == right
        elif expr.operator in ['!=', '不等']:
            return left != right
        
        else:
            self.error(f"未知的二元运算符: {expr.operator}")
    
    def evaluate_unary_op(self, expr: UnaryOp) -> Any:
        """求值一元运算"""
        operand = self.evaluate_expression(expr.operand)
        
        if expr.operator == '-':
            return -operand
        elif expr.operator in ['不是', 'not']:
            return not self.is_truthy(operand)
        else:
            self.error(f"未知的一元运算符: {expr.operator}")
    
    def evaluate_function_call(self, expr: FunctionCall) -> Any:
        """求值函数调用"""
        function = self.current_env.get(expr.name)
        
        # 求值参数
        args = [self.evaluate_expression(arg) for arg in expr.args]
        
        # 内置函数（Python函数）
        if callable(function) and not isinstance(function, HangzhouFunction):
            try:
                return function(*args)
            except Exception as e:
                self.error(f"调用内置函数 {expr.name} 时出错: {str(e)}")
        
        # 用户定义函数
        elif isinstance(function, HangzhouFunction):
            return self.call_user_function(function, args)
        
        else:
            self.error(f"{expr.name} 不是一个函数")
    
    def call_user_function(self, function: HangzhouFunction, args: List[Any]) -> Any:
        """调用用户定义的函数"""
        if len(args) != len(function.params):
            self.error(f"函数 {function.name} 期望 {len(function.params)} 个参数，但提供了 {len(args)} 个")
        
        # 创建新的环境
        function_env = Environment(self.current_env)
        
        # 绑定参数
        for param, arg in zip(function.params, args):
            function_env.define(param, arg)
        
        # 保存当前环境，切换到函数环境
        previous_env = self.current_env
        self.current_env = function_env
        
        try:
            # 执行函数体
            for statement in function.body:
                self.execute_statement(statement)
            
            # 如果没有显式返回，返回None
            return None
        
        except ReturnException as ret:
            return ret.value
        
        finally:
            # 恢复环境
            self.current_env = previous_env
    
    def is_truthy(self, value: Any) -> bool:
        """判断值的真假"""
        if value is None:
            return False
        elif isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            return value != 0
        elif isinstance(value, str):
            return len(value) > 0
        else:
            return True
    
    def stringify(self, value: Any) -> str:
        """将值转换为字符串"""
        if value is None:
            return "空的"
        elif isinstance(value, bool):
            return "真的" if value else "假的"
        elif isinstance(value, str):
            return value
        else:
            return str(value)

    def _check_62_easter_egg(self):
        """
        62彩蛋：随机触发有趣的杭州话提示
        """
        self._easter_egg_counter += 1
        if self._easter_egg_counter % 62 == 0:
            # 每62次操作触发一次彩蛋
            message = random.choice(self._secret_62_messages)
            print(f"\n🥚 [62彩蛋] {message}")

    def _check_13_easter_egg(self):
        """
        十三点彩蛋：随机触发有趣的杭州话提示
        """
        if random.random() < 0.13:  # 13%的概率触发
            message = random.choice(self._secret_13_messages)
            print(f"\n🥚 [十三点彩蛋] {message}")

    def execute(self, ast):
        """
        执行抽象语法树
        """
        self._check_62_easter_egg()
        self._check_13_easter_egg()  # 添加十三点彩蛋检查
        # 原有的执行逻辑
        ...

def interpret(program: Program) -> List[str]:
    """便捷函数：解释执行程序"""
    interpreter = HangzhouInterpreter()
    return interpreter.interpret(program)

def interpret_text(text: str) -> List[str]:
    """便捷函数：解释执行文本"""
    from parser import parse_text
    program = parse_text(text)
    return interpret(program) 