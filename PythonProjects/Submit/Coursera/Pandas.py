import pandas as pd
import numpy as np
import math
# # obj = pd.Series([2, 7, -5, 3])
# # print(obj)
# # print(obj.values)
# # print(obj.index)
# # obj2 = pd.Series([4,7,-5,3], index=['d', 'b', 'a', 'c'])
# # print(obj2)
# # print(obj2.index)
# # print(obj2['a'])
# # obj2['d'] = 6
# # print(obj2)
# # temp = obj2[['c', 'a', 'd']]
# # print(temp)
# # print(obj2[obj2>0])
# # print(obj2*2)
# # print(np.exp(obj2))
# # temp = 'e' in obj2
# # print(temp)
# # sdata= {'Ohio': 3500, 'Texas': 71000, ' Oregon': 16000, 'Utah': 5000}
# # obj3 = pd.Series(sdata)
# # print(obj3)
# # states =['Cali', 'Ohio', 'Oregon', 'Texas']
# # obj4 = pd.Series(sdata, index=states)
# # print(obj4)
# # print(pd.isnull(obj4))
# # print(pd.notnull(obj4))
# # print(obj4  + obj3)
# # temp = obj4.name = 'population'
# # print(temp)
# # temp1=obj4.index.name = 'state'
# # print(temp1)
# # print(obj4)
#
# data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada',' Nevada', 'Nevada'],
#         'year' : [2000, 2001, 2002, 2001, 2002, 2003],
#         'pop': [1.5,1.7, 3.6, 2.4, 2.9, 3.2]}
# # frame = pd.DataFrame(data)
# # print(frame)
# # print(frame.head())
# # temp = pd.DataFrame(data, columns=['year', 'state', 'pop'])
# # print(temp)
# # frame2 =  pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
# #                        index=['one', 'two', 'three', 'four', 'five', 'six'])
# # print(frame2)
# # print(frame2.columns)
# # print(frame2['state'])
# # print(frame2.year)
# # print(frame2.loc['three'])
# # frame2['debt']= 16.5
# # frame2['debt'] = np.arange(6.)
# # print(frame2)
# # val = pd.Series([-1.2, -1.5, -1.7],
# #                 index=['two', 'four', 'five'])
# # frame2['debt'] = val
# # print(frame2)
# pop = {'Nevada': {2001: 2.4, 2002: 2.9},
#        'Ohio' : {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# frame3 = pd.DataFrame(pop)
# frame3.T
# temp = pd.DataFrame(pop, index=[2001, 2002, 2003])
# # print(temp)
# pdata = {'Ohio' : frame3['Ohio'][:1],
#            'Nevada': frame3['Nevada'][:2]}
# print(pd.DataFrame(pdata))
# print(frame3.values)
# a = frame3.index.name = 'year'
# print(a)
# b = frame3.columns.name = ' state'
# print(b)

# obj = pd.Series(range(3), index=['a', 'b', 'c'])
# index = obj.index
# print(index)
# print(index[1:])

# labels = pd.Index(np.arange(3))
# print(labels)
# obj2 = pd.Series([1.5, -2.5, 0], index= labels)
# print(obj2)
# temp = obj2.index is labels
# print(temp)

# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# obj1 = pd.Series(sdata)
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj2 = pd.Series(sdata, index=states)
# obj3 = pd.isnull(obj2)
#
# print(math.isnan(obj2['California']))
# x=obj2['California']
# print(obj2['California'] != x)
# print(obj3['California'])
# print(obj2['California'] == None)

# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d','b','a','c'])
# print(obj)
# obj2 = obj.reindex(['a', 'b','c','d'])
# print(obj2)
# obj3 = pd.Series(['blue', 'yellow', 'purple'], index=[0,2,4])
# print(obj3)
# temp=obj3.reindex(range(6), method='ffill')
# print(temp)
# frame = pd.DataFrame(np.arange(9).reshape((3,3)),
#                      index=['a', 'b', 'c'],
#                      columns=['Ohio', 'Texas', 'Cali'])
# print(frame)
# frame2 = frame.reindex(['a', 'b','c','d'])
# # print(frame2)
# states = ['Texas', 'Utah', 'Cali']
# frame3=frame.reindex(columns = states)
# print(frame3)
# frame4 = frame.loc[['a', 'b', 'c', 'd'], states]
# print(frame4)

# obj = pd.Series(np.arange(5.), index=['a', 'b','c', 'd', 'e'])
# print(obj)
# obj2 = obj.drop(['c', 'd'])
# print(obj2)
#
# data = pd.DataFrame(np.arange(16).reshape((4,4)),
#                     index=['Ohio', 'cali', 'Utah', 'NY'],
#                     columns=['one', 'two', 'three', 'four'])
# temp = data.drop(['cali', 'NY'])
# temp1 = data.drop('two', axis=1)
# temp2 = data.drop(['two', 'four'], axis='columns')
# temp3 = obj.drop(['c'], inplace=True)
# print(temp3)

# obj = pd.Series(np.arange(4.), index=['a','b','c','d'])
# print(obj)
# temp = obj['b' : 'c']= 5
# print(temp)

# data = pd.DataFrame(np.arange(16).reshape((4,4)),
#                     index=['Ohio', 'Colorado', 'Utah', 'NY'],
#                     columns=['one', 'two', 'three', 'four'])
# print(data)
# temp=data.loc['Colorado', ['two', 'three']]
# print(temp)
# print(data.iloc[2,[3,0,1]])

# ser = pd.Series(np.arange(3.))
# # print(ser)
# ser2 = pd.Series(np.arange(3.), index=['a','b','c'])
# # print(ser2[-1])
# print(ser.loc[:1])
# print(ser[:1])
# print(ser.iloc[:1])

# s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a','c','d','e'])
# s2 = pd.Series([-2,1, 3.6, -1.5, 3.1], index=['a','c','e','f','g'])
# res = s1+s2
# print(res)

# df1 = pd.DataFrame(np.arange(12.).reshape((3,4)),
#                    columns=list('abcd'))
# df2 = pd.DataFrame(np.arange(20.).reshape((4,5)),
#                    columns=list('abcde'))
# print(df1)
# print(df2)
# temp = df2.loc[1, 'b'] = np.nan
# print(temp)
# print(df1+df2)
# print(df1.add(df2, fill_value= 0))
# print(1/df1)
# print(df1.rdiv(1))
# temp1 = df1.reindex(columns= df2.columns, fill_value=0)
# print(temp1)

# arr = np.arange(12.).reshape((3,4))
# print(arr)
# arr[0]
# print(arr[0])
# print(arr - arr[0])

# frame = pd.DataFrame(np.arange(12.).reshape((4,3)),
#                      columns=list('bde'),
#                      index=['Utah', 'Ohio', 'Texas', 'Oregon'])
# print(frame)
# print(np.abs(frame))
# f = lambda x: x.max() - x.min()
# # print(frame.apply(f))
# temp = frame.apply(f, axis="columns")
# # print(temp)
# def f(x):
#     return pd.Series([x.min(), x.max()], index=['min', 'max'])
# print(frame.apply(f))
# format = lambda x: '%.2f' % x
# temp1 = frame.applymap(format)
# print(temp1)

# obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
# print(obj.sort_index())
# frame = pd.DataFrame(np.arange(8).reshape((2,4)),
#                      index=['three', 'one'],
#                      columns=['d','a','b','c'])
# print(frame.sort_index())
# print(frame.sort_index(axis=1))
#
# print(frame.sort_index(axis=1, ascending=False))
# obj = pd.Series([4,np.nan,7,np.nan,-3,2])
# print(obj.sort_values())
# frame = pd.DataFrame({'b': [4,7,-3,2],
#                       'a': [0,1,0,1],
#                       'c': [-2,5,8,-2.5]})
# print(frame)
# print(frame.sort_values(by='b'))
# print(frame.sort_values(by = ['a','b']))
# print(frame.reindex(columns=['a','b']))
# obj = pd.Series([7,-5,7,4,3,0,4])
# print(obj.rank())
# print(obj.rank(method='first'))
# print(obj.rank(ascending=False, method='max'))
# print(frame)
# temp = frame.rank(axis='columns')
# print(temp)

# obj = pd.Series(range(5), index=['a','a','b','b','c'])
# print(obj)
# print(obj.index.is_unique)
# print(obj['a'])
# df = pd.DataFrame(np.random.randn(4,3), index=['a','a', 'b','b'])
# print(df)
# print(df.loc['b'])

# df = pd.DataFrame([['a', 'b'], ['c', 'd'],
#                    ['n', 'nn'], ['e', 'f']],
#                   index=['a', 'b', 'c', 'd'],
#                   columns=['one', 'two'])
# print(df)
# print(df.sum(axis='columns'))
# print(df.mean(axis = 'columns', skipna = False))
# obj = pd.Series(['a','a''b','c']*4)
# print(obj.describe())
# obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# uniques = obj.unique()
# print(uniques)
# temp = pd.value_counts(obj.values, sort=False)
# print(temp)
# print(obj.isin(['b','c']))
# s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
# s2 = pd.Series({'Alice' : 1, 'Jack':2, 'Molly' : 3})
# temp = s2.loc[1]
# print(s2[1])

df = pd.DataFrame([['Alice', 20 , 'F'],
                   ['Jack', 22, 'M']],
                  index=['Mathematics', 'Sociology'],
                  columns=['Name', 'Age', 'Gender'])
temp = df['Mathematics']
print(temp)

