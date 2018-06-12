# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:23:04 2018

@author: Balasubramaniam
"""

import os

path="C:/Program Files (x86)/Microsoft Visual Studio/Shared/Anaconda3_64/Lib/site-packages/sklearn/datasets/data"


if(os.path.exists(path)):
    print("directory exists")
    for(dirpath,dirnames,filenames) in os.walk(path):
        for file in filenames:
            (fileName,extension)=os.path.splitext(file)
            if((extension==".csv") and (fileName=="iris")):
                #print(fileName)
                #read file content
                contents=open(path+"/"+file,"r")
                rows=[]
                for line in contents:
                    rows.append(line)
                for row in rows[1:]:
                    print(row)
                
                    
                    
                    
                    
                    
                    
                    