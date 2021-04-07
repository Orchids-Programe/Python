def find(s, e, coins):
    length = e-s+1
    oneTwoLen = int(length/2)
    if length <= 2:
        return LenlessThanTwo(s, e, coins)

    if length % 2 == 0:
        weight1=getWeight(s, s+oneTwoLen-1, coins)
        weight2=getWeight(s+oneTwoLen, e, coins)
        if weigh(weight1, weight2) == -1:
            return find(s, s+oneTwoLen-1, coins)
        else:
            return find(s+oneTwoLen, e, coins)
    elif length % 2 == 1:
        weight1 = getWeight(s, s+oneTwoLen - 1, coins)
        weight2 = getWeight(s+oneTwoLen, e - 1, coins)
        weight3 = coins[e]
        if weigh(weight1, weight2) == 0:
            return e
        elif weigh(weight1,weight2) == -1:
            return find(s, s+oneTwoLen - 1, coins)
        else:
            return find(s+oneTwoLen, e - 1, coins)

def LenlessThanTwo(s, e, coins):
    length = e-s+1
    if length == 1:
        return s
    else:
        if weigh(coins[e], coins[s]) == 1:
            return s
        else:
            return e

def getWeight(s, e, coins):
    sum = 0
    for i in range(s, e+1):
        sum += coins[i]
    return sum


def weigh(left, right):
    if left > right:
        return 1
    elif left < right:
        return -1
    else:
        return 0

coins=[2,2,2,2,2,2,2,2,1,2,2]
print(find(0, len(coins)-1, coins))