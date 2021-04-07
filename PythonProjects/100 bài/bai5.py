class String(object):
    def __init__(self):#method tạo chuỗi
        self.s = ''
    def getString(self):
        self.s = input('Nhap chuoi : ')
    def printString(self):
        print(self.s.upper())
strObj = String()
strObj.getString()
strObj.printString()