s = "LVIII"

def romanToInteger(s):
    if len(s) == 0:
        return 0
    else:
        romanList = list(s)
        numberToReturn = 0
        numberList = createNumberList(romanList)
        if len(numberList) == 1:
            return numberList[0]

        for i in range(len(numberList)):
            if i + 1 < len(numberList) and numberList[i] < numberList[i+1]:
                numberToReturn -= numberList[i]
            else:
                numberToReturn += numberList[i]
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


def romanToIntegerNeetcode(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    res = 0
    for i in range(len(s)):
        if i+1 < len(s)  and roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res



# print(romanToInteger(s))
print(romanToIntegerNeetcode(s))
