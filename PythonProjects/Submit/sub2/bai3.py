def fact(n):
    temp = 1
    for i in range(1, n+1):
        temp = temp*i
    return temp
def ncr(n, r):
    return int(fact(n) / (fact(n - r) * fact(r)))

m = int(input('Kich thuoc m = '))

for i in range(0,m):
    for j in range(0,i+1):
        print(ncr(i,j),' ', end='')
    print(' ')
