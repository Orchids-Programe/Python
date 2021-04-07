import matplotlib.pyplot as plt
import time
import numpy as np
def selectionSort(A):
    for i in range(0,len(A)-1):
        min_index=i
        for j in range(i+1,len(A)):
            if A[j] < A[min_index]:
                min_index=j
        key=A[i]
        A[i]=A[min_index]
        A[min_index]=key
    return A

def CreateArray(n):
    return np.random.randint(100,size=n)

def calTime(n):
    start=time.time()
    selectionSort(CreateArray(n))
    return time.time()-start



n_length = [10,10**2,10**3,10**4]

time = [calTime(i) for i in n_length]

plt.scatter(n_length,time, s=10)

plt.title("Cal Time ")

plt.xlabel("Length")
plt.ylabel("Tỉme")
plt.show()