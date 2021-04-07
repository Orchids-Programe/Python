def Split(n):
    i = 1
    list = []
    for i in range(1,n+1):
        if(n % i == 0):
            list.append(i)
    if len(list) == 0:
        list.append(n)
    return list
def printMatrix(list,n):
    print(str(n),end = ' ')
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if list[i]*list[j] == n:
                print("="+ str(list[i]) + 'x' +str(list[j]),end = ' ')


    for i in range(0, int(list[i])):
        for j in range(0,int(list[j])):
            matrix[i][j] = int(input())
    for i in range(0,len(int[i])):
        for j in range(0,int(list[j])):
            print(matrix[i][j], end=' ')
        print()

n = int(input('Nhap n : '))
a = Split(n)
printMatrix(a,n)
    