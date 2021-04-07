#aList = [1,2,3,4,5,6,7,8,9,10]
#temp = list(map(lambda x: x**2, filter(lambda x: x% 2 == 0,aList)))
#print(temp)

listA = [1,2,3,4,5,6,7,8,9]
listB = [1,2,3,4,5,7]
setA = set(listA)
setB = set(listB)
print('Cac pt chung cua 2 danh sach')
print(setA.intersection(setB))
print('Co trong A ma khong co trong B')
print(setB.difference(setA))
print('Co trong B ma khong co trong A')
print(setB.difference(setA))
print(setA.union(setB))