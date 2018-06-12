# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:15:53 2018

@author: Balasubramaniam
"""

import pymysql;

def createConnection():
    
    conn=pymysql.connect(host="localhost",user="root",
                   passwd="vignesh",
                   db="citidb_2018")
    return conn


def addCustomer(data):
    connObj=createConnection();
    cursor=connObj.cursor();
    print("Cursor ready...");     
    try:
        cursor.execute("""insert into Customer values 
    ('%d','%s','%s')""" %(data[0],data[1],data[2]));
        #cursor.execute(query);
        connObj.commit()
    except pymysql.Error as e:
        print("Exception occurred",e )
        connObj.rollback()
        
def fetchByCustomerId(id):
    conn=createConnection()
    cursor=conn.cursor()
    cursor.execute("""select * from Customer where 
    Customer_Id='%d'""" %(id))
    return cursor.fetchall()

#import datetime        
#customer=[48658,"Sanjay",datetime.date(1987,4,4)]        
#addCustomer(customer)
for row in fetchByCustomerId(48658):
    print(row[2].strftime("%A,%B,%Y"))        
        
        