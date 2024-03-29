
def addBinary(a:str, b:str) -> str:
    res = ""
    carry = 0 
    
    # Reversing the numbers
    a, b = a[::-1], b[::-1]
    
    # a and b are not the same length 
    for i in range(max(len(a), len(b))):
        digitA = int(a[i]) if i < len(a) else 0 
        digitB = int(b[i]) if i < len(b) else 0 
        
        total = digitA + digitB + carry 
        char = str(total % 2)
        res = char + res 
        carry = total // 2 
        
    if carry: 
        res = "1" + res 
    return res

print(addBinary("11", "1"))