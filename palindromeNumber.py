x = 121121
# print(len(str(x)))
def reversingNumber(numberToReverse):
    reversedNumber = 0
    while numberToReverse > 0:
        a = numberToReverse % 10
        reversedNumber = reversedNumber * 10 + a
        numberToReverse = numberToReverse // 10
    return reversedNumber

def checkPalindrome(x):
    if x <= 0 or len(str(x)) <= 2:
        return False
    reversedResult = reversingNumber(x)
    if reversedResult == x:
        return True
    else:
        return False

print(checkPalindrome(x))

# ANOTHER SOLUTION
def isPalindrome(x) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10
    return True if (x == result or x == result // 10) else False
