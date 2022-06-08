'''
You live in the city of Cartesia where all roads are laid out in a
perfect grid. You arrived ten minutes too early to an appointment,
so you decided to take the opportunity to go for a short walk.

The city provides its citizens with a Walk Generating App on their
phones -- everytime you press the button it sends you an array of
one-letter strings representing directions to walk
(eg. ['n', 's', 'w', 'e']). You always walk only a single
block for each letter (direction) and you know it takes you
one minute to traverse one city block, so create a function that
will return true if the walk the app gives you will take you exactly
ten minutes (you don't want to be early or late!) and will,
of course, return you to your starting point.
Return false otherwise.
'''

from typing import List
walk =  ['w', 'w', 'n', 'w', 'e', 'e', 'e', 's', 'e', 'w']

def validWalk(walk: List[int]) -> bool:
    if len(walk) != 10:
        return False
    else:
        stack = []
        for i in range(len(walk)):
            if len(stack) == 0:
                stack.append(walk[i])
            else:
                if(walk[i] == 'n' and stack[-1] == 's') or (walk[i] == 's' and stack[-1] == 'n'):
                    stack.pop()
                elif(walk[i] == 'w' and stack[-1] == 'e') or (walk[i] == 'e' and stack[-1] == 'w'):
                    stack.pop()
                else:
                    stack.append(walk[i])
        if len(stack) != 0:
            return False
        else:
            return True

def validWalkBetterSolution(walk: List[int]) -> bool:
    if len(walk) != 10:
        return False
    else:
        if(walk.count('n') == walk.count('s')) and (walk.count('e') == walk.count('w')):
            return True
        else:
            return False

def validWalkDirectionSolution(walk: List[int]) -> bool:
    if len(walk) != 10:
        return False
    x, y = 0, 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y-=1
        elif direction == 'w':
            x+=1
        elif direction == 'e':
            x-=1
    if x == y == 0:
        return True
    else:
        return False 





print(validWalk(walk))
print(validWalkBetterSolution(walk))