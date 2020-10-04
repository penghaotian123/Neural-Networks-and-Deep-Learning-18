#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
a=np.loadtxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\BeijingPM20100101_20151231.csv',delimiter=',',dtype='str',skiprows=1)
beijingdata=np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]])
for i in a:
     if i[6]!='NA' and i[7]!='NA' and i[8]!='NA':
         beijingdata=np.append(beijingdata,[i],axis=0)
np.savetxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\beijing.csv',beijingdata,fmt='%s',delimiter=',')
#读取文件，只读第1,2,6,7,8，且跳过第一行的标题
beijingdata=np.loadtxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\beijing.csv',delimiter=',',dtype='int',skiprows=1,usecols=(1,2,6,7,8))
#所有的小时数
hours=beijingdata.shape[0]*3
#重度污染
heavy_count=np.sum(beijingdata[:,[2,3,4]]>150)
heavy_lu=heavy_count/hours
#中度污染
medium_count=np.sum(beijingdata[:,[2,3,4]]>75)-heavy_count
medium_lu=medium_count/hours
#轻度污染
light_count=np.sum(beijingdata[:,[2,3,4]]>35)-medium_count-heavy_count
light_lu=light_count/hours
#良好
good_count=np.sum(beijingdata[:,[2,3,4]]>0)-light_count-heavy_count-medium_count
good_lu=good_count/hours
print('不同程度的污染所占用的时间 重度：',heavy_lu,'中度：',medium_lu,'轻度：',light_lu,'良好：',good_lu)


# In[ ]:




