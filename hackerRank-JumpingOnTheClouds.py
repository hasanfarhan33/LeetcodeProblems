'''
There is a new mobile game that starts with consecutively numbered clouds. 

Some of the clouds are thunderheads and others are cumulus. 

The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 

The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion 
to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.
'''

def jumpingOnClouds(cloudArray): 
    jumpCount = 0
    curIndex = 0
    curCloud = cloudArray[curIndex]
    nextCloud = curIndex + 1
    nextNextCloud = curIndex + 2
    
    while nextNextCloud < len(cloudArray): 
        if cloudArray[nextCloud] == 1 and cloudArray[nextNextCloud] == 0: 
            jumpCount += 1 
            curIndex = nextNextCloud
            nextCloud, nextNextCloud = curIndex + 1, curIndex + 2  
        elif cloudArray[nextCloud] == 0 and cloudArray[nextNextCloud] == 1: 
            jumpCount += 1 
            curIndex = nextCloud 
            nextCloud, nextNextCloud = curIndex + 1, curIndex + 2 
        elif cloudArray[nextCloud] == 0 and cloudArray[nextNextCloud] == 0: 
            jumpCount += 1 
            curIndex = nextNextCloud 
            nextCloud, nextNextCloud = curIndex + 1, curIndex + 2 
    
    if nextCloud < len(cloudArray) and cloudArray[nextCloud] == 0: 
        jumpCount += 1
    
    return jumpCount
        

cArray = [0, 1, 0, 0, 0, 1, 0]

print(jumpingOnClouds(cArray))