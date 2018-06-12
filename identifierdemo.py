# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 10:46:15 2018

@author: Balasubramaniam
"""
#identifier declaration
organizationName="Citi Corp"
#firstName=input("Enter your Name")
#print("Organization Name=%s\nFirst Name=%s" %(organizationName,firstName))
#type checking
#print(type(firstName))
#typecast
#age=int(input("Enter Age"))

firstName="Sanjay"
lastName="Kapoor"
age=47
print(organizationName+""+firstName+" "+lastName+""+str(age))
print(type(age))

import datetime
dob=datetime.date(1970,12,2)
strdob=dob.strftime("%A,%B,%Y")
print("DOB=%s" %(strdob))

#decimal to binary conversion
print(bin(3856))
#binary to decimal
print(int('0b111100010000',2))
#complex number
print(complex(45,67))





