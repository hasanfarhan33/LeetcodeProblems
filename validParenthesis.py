s = "{}[]()"
s1 = "["


def validParenthesis(s:str):
    stack = []
    for i, c in enumerate(s):
        if c =='(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if c == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

            elif c == '}':
                if stack:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

            elif c == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False

    if not stack:
        return True
    else:
        return False


def validParenthesisWithoutStack(s:str):
    res = 0
    for i, c in enumerate(s):
        if c == '(':
            res+=1
        elif c=='[':
            res+=2
        elif c=='{':
            res+=3
        elif c==')':
            res-=1
        elif c==']':
            res-=2
        elif c=='}':
            res-=3
    if res == 0:
        return True
    else:
        return False


def validParenthesisWithHash(s):
    stack = []
    brackets = {')':'(',
                '}':'{',
                ']':'['}
    for c in s:
        if c in brackets:
            if not stack:
                return False
            elif stack and stack[-1] == brackets[c]:
                stack.pop()
        else:
            stack.append(c)
    return True if not stack else False

print(validParenthesisWithHash(s))