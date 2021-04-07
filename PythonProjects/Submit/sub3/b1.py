#from _operator import itemgetter
#def keySort(ele):
#    return ele*(ele%2)
#List = []
#print('Nhap chuoi : ')
#while True:
#    a = input('Start : ')
#    if not a:
#        break
#    aList.append(a.split(','))
#b = []
#b = aList[0]
#h = []
#a1 = []
#for i in  range(0,len(b)):
#    h.append(int(b[i]))
#h.sort(key=keySort())
#a2 = []
#for i in range(0, len(h)):
#    if h[i] % 2 == 0:
#        a1.append(h[i])
#    else:
#        a2.append(h[i])
#a1.sort(key=None, reverse=True)
#a2.sort(key = None, reverse=False)
#sapxep = []
#sapxep = a1+a2
#print(sapxep)

#import numpy as np
def keySort(ele):
    return ele*(ele%2)
aList = list(map(int, input('Nhap day so : ').split(' ')))
#aList = np.random.randint(int(input()), size = 10)
print(aList)
aList.sort(key = keySort)

c = []
l = []
for i in range(0, len(aList)):
    if aList[i] % 2 == 0:
        c.append(aList[i])
    else:
        l.append(aList[i])
c.sort(key = None, reverse = False)
l.sort(key = None, reverse = True)
sapxep = c + l
print(sapxep)