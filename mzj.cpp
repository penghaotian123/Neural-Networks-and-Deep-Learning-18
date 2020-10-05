import math
import numpy as np
def jisuan(z):
    return 1/(1+math.exp(-z))
print(jisuan(0))
class Perceptor(object):
    def __init__(self,j,k):
        self.j=j
        self.k=k
    def __call__(self,x):
        return jisuan(np.dot(x,self.j)+self.k)
p=Perceptor([1,2,3],-4)
output=p([1,0,1])
print(output)
output=p([1,1,0])
print(output)


import numpy as np
import pandas as pd
df = pd.read_csv('BeijingPM20100101_20151231.csv', encoding='UTF-8', usecols=[1, 2, 3, 4, 5, 6, 7, 8])
data_arr=np.array(df.dropna(axis = 0))
hour_val=np.mean(data_arr[:,5:],axis=1)
print(data_arr)
# 总小时数
n_hours=hour_val.shape[0]
# 重度污染小时数以及占比
n_heavy_hours=hour_val[hour_val>150].shape[0]
print(n_heavy_hours/n_hours)
# 中度污染
n_medium_hours=hour_val[(hour_val>75) & (hour_val<=150)].shape[0]
print(n_medium_hours/n_hours)
# 轻度污染
n_light_hours = hour_val[(hour_val > 35) & (hour_val <= 75)].shape[0]
print(n_light_hours/n_hours)
# 优良空气
n_good_hours = hour_val[hour_val <= 35].shape[0]
print(n_good_hours/n_hours)


years=np.unique(data_arr[:,0])
print(years)
for year in years:
    # 获取当前年份数据
    year_data_arr=data_arr[data_arr[:,0]==year]  
     # 获取数据的月份
    month_list=np.unique(year_data_arr[:,1])
    print("-----分割-----")
    for month in month_list:
        # 获取月份的所有数据
        month_data_arr=year_data_arr[year_data_arr[:,1]==month]
           # 计算当前月份PM的均值
        mean_vals=np.mean(month_data_arr[:,5:],axis=0).tolist()
        print(mean_vals)
