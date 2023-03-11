import sys

# Define a stack class


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Tokenize the arithmetic expression


def tokenize(expr):
    for p in ['(', ')']:
        expr = expr.replace(p, f' {p} ')
    return expr.split()

# Evaluate the arithmetic expression


def evaluate(expr):
    stack = Stack()
    for token in reversed(tokenize(expr)):
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                stack.push(op1 / op2)
    return stack.pop()


# Get the arithmetic expression from the command line argument
expression = sys.argv[1]
if expression.startswith("'") and expression.endswith("'"):
    expression = expression[1:-1]


# Evaluate the arithmetic expression and print the result
result = evaluate(expression)
print(result)
