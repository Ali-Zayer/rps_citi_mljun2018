# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:00:44 2018

@author: Balasubramaniam
"""
import datetime
customerList=[[23747,"Anoop",datetime.date(1987,1,1)],
               [56783,"Sunil",datetime.date(1965,4,27)],
               [6397,"Sudeep",datetime.date(2001,11,4)],
               [78697,"Rahul",datetime.date(1999,7,29)]]

for obj in customerList:
    if(obj[0]>7000):
        print(obj[1],"-->",obj[2].strftime("%A,%B,%Y"))
        
#zip
projects=["Banking","Insurance","CreditCard"]
locations=["Chennai","Pune","Bangalore"]
clients=["HSBC","Royal Sundaram","VISA"]

for(p,l,c) in zip(projects,locations,clients):
    print(p,"-->",l,"--->",c)
    
print(projects[:-1])
print(locations[0:2])

#tuple
gender=("MALE","FEMALE","TANSGENDER")

#configuration values
configData=(["192.67.89.90","sa","admin@123"],
            ["192.67.91.90","root","admin@123"],
            ["216.67.89.90","admin","admin@123"])
configData[0].append("test")
print(configData[0])

    
    
    
        
           
            