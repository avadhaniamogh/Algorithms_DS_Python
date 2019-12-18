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

def valid_parenthesis_count(str):
    count1 = 0
    count2 = 0
    count3 = 0
    for c in str:
        if c == '(':
            count1 += 1
        if c == '{':
            count2 += 1
        if c == '[':
            count3 += 1
        if c == ')':
            if count1 == 0: return False
            count1 -= 1
        if c == '}':
            if count2 == 0: return False
            count2 -= 1
        if c == ']':
            if count3 == 0: return False
            count3 -= 1

    print count1, count2, count3
    return count1 == 0 and count2 == 0 and count3 == 0




str = "[{{}}]"
print valid_parenthesis_count(str)
