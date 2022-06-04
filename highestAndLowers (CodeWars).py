'''
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.
'''

numbers = "1 2 3 4 5"

def highestAndLowest(numbers: str):
    numbers = numbers.split(' ')
    numbers = [int(number) for number in numbers]
    numbers.sort()
    result = str(numbers[-1]) + " " + str(numbers[0])
    return result

highestAndLowest(numbers)