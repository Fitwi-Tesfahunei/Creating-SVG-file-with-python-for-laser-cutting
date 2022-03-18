# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:57:25 2022

@author: User
"""
import numpy as np


"""User Defined Inputs"""

# Dimensions
# Multiply the values by 3.78 to convert them from mm to pixels
w = input("Enter box width in mm:\n")
w = float(w)
w = w*3.78;
if w<70*3.78:
    raise Exception("Error: Please enter dimensions over 70mm")
elif w>150*3.78:
    raise Exception("Error: Please enter height less than 150mm")
l = input("Enter box length in mm:\n")
l = float(l)
l = l*3.78;
if l<70*3.78:
    raise Exception("Error: Please enter dimensions over 70mm")
elif l>150*3.78:
    raise Exception("Error: Please enter height less than 150mm")
h = input("Enter box height in mm:\n")
h = float(h)
h = h*3.78;
if h<70*3.78:
    raise Exception("Error: Please enter dimensions over 70mm")
elif h>150*3.78:
    raise Exception("Error: Please enter height less than 150mm")


#Input Texts
T = input("Enter your initials: \n")
if len(T)==0:
    raise Exception("Error: Please enter your initials.")
elif len(T)>10:
    raise Exception("Error: You can't enter more than 10 characters.")
E = input("Write a text of your liking here:\n")
if len(E)==0:
    raise Exception("Error: Please write a text.")
elif len(E)>10:
    raise Exception("Error: You can't enter more than 10 characters.")
A = input("Write a text of your liking here:\n")
if len(A)==0:
    raise Exception("Error: Please write a text.")
elif len(A)>10:
    raise Exception("Error: You can't enter more than 10 characters.")


"""Constant Parameters"""

t = 3*3.78 # thickness of the acrylic
db = 2.5*3.78 # bolt diameter
r = db/2 # bolt radius
r = str(r)
d1 = 2*3.78
d2 = 4*3.78;
t1 = 2*3.78
t2 = 1.2*3.78
g = 10*3.78;
x = 10 # gap
r_f = 15*3.78/2 #for opening the box


"""Face 1"""

Face_1 = [t,0,t,h/3-g/2,0,h/3-g/2,0,h/3+g/2,t,h/3+g/2,t,2*h/3-g/2,0,2*h/3-g/2,0,2*h/3+g/2,t,2*h/3+g/2,t,h,
          
          l/3-g/2,h,l/3-g/2,h-t,
          l/3-db/2,h-t,l/3-db/2,h-t-d1,l/3-db/2-t2,h-t-d1,l/3-db/2-t2,h-t-d1-t1,l/3-db/2,h-t-d1-t1,l/3-db/2,h-t-d1-t1-d2,
          l/3+db/2,h-t-d1-t1-d2,l/3+db/2,h-t-d1-t1,l/3+db/2+t2,h-t-d1-t1,l/3+db/2+t2,h-t-d1,l/3+db/2,h-t-d1,l/3+db/2,h-t,
          l/3+g/2,h-t,l/3+g/2,h,2*l/3-g/2,h,2*l/3-g/2,h-t,
          2*l/3-db/2,h-t,2*l/3-db/2,h-t-d1,2*l/3-db/2-t2,h-t-d1,2*l/3-db/2-t2,h-t-d1-t1,2*l/3-db/2,h-t-d1-t1,2*l/3-db/2,h-t-d1-t1-d2,
          2*l/3+db/2,h-t-d1-t1-d2,2*l/3+db/2,h-t-d1-t1,2*l/3+db/2+t2,h-t-d1-t1,2*l/3+db/2+t2,h-t-d1,2*l/3+db/2,h-t-d1,2*l/3+db/2,h-t,
          2*l/3+g/2,h-t,2*l/3+g/2,h,l-t,h,
          
          l-t,2*h/3+g/2,l,2*h/3+g/2,l,2*h/3-g/2,l-t,2*h/3-g/2,l-t,h/3+g/2,l,h/3+g/2,l,h/3-g/2,l-t,h/3-g/2,l-t,0,
          
          2*l/3+g/2,0,2*l/3+g/2,t,2*l/3-g/2,t,2*l/3-g/2,0,l/3+g/2,0,l/3+g/2,t,l/3-g/2,t,l/3-g/2,0]

Face_1 = str(Face_1)[1:-1]

cx1_1 = t/2
cx1_1 = str(cx1_1)
cy1_1 = h/3
cy1_1 = str(cy1_1)
cx2_1 = t/2
cx2_1 = str(cx2_1)
cy2_1 = 2*h/3
cy2_1 = str(cy2_1)
cx3_1 = l-t/2
cx3_1 = str(cx3_1)
cy3_1 = h/3
cy3_1 = str(cy3_1)
cx4_1 = l-t/2
cx4_1 = str(cx4_1)
cy4_1 = 2*h/3
cy4_1 = str(cy4_1)


"""Face 2"""

Face_2 = [l+x+l+x,0,l+x+l+x,h/3-g/2,t+l+x+l+x,h/3-g/2,
          t+l+x+l+x,h/3-db/2,t+d1+l+x+l+x,h/3-db/2,t+d1+l+x+l+x,h/3-db/2-t2,t+d1+t1+l+x+l+x,h/3-db/2-t2,t+d1+t1+l+x+l+x,h/3-db/2,t+d1+t1+d2+l+x+l+x,h/3-db/2,
          t+d1+t1+d2+l+x+l+x,h/3+db/2,t+d1+t1+l+x+l+x,h/3+db/2,t+d1+t1+l+x+l+x,h/3+db/2+t2,t+d1+l+x+l+x,h/3+db/2+t2,t+d1+l+x+l+x,h/3+db/2,t+l+x+l+x,h/3+db/2,
          t+l+x+l+x,h/3+g/2,0+l+x+l+x,h/3+g/2,0+l+x+l+x,2*h/3-g/2,t+l+x+l+x,2*h/3-g/2,
          t+l+x+l+x,2*h/3-db/2,t+d1+l+x+l+x,2*h/3-db/2,t+d1+l+x+l+x,2*h/3-db/2-t2,t+d1+t1+l+x+l+x,2*h/3-db/2-t2,t+d1+t1+l+x+l+x,2*h/3-db/2,t+d1+t1+d2+l+x+l+x,2*h/3-db/2,
          t+d1+t1+d2+l+x+l+x,2*h/3+db/2,t+d1+t1+l+x+l+x,2*h/3+db/2,t+d1+t1+l+x+l+x,2*h/3+db/2+t2,t+d1+l+x+l+x,2*h/3+db/2+t2,t+d1+l+x+l+x,2*h/3+db/2,t+l+x+l+x,2*h/3+db/2,
          t+l+x+l+x,2*h/3+g/2,0+l+x+l+x,2*h/3+g/2,0+l+x+l+x,h,
          
          w/3-g/2+l+x+l+x,h,w/3-g/2+l+x+l+x,h-t,
          w/3-db/2+l+x+l+x,h-t,w/3-db/2+l+x+l+x,h-t-d1,w/3-db/2-t2+l+x+l+x,h-t-d1,w/3-db/2-t2+l+x+l+x,h-t-d1-t1,w/3-db/2+l+x+l+x,h-t-d1-t1,w/3-db/2+l+x+l+x,h-t-d1-t1-d2,
          w/3+db/2+l+x+l+x,h-t-d1-t1-d2,w/3+db/2+l+x+l+x,h-t-d1-t1,w/3+db/2+t2+l+x+l+x,h-t-d1-t1,w/3+db/2+t2+l+x+l+x,h-t-d1,w/3+db/2+l+x+l+x,h-t-d1,w/3+db/2+l+x+l+x,h-t,
          w/3+g/2+l+x+l+x,h-t,w/3+g/2+l+x+l+x,h,2*w/3-g/2+l+x+l+x,h,2*w/3-g/2+l+x+l+x,h-t,
          2*w/3-db/2+l+x+l+x,h-t,2*w/3-db/2+l+x+l+x,h-t-d1,2*w/3-db/2-t2+l+x+l+x,h-t-d1,2*w/3-db/2-t2+l+x+l+x,h-t-d1-t1,2*w/3-db/2+l+x+l+x,h-t-d1-t1,2*w/3-db/2+l+x+l+x,h-t-d1-t1-d2,
          2*w/3+db/2+l+x+l+x,h-t-d1-t1-d2,2*w/3+db/2+l+x+l+x,h-t-d1-t1,2*w/3+db/2+t2+l+x+l+x,h-t-d1-t1,2*w/3+db/2+t2+l+x+l+x,h-t-d1,2*w/3+db/2+l+x+l+x,h-t-d1,2*w/3+db/2+l+x+l+x,h-t,
          2*w/3+g/2+l+x+l+x,h-t,2*w/3+g/2+l+x+l+x,h,w+l+x+l+x,h,
          
          w+l+x+l+x,2*h/3+g/2,w-t+l+x+l+x,2*h/3+g/2,
          w-t+l+x+l+x,2*h/3+db/2,w-t-d1+l+x+l+x,2*h/3+db/2,w-t-d1+l+x+l+x,2*h/3+db/2+t2,w-t-d1-t1+l+x+l+x,2*h/3+db/2+t2,w-t-d1-t1+l+x+l+x,2*h/3+db/2,w-t-d1-t1-d2+l+x+l+x,2*h/3+db/2,
          w-t-d1-t1-d2+l+x+l+x,2*h/3-db/2,w-t-d1-t1+l+x+l+x,2*h/3-db/2,w-t-d1-t1+l+x+l+x,2*h/3-db/2-t2,w-t-d1+l+x+l+x,2*h/3-db/2-t2,w-t-d1+l+x+l+x,2*h/3-db/2,w-t+l+x+l+x,2*h/3-db/2,
          w-t+l+x+l+x,2*h/3-g/2,w+l+x+l+x,2*h/3-g/2,w+l+x+l+x,h/3+g/2,w-t+l+x+l+x,h/3+g/2,
          w-t+l+x+l+x,h/3+db/2,w-t-d1+l+x+l+x,h/3+db/2,w-t-d1+l+x+l+x,h/3+db/2+t2,w-t-d1-t1+l+x+l+x,h/3+db/2+t2,w-t-d1-t1+l+x+l+x,h/3+db/2,w-t-d1-t1-d2+l+x+l+x,h/3+db/2,
          w-t-d1-t1-d2+l+x+l+x,h/3-db/2,w-t-d1-t1+l+x+l+x,h/3-db/2,w-t-d1-t1+l+x+l+x,h/3-db/2-t2,w-t-d1+l+x+l+x,h/3-db/2-t2,w-t-d1+l+x+l+x,h/3-db/2,w-t+l+x+l+x,h/3-db/2,
          w-t+l+x+l+x,h/3-g/2,w+l+x+l+x,h/3-g/2,w+l+x+l+x,0,l+x+l+x+2*w/3+g/2,0,l+x+l+x+2*w/3+g/2,t,l+x+l+x+2*w/3-g/2,t,l+x+l+x+2*w/3-g/2,0,
          l+x+l+x+w/3+g/2,0,l+x+l+x+w/3+g/2,t,l+x+l+x+w/3-g/2,t,l+x+l+x+w/3-g/2,0,]

Face_2 = str(Face_2)[1:-1]


"""Face 3"""

Face_3 = [t,t+h+x,t,l/3-g/2+h+x,0,l/3-g/2+h+x,0,l/3+g/2+h+x,t,l/3+g/2+h+x,t,2*l/3-g/2+h+x,0,2*l/3-g/2+h+x,0,2*l/3+g/2+h+x,t,2*l/3+g/2+h+x,t,l-t+h+x,
          w/3-g/2,l-t+h+x,w/3-g/2,l+h+x,w/3+g/2,l+h+x,w/3+g/2,l-t+h+x,2*w/3-g/2,l-t+h+x,2*w/3-g/2,l+h+x,2*w/3+g/2,l+h+x,2*w/3+g/2,l-t+h+x,w-t,l-t+h+x,
          w-t,2*l/3+g/2+h+x,w,2*l/3+g/2+h+x,w,2*l/3-g/2+h+x,w-t,2*l/3-g/2+h+x,w-t,l/3+g/2+h+x,w,l/3+g/2+h+x,w,l/3-g/2+h+x,w-t,l/3-g/2+h+x,w-t,t+h+x,
          2*w/3+g/2,t+h+x,2*w/3+g/2,0+h+x,2*w/3-g/2,0+h+x,2*w/3-g/2,t+h+x,w/3+g/2,t+h+x,w/3+g/2,0+h+x,w/3-g/2,0+h+x,w/3-g/2,t+h+x]

Face_3 = str(Face_3)[1:-1]

cx1_3 = w/3
cx1_3 = str(cx1_3)
cy1_3 = t/2+h+x
cy1_3 = str(cy1_3)
cx2_3 = 2*w/3
cx2_3 = str(cx2_3)
cy2_3 = t/2+h+x
cy2_3 = str(cy2_3)
cx3_3 = w-t/2
cx3_3 = str(cx3_3)
cy3_3 = l/3+h+x
cy3_3 = str(cy3_3)
cx4_3 = w-t/2
cx4_3 = str(cx4_3)
cy4_3 = 2*l/3+h+x
cy4_3 = str(cy4_3)
cx5_3 = 2*w/3
cx5_3 = str(cx5_3)
cy5_3 = l-t/2+h+x
cy5_3 = str(cy5_3)
cx6_3 = w/3
cx6_3 = str(cx6_3)
cy6_3 = l-t/2+h+x
cy6_3 = str(cy6_3)
cx7_3 = t/2
cx7_3 = str(cx7_3)
cy7_3 = 2*l/3+h+x
cy7_3 = str(cy7_3)
cx8_3 = t/2
cx8_3 = str(cx8_3)
cy8_3 = l/3+h+x
cy8_3 = str(cy8_3)


"""Face 4"""

Face_4 = [w+x+l+x+l+x,0,w+x+l+x+l+x,h/3-g/2,t+w+x+l+x+l+x,h/3-g/2,
          t+w+x+l+x+l+x,h/3-db/2,t+d1+w+x+l+x+l+x,h/3-db/2,t+d1+w+x+l+x+l+x,h/3-db/2-t2,t+d1+t1+w+x+l+x+l+x,h/3-db/2-t2,t+d1+t1+w+x+l+x+l+x,h/3-db/2,t+d1+t1+d2+w+x+l+x+l+x,h/3-db/2,
          t+d1+t1+d2+w+x+l+x+l+x,h/3+db/2,t+d1+t1+w+x+l+x+l+x,h/3+db/2,t+d1+t1+w+x+l+x+l+x,h/3+db/2+t2,t+d1+w+x+l+x+l+x,h/3+db/2+t2,t+d1+w+x+l+x+l+x,h/3+db/2,t+w+x+l+x+l+x,h/3+db/2,
          t+w+x+l+x+l+x,h/3+g/2,w+x+l+x+l+x,h/3+g/2,0+w+x+l+x+l+x,2*h/3-g/2,t+w+x+l+x+l+x,2*h/3-g/2,
          t+w+x+l+x+l+x,2*h/3-db/2,t+d1+w+x+l+x+l+x,2*h/3-db/2,t+d1+w+x+l+x+l+x,2*h/3-db/2-t2,t+d1+t1+w+x+l+x+l+x,2*h/3-db/2-t2,t+d1+t1+w+x+l+x+l+x,2*h/3-db/2,t+d1+t1+d2+w+x+l+x+l+x,2*h/3-db/2,
          t+d1+t1+d2+w+x+l+x+l+x,2*h/3+db/2,t+d1+t1+w+x+l+x+l+x,2*h/3+db/2,t+d1+t1+w+x+l+x+l+x,2*h/3+db/2+t2,t+d1+w+x+l+x+l+x,2*h/3+db/2+t2,t+d1+w+x+l+x+l+x,2*h/3+db/2,t+w+x+l+x+l+x,2*h/3+db/2,
          t+w+x+l+x+l+x,2*h/3+g/2,0+w+x+l+x+l+x,2*h/3+g/2,0+w+x+l+x+l+x,h,
          
          w/3-g/2+w+x+l+x+l+x,h,w/3-g/2+w+x+l+x+l+x,h-t,
          w/3-db/2+w+x+l+x+l+x,h-t,w/3-db/2+w+x+l+x+l+x,h-t-d1,w/3-db/2-t2+w+x+l+x+l+x,h-t-d1,w/3-db/2-t2+w+x+l+x+l+x,h-t-d1-t1,w/3-db/2+w+x+l+x+l+x,h-t-d1-t1,w/3-db/2+w+x+l+x+l+x,h-t-d1-t1-d2,
          w/3+db/2+w+x+l+x+l+x,h-t-d1-t1-d2,w/3+db/2+w+x+l+x+l+x,h-t-d1-t1,w/3+db/2+t2+w+x+l+x+l+x,h-t-d1-t1,w/3+db/2+t2+w+x+l+x+l+x,h-t-d1,w/3+db/2+w+x+l+x+l+x,h-t-d1,w/3+db/2+w+x+l+x+l+x,h-t,
          w/3+g/2+w+x+l+x+l+x,h-t,w/3+g/2+w+x+l+x+l+x,h,2*w/3-g/2+w+x+l+x+l+x,h,2*w/3-g/2+w+x+l+x+l+x,h-t,
          2*w/3-db/2+w+x+l+x+l+x,h-t,2*w/3-db/2+w+x+l+x+l+x,h-t-d1,2*w/3-db/2-t2+w+x+l+x+l+x,h-t-d1,2*w/3-db/2-t2+w+x+l+x+l+x,h-t-d1-t1,2*w/3-db/2+w+x+l+x+l+x,h-t-d1-t1,2*w/3-db/2+w+x+l+x+l+x,h-t-d1-t1-d2,
          2*w/3+db/2+w+x+l+x+l+x,h-t-d1-t1-d2,2*w/3+db/2+w+x+l+x+l+x,h-t-d1-t1,2*w/3+db/2+t2+w+x+l+x+l+x,h-t-d1-t1,2*w/3+db/2+t2+w+x+l+x+l+x,h-t-d1,2*w/3+db/2+w+x+l+x+l+x,h-t-d1,2*w/3+db/2+w+x+l+x+l+x,h-t,
          2*w/3+g/2+w+x+l+x+l+x,h-t,2*w/3+g/2+w+x+l+x+l+x,h,w+w+x+l+x+l+x,h,
          
          w+w+x+l+x+l+x,2*h/3+g/2,w-t+w+x+l+x+l+x,2*h/3+g/2,
          w-t+w+x+l+x+l+x,2*h/3+db/2,w-t-d1+w+x+l+x+l+x,2*h/3+db/2,w-t-d1+w+x+l+x+l+x,2*h/3+db/2+t2,w-t-d1-t1+w+x+l+x+l+x,2*h/3+db/2+t2,w-t-d1-t1+w+x+l+x+l+x,2*h/3+db/2,w-t-d1-t1-d2+w+x+l+x+l+x,2*h/3+db/2,
          w-t-d1-t1-d2+w+x+l+x+l+x,2*h/3-db/2,w-t-d1-t1+w+x+l+x+l+x,2*h/3-db/2,w-t-d1-t1+w+x+l+x+l+x,2*h/3-db/2-t2,w-t-d1+w+x+l+x+l+x,2*h/3-db/2-t2,w-t-d1+w+x+l+x+l+x,2*h/3-db/2,w-t+w+x+l+x+l+x,2*h/3-db/2,
          w-t+w+x+l+x+l+x,2*h/3-g/2,w+w+x+l+x+l+x,2*h/3-g/2,w+w+x+l+x+l+x,h/3+g/2,w-t+w+x+l+x+l+x,h/3+g/2,
          w-t+w+x+l+x+l+x,h/3+db/2,w-t-d1+w+x+l+x+l+x,h/3+db/2,w-t-d1+w+x+l+x+l+x,h/3+db/2+t2,w-t-d1-t1+w+x+l+x+l+x,h/3+db/2+t2,w-t-d1-t1+w+x+l+x+l+x,h/3+db/2,w-t-d1-t1-d2+w+x+l+x+l+x,h/3+db/2,
          w-t-d1-t1-d2+w+x+l+x+l+x,h/3-db/2,w-t-d1-t1+w+x+l+x+l+x,h/3-db/2,w-t-d1-t1+w+x+l+x+l+x,h/3-db/2-t2,w-t-d1+w+x+l+x+l+x,h/3-db/2-t2,w-t-d1+w+x+l+x+l+x,h/3-db/2,w-t+w+x+l+x+l+x,h/3-db/2,
          w-t+w+x+l+x+l+x,h/3-g/2,w+w+x+l+x+l+x,h/3-g/2,w+w+x+l+x+l+x,0,w+x+l+x+l+x+2*w/3+g/2,0,w+x+l+x+l+x+2*w/3+g/2,t,w+x+l+x+l+x+2*w/3-g/2,t,w+x+l+x+l+x+2*w/3-g/2,0,
          w+x+l+x+l+x+w/3+g/2,0,w+x+l+x+l+x+w/3+g/2,t,w+x+l+x+l+x+w/3-g/2,t,w+x+l+x+l+x+w/3-g/2,0]

Face_4 = str(Face_4)[1:-1]


"""Face 5"""

Face_5 = [t+l+x,0,t+l+x,h/3-g/2,0+l+x,h/3-g/2,0+l+x,h/3+g/2,t+l+x,h/3+g/2,t+l+x,2*h/3-g/2,0+l+x,2*h/3-g/2,0+l+x,2*h/3+g/2,t+l+x,2*h/3+g/2,t+l+x,h,
          
          l/3-g/2+l+x,h,l/3-g/2+l+x,h-t,
          l/3-db/2+l+x,h-t,l/3-db/2+l+x,h-t-d1,l/3-db/2-t2+l+x,h-t-d1,l/3-db/2-t2+l+x,h-t-d1-t1,l/3-db/2+l+x,h-t-d1-t1,l/3-db/2+l+x,h-t-d1-t1-d2,
          l/3+db/2+l+x,h-t-d1-t1-d2,l/3+db/2+l+x,h-t-d1-t1,l/3+db/2+t2+l+x,h-t-d1-t1,l/3+db/2+t2+l+x,h-t-d1,l/3+db/2+l+x,h-t-d1,l/3+db/2+l+x,h-t,
          l/3+g/2+l+x,h-t,l/3+g/2+l+x,h,2*l/3-g/2+l+x,h,2*l/3-g/2+l+x,h-t,
          2*l/3-db/2+l+x,h-t,2*l/3-db/2+l+x,h-t-d1,2*l/3-db/2-t2+l+x,h-t-d1,2*l/3-db/2-t2+l+x,h-t-d1-t1,2*l/3-db/2+l+x,h-t-d1-t1,2*l/3-db/2+l+x,h-t-d1-t1-d2,
          2*l/3+db/2+l+x,h-t-d1-t1-d2,2*l/3+db/2+l+x,h-t-d1-t1,2*l/3+db/2+t2+l+x,h-t-d1-t1,2*l/3+db/2+t2+l+x,h-t-d1,2*l/3+db/2+l+x,h-t-d1,2*l/3+db/2+l+x,h-t,
          2*l/3+g/2+l+x,h-t,2*l/3+g/2+l+x,h,l-t+l+x,h,
          
          l-t+l+x,2*h/3+g/2,l+l+x,2*h/3+g/2,l+l+x,2*h/3-g/2,l-t+l+x,2*h/3-g/2,l-t+l+x,h/3+g/2,l+l+x,h/3+g/2,l+l+x,h/3-g/2,l-t+l+x,h/3-g/2,l-t+l+x,0,
          
          2*l/3+g/2+l+x,0,2*l/3+g/2+l+x,t,2*l/3-g/2+l+x,t,2*l/3-g/2+l+x,0,l/3+g/2+l+x,0,l/3+g/2+l+x,t,l/3-g/2+l+x,t,l/3-g/2+l+x,0]

Face_5 = str(Face_5)[1:-1]

cx1_5 = t/2+l+x
cx1_5 = str(cx1_5)
cy1_5 = h/3
cy1_5 = str(cy1_5)
cx2_5 = t/2+l+x
cx2_5 = str(cx2_5)
cy2_5 = 2*h/3
cy2_5 = str(cy2_5)
cx3_5 = l-t/2+l+x
cx3_5 = str(cx3_5)
cy3_5 = h/3
cy3_5 = str(cy3_5)
cx4_5 = l-t/2+l+x
cx4_5 = str(cx4_5)
cy4_5 = 2*h/3
cy4_5 = str(cy4_5)


"""Face 6"""

Face_6 = [t+w+x,t+h+x,t+w+x,l/3-g/2+h+x,w+x,l/3-g/2+h+x,w+x,l/3+g/2+h+x,t+w+x,l/3+g/2+h+x,t+w+x,2*l/3-g/2+h+x,w+x,2*l/3-g/2+h+x,w+x,2*l/3+g/2+h+x,t+w+x,2*l/3+g/2+h+x,t+w+x,l-t+h+x,
          w/3-g/2+w+x,l-t+h+x,w/3-g/2+w+x,l+h+x,w/3+g/2+w+x,l+h+x,w/3+g/2+w+x,l-t+h+x,2*w/3-g/2+w+x,l-t+h+x,2*w/3-g/2+w+x,l+h+x,2*w/3+g/2+w+x,l+h+x,2*w/3+g/2+w+x,l-t+h+x,w-t+w+x,l-t+h+x,
          w-t+w+x,2*l/3+g/2+h+x,w+w+x,2*l/3+g/2+h+x,w+w+x,2*l/3-g/2+h+x,w-t+w+x,2*l/3-g/2+h+x,w-t+w+x,l/3+g/2+h+x,w+w+x,l/3+g/2+h+x,w+w+x,l/3-g/2+h+x,w-t+w+x,l/3-g/2+h+x,w-t+w+x,t+h+x,
          2*w/3+g/2+w+x,t+h+x,2*w/3+g/2+w+x,0+h+x,2*w/3-g/2+w+x,0+h+x,2*w/3-g/2+w+x,t+h+x,w/3+g/2+w+x,t+h+x,w/3+g/2+w+x,0+h+x,w/3-g/2+w+x,0+h+x,w/3-g/2+w+x,t+h+x]

Face_6 = str(Face_6)[1:-1]

cx1_6 = w+x+w/2;
cx1_6 = str(cx1_6)
cy1_6 =h+x+l/3
cy1_6 = str(cy1_6)
cx2_6 = w+x+w/3
cx2_6 = str(cx2_6)
cy2_6 = h+x+2*l/3
cy2_6 = str(cy2_6)
cx3_6 =w+x+2*w/3
cx3_6 = str(cx3_6)
cy3_6 = h+x+2*l/3
cy3_6 = str(cy3_6)


"""Generate SVG File"""

f = open("box2.svg", "w")
f.write('<?xml version="1.0" encoding="UTF-8" ?>')
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">')

"""Holes in Face 1"""

f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx1_1,cy1_1,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx2_1,cy2_1,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx3_1,cy3_1,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx4_1,cy4_1,r))


"""Holes in Face 3"""

f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx1_3,cy1_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx2_3,cy2_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx3_3,cy3_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx4_3,cy4_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx5_3,cy5_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx6_3,cy6_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx7_3,cy7_3,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx8_3,cy8_3,r))


"""Holes in Face 5"""

f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx1_5,cy1_5,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx2_5,cy2_5,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx3_5,cy3_5,r))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx4_5,cy4_5,r))


"""Holes in Face 6"""

f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx1_6,cy1_6,r_f))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx2_6,cy2_6,r_f))
f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="1" fill = "none"/>'%(cx3_6,cy3_6,r_f))


"""Fractals"""

r3 = 40 # Radius of spiral
th = np.arange(0,10*np.pi,0.1) # theta
r1 = 10*3.78; # Radius of circle

for i in th:
    x1 = l+x+l/2+r3*np.cos(i)
    y1 = h/2+r3*np.sin(i)
    f.write('<circle cx="%s" cy="%s" r="%s" stroke = "black" stroke-width="2" fill = "none"/>'%(x1,y1,r1))
    r1 = r1-0.2 
    r3 = r3+0.5 

f.write('<image x="%5.2f" y="%5.2f" width="%5.2f" height="%5.2f" href="columbia.svg"/>'%(l/2-l*100/378,h/3-h*100/378,l*200/378,h*200/378))
f.write('<text x="%5.2f" y="%5.2f" dominant-baseline="middle" text-anchor="middle" stroke-width="2" stroke = "black" font-size="20">DIGITAL MANUFACTURING</text>'%(l/2,2*h/3))
f.write('<text x="%5.2f" y="%5.2f" dominant-baseline="middle" text-anchor="middle" stroke-width="4" stroke = "black" font-size="60">%s</text>'%(w+x+w/2,h+x+l/3+(l/3)*2/3,T))
#f.write('<text x="%5.2f" y="%5.2f" dominant-baseline="middle" text-anchor="middle" stroke-width="4" stroke = "black" font-size="60">2 &#8734; &#38; &#8811;</text>'%(l+x+l+x+w/2,h/2))
f.write('<text x="%5.2f" y="%5.2f" dominant-baseline="middle" text-anchor="middle" stroke-width="4" stroke = "black" font-size="60">%s</text>'%(l+x+l+x+w/2,h/2,E))
f.write('<text x="%5.2f" y="%5.2f" dominant-baseline="middle" text-anchor="middle" stroke-width="4" stroke = "black" font-size="60">%s</text>'%(l+x+l+x++w+x+w/2,h/2,A))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_1))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_2))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_3))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_4))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_5))
f.write('<polygon points = "%s px" stroke = "black" stroke-width="1" fill = "none"/>'%(Face_6))

f.write('</svg>')
f.close()