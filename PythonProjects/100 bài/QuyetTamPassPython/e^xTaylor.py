from math import sqrt
def exp(x,n):
    e = 0
    p = 1
    for i in range(1, n+2):
        e = e + p
        p = p*x/i
    return e
x = float(input('x = '))
n = int(input('n = '))
print('Gia tri e^',x,' la :',exp(x,n), end='')

def tongchan(n):
    sum = 0
    count = 0
    while count < n:
        sum += count
        count += 2
    print('Tong la : ',sum)
tongchan(n)

