import numpy as np
aList = np.random.randint(int(input()), size = 10)
print(aList)
def findmax(aList):
    print('Phan tu co gia trị lon nhat la : ',max(aList))
def findmin(aList):
    print('Phan tu co gia tri nho nhat la : ',min(aList))
#tìm số xuất hiện nhiều nhất
    
def getMax(aList):
    max = -1
    count = 0
    c = ' '
    for i in aList:
        count(aList[i]) += 1
    for i in aList:
        if max < count(aList[i]):
            max = count(aList[i])
            c = i
    return c, max
findmax(aList)
findmin(aList)
print(getMax(aList))