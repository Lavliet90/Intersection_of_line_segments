#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
The number line contains two segments: [a1; b1] and [a2; b2]. 
Write a program that finds their intersection.
The intersection of two segments can be:
line segment;
dot;
empty set.

Input data format:
4 integers a1, b1, a2, b2 are fed to the program input one  each separate line. 
It is guaranteed that a1 < b1 And a2 <b2

Output data format
The program must display on the boundaries of a segment that is an intersection, either a common point, or the text "empty set".


'''
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a>=c>=b>=d) or (a<=c<=b<=d):
    if c==b:
        print(c)
    else:
        print(c, b, sep=" ")
elif (c>=a>=d>=b) or (c<=a<=d<=b):
    if a==d:
        print(a)
    else:
        print(a, d, sep=" ")
elif (a>=b>=c>=d) or (a<=b<=c<=d):
    if b==c:
        print(b)
    else:
        print("пустое множество")
elif (a>=c>d>=b) or (a<=c<d<=b):
    print(c, d, sep=" ")
elif (c>=a>b>=d) or (c<=a<b<=d):
    print(a, b, sep=" ")
else:
    print("пустое множество")

