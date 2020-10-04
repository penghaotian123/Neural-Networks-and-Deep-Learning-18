#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas
import numpy as np

a=np.loadtxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\BeijingPM20100101_20151231.csv',delimiter=',',dtype='str',skiprows=1)
beijingdata=np.array([[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]])
for i in a:
     if i[1]=='2013'and i[6]!='NA' and i[7]!='NA' and i[8]!='NA':
         beijingdata=np.append(beijingdata,[i],axis=0)
np.savetxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\beijing.csv',beijingdata,fmt='%s',delimiter=',')
beijingdata=np.loadtxt('C:\\Users\\12700\\Desktop\\网课\\人工网络神经\\beijing.csv',delimiter=',',dtype='int',skiprows=1,usecols=(2,6,7,8))
ds=beijingdata[1].groupby(beijingdata[0]).mean()
dsh=beijingdata[2].groupby(beijingdata[0]).mean()
nzg=beijingdata[3].groupby(beijingdata[0]).mean()
print(ds,dsh,nzg)


# In[ ]:





# In[ ]:




