#Tính tổng các giá trị chẵn, tổng giá trị lẻ, tổng các giá trị trong một dãy số.
sum = 0
def sumchan(n):
    global sum
    for i in n:
        if(i % 2 == 0):
            sum = sum + i
    return sum
def sumle(n):
    global sum
    for i in n:
        if (i % 2 != 0):
            sum +=i
    return sum
def sumList(n):
    return sum(n)

n = int(input('Nhap so phan tu cua day : '))
nList = [0 for i in range(0,n)]
for i in range(0,n):
    nList[i] = int(input('nList ['+str(i)+'] = '))
print('Tong cac so chan la : ',sumchan(nList))
print('Tong cac so le la : ',sumle(nList))
print('Tong chuoi la : ',sumList(nList))