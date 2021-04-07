#name = input("Enter your name: ")
#print(name)
#print(type(name))

#s = 'hello HaVuLong'.title()
#print(s)
#s = 'abc'.rjust(12,'*')
#print(s)
#s = 'Hà Vũ'.encode()
#print(s)
#s = '*'.join(['Ha', 'Vu', 'Long'])
#print(s)
#s = 'abc Ha abc Long'.replace('abc','Vu',1)
#print((s))
#s = '***abc****'.strip('*')
#print(s)
#s = 'Ha Vu Long How Long KTeam'.rpartition('Long')
#print(s)
#s = 'How Kteam Ha Vu Long'.partition('z')
#print(s)
#s = 'How Kteam Ha Vu Long'.count('o',0,10)
#s = 'How Kteam Ha Vu Long'.startswith('Ho',0,7)
#s = 'How Kteam Ha Vu Long'.endswith('Long')
#s = 'How Kteam Ha Vu Long'.find('K')
#s = 'How Kteam Ha Vu Long'.rfind('L')
#s = 'How Kteam Ha Vu Long'.index('Vu')
#s = ('How Kteam Ha Vu Long'.title()).istitle()
#s = '    '.isspace()
#s = [1,2,3,'abc',[1,2]]
#s[1] = 'long'
#matrix
#s= [[1,2,3],[4,5,6],[7,8,9]]
#print(s[0])
#print(s[1])
#print(s[2])
#2 list
#s = [1,2,3,4]
#p = list(s)
#rint(s)
#print(p)
#p[0] = ['a']
#print(s)
#print(p)
#s = [1,5,2,3,4]
#p=s.sort()
#print(p)
#tup = (i for i in range(10) if i % 2 == 0)
#a = tuple(tup) # generator expresstion
#tup = (1,2,3,4,5)
#a = tup[::-1] #dao nguoc
#print(a)
#print('ab'*5)
#def grow(b, a = 2):
#    return a*b;
#x = 3
#print(grow(x,3))
result = 0
x, y, z = 5 , 6, 3
# biến toàn cục
#def maxInTriple():
#    return max(max(x, y),z)
#def double(max):
#    global result
#    result = maxInTriple()*2
#    print(result)
#print(maxInTriple())
#double(max)
#from math import sqrt
#x = sqrt
#print(x(9))
#lambda
#f = lambda x, y : 10 if x == y else 2
#print(f(5,5))
#bộ sinh
#def gen():
#    yield 1
#    yield 'aaaa'
#    yield 3.5
#f = gen()
#print(next(f))
#print(next(f))
#print(next(f))
#sử dụng vòng lặp
#for i in gen():
#    print(i)
#x = 2.1 - 1.1
#y = 3.1 - 2.1
#print('x = ', x, 'y = ',y)
#x == y
thisdict = {
    'brand' : 'Fond',
    'model' : 'Mustang',
    'year' : '1964'
}
#for x,y in thisdict.items():
#    print(x,y)
#if 'model' in thisdict:
#    print('YES')
#thisdict['color'] = 'red'
#print(thisdict)
# import re
# list = 'Ha Vu Long May tinh thong tin'
# match = re.search(r'Long',list)
# if match:
#     print(match.group()) #in ra chuoi
# else:
#     print('Not found!')
thisdict = {
    'brand' : 'Front',
    'model' : 'Mustang',
    'year' : 1964
}
print(thisdict)
x = thisdict['model']
y = thisdict.get('model')
print(x, y)
thisdict['year'] = 2020
print(thisdict)
#in ra các khóa
for x in thisdict:
    print(x)
#in ra giá trị của khóa
for x in thisdict.values():
    print(x)
#for x in thisdict:
#    print(thisdict[x])
#in ra khoa_giatricuakhoa
for x in thisdict.items():
    print(x)
print(len(thisdict))
#them phan tu
thisdict['color'] = 'red'
print(thisdict)
#xoa
thisdict.pop('model') # del thisdict['model']
print(thisdict)
thisdict.popitem()
print(thisdict)
#xoa ca dict
#del thisdict # thisdict.clear()
#copy
mydict = thisdict.copy()
print(mydict)
#cach copy khac mydict = dict(thisdict)
#print(mydict)