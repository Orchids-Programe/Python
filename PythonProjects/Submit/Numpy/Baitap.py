# đổi chỗ hai cột trong mảng hai chiều
import numpy as np
arr = np.array(1,10).reshape(3,3)
print(arr)
arr[:,[1,0,2]]