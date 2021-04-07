n = int(input('Nhap so : '))
def dec2bin(n):
    s = '' #lưu kết quả phần dư
    while n: #liên tục phép chia hết cho 2
        s = str(n%2) + s #chia 2 hết phần dư
        n = n/2 #Gán lại n bằng phần nguyên của n /2
    print('Số nhị phân tương ứng la : '+str(s))
dec2bin(n)
