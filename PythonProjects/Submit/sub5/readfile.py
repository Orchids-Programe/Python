#f = open("demo.txt", 'r', encoding='utf-8')
#Đọc cả tệp
#print(f.read())
#print(f.readlines())
#Đọc n ký tự đầu
#print(f.read(5))
#Đọc từng dòng
# print(f.readline())
# print(f.readline())

#demo ghi dữ liệu
# f = open("demo.txt", 'a', encoding='utf-8')
# f.write('Them mot dong nuaaaaaa')
# f.close()
# f = open("demo.txt", 'r', encoding='utf-8')
# print(f.read())
# f.close()

#demo ghi đè
# f = open("demo.txt", 'w', encoding='utf-8')
# f.write('Dữ liệu đã bị đè lên')
# f.close()
# f = open("demo.txt", 'r', encoding='utf-8')
# print(f.read())
# f.close()
f = open("demo.txt", 'w', encoding='utf-8')
f.write('Dong 1\n Dong 2\n Dong 3')
f.close()
for line in open('demo.txt', 'r', encoding='utf-8'):
    print(line, end='')
print(open('demo.txt','r', encoding='utf-8'))
