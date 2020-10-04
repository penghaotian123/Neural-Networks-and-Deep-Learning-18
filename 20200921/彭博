import pandas as pd

import numpy as np
import math

def f(x,w):
    return np.dot(x,w)
y=f([1,0,1,1,0,1],[1,2,3,4,5,6])
b=1
z=y+b
def sigmoid(z):
    return 1/(1+math.exp(-z))
print(sigmoid(z))

file_path = "./5/BeijingPM20100101_20151231.csv"
df = pd.read_csv(file_path)
wr150 = df[(df['PM_Dongsi'] > 150) | (df['PM_Dongsihuan'] > 150) | (df['PM_Nongzhanguan'] > 150)].count().sum()
wr75 = df[(df['PM_Dongsi'] > 75) | (df['PM_Dongsihuan'] > 75) | (df['PM_Nongzhanguan'] > 75)].count().sum()
wr35 = df[(df['PM_Dongsi'] > 35) | (df['PM_Dongsihuan'] > 35) | (df['PM_Nongzhanguan'] > 35)].count().sum()
wr0 = df[(df['PM_Dongsi'] > 0) | (df['PM_Dongsihuan'] > 0) | (df['PM_Nongzhanguan'] > 0)].count().sum()

print('重度污染：{:.3f}'.format(wr150/wr0))
print('中度污染：{:.3f}'.format((wr75-wr150)/wr0))
print('轻度污染：{:.3f}'.format((wr35-wr75)/wr0))
print('良好：{:.3f}'.format((wr0-wr35)/wr0))
print('东四PM平均值：{:.3f}'.format(df['PM_Dongsi'].sum()/df['PM_Dongsi'].count()))
print('东四环PM平均值：{:.3f}'.format(df['PM_Dongsihuan'].sum()/df['PM_Dongsihuan'].count()))
print('农展馆PM平均值：{:.3f}'.format(df['PM_Nongzhanguan'].sum()/df['PM_Nongzhanguan'].count()))
