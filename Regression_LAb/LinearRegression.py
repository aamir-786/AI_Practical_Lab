import pandas as pd
import numpy as np
df = pd.read_csv('D:\AI_Practical_Lab\Regression_LAb\Home_Prices.csv')
#print('Original Data',df)

print("Before NAN\n",df.head())
#df.fillna(np.random.randint(100), inplace=True)
#print("After NAN\n",df.head())

print("After DroPNA",df.dropna())

