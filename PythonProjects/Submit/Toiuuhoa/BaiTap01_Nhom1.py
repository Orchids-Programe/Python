#Nhom 1

#Bai 4
import  math
import numpy as np
import matplotlib.pyplot as plt

def get_type_of_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('VSN')
            else:
                print('VN')
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print('VN')
        elif delta == 0:
            x = -b / (2 * a)
            print('PT co nghiem ', x)
        else:
            x1 = float((-b - math.sqrt(delta)) / 2 * a)
            x2 = float((-b + math.sqrt(delta)) / 2 * a)
            print(x1, x2)

a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))
get_type_of_quadratic(a,b,c)

def f(x):
    return a*x*x + b*x + c

x1 = np.linspace(start=-3, stop=3, num=100)
plt.xlim(-5, 5)
plt.ylim(-8, 8)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x1, f(x1))
plt.show()


# Bai 4
#Tao ma tran co n
print("Nhap n : ")
n = int(input())
print("Ma tran A la : ")
A = np.random.randint(11, size=(n, n))
print(A)

#Nghich dao
print("Ma tran nghich dao la : ")
B = np.linalg.inv(A)
print(B)

