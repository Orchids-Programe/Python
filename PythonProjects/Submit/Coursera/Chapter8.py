import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Lap chi muc phan cap
data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
# print(data)
# print(data.index)
# print(data[['b','d']])
# print(data.loc[:, 2])
# print(data.stack())
# frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
#                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
#                      columns=[['Ohio', 'Ohio', 'Colorado'],
#                               ['Green', 'Red', 'Green']])
# print(frame)
# frame.index.names = ['key1', 'key2']

#sap xep cac cap do
# print(frame.swaplevel('key1', 'key2'))
# print(frame.sort_index(level=1))
# print(frame.swaplevel(0,1).sort_index(level=0))

#Thong ke tom tat theo cap do
# print(frame.sum(level = 'key2'))

#Lap chi muc voi cac cot cua dataframe
# frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
#                       'c': ['one', 'one', 'one', 'two', 'two',
#                             'two', 'two'],
#                       'd': [0, 1, 2, 0, 1, 2, 3]})
# print(frame)
# frame2 = frame.set_index(['c', 'd'])
# print(frame2)
# print(frame2.reset_index())

#Ket hop va hop nhat du lieu
#Tham gia kHung dl kieu co so du lieu
# df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data1': range(7)})
# df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
#                     'data2': range(3)})
# print(df1)
# print(df2)

# print(pd.merge(df1, df2, on='key'))
# df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                     'data1': range(7)})
# df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
#                     'data2': range(3)})
# temp = pd.merge(df3, df4, left_on='lkey', right_on='rkey')
# print(temp)
# print(pd.merge(df1, df2, how='outer'))

#Ghep noi doc theo truc
# arr = np.arange(12).reshape((3,4))
# print(arr)
# print(np.concatenate([arr, arr], axis=1))
# s1 = pd.Series([0, 1], index=['a', 'b'])
# s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
# s3 = pd.Series([5, 6], index=['f', 'g'])
# print(pd.concat([s1, s2, s3]))
# result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
# print(result)
# print(result.unstack())

#Xoay 'dai' sang dinh dang 'rong'
# print(pd.Period('01/12/2019', 'M') + 5)

frames = ['P2010', 'P2011', 'P2012', 'P2013','P2014', 'P2015']
df['AVG'] = df[frames].apply(lambda z: np.mean(z), axis=x)
result_df = df.drop(frames,axis=y)

