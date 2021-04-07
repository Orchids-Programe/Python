from math import sqrt
n = int(input('Nhap so : '))
def isSquare(n):
    if n <= 0:
        return False
    t = int(sqrt(n))
    for i in range(1,n+1):
        if t*t == n:
            return True
        else:
            return False
def main(n):
    if isSquare(n) == True:
        print(n,'la so chinh phuong!')
    else:
        print(n,'khong la so chinh phuong!')
main(n)


