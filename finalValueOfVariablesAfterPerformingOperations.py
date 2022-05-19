from typing import List

'''
There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final 
value of X after performing all the operations.
'''

def finalValueAfterOperations(operations: List[str]) -> int:
    res = 0
    for operation in operations:
        if operation.__contains__("+"):
            res += 1
        elif operation.__contains__("-"):
            res -= 1
    return res

def finalValueAfterOperations1(operations: List[str]) -> int:
    return sum(-1 if i in "--X--" else 1 for i in operations)

operations = ["X++","++X","--X","X--"]

print(finalValueAfterOperations(operations))
print(finalValueAfterOperations1(operations))