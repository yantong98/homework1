
# coding: utf-8

# In[7]:


a=input('Please type anything:')


# In[8]:


d=dict()


# In[10]:


for c in a:
    if(c in d):
        d[c]=(d[c]+1)
    else:
        d[c]=1
word=d.keys()
number=d.values()
for item in d.items():
    word,number=item
    print("'"+word+"'",":",number)

