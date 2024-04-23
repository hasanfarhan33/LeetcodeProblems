'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
'''

def urlify(input: str) -> str: 
    stringBuilder = ""
    stringToAdd = "%20" 
    for c in input: 
        if c != " ": 
            stringBuilder += c 
        else: 
            stringBuilder += stringToAdd 
    return stringBuilder 

# Solution without extra variable 
'''
Start at the end    
'''

testString = "Mr John Smith"

print(urlify(testString, 13)) 