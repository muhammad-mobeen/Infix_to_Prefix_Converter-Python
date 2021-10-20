from collections import deque              # Importing deque


class Stack:                               # Initiating stack class
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


def infix_to_prefix(exp):                                   # Function for infix to prefix conversion
    operand = Stack()       # stack for operators.
    operator = Stack()      # stack for operands.
    precedence = {'^': 5,'*': 4,'/': 4,'+': 3,'-': 3,'(': 2,')': 1}
    # Loop for itterating through expression
    for c in exp:
        # If current character is an
        # opening bracket, then
        # push into the operators stack.
        if c == '(':
            operator.push(c)

        # If current character is a
        # closing bracket, then pop from
        # both stacks and push result
        # in operands stack until
        # matching opening bracket is
        # not found.
        elif c == ')':
            while operator.size() != 0 and operator.top() != '(':
                op1 = operand.pop()
                op2 = operand.pop()
                opr = operator.pop()
                tmp = opr + op2 + op1
                operand.push(tmp)

            # Pop opening bracket from stack.
            operator.pop()

        # If current character is an
        # operand then push it into
        # operands stack.
        elif c.isalpha() or c in '1234567890':
            operand.push(c)

        # If current character is an
        # operator, then push it into
        # operators stack after popping
        # high priority operators from
        # operators stack and pushing
        # result in operands stack.
        elif c in '+-*/':
            while operator.size() != 0 and precedence.get(c) <= precedence.get(operator.top()):
                op1 = operand.pop()
                op2 = operand.pop()
                opr = operator.pop()
                tmp = opr + op2 + op1
                operand.push(tmp)
            operator.push(c)
        else:
            print("Error: Wrong expression!")

    # If current character is an
    # operator, then push it into
    # operators stack after popping
    # high priority operators from
    # operators stack and pushing
    # result in operands stack.
    while operator.size() != 0:
        op1 = operand.pop()
        op2 = operand.pop()
        opr = operator.pop()
        tmp = opr + op2 + op1
        operand.push(tmp)
    # Final prefix expression is
    # present in operands stack.
    return operand.top()

# Calling function and pasrsing our expresion for conversion:-
print(infix_to_prefix("c*a+b"))