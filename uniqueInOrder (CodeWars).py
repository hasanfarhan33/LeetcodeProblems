'''
Implement the function unique_in_order which takes as argument a sequence and returns
a list of items without any elements with the same value next to each other and preserving the
 original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

iterable = 'ABBCcAD'
def uniqueInOrder(iterable):
    res = []
    for i in range(len(iterable) - 1):
        if iterable[i] == iterable[i + 1]:
            i += 1
            if i + 1 == len(iterable):
                res.append(iterable[i])
        else:
            res.append(iterable[i])
            if i + 1 == len(iterable):
                res.append(iterable[i + 1])
    return res


def uniqueInOrderBetter(iterable):
    res = []
    for item in iterable:
        if len(res) < 1 or not item == res[len(res) - 1]:
            res.append(item)
    return res


print(uniqueInOrder(iterable))
print(uniqueInOrderBetter(iterable))