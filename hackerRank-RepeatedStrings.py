'''
There is a string s, of lowercase English letters that is repeated infinitely many times. Given an integer n, 
find and print the number of letter a's in the first  letters of the infinite string.
'''
# This leads to memory error 
def repeatedString(s: str, n: int): 
    while len(s) < n: 
        s += s 
    
    aCount = 0
    for i in range(n): 
        if s[i] == "a": 
            aCount += 1 
    return aCount 

def repeatedStringNoMem(s: str, n: int): 
    numOfPasses = 0 
    aCount = 0 
    while numOfPasses < n: 
        for c in s: 
            if c == "a": 
                aCount += 1
        numOfPasses += len(s)
    return aCount 

string = "abcac"
n = 10 

print(repeatedStringNoMem(string, n))