n = int(input('Nhap so phan tu cua day : '))
list = [0 for i in range(0,n)]
for i in range(0,n):
    list[i] = int(input('list ['+str(i)+'] = '))

def dandau(n):
    for i in range(0,len(list)-1):
        if list[i]*list[i+1] > 0:
            return print('False')
    else:
        return print('True')
def daytang(n):
    for i in range(0, len(list)-1):
        if list[i+1] - list[i] < 0:
            return print('False')
    else:
        return print('True')
def CSC(n):
    x = list[1] - list[0]
    for i in range(0,len(list)-1):
        if x != list[i+1] - list[i]:
            return print('False')
    else:
        return print('True')

def CSN(n):
    x = list[1]/list[0]
    for i in range(1, len(list)-1):
        if x != list[i+1]/list[i]:
            return print('False')
    else:
        return print('True')

dandau(list)
daytang(list)
CSC(list)
CSN(list)
