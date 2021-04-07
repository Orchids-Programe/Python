import locale
from itertools import compress
def splitName(str):
    w = str.split(' ')
    if(len(w) == 1):
        return ['', w[0]]
    else:
        x = w[0] # họ đệm
        for i in range(1, len(w) - 1):
            x += ' '+w[i]
        return [x, w[len(w) - 1]] #return 'hodem' 'ten'
n = int(input('Nhap so n = '))
name = ['' for i in range(0,n)]
for i in range(0,n):
    name[i] = (str) (input()) #nhập họ và ten

#provinces=['Hải Dương Ánh','Hưng Yên Anh','Hà Nội Dăng','Hải Phòng Hiếu','Hậu Giang Nhung','Hòa Bình Thưởng','Hà Nam Linh',
#'Hà Giang Ninh','Hà Tĩnh W', 'Lào Cai Z', 'Quảng Ninh Đăng']

#sname = [['',''] for i in range(0,len(provinces))]
#for i in range(0, len(provinces)):
#    sname[i] = splitName(provinces[i])
name.sort(key = lambda x: (locale.strxfrm(x[1])))
print(name)
locale.setlocale(locale.LC_COLLATE, 'vi')

#sname.sort(key = lambda x: (locale.strxfrm(x[1])))
#print(sname)