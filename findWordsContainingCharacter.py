'''
LEETCODE 2942
'''

from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]: 
    output = [] 
    for i in range(len(words)): 
        if x in words[i]: 
            output.append(i)
    return output

words = ["leet", "code"]
x = "e"