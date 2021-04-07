#in ra các số nguyên tố nhỏ hơn n
# from math import sqrt
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) +1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input('Nhap vao so n : '))
# print('So nguyen to nho hon n la : ')
# count = 0
# for i in range(2,n):
#     if isPrime(i):
#         print(i,end=' ')
#         count += 1
# if count == 0:
#     print('Khong co so nguyen to nao nho hon n')

#tinh e^x theo taylor
import math
# def exp(x, n):
#     result = 0
#     p = 1
#     for i in range(1, n+2):
#         result = result + p
#         p = p*x/i
#     return result
# x = float(input('Nhap vao x : '))
# n = int(input('Nhap n = '))
# print('Ket qua la : ',exp(x,n), sep=' ')
# print('So sanh voi ket qua may tinh : ', math.exp(x),sep= ' ')

#Tong cac so nguyen chan nho hon n
# n = int(input('Nhap n : '))
# def sumEle(n):
#     sum = 0
#     count = 0
#     while count < n:
#         sum += count
#         count += 2
#     print('Tong cac so chan nho hon n la : ',sum)
# sumEle(n)

#Giải và biện luận phương trình bậc hai 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
from math import sqrt
# a = int(input())
# b = int(input())
# c = int(input())
# def bienluan(a,b,c):
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 print('VSN')
#             else: print('VN')
#         else:
#             print('Nghiem cua phuong trinh la : ',(-c/b))
#     else:
#         delta = b**2 - 4*a*c
#         if delta < 0:
#             print('VN')
#         else:
#             x1 = (-b + sqrt(delta)) / (2*a)
#             x2 = (-b - sqrt(delta)) / (2*a)
#             print('Phuong trinh co hai nghiem : ',x1,x2)
# bienluan(a,b,c)

#ktra 3 cạnh tam giác và tính chu vi và diện tích
# a = int(input())
# b = int(input())
# c = int(input())
# def C(a,b,c):
#     return (a+b+c)
# def S(a,b,c):
#     p = (a+b+c)/2
#     return math.sqrt(p*(p-a)*(p-b)*(p-c))
# def checkretangle(a,b,c):
#     if(a > 0 & b>0 & c>0 & a+b>c & b+c>a & a+c>b):
#         print('Thoa man 3 canh cua tam giac')
#         print('Chu vi cua tam giac la : ',C(a,b,c))
#         print('Dien tich cua tam giac la : ',S(a,b,c))
#     else:
#         print('Khong thoa man la 3 canh cua tam giac')
# checkretangle(a,b,c)

#So chinh phương
# n = int(input('Nhap n = '))
# def isPalindrome(n):
#     if n < 0:
#         return False
#     t = int(sqrt(n))
#     for i in range(1, n+1):
#         if t*t == n:
#             return True
#         else:
#             return False
# def result(n):
#     if isPalindrome(n):
#         print('La so chinh phuong')
#     else:
#         print('Khong phai la so chinh phuong')
# result(n)

#Giai thua kep
# n = int(input('Nhap n = '))
# def factorial(n):
#     temp = 1
#     if n % 2 == 0:
#         for i in range(2,n+1,2):
#             temp *= i
#     else:
#         for i in range(1, n+1,2):
#             temp *= i
#     print(str(n),'!! = ', str(temp))
# factorial(n)

#Bộ pytago
# n = int(input())
# for i in range (1,n+1):
#     for j in range (i+1,n+1):
#         for k in  range (j+1, n+1):
#             if(i*i + j*j == k*k):
#                 print("("+str(i)+", "+str(j)+", "+str(k)+")")

#Tong chan tong le
# def sumEle(a):
#     return sum(i for i in a if i%2 == 0)
# def sumOld(a):
#     return sum(i for i in a if i%2 == 1)
# n = int(input('Nhap so phan tu cua day : '))
# aList = []
# for i in range(0,n):
#     aList.append(int(input('list['+str(i)+'] = ')))
# print('Tong chan ',sumEle(aList))
# print('Tong le : ',sumOld(aList))

#Đếm từ
# def wordcount(s):
#     tokens = s.split(' ')
#     words = list(dict.fromkeys(tokens))
#     counts = [tokens.count(words[i]) for i in range(0,len(words))]
#     return words, counts
# text = 'lua nep la lua nep nuong lua len lop lop long nang lang lang'
# words, counts = wordcount(text)
# for i in range(0, len(words)):
#     print(words[i],':',counts[i])

#Matran chuyen vi
# def inputMatrix(matrix):
#     for i in range(0,len(matrix)):
#         for j in range(0,len(matrix[i])):
#             matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+'] = '))
# def outputMatrix(matrix):
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
# def chuyenvi(matrix):
#     t = [[0 for j in range(0, len(matrix))] for i in range(0, len(matrix[0]))]
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             t[j][i] = matrix[i][j]
#         return t
# m = int(input('Nhap so hang : '))
# n = int(input('Nhap so cot : '))
# matrix = [[0 for j in range(0,n)] for i in range(0,m)]
# inputMatrix(matrix)
# outputMatrix(matrix)
# t = chuyenvi(matrix)
# print('Ma tran chuyen vi la : ')
# outputMatrix(t)

#Day so
# a = int(input('Nhap day so : '))
# def dandau(a):
#     for i in range(len(a) -1):
#         if(a[i] * a[i+1] >= 0):
#             print('Khong la day dan dau')
#         else:
#             print('La day dan dau')
# def daytang(a):
#     for i in range(len(a) -1):
#         if a[i+1] - a[i] < 0:
#             print('Khong la day tang')
#         else:
#             print('La day tang')
# def CSC(a):
#     if len(a) < 2:
#         print('Khong la CSC')
#     elif len(a) == 2:
#         print('La CSC')
#     else:
#         k = a[1] - 1[0]
#         for i in range(1, len(a) - 1):
#             if(a[i+1] - a[i] != k):
#                 print('Khong la CSC')
#             else:
#                 print('La CSC')
# def CSN(a):
#     if len(a) < 2:
#         print('Khong la CSN')
#     elif len(a) == 2:
#         print('La CSN')
#     else:
#         p = a[1]/a[0]
#         for i in range(0, len(a) - 1):
#             if a[i+1]/a[i] != p:
#                 print('Khong la CSN')
#             else:
#                 print('La CSN')
# dandau(a)
# daytang(a)
# CSC(a)
# CSN(a)

#Toi gian phan so
# def ucln(a,b):
#     while a != b:
#         if a > b:
#             a = a-b
#         else:
#             a = a+b
#     return a
# def bcnn(a,b):
#     return int((a*b) / ucln(a,b))
# def toigian(a,b):
#     temp = ucln(a,b)
#     tu = a/temp
#     mau = b/temp
#     print(str(tu)+ '/' +str(mau))
# a = int(input('Nhap a = '))
# b = int(input('Nhap b = '))
# print('UCLN la ', ucln(a,b))
# print('BCNN la ', bcnn(a,b))
# toigian(a,b)

#Tam gia pascal
# n = int(input('Nhap n = '))
# def fact(n):
#     fac = 1
#     for i in range(1,n+1):
#         fac *= i
#     return fac
# def ncr(i,j):
#     return (int) (fact(i) / (fact(i-j)*fact(j)))
# def printPS(n):
#     for i in range(0, n+1):
#         for j in range(0, i+1):
#             print(ncr(i,j),end=' ')
#         print()
# printPS(n)

#Tra ve ky tu xuat hien nhieu nhat
# def getMax(str):
#     count = [0]*256
#     max = -1
#     char = ' '
#     for i in str:
#         count[ord(i)] += 1
#     for i in str:
#         if max < count[ord(i)]:
#             max = count[ord(i)]
#             char = i
#     return char, max
# str = input('Nhap chuoi : ')
# print(getMax(str))

#diem yen ngua
# def inputMatrix(matrix):
#     for i in range(0,len(matrix)):
#         for j in range(0, len(matrix[i])):
#             matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+'] ='))
# def outputMatrix(matrix):
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             print(matrix[i][j], end=' ')
#         print()
## def minhang(matrix):
##     for i in range(0,m):
##         min = matrix[i][0]
##         for j in range(0,n):
##             if matrix[i][j] < min:
##                min = matrix[i][j]
##     return min
## def maxcot(matrix):
##     for i in range(0,m):
##         max = matrix[0][j]
##         for j in range(0,n):
##             if matrix[i][j] > max:
##                 max = matrix[i][j]
##     return max
# def diemyenngua(matrix):
#     # for i in range(0,m):
#     #     for j in range(0,n):
#     #         if maxcot(matrix[i][j]) & minhang(matrix[i][j]):
#     #             print('Diem yen ngua : ',matrix[i][j])
#     for i in range(0,m):
#         minhang[i] = matrix[i][0]
#         for j in range(0,n):
#             if mincot[i] > matrix[i][j]:
#                 mincot[i] = matrix[i][j]
#     for j in range(0,n):
#         max[j] = matrix[0][j]
#         for i in range(0,m):
#             if maxcot[j] < matrix[i][j]:
#                 maxcot[j] = matrix[i][j]
#     for i in range(0,m):
#         for j in range(0,n):
#             if (matrix[i][j] == minhang[i] & matrix[i][j] == maxcot[j]):
#                 print('Diem yen ngua la : ', matrix[i][j])
#
# m = int(input('Nhap so hang : '))
# n = int(input('Nhap so cot : '))
# matrix = [[0 for j in range(0,n)] for i in range(0,m)]
#
# inputMatrix(matrix)
# outputMatrix(matrix)
# diemyenngua(matrix)

#Ma tran ma phuong
# def isMagicSquare(matrix):
#     sum = 0
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             if (i == j):
#                 sum = sum + matrix[i][j]
#
#     # Tổng phần tử trên các hàng
#     for i in range(0, len(matrix)):
#         sum1 = 0
#         for j in range(0, len(matrix[i])):
#             sum1 = sum1 + matrix[i][j]
#         if (sum == sum1):
#             flag = 1
#         else:
#             flag = 0
#             break
#     # Tổng phần tử của cột
#     for i in range(0, len(matrix)):
#         sum2 = 0
#         for j in range(0, len(matrix[i])):
#             sum2 = sum2 + matrix[j][i]
#         if (sum == sum2):
#             flag = 1
#         else:
#             flag = 0
#             break
#     if flag == 1:
#         return True
#     else:
#         return False
#
#
# def inputMatrix():
#     m = []
#     while (1):
#         n = input()
#         if not n:
#             break
#         part = n.split('\t')
#         m += [part]
#     mm = [[0 for j in range(0, len(m[i]))] for i in range(0, len(m))]
#     for i in range(0, len(m)):
#         for j in range(0, len(m[i])):
#             mm[i][j] = (int)(m[i][j])
#     return mm
