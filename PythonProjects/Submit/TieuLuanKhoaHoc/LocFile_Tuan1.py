import pandas as pd
file1 = pd.read_csv('o201801.csv')
# print(file1.head())

b = pd.read_csv('r201801.csv')
# print(b.head())

c = pd.read_csv('fptshop.csv')

maShop = 30898
date1 = '2018-01-01'
date2 = '2018-01-06'
maSP = 'Apple ĐTDĐ iPhone 6s Plus 32GB Gold (A1687)_MN2X2VN/A'

#du lieu tieu thu san pham x tai shop
def saleShop(data, maSP):
    res = data[data['desc'] == maSP]
    arr = list[res['shop']]
    result = dict((x, arr.count(x)) for x in set(arr))
    # print(result)
    return result
#
# print('So luong san pham cua tung maSP ban duoc trong thang')
# print(saleShop(b, maSP))



#Doanh so tai 1 shop
def amountShop(data, maShop):
    value = data[(data['shop'] == maShop) & (data['status'] == 'F')]
    return sum(value['amount'])


print('Doanh so tai shop '+ str(maShop))
print(amountShop(file1, maShop))

#Doanh so ban hang tu date1 den date2
def amountShopDate(data, maShop, date1, date2):
    data['date'] = pd.to_datetime(data['date'])
    df = data.loc[(data['date'] >= date1) & (data['date'] <= date2)]
    value = df[(df['shop'] == maShop) & (df['status'] == 'F')]
    return sum(value['amount'])

print('Doanh so tai shop '+ str(maShop) + ' tu ' + date1 + ' toi ' +date2)
print(amountShopDate(file1, maShop, date1, date2))

def amountInProvince(data, maPr):
    d = list(data[data['Provinces'] == maPr]['Code'])
    total = sum(amountShop(file1, i) for i in d)
    return total
maPr = 'Hà Nội'
print('Doanh so cac shop tai '+maPr)
print(amountInProvince(c, maPr))

#dự báo các thứ trong tuần (dùng các hàm thời gian để tính ra thứ)
#cố định 1 cửa hàng và 1 sản phẩm, ta có 52 giá trị ứng với 52 tuần (tính theo số lượng sp)
#vẽ biểu đồ thể hiện
#mô phỏng lại cách quản lý cửa hàng
#nhìn vào các tuần trước để dự báo số lượng cho tuần 2
#sai số dự báo
#output ra cả năm của sai số của dự báo
#đưa ra 2 số liệu dự báo thừa và dự báo thiếu  (chết vốn và doanh thu)
#với cách dự báo hiện tại, thì bị vướt bao nhiêu và thiếu bao nhiêu trong 52 tuần
#nên đưa ra cách dự báo khác ví dụ lấy trung binh 2 tuần trước để đưa ra dự báo của tuần thứ 3
#yêu cầu: đưa ra 2 biểu đồ doanh số từng tuần của sản phẩm và 1 shop
# (của dự báo bằng tay của fpt và sai số dự báo của fpt)
#dự báo của cả hanoi và của 1 shop cụ thể (bằng biểu đồ)
#tiếp tục dự báo cho tỉnh
#tự phát triển các phương pháp của mình
#lưu ý dùng số lượng (quantity)
#lọc với những sản phẩm giá trị lớn (trên 3 triệu), k cần quá quan tâm tới những sp giá trị nhỏ
#
#dùng ip6 để dự báo cho ip7
#sử dụng cột khuyến mai, xem có ảnh hưởng tới quantity không? và sử dụng để dự báo (có thể dùng tới cả địa điểm của shop)
#yêu cầu tuần tới: làm biểu đồ tham số là maSP và MaLocation : tỉnh hoặc shop
#vì sử dụng tuần trước để dự báo cho tuần sau nên chỉ cần vẽ từ tuần 2 tới tuần 52
# sai số: thừa, thiếu, tổng thừa và tổng thiếu
#biểu diễn của các cách dự báo của fpt(tuần trước cho tuần sau) và của mình(trung bình 2 tuần trước cho tuần sau)
#dùng cho 10 ngày để dự báo
#dùng tuần sẽ có phân phối như nhau (còn 5 ngày thì có thể bao gồm cả t7 cn hoặc khoogn có)
#bỏ các dữ liệu mua nhiều sp 1 lúc( ví dụ mua 5 cái) đó là các đơn hàng dự án, chỉ quan tâm tới bán lẻ (hơn 2 sp thì sẽ là dự án)
# cần loc quantity > 2, k cần quan tâm tới các sp giá trị nhỏ, quan tâm tới các sản phẩm đem lại doanh thu lớn (list thầy gửi)
#top các sản phẩm có doanh thu lớn, theo số lượng (50 sp có doanh thu tốt nhất suy ra các sản phẩm chủ lực)