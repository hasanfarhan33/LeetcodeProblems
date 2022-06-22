'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are
represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    * You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the
      amount of fruit each basket can hold.
    * Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree)
      while moving to the right. The picked fruits must fit in one of your baskets.
    * Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.
'''
from typing import List
fruits = [1, 2, 1]

def totalFruits(fruits:List[int]) -> int:
    left = 0
    pickedFruits = {}

    for right, fruit in enumerate(fruits):
        pickedFruits[fruit] = 1 + pickedFruits.get(fruit, 0)
        if(len(pickedFruits) > 2):
            pickedFruits[fruits[left]] -= 1
            if pickedFruits[fruits[left]] == 0: del pickedFruits[fruits[left]]
            left += 1
    return right - left + 1

print(totalFruits(fruits))



