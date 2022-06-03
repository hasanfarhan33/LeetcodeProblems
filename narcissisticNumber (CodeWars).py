value = 371

def narcissistic(value:int):
    if value < 0:
        return False
    eachDigits = [int(x) for x in str(value)]
    total = 0
    for num in eachDigits:
        total += num**len(eachDigits)
    if total != value:
        return False
    else:
        return True

narcissistic(value)