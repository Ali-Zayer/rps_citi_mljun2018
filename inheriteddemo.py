# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:12:00 2018

@author: Balasubramaniam
"""
from oopsdemo import Product
class SeasonalProduct(Product):
    
    def __init__(self,id,name,dop,period):
        Product.__init__(self,id,name,dop)
        self.__period=period

import datetime        
obj = SeasonalProduct(315453,"Coke",datetime.date(2018,6,8),"Summer")
print(obj.getProductId())
