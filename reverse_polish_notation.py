def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            op2 = stack.pop()
            op1 = stack.pop()
            if token == "+":
                stack.append(op1 + op2)
            elif token == "-":
                stack.append(op1 - op2)
            elif token == "*":
                stack.append(op1 * op2)
            elif token == "/":
                stack.append(int(op1 / op2))
        else:
            stack.append(int(token))
    return stack[-1]
