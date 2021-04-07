# sothunhat=input("Nhap so thu 1 : ")
# sothuhai=input("Nhap so thu 2 : ")
# try:
#     so1=int(sothunhat)
#     so2=int(sothuhai)
#     tong= so1 + so2
#     print("Tong hai so la : ", tong)
# except:
#     print("Dinh dang dau vao khong hop le!!")

# ten=input("Nhap ten : ")
# print('Xin', 'chao', 'toi', 'ten' , 'la ', ten, sep='==')

# sothapphan=input("Nhap so thap phan : ")
# try:
#     nhapso=int(sothapphan)
#     print("so thap phan %d trong he b2at phan la : %o" % (nhapso, nhapso))
# except:
#     print("Nhap dau vao sai dinh dang!!")
# firstname = 'Ha Vu Long la ten cua toi'.split(' ')[0]
# lastname = 'Moi nguoi thuong goi toi la Long'.split(' ')[-1]
# fullname = firstname +' '+ lastname
# print(fullname)
# x = {'nguoi1': 19, 'linh2': 18}
# # for tuoi in x.values():
# #     print(tuoi)
# person = '{} thi {} trong khi {} nen tong so tuoi cua hai nguoi la {}'
# print(person.format(x['nguoi1'], x['linh2'],x['nguoi1'], x['nguoi1']+x['linh2']))
# from PIL import Image
# from IPython.display import display
# img = Image.open('C:\\Users\\ABC\\Downloads\\2.jpg')
# display(img)
import re

# text = "Long rat la dep zaiii. Long 18 tuoi. Long o son tay"
# # if re.search('dep', text):
# #     print('Yes, Long is very handsome')
# # else:
# #     print('No, Long is very very handsome')
#
# re.split("Long", text)
# re.findall("Long", text)
text = "Long works diligantly. Long gets good grades. Our student Long is succesful"
re.search("^Long", text, flags=0)
