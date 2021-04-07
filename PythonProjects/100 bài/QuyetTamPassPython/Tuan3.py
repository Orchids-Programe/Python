#Dem số từ trong văn bản
# text = 'lua nep la lua nep nuong lua len lop lop long nang lang lang'
# wordcount = {}
# for w in text.split(' '):
#     wordcount[w] = wordcount.get(w,0)+1
# print(wordcount)

#Bai1
# import numpy as np
# def keySort(ele):
#     return ele*(ele%2)
# aList = list(map(int, input('Nhap day so : ').split(' ')))
# print(aList)
# aList.sort(key = keySort)
# c = []
# l = []
# for i in range(0,len(aList)):
#     if aList[i] % 2 == 0:
#         c.append(aList[i])
#     else:
#         l.append(aList[i])
# c.sort(key= None, reverse= False)
# l.sort(key= None, reverse= True)
# sapxep = c + l
# print(sapxep)
#random
# aList = np.random.randint(int(input()), size= 10)
# print(aList)
# def findMax(aList):
#     print('Max : ', max(aList))
# def findMin(aList):
#     print('Min : ', min(aList))
# def getMax(aList):
#     max = -1
#     count = 0
#     c = ' '
#     for i in aList:
#         count += 1
#     for i in aList:
#         if max < count:
#             max = count
#             c = i
#     print(c,max)
# findMax(aList)
# findMin(aList)
# getMax(aList)

#tinh phuong sai
import math
# aList = [1,2,3,4,5]
# def trungbinhconge(s):
#     return sum(s) / len(s)
# def lamda(s):
#     avg = trungbinhconge(s)
#     result = sum([(i-avg)**2 for i in s]) / len(s)
#     return result
# def standard(s):
#     result = math.sqrt(lamda(s))
#     return result

#tinh goc giua hai vecto
# def tuso(u,v):
#     return sum([u[i]*v[i] for i in range(0,len(u))])
# def mauso(u):
#     x = sum([pow(i,2) for i in u])
#     y = round(math.sqrt(x),4) #lamtron nhaaaa
#     return y
# def cosinuv(u,v):
#     tu = tuso(u,v)
#     mau = mauso(u) * mauso(v)
#     result = tu / mau
#     return result

#Cong 2 so nguyen a[1,2,4,5] + b[7,8,9] = c[2,0,3,4]
# a = [1,2,4,5]
# b = [7,8,9]
# def addNum(a,b):
#     list1 = []
#     list2 = []
#     for i in range(0, len(a)):
#         list1.append(str(a[i]))
#     for i in range(0, len(b)):
#         list2.append(str(b[i]))
#     x = int(''.join(list1))
#     y = int(''.join(list2))
#     sum = x + y
#     length = str(sum)
#     c = []
#     for i in length:
#         c.append(int(i))
#     print(c)
# addNum(a,b)

#Tim phan tu duy nhat trong sach Ví dụ a = [1,2,3,2,3,1,4,5,4] phần tử cần tìm là 5
# a = [1,2,3,2,3,1,4,5,4]
# def findUniq(a):
#     a = sorted(a)
#     print(a)
#     m = 0
#     while m < len(a)-1:
#         if a[m] != a[m+1]:
#             return a[m]
#         else:
#             m = m + 2
#     print(a[len(a)-1])
# findUniq(a)

#Di chuyen so 0 sang phai tu file
def zeroMove(file):
    f = open('file.txt','r')
    list = f.read().split(' ')
    list0 = []
    listn = []
    for i in list:
        int(i)
        if int(i) == 0:
            list0.append(int(i))
        if int(i) != 0:
            listn.append(int(i))
    result = listn + list0
    print(result)
zeroMove(file)
