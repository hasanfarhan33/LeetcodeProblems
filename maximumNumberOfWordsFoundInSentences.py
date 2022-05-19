from typing import List

'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
'''

def mostWordsFound(sentences: List[str]) -> int:
    maxWordCount = 0
    for sentence in sentences:
        currentWordCount = len(sentence.split(" "))
        if currentWordCount > maxWordCount:
            maxWordCount = currentWordCount
    return maxWordCount

def mostWordsFound1(sentences: List[str]) -> int:
    return(max(len(sentence.split(' ')) for sentence in sentences))

sentences = ["please wait", "continue to fight", "continue to win", "there must be a better way to solve this problem"]

print(mostWordsFound(sentences))
print(mostWordsFound1(sentences))