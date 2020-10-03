#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
def sigmoid(z):
    return 1/(1+math.exp(-z))
print(sigmoid(0))


# In[5]:


import numpy as np
class Perceptor(object):
    def __init__(self,w,b):
        self.w=w
        self.b=b
    def __call__(self,x):
        return sigmoid(np.dot(x,self.w)+self.b)
p=Perceptor([1,2,3],-4)
output=p([1,0,1])
print(output)


# In[ ]:


import csv
import os
import configparser
import numpy as np
def load_data(data_file,usecols):
    data=[]
    with open("C:\user\liqianyi\人工神经网络\BeijingPM20100101_20151231.csv",'r') as csvfile:
        data_reader=csv.DictReader(csvfile)
        for row in data_reader:
            row_data=[]
            for col in usecols:
                str_val=row[col]
                row_data.append(float(str_val) if str_val!='NA' else np.nan)
                if not any(np.isnan(row_data)):
                    data.append(row_data)
                    data_arr=np.array(data)
                    return data_arr
def get_polluted_perc(data_arr):
    hour_val=np.mean(data_arr[:,6:8],axis=1)
    n_hours=hour_val.shape[0]
    n_heavy_hours=hour_val[hour_val>150].shape[0]
    n_medium_hours=hour_val[(hour_val>75) & (hour_val<=150)].shape[0]
    n_light_hours = hour_val[(hour_val > 35) & (hour_val <= 75)].shape[0]
    n_good_hours = hour_val[hour_val <= 35].shape[0]
    polluted_perc_list= [n_heavy_hours / n_hours, n_medium_hours / n_hours,
                          n_light_hours / n_hours, n_good_hours / n_hours]
    return polluted_perc_list
def save_stats_to_csv(results_arr,save_file,headers):
    with open(save_file,'w',newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(headers)
        for row in results_arr.tolist():
            writer.writerow(row)
def main():
    polluted_state_list=[]
    for city_name,(filename,cols) in config.data_config_dict.items():
        data_file=os.path.join(config.dataset_path,filename)
        usecols=config.common_cols+['PM_'+col for col in cols]
        data_arr=load_data(data_file,usecols)
        print('{}共有{}行有效数据'.format(city_name,data_arr.shape[0]))
        print('{}的前10行数据：'.format(city_name))
        print(data_arr[:10])
        polluted_perc_list=get_polluted_perc(data_arr)
        polluted_state_list.append([city_name]+polluted_perc_list)
        print('{}的污染小时数百分比{}'.format(city_name,polluted_perc_list))
        results_arr=get_avg_pm_per_month(data_arr)


# In[ ]:





# In[ ]:





# In[ ]:




