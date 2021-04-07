from statistics import mean
aList = list(map(float, input('Nhap day so : ').split(' ')))
print(aList)
def getM(aList):
    return round(mean(aList), 2)
def phuongsai(aList):
    e = getM(aList)
    print(e)
    x = [round(pow(i-e,2), 2) for i in aList]
    return getM(x)

print(phuongsai(aList))


# import math
# def mean(s):
#     a = [float(i) for i in s]
#     sum = 0
#     for i in a:
#         sum += i
#     return (float)(sum/(len(a)))
# def variance(s):
#     a = [float(i) for i in s]
#     sum = 0
#     for i in a:
#         sum += (i-mean(s)) * (i-mean(s))
#     kq = (float)(sum/(len(a)))
#     return kq
# def standarddeviation(s):
#     kq= math.sqrt(variance(s))
#     return kq