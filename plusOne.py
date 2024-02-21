
'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 

The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
from typing import List 

def plusOne(digits: List[int]) -> List[int]: 
    digits = map(str, digits)
    digits = "".join(digits)
    digits = int(digits) 
    
    digits += 1 
    
    digits = str(digits)
    digits = list(digits)
    digits = [int(num) for num in digits]
    
    print(digits)
    
def plusOneBetter(digits: List[int]) -> List[int]:
    # Iterating through an array in reverse
    for i in range(len(digits) -1, -1, -1):
        if digits[i] == 9: 
            digits[i] = 0 
        else: 
            digits[i] = digits[i] + 1 
            return digits 
    return [1] + digits 
     
print(plusOneBetter([1,2,9]))
    