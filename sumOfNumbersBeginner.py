def get_sum(a,b):
    if a == b: return a 
    sum = 0 
    if a < b: 
        for i in range(a, b + 1):
            sum += i 
        return sum 
    if b < a: 
        for i in range(b, a + 1):
            sum += i 
        return sum 
    
print(get_sum(3, 6))