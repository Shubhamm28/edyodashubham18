#!/usr/bin/env python
# coding: utf-8

# In[6]:


class pow_class:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(pow_class().pow(15,5))
print(pow_class().pow(18, 2))
print(pow_class().pow(144, 2))


# In[ ]:




