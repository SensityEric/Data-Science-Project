# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a= 'wiafe kwabena eric'

b = a.title()

#print(b)

#int,string,bool,float
#List,Tuple,Set and Dictionary

#LIST bot same and different data type and can be modify

myClass =[34,23,1,3,4,21,67]


myClass2=[4,23,1,3.5,4,1,7,"Sensity"]
                     

c = myClass + myClass2

#print(c)

#Tuple Once set they can not be change

list1 = [1,3,"Kwabena"]

tuple1 = tuple(list1)

#tuple1[2] = 'Sensity'

#Set - Prevent Duplicate of elements

list2 = ['Sensity','Kwabena','Sensity']

#set1 = set(list2)

#print(set1)

# Dictionary Asi=signment Key value Pairs

#dict1 = {"A":80,"B":75,'C':65}

#dict1["W"] = 200

import numpy as np

a= np.arange(15).reshape(3,5)

#print(a)

a1= np.array([[1,3,2,5,4,6],[1,14,5,4,3,6]])
a2= np.array([[2,9,2,6,4,12],[10,4,5,6,1,10]])
  
#print(a1+a2)
a4= a2.dot(a1.reshape(6,2))
           
#print(a4)

a5 = np.sin(a4)
print(a5)

a6 = np.cos(a4)
print(a6)

#print(a1.reshape(6,2))
#print(a1.transpose())
#print(b)

#print(type(b1))

#Quadratic Equatiion

a7 = a5**2 + a6**2

# print(a7) 


#np1 = np.ones(20)
#print(np1)
np2 =np.ones((6,2),dtype = int)

print(np2)




