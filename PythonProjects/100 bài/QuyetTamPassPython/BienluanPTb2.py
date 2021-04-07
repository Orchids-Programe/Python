from math import sqrt
# #ax2 + bx + c = 0
# a = int(input())
# b = int(input())
# c = int(input())
# def bienluan(a,b,c):
#     if(a == 0):
#         if b == 0:
#             if c == 0:
#                 print('VSN')
#             else:
#                 print('VN')
#     else:
#         delta = b**2 - 4*a*c
#         if delta < 0:
#             print('VN')
#         if delta == 0:
#             print('PT co 1 nghiem suy nhat : ',(-b/2*a))
#         if delta > 0:
#             x1 = (-b + sqrt(delta)) / 2*a
#             x2 = (-b - sqrt(delta)) / 2*a
#             print('PT co 2 nghiem la : ',x1,x2)
# bienluan(a,b,c)
#
# def tamgiac(a,b,c):
#     if(a>0 & b>0 & c>0 & a+b>c & b+c>a & a+c > b):
#         print('S = ',dientich(a,b,c), 'C = ',chuvi(a,b,c))
#     else:
#         print('INVALID')
# def chuvi(a,b,c):
#     return (float) (a+b+c)
# def dientich(a,b,c):
#     p = (a+b+c) / 2
#     return sqrt(p*(p-a)*(p-b)*(p-c))
# tamgiac(a,b,c)
#

n = int(input('n = '))
# def isSquare(n):
#     if n < 0:
#         return False
#     t = int(sqrt(n))
#     for i in range(1,n+1):
#         if t*t == n:
#             return True
#         else:
#             return False
# def main(n):
#     if isSquare(n) == True:
#         print(n,'la so chinh phuong')
#     else:
#         print('False')
# main(n)

# def DualFactorial(n):
#     temp = 1
#     if n % 2 == 0:
#         for i in range(2,n+1,2):
#             temp *= i
#     else:
#         for i in range(1,n+1,2):
#             temp *= i
#     print('Ket qua la',temp)
# DualFactorial(n)

def tamgiacpitago(n):
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1, n+1):
                if(i*i + j*j == k*k):
                    print('('+str(i)+','+str(j)+','+str(k)+')')
tamgiacpitago(n)