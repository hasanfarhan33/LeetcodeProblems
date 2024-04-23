'''
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
'''

s = "hello"

def scoreOfString(s: str) -> int: 
    score = 0 
    stringLen = len(s)
    
    for i in range(stringLen - 1): 
        score += abs(ord(s[i]) - ord(s[i+1]))
        
    return score 

print(scoreOfString(s))