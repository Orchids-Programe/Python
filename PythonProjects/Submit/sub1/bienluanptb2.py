from math import sqrt
a = int(input('Nhap a = '))
b = int(input('Nhap b = '))
c = int(input('Nhap c = '))

def solver(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('VSN')
            else:
                print('VN')
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('VN')
        elif delta == 0:
            x = -b/(2*a)
            print('PT co nghiem ',x)
        else:
            x1 = float((-b - sqrt(delta))/2*a)
            x2 = float((-b + sqrt(delta))/2*a)
            print(x1,x2)
solver(a,b,c)
