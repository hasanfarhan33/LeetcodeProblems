'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with 
matching colors there are.
'''

def sockMerchant(n, ar): 
    sockDict = dict() 
    for sock in ar: 
        sockDict[sock] = sockDict.get(sock, 0) + 1 
    
    # Iterate through the dictionary 
    numOfPairs = 0 
    for (sock, nums) in sockDict.items(): 
        numOfPairs += int(nums // 2)
    print(numOfPairs)

sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])