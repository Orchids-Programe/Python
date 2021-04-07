import re
import numpy as np
# string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
# result = re.findall('b[ao]t', string)
# print(result)
# a1 = np.random.rand(4)
# a2 = np.random.rand(4, 1)
# a3 = np.array([[1, 2, 3, 4]])
# a4 = np.arange(1, 4, 1)
# a5 = np.linspace(1 ,4, 4)
#
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print("------------")
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)
# print(a4.shape)
# print(a5.shape)

# old = np.array([[1, 1, 1], [1, 1, 1]])
# new = old
# new[0, :2] = 0
# print(old)
# s = 'ACAABAACAAAB'
# result = re.findall('A{1,2}', s)
# L = len(result)
# print(result)
# print(L)
text=r'''Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.
'''

pattern = X
print(len(re.findall(pattern,text)))