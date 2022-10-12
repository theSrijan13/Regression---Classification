#!/usr/bin/env python
# coding: utf-8

# In[2]:


# python program to draw squre using turtle
import turtle
skk=turtle.Turtle()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
turtle.done()


# In[3]:


#python programming to draw star using turtle
import turtle
star=turtle.Turtle()
star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()


# In[1]:


#python programming to draw spiral helix using turtle programming
import turtle
loadWindow=turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    
turtle.exitonclick()


# In[2]:


# python program to draw rainbow benzene using turtle programming
import turtle
colors = ["red","purple","blue","green","orange","yellow"]
t=turtle.Pen()
turtle.bgcolor('Black')
for x in range (360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)


# In[ ]:




