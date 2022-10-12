#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import _thread


# In[6]:


# using threading module
def thread_test(name,wait):
    i=0
    while(i<=3):
        time.sleep(wait)
        print("Running %s\n" %name)
        i=i+1
    print("%s has finished the execution " %name)
if __name__== "__main__" :
        _thread.start_new_thread(thread_test,("First thread",3))
        _thread.start_new_thread(thread_test,("Second thread",4))
        _thread.start_new_thread(thread_test,("Third thread",1))
    
        


# In[7]:


#using threading module

import threading
import time

class mythreadtest(threading.Thread):
    def __init__(self,id,name,i):
        threading.Thread.__init__(self)
        self.id=id
        self.name=name
        self.i=i
    def run(self):
        thread_test(self.name,self.i,5)
        print("%s has finished education "%self.name)
def thread_test(name,wait,i):
    
    while i:
        time.sleep(wait)
        print("Running %s\n "%name)
        i=i-1
        
if __name__ == "__main__":
    t1= mythreadtest(1,"First",5)
    t2= mythreadtest(2,"second",4)
    t3=mythreadtest(3,"third",7)
    # It will call run () method automatically for t1
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    


# In[ ]:




