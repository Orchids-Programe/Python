import numpy as np
from numpy import nan as NA
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
# cleaned = data.dropna()
# print(data)
# print(cleaned)
# print(data.dropna(how='all'))
# temp=data[4] = NA
# print(data.dropna(axis=1, how='all'))

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[4:, 1] = NA
df.iloc[2:, 2] = NA
# print(df.dropna())
# print(df.dropna(thresh=2))
# print(df.fillna(0))
# print(df.fillna({1: 0.5, 2:0}))
# print(df.fillna(method='ffill', limit=2))
# data = pd.Series([1., NA, 3.5, NA, 7])
# print(data.fillna(data.mean()))

# CHUYEN DOI DU LIEU
#Loai bo trung lap
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
# print(data.duplicated())
# print(data.drop_duplicates())
# data['v1'] = range(7)
# data.drop_duplicates(['k1'])
# print(data)
# temp = data.drop_duplicates(['k1', 'k2'], keep='last')
# print(temp)

#Chuyen doi du lieu bang ham hoac anh xa
# data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
#                               'Pastrami', 'corned beef', 'Bacon',
#                               'pastrami', 'honey ham', 'nova lox'],
#                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print(data)
meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}
# lowercased = data['food'].str.lower()
# print(lowercased)
# data['animal'] = lowercased.map(meat_to_animal)
# data['food'].map(lambda x: meat_to_animal[x.lower()])
# print(data)

#Thay the gia tri
# data = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(data)
# print(data.replace([-999,-1000], np.nan))
#Doi ten chi muc
#Roi rac
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
# print(cats)
# print(cats.codes)
# print(cats.categories)
# print(pd.value_counts(cats))
# data = np.random.randn(1000)  # Normally distributed
# cats = pd.qcut(data, 4)  # Cut into quartiles
# print(cats)
# print(pd.value_counts(cats))

#Phat hien va loc ngoai le
# data = pd.DataFrame(np.random.randn(1000, 4))
# print(data.describe())
# print(np.sign(data).head())

#Hoan vi va lay mau ngau nhien
# df = pd.DataFrame(np.arange(5*4).reshape((5,4)))
# sampler = np.random.permutation(5)
# print(df)
# print(sampler)
# print(df.take(sampler))
# print(df.sample(n=3))
# choices = pd.Series([5,7,-1,6,4])
# draws = choices.sample(n=10, replace=True)
# print(draws)

#Bien gia
# df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
#                    'data1': range(6)})
# print(df)
# print(pd.get_dummies(df['key']))

#Thao tac chuoi
#Phuong phap doi tuong chuoi
# val = 'a,b, guido'
# print(val.split(','))
# pieces = [x.strip() for x in val.split(',')]
# print(pieces)
# first, second, third = pieces
# first + '::' + second + '::' + third
# '::'.join(pieces)
# 'guido' in val
# print(val.index(','))
# print(val.find(':'))
# print(val.count(','))
# temp=val.replace(',', ':')
# print(temp)

#Regex
import re
# text = 'foo    bar\t baz   \tquz'
# print(re.split('\s+', text))
# print(text)
# regex = re.compile('\s+')
# print(regex.split(text))
# print(regex.findall(text))
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall( text))