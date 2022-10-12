#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
a=tk.Tk()
a.mainloop()


# In[2]:


b=tk.Tk()
b=tk.Label (text="Hello all students - 20 Batch", bg="blue", fg="white")
b.pack() # pack() method helps you to add widget on the windowb.mainloop()


# In[3]:


w=tk.Tk()w.title ("My Widget Window-Virendra")
b=tk.Button (w, text="Click Me", width=40, height=25, bg="red", fg="blue")
b.pack()
w.mainloop()


# In[ ]:


# Let us understand simple example of text box (text widget)
import tkinter as tk
t=tk.Tk()
t1=tk.Entry () # a blank text boxt1=tk.Entry (bg="blue", fg="white")t1.pack()t.mainloop()


# In[ ]:


mt=tk.Tk()
t2=tk.Text() # Text () method is used to represent multiline text boxt2.pack()mt.mainloop()


# In[ ]:


f=tk.Tk()
f1=tk.Frame() # blank frame and output will be similar to only plain windowf1.pack()f.mainloop()


# In[ ]:


f=tk.Tk()# creating two frames variables
f1=tk.Frame() 
f2=tk.Frame ()# we are creating two frames and adding two labels on them# master parameter will help you to decide which label belong to which 
framel1=tk.Label (master=f1, text="First Label")
l1.pack()
l2=tk.Label (master=f2, text="Second Label")
l2.pack()
f1.pack()
f2.pack()
f.mainloop()


# In[ ]:


f=tk.Tk()# creating two frames variables
f1=tk.Frame() 
f2=tk.Frame ()# we are creating two frames and adding two labels on them# master parameter will help you to decide which label belong to which 
framel1=tk.Label (master=f2, text="First Label")
l1.pack()
l2=tk.Label (master=f1, text="Second Label")
l2.pack()
f1.pack()
f2.pack()
f.mainloop()


# In[ ]:




