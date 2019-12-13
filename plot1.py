# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:20:14 2019

@author: Gaurav

"""

import random
from timeit import default_timer as time
import matplotlib.pyplot as plt

def binary_search(arr,x,l,r):
    flag=0
    while l <= r: 
        print("a")
        mid =int((l+(r-1))/2)
          
        if arr[mid] == x:
            flag=1
            break;
     
        elif arr[mid] < x: 
            print("b")
            l = mid + 1
  
        else: 
            print("c")
            r = mid - 1
    if flag==1:
        print("found")
        return 0
    else:
        print("not found")
        return -1

def linearsearch(numbers,numcheck):
    flag=0
    for i in numbers:
        if i==numcheck:
            flag=1
            break;
    if flag==1:
        print("found")
        return 0
    else:
        print("not found")
        return -1

time_linear=[]
time_binary=[]
size_binary=[]
size_linear=[]
numbers=[]
numcheck=0
start=0 
end=0
sizes = list(range(5000,51000,5000))
for size in sizes:
     numbers = random.sample(range(1, size+1), size)
     numcheck = random.randint(1,size)
     
     size_linear.append(size)
     
     start = time()
#    Linear:
     flag=0
     for i in numbers:
         if i==numcheck:
             flag=1
             break;
     if flag==1:
         print("Found")
     else:
         print("not found")
     end = time()
     total = end-start
     time_linear.append(total)
     
     numbers.sort()
     start = time()  
     l=0
     r=i-1
     while l <= r: 
        mid = int((l+(r))/2)
        print(mid)
        if numbers[mid] == numcheck:
            flag=1
            break;
     
        elif numbers[mid] < numcheck: 
            l = mid + 1
            print("<")
        else: 
            r = mid - 1
            print(">")
     if flag==1:
         print("found")
     else:
         print("not found")
     end = time()
         ##if check!=-1:
           #  break 
     time_binary.append(end-start) 
     size_binary.append(size)
     
plt.scatter(size_linear,time_linear)
plt.ylabel('Time')
#plt.autoscale()
plt.show()
plt.scatter(size_binary,time_binary)
plt.ylabel('Time')
#plt.autoscale()

plt.plot(size)
plt.show()
plt.plot(size_linear, time_linear, 'r--', size_binary,time_linear, 'bs')
#plt.autoscale()
plt.show()