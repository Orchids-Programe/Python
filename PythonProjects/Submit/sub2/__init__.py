def isMagicSquare(matrix):
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
        return True
    else:
        return False

def inputMatrix():
    m = []
    while (1):
        n = input()
        if not n:
            break
        part = n.split('\t')
        m += [part]
    mm = [[0 for j in range(0, len(m[i]))] for i in range (0, len(m))]
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            mm[i][j] = (int)(m[i][j])
    return mm
    