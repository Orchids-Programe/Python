from math import sqrt
a = float(input('Nhap a = '))
b = float(input('Nhap b = '))
c = float(input('Nhap c = '))

def tamgiac(a,b,c):
    if (a>0) and (b>0) and (c>0) and (a+b>c) and (a+c>b) and (b+c>a):
        print('La do dai cua tam giac!')
    else:
        print('Khong tao thanh tam giac')
def chuvi(a,b,c):
    print('C = ',(a+b+c))
def dientich(a,b,c):
    p = (a+b+c)/2
    print('S = ',sqrt(p*(p-a)*(p-b)*(p-c)))
tamgiac(a,b,c)
chuvi(a,b,c)
dientich(a,b,c)