'''
LEETCODE 1137: N-th Tribonacci Number
'''

def tribonacci(n: int) -> int: 
    prev_trib = [0] * n
    for i in range(n): 
        if i == 0: 
            prev_trib[i] = 0 
        elif i == 1: 
            prev_trib[i] = 1
        elif i == 2: 
            prev_trib[i] = 1 
        else:
            prev_trib[i] = prev_trib[i-1] + prev_trib[i-2] + prev_trib[i-3]
    
    nth_trib = prev_trib[n - 1] + prev_trib[n - 2] + prev_trib[n - 3]
    return nth_trib

n = 4 
print(tribonacci(n))