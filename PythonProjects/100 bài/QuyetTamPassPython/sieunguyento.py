from math import sqrt
n = int(input('Nhap so n : '))
def isPrime(n):
    if(n < 2):
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True
# def SuperPrime(n):
#     if isPrime(n):
#         if n < 10:
#             return True
#         else:
#             if isPrime(int(n/10)):
#                 print("True")
#             else:
#                 print("False")
#     else:
#         print("False")
# SuperPrime(n)

#in ra cac so nguyen to nho hon n
count = 0
print('Cac so nguyen to nho hon ',n,' la :')
for i in range(2,n):
    if isPrime(i):
        print(i,',', end=' ')
        count += 1
if count == 0:
    print('Khong co so nguyen to')
print()

