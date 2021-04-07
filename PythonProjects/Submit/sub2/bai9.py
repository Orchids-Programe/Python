def inputMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+']='))
def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
def maphuong(matrix):
    #Tổng phần tử trên các đường chéo
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (i == j):
                sum = sum + matrix[i][j]

    #Tổng phần tử trên các hàng
    for i in range(0, len(matrix)):
        sum1 = 0
        for j in range(0, len(matrix[i])):
            sum1 = sum1 + matrix[i][j]
        if( sum == sum1):
            flag = 1
        else:
            flag = 0
            break
    #Tổng phần tử của cột
    for i in range(0, len(matrix)):
        sum2 = 0
        for j in range(0, len(matrix[i])):
            sum2 = sum2 + matrix[j][i]
        if(sum == sum2):
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print('Ma tran tren la ma phuong!')
    else:
        print('Ma tran tren khong phai la ma phuong!')


m = int(input('Nhap so hang: '))
n = int(input('Nhap so cot : '))
matrix = [[0 for j in range(0,n)] for i in range(0,m)]

inputMatrix(matrix)
printMatrix(matrix)
maphuong(matrix)

