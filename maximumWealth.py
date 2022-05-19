from typing import List

'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money 
the i customer has in the j bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The 
richest customer is the customer that has the maximum wealth.
'''

def maximumWealth(accounts: List[List[int]]) -> int:
    maxWealth = 0
    for account in accounts:
        currentWealth = sum(account)
        if currentWealth > maxWealth:
            maxWealth = currentWealth
    return maxWealth

accounts = [[3, 4, 2], [2, 5, 3], [2, 1, 3], [5, 3, 5]]

print(maximumWealth(accounts))