from _operator import itemgetter
aList = []
print('Nhap danh sach theo thu tu Ten Tuoi Diem')
while True:
    t = input('Them bo : ').strip()
    if not t:
        break
    aList.append(tuple(t.split(',')))
aList.sort(key= itemgetter(0,1,2), reverse=False);
print(aList)