def accum(st):
    l_array = []
    char_count = 0 
    for i, char in enumerate(st): 
        l_array.append(char.upper() + char.lower() * i)
    result = "-".join(l_array)
    return result

print(accum("abcd"))