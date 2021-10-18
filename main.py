from collections import deque


class Stack:
    def __init__(self) -> None:
        self.control = deque()

    def push(self, val):
        self.control.append(val)

    def pop(self):
        if len(self.control) == 0:
            return 0
        else:
            return self.control.pop()

    def top(self):
        if len(self.control) == 0:
            return 0
        else:
            return self.control[-1]

    def size(self):
        return len(self.control)
    
    def is_empty(self):
        return len(self.control) == 0


def infix_to_prefix(exp):
    operand = Stack()
    operator = Stack()
    precedence = {'^': 5,'*': 4,'/': 4,'+': 3,'-': 3,'(': 2,')': 1}
    for c in exp:
        if c == '(':
            operator.push(c)
        elif c == ')':
            while operator.size() != 0 and operator.top() != '(':
                op1 = operand.pop()
                op2 = operand.pop()
                opr = operator.pop()
                tmp = opr + op2 + op1
                operand.push(tmp)
            operator.pop()
        elif c.isalpha() or c in '1234567890':
            operand.push(c)
        elif c in '+-*/':
            while operator.size() != 0 and precedence.get(c) <= precedence.get(operator.top()):
                op1 = operand.pop()
                op2 = operand.pop()
                opr = operator.pop()
                tmp = opr + op2 + op1
                operand.push(tmp)
            operator.push(c)
    while operator.size() != 0:
        op1 = operand.pop()
        op2 = operand.pop()
        opr = operator.pop()
        tmp = opr + op2 + op1
        operand.push(tmp)
    return operand.top()


s = "c*a+b"
print(infix_to_prefix(s))