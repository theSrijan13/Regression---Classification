#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating a class named Angle
class Angle:
    def __init__(self,radius,angle):
        #initializing radius and angle
        self.radius=radius
        self.angle=angle
     #creating a function name Archlength
    def Archlength(self):
        # formual to determine archlength is given below
        Al=(2*3.14*self.radius)*(self.angle/360)
        print("The Archlength of the angle is : ",Al)
A1=Angle(5,120)
#calling the function
A1.Archlength()


# In[2]:


#creating a class named Rectangle
class Rectangle:
    def __init__(self,length,breadth):
    #initializing length and breadth
        self.length=length
        self.breadth=breadth
    #creating function Area 
    def Area(self):
        area=self.length*self.breadth
        print("Area is ",area)
#creating an object of the class
r1=Rectangle(5,7)
r2=Rectangle(7,8)
#calling the function
r1.Area()
r2.Area()


# In[4]:


#creating a class named BankAccount
class BankAccount:
    def __init__(self):
    #intializing balance to 0
        self.balance=0
    # creating a function name deposit
    def deposit(self):
        amount=float(input("enter the amount to be deposited"))
        self.balance+=amount
        print("amount deposited ",amount)
     # creating a function name withdraw
    def withdraw(self):
        amount=float(input("enter the amount to be withdrawn" ))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw ",amount)
        else:
            print("Insufficient Balance")
    #creating a function show balance to show the balance
    def showBalance(self):
        print("Available Balance ",self.balance)
#creating an object of the class
Ba=BankAccount()
#calling the function
Ba.deposit()
Ba.withdraw()
Ba.showBalance()


# In[5]:


# Defining parent class
class Parent():     
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Child(Parent):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)        
#Creating object of the class
obj1 = Parent()
obj2 = Child()
# calling the function  
obj1.show()
obj2.show()


# In[6]:


#creating Base class 1
class Calculation1:
    def summ(self,a,b):
        return a+b
#creating Base class 2
class Calculation2:
    def multiply(self,a,b):
        return a*b
#creating Derived class
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b
#creating the object for derived class
d=Derived()
#calling the function
print(d.summ(10,20))
print(d.multiply(10,20))
print(d.Divide(10,20))


# In[1]:


import math
# taking input of centre,radius and any point
x1=float(input("enter the x cordinate of centre : "))
y1=float(input("enter the y coordinate of centre :"))
r=float(input("enter the radius of circle : "))
x2=float(input("enter the x cordinate of point : "))
y2=float(input("enter the y cordinate of point : "))
# check for distance between point and center point of circle
pc=math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
#checking whether the point lies inside,outside of the circle through if else condition 
if(pc>r):
    print("Point lies outside the circle")
elif(pc<r):
    print("Point lies inside the circle")
elif(pc==r):
    print("Point lies in the boundry of circle")
else:
    print("Wrong entry")
    


# In[6]:





# In[9]:


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __sub__(self,other):
        x=self.x - other.x
        y=self.y - other.y
        


p1 = Point(5,2)
p2 = Point(4,1)

print(p1+p2)
print(p1-p2)


# In[9]:


#importing the pandas library
import pandas as pd
# determining the location of text file
read_file = pd.read_csv (r'C:\Users\HP\Documents\ss.txt')
# converting the text file to csv file
read_file.to_csv (r'C:\Users\HP\Documents\ss.csv', index=None)


# In[12]:


import pickle

# write python dict to a file
mydict = {'Srijan': 1, 'Virend': 2, 'Surya': 3}
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

# read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()

print(mydict)
print(mydict2)


# In[15]:


# importing panda library
import pandas as pd
  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("ss.txt")
  
# storing this dataframe in a csv file
dataframe1.to_csv('ss.csv', index = None)


# In[ ]:




