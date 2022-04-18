"""
__________BASEBALL GAME__________
GIVEN AN ARRAY OF STRINGS
int(x) -> record a new score
+ -> record a new score that is the sum of the previous two scores
D -> record a new score that is double of the previous two scores
C -> remove the previous score from the record
"""
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]

def scoreBasketball(ops):
    res = []
    j = 0

    if len(ops) == 0:
        return None

    if len(ops) == 1:
        return int(ops[0])

    if len(ops) > 1:
        for i in range(len(ops)):
            if ops[i].lstrip('-').isdigit():
                res.append(int(float((ops[i]))))
                j+=1

            elif ops[i] == "+":
                res.append(res[j-2] + res[j-1])
                j+=1

            elif ops[i] == "D":
                res.append(res[j-1] * 2)
                j+=1

            elif ops[i] == "C":
                res.remove(res[j-1])
                j-=1

        return sum(res)

print(scoreBasketball(ops))
# scoreBasketball(ops)