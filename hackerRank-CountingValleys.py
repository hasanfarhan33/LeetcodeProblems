'''
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, 
for every step it was noted if it was an uphill, , or a downhill,  step. 

Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. 
We define the following terms:

* A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level 
and ending with a step down to sea level.

* A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level 
and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
'''

def countingValleys(steps, path): 
    altitude = 0 
    numValleys = 0 
    inValley = False 
    for char in path: 
        if char == "U": 
            altitude += 1 
        elif char == "D": 
            altitude -= 1 
        
        if altitude >= 0: 
            inValley = False 
        if altitude < 0 and not inValley: 
            numValleys += 1 
            inValley = True 
    return numValleys

print(countingValleys(8, ["D","D", "U","U","U","U","D","D"]))