x = int(input('Nhap x = '))
y = int(input('Nhap y = '))
def toado(x,y):
    if x == 0:
        if y == 0:
            print('Điểm đó trung tâm O')
        else:
            print('Điểm đó nằm trên trục Oy')
    else:
        if y != 0:
            print('Điểm đó nằm trên trục Ox')
        else:
            print('Điểm đó có tọa độ (x,y) = ', x, y)
            if x < 0:
                if y < 0:
                    print('Điểm nằm ở góc phần tư thứ III')
                else:
                    print('Điểm nằm ở góc phần tư thứ II')
            else:
                if y > 0:
                    print('Điểm nằm ở góc phần tư thứ I')
                else:
                    print('Điểm nằm ở góc phần tư thứ VI')
toado(x,y)
