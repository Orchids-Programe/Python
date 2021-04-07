import os
def check_X(filename, x, path):
    list = open(filename,'r', encoding='utf-8')
    for line in list:
        if x in line:
            return (path + '/' + filename, line)
def searchInFiles(x, path):
    file = os.listdir(path)
    list = []
    for filename in file:
        if(check_X(filename,x,path) != None) :
            list.append(check_X(filename,x,path))
    re = sorted(list, key= lambda list: list[0])
    return re