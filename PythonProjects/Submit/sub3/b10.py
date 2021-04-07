from math import cos
import math
import random

def tichvector(u, v):
    return sum([u[i] * v[i] for i in range(0, len(u))])

def modun(u):
    x = [pow(i,2) for i in u]
    sx = round(sum(x), 4)
    return round(math.sqrt(sx), 4)

def ketqua(u , v):
    tuso = tichvector(u,v)
    mauso = modun(u) * modun(v)
    res = round(tuso / mauso, 4)
    print(res)

if __name__ == "__main__":
    print("cs.py")
    n = int(input('Nhap n = '))
    a = [[random.randint(-2,2) for i in range(0,15)] for i in range(0,n)]
    print(a)
    u = [random.randint(-2,2) for i in range(0,15)]
    v = [random.randint(-2,2) for i in range(0,15)]
    ketqua(u,v)