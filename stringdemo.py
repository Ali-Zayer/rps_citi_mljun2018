# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:00:47 2018

@author: Balasubramaniam
"""

firstName="shyam"
print(firstName.capitalize())

for _ in firstName[0:]:
    print(_)

#list
randomList=[]    
import random
for _ in range(1,100):
   temp=random.randint(10,10000) 
   if(temp>5000):
       randomList.append(temp)
       
randomList.sort()

print(randomList)

import base64

seqNo=567
pnrNo=base64.b64encode(str(seqNo).encode(encoding='utf-8', errors='strict'))
print(pnrNo)

print(firstName.center(len(firstName)+25,"*"))
print(firstName.rjust(len(firstName)+25,"*"))
print(firstName.ljust(len(firstName)+25,"*"))




