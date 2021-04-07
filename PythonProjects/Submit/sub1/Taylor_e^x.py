import math
def exp(x,n):
    e = 0
    p = 1
    for i in range(1,n+2):
        e = e + p
        p = p*x/i
    return e

x =  float(input('Nhap x = '))
n = int(input('Nhap n = '))
print('e^',x,' = ',exp(x,n),sep='')
print('Ham tinh e mu x trong module math e^',x,' = ',math.exp(x), sep='')