# Check for valid parenthesis in the input

def valid_parenthesis(str):
    stack = []
    for c in str:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == ')' or c == '}' or c == ']':
            if len(stack) > 0:
                popped = stack.pop()
                if popped != c:
                    return False
            else:
                return False
    return len(stack) == 0


str = "{}[]as"
print valid_parenthesis(str)
