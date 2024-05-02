'''
LEETCODE 2413: Smallest Even Multiple 
'''

def smallestEvenMultiple(n: int) -> int: 
    for num in range(n, (n * 2) + 1): 
        if num % 2 == 0 and num % n == 0: 
            return num 

n = 5

print(smallestEvenMultiple(n))