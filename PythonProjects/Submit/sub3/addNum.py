def addNum(a,b):
    s = ''
    x = [str(i) for i in a]
    y = [str(i) for i in b]
    a = int(s.join(x))
    b = int(s.join(y))
    c = list(str(a+b))
    d = [int(i) for i in c]
    return d
