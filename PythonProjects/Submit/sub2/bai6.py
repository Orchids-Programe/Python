def inputMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0,len(matrix[i])):
            matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+'] = '))
def outputMatrix(matrix):
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
def minhang(matrix):
    min = matrix[0][0]
    for i in range(0,m):
        min = matrix[i][0]
        for j in range(0,n):
            if matrix[i][j] < min:
                min = matrix[i][j]
    return min

def maxcot(matrix):
    max = matrix[0][0]
    for j in range(0,n):
        max = matrix[0][j]
        for i in range(0,m):
            if matrix[i][j] > max:
                max = matrix[i][j]
    return max
def yenngua(matrix):
    minhangg = []
    maxcott = []
    for i in range(0,m):
        minhangg = matrix[i][0]
        for j in range(0,n):
            if minhangg > matrix[i][j]:
                minhangg = matrix[i][j]
    for j in range(0,n):
        maxcott = matrix[0][j]
        for i in range(0,m):
            if(maxcott < matrix[i][j]):
                maxcott = matrix[i][j]
    for i in range(0,m):
        for j in range(0,n):
            if((matrix[i][j] == minhangg) & (matrix[i][j] == maxcott)):
                print('Diem Yen ngua = ', matrix[i][j])


m = int(input('Nhap so hang m = '))
n = int(input('Nhap so cot n = '))
matrix = [[0 for j in range(0,n)] for i in range(0,m)]

inputMatrix(matrix)
outputMatrix(matrix)
# print('Min hang : ',str(min))
#
# print('Max cot : ',str(max))
yenngua(matrix)

