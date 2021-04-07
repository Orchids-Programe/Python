while True:
    try:
        x = int(input('Nhap so nguyen : '))
        break
    except ValueError:
        print('Can nhap vao so nguyen')