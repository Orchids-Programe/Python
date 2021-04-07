class Computer:
    def __init__(self):
        self.__maxPrice = 900
    def sell(self):
        print('Gia ban la : ',self.__maxPrice)
    def setMaxPrice(self, price):
        self.__maxPrice = price
c = Computer()
c.sell()
#đổi giá bán sản phẩm
# cách này sai : c.__maxPrice = 1000
c.setMaxPrice(1000)
c.sell()