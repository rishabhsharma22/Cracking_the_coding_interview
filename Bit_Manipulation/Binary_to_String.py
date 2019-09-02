#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:03:47 2019

@author: rishabh
"""

def toBinary(num):
    if (num>=1 or num<=0):
        return "Error"
    
    ans = "."
    
    while(num>0):
        if(len(ans) >= 32):
            return "Error"
        
        
        b = num*2
        if (b>=1):
            
            ans = ans + "1"
            num = b-1
            
        else:
            ans = ans+"0"
            num = b
            
    return ans

n = 0.625
result = toBinary(n) 
print( result) 

