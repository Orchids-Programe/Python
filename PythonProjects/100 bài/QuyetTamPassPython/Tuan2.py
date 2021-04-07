# def sumEven(a):
#     return sum(a[i] for i in range(0, len(a)) if a[i]%2 == 0)
# def sumOld(a):
#     return sum(i for i in a if i % 2 == 1)
# n = int(input('Nhap do dai cua day so : '))
# aList = []
# for i in range(0, n):
#     aList.append(int(input()))
# print(sumEven(aList))
# print(sumOld(aList))

#Đếm số từ trong văn bản
# def wordCount(s):
#     token = s.split(' ')
#     w = []
#     c = []
#     for t in token:
#         if t not in w:
#             w.append(t)
#             c.append(count(t,token))
#     return w, c
#
#
# def count(w, token):
#     count = 0
#     for t in token:
#         if w == t:
#             count +=1
#     return count
# text = "lúa nếp là lúa nếp làng lúa lên lớp lớp lòng nàng lâng lâng"
# words, counts = wordCount(text)
# for i in range(0,len(words)):
#     print(words[i],':',counts[i])

# def wordcount(s):
#     tokens = s.split(' ')
#     words = list(dict.fromkeys(tokens))
#     counts = [tokens.count(words[i]) for i in range(0, len(words))]
#     return words, counts
# text = 'lua nep la lua nep nuong lua len lop lop long nang lang lang'
# words, counts = wordcount(text)
# for i in range(0, len(words)):
#     print(words[i],':',counts[i])

#matrix
# def inputMatrix(matrix):
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+'] = '))
# def outputMatrix(matrix):
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             print(matrix[i][j], end= ' ')
#         print()
# def chuyenvi(matrix):
#     t = [[0 for j in range(0,len(matrix))] for i in range(0,len(matrix[0]))]
#     for i in range(0,len(matrix)):
#         for j in range(0,len(matrix[i])):
#             t[j][i] = matrix[i][j]
#     return t
#
# m = int(input('Nhap so hang : '))
# n = int(input('Nhap so cot : '))
# matrix = [[0 for j in range(0,n)] for i in range(0,m)]
# inputMatrix(matrix)
# outputMatrix(matrix)
# t = chuyenvi(matrix)
# print('Ma tran chuyen vi : ')
# outputMatrix(t)

# #tam giac Pascal
# def fact(n):
#     fac = 1
#     for i in range(1, n+1):
#         fac = fac * i
#     return fac
# def nrc(i, j):
#     return (int) (fact(i) / (fact(j)*fact(i-j)))
# def printTriangle(n):
#     for i in range(0, n+1):
#         for j in range(0, i+1):
#             print(nrc(i,j), end=' ')
#         print()
# n = int(input())
# printTriangle(n)

#ky tu xuat hien nhieu nhat
# def getMax(str):
#     count = [0]* 256
#     max = -1
#     c = ' '
#     for i in str:
#         count[ord(i)] += 1
#     for i in str:
#         if max < count[ord(i)]:
#             max = count[ord(i)]
#             c = i
#     return c, max
# str = input('Nhap chuoi : ')
# print(getMax(str))

#diem yen ngua
def inputMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = int(input('matrix['+str(i)+']['+str(j)+'] = '))
def outputMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
# def minhang(matrix):
#     min = matrix[0][0]
#     for i in range(0,m):
#         min = matrix[i][0]
#         for j in range(0,n):
#             if matrix[i][j] < min:
#                 min = matrix[i][j]
#     return min
# def maxcot(matrix):
#     max = matrix[0][0]
#     for j in range(0, n):
#         max = matrix[0][j]
#         for i in range(0,m):
#             if matrix[i][j] > max:
#                 max = matrix[i][j]
#     return max

#ma tran ma phuong
def maphuong(matrix):
    #Tong duong cheo
    sum = 0
    for i in range(0,m):
        for j in range(0,n):
            if i == j:
                sum += matrix[i][j]
    #Tong hang
    for i in range(0,m):
        sum1 = 0
        for j in range(0,n):
            sum1 += matrix[i][j]
        if sum == sum1:
            flag = 1
        else:
            flag = 0
    #Tong cot
    for i in range(0,m):
        sum2 = 0
        for j in range(0,n):
            sum2 += matrix[j][i]
        if sum == sum2:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        print('Ma tran ma phuong')
    else:
        print('Ma tran khong phai la ma phuong')


m = int(input('Nhap so hang : '))
n = int(input('Nhap so cot : '))
matrix = [[0 for j in range(0,n)] for i in range(0,m)]
inputMatrix(matrix)
outputMatrix(matrix)
# print('Min hang ', minhang(matrix))
# print('Max cot ', maxcot(matrix))
maphuong(matrix)