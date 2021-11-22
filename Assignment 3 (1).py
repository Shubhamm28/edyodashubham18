#!/usr/bin/env python
# coding: utf-8

# In[2]:


Sample_List=(8, 2, 3, 0, 7)
print(sum(Sample_List))


# In[9]:


sample_string="1234abcd"
print('expected output:',sample_string[7::-1])


# In[77]:


sample_string=('The quick Brow Fox')
a=0
b=0
for i in sample_string:
    if(i.islower()):
            a=a+1
    elif(i.isupper()):
            b=b+1
print("The number of lowercase characters is:")
print(a)
print("The number of uppercase characters is:")
print(b)

