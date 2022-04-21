testCases = ["A man, a plan, a canal: Panama", "race a car", " "]

def validPalindrome(string : str):
    string = ''.join(e for e in string.lower() if e.isalnum())
    if string.isspace():
        return True
    if len(string) == 1:
        return True

    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i, j = i + 1, j -1
    return True


for testCase in testCases:
    print(validPalindrome(testCase))