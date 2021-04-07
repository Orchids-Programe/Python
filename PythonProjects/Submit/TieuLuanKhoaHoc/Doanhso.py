import pandas as pd
value = pd.read_csv('r201801.csv')
# print(value.head())

result = value[value['desc'] == 'ĐTDĐ Nokia 105 SS (2017) Black']
# print(result.head())
# print(len(result))

a = list(value['shop'])
res = dict((x,a.count(x)) for x in set(a))
print(res)
data = pd.read_csv('o201801.csv')
rs = data[data['shop'] == 30414]
val = rs[rs['status'] == 'F']
# print(val.head())
# print(rs.head())
# print(sum(val['amount']))
# print(sum(value['price']))

date1 = '2018-01-01'
date2 = '2018-01-06'
data['date'] = pd.to_datetime(data['date'])

df = data.loc[(data['date'] >= date1) & (data['date'] <= date2)]
print(df)


