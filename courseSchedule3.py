'''
There are n different online courses numbered from 1 to n. You are given an array courses
where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken
continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
'''

from typing import List

courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# TODO: Add a better algorithm here
def scheduleCourse(courses:List[int]) -> int:
    courseHash = {}
    currentDay = 1
    for duration, lastDay in courses:
        courseHash[duration] = lastDay

    for duration, lastDay in courses:
        currentDay = currentDay + duration
        if currentDay > courseHash[duration]:
            currentDay = 1
            continue
        else:
            res += 1
            courseHash.pop(duration) # Took the class so remove from consideration
            

scheduleCourse(courses)