'''
https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

'''

def find_nb(m): 
    cube_count = 1
    check = 0 
    while check <= m: 
        check += cube_count ** 3 
        if check == m: return cube_count
        cube_count += 1 
    return -1

print(find_nb(1071225))