#!/usr/bin/env python
# coding: utf-8

# In[14]:


li=[]
s=[1,1,5]
while True:
    li.append(int(input("enterlist elements::")))
    c=input("enter y/n::")
    c=c.lower()
    if not c.startswith('y'):
        break
    print(li)
    n=0
    
while n<len(li) and len(s)>0:
    if (li[n]==s[0]):
        s.pop()
    n+=1
if len(s)==0:
        print("match")
else:
        print("gone")


# In[ ]:




