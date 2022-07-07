'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

'''

x = 'man i need a taxi up to ubud'

def high(x:str)->str:
    highestScore = 0
    maxWord = ""
    for word in x.split(' '):
        curScore = 0
        for c in word:
            curScore += ((ord(c)-ord('a')) + 1)
        if curScore > highestScore:
            highestScore = curScore
            maxWord = word
    return maxWord

print(high(x))