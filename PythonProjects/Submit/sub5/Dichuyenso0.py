def zeroMove(fileName):
    f = open('fileName.txt','r')
    list = f.read().split(' ')
    for i in range(len(list)):
        list[i] = int(list[i])
        if(list[i] == 0):
            j = i
            while j < len(list) - 1:
                list[j] = list[j + 1]
                j = j+1
            list[len(list) - 1] = 0
    print(list)
zeroMove('reverse.txt')
