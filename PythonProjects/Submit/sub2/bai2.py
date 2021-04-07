def ucln(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def bcnn(a,b):
    return int((a*b) / ucln(a,b))
def toigianphanso(a,b):
    temp = ucln(a,b)
    x = a/temp
    y = b/temp
    print(str(x) +'/'+ str(y))
a = int(input('Nhap a = '))
b = int(input('Nhap b = '))
print('UCLN la : ', ucln(a,b))
print('BCNN la : ', bcnn(a,b))
toigianphanso(a,b)