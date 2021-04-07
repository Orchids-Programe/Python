from math import sqrt
n = int(input('Nhap so : '))
def isPrime(n):
    if(n < 2):
        return  False
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True
count = 0
print('Cac so nguyen to nho hon', n ,'la : ')
for i in range(2,n):
    if isPrime(i):
        print(i,', ', end='')
        count+=1
if count == 0:
    print('Khong co so nguyen to!')
