'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

# Solution with additional data structures 
def isUnique(string) -> bool: 
    visited = set() 
    for c in string: 
        if c in visited: 
            return False 
        else: 
            visited.add(c)
    return True 

# Solution without additional data structures 
def isUnique_ascii(string) -> bool: 
    if len(string) > 128: 
        return False 
    
    char_set = [False for _ in range(128)]
    
    for c in string: 
        val = ord(c) 
        if char_set[val]: 
            return False 
        else: 
            char_set[val] = True 
    return True 

testString = "shame"

print(isUnique_ascii(testString))