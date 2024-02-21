'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
 
 '''


def lengthOfLastWord(s: str) -> int:
        count= 0 
        s = s.strip()
        #Iterating through a string in reverse 
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ": 
                count += 1
            else: 
                return count 
        return count 
    
print(lengthOfLastWord("Fly me to the moon "))