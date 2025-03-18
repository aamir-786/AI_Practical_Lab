#import dirtydata.csv

import pandas as pd
df = pd.read_csv('dirtydata.csv')
print('Original Data',df)
df.info()
df.describe()
df.tail()
df.head()
df.columns
df.shape
df.dtypes
df.isnull().sum()
print("Data after removing duplicates", df.drop_duplicates())
print("Data after removing missing values", df.describe())
print("Data after removing missing values", df.dropna())
print("Data after replacing missing values Fillna", df.fillna(130))


#print("Data after replacing missing values", df.fillna(int(130),inplace=True))
#print("Data after replacing missing values with mean", df.fillna(df.mean(),inplace=True))

