str = "LVIII"

def romanToInteger(str):
    if len(str) == 0:
        return 0
    else:
        romanList = list(str)
        numberToReturn = 0
        numberList = createNumberList(romanList)
        if len(numberList) == 1:
            return numberList[0]

        for i in range(len(numberList) - 1):
            if numberList[i] >= numberList[i+1]:
                numberToReturn += numberToReturn + (numberList[i] + numberList[i+1])
            else:
                numberToReturn += numberToReturn + abs(numberList[i] - numberList[i+1])
        return numberToReturn


def createNumberList(romanList):
    numberList = []
    for i in range(len(romanList)):
        if romanList[i] == 'I':
            numberList.append(1)
        elif romanList[i] == 'V':
            numberList.append(5)
        elif romanList[i] == 'X':
            numberList.append(10)
        elif romanList[i] == 'L':
            numberList.append(50)
        elif romanList[i] == 'C':
            numberList.append(100)
        elif romanList[i] == 'D':
            numberList.append(500)
        elif romanList[i] == 'M':
            numberList.append(1000)

    return numberList


print(romanToInteger(str))

