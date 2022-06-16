'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would
 always evaluate to a result, and there will not be any division by zero operation.
'''
from typing import List

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())
        elif c == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == '*':
            stack.append(stack.pop() + stack.pop())
        elif c == '/':
            a,b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[-1]


print(evalRPN(tokens))