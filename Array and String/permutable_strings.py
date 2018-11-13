# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:27:39 2018

@author: Rishabh Sharma
"""

#Program to find if a string is permutation of another string or not

def is_permutation(str1, str2):
    
    if len(str1)!= len(str2):
        return False
    
    count1 = [0]*256
    count2 = [0]*256
    
    
    
    for elem in str1:
        count1[ord(elem)]+=1
    for elem in str2:
        count2[ord(elem)]+=1
        
    for i in range(256):
        if count1[i] != count2[i]:
            return False
    return True