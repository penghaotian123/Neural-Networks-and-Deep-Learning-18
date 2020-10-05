#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
import numpy as np
def sigmoid(z):
    return 1/(1+math.exp(-z))

class Perceptor(object):
    def __init__(self,w,b):
        self.w=w
        self.b=b
    def __call__(self,x):
        return sigmoid(np.dot(x,self.w)+self.b)
p=Perceptor([1,2,3],-4)
output=p([1,1,0])
print(output)


# In[ ]:




