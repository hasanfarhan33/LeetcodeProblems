'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
'''

s = 'ab#c'
t = 'ad#c'

def backspaceCompare(s:str, t:str):
    s = list(s)
    t = list(t)
    for i in range(len(s)):
        if s[i] == '#':
            s.pop(i-1)
            s.pop(i)
    for j in range(len(t)):
        if t[j] == '#':
            t.pop(j-1)
            t.pop(j)
    if s == t:
        return True
    return False


def backspaceCompareLeetcodeSolution(s:str, t:str):
    i, j = len(s) - 1, len(t) - 1
    backS = backT = 0
    while True:
        while i >= 0 and (backS or s[i] == '#'):
            backS += 1 if s[i] == '#' else -1
            i -= 1
        while j >= 0 and (backT or t[j] == '#'):
            backT += 1 if t[j] == '#' else -1
            j -= 1
        if not (i >= 0 and j >= 0 and s[i] == t[j]):
            return i == j == -1
        i, j = i - 1, j - 1



print(backspaceCompare(s, t))