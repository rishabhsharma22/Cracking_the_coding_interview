# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 23:47:41 2018

@author: Rishabh Sharma
"""

# One Away: Given two strings check if the strings are one away from the other or not. The possible operations can be insertion, deletion or replacement.

"""
The approach is following

We will look at each character at a time. If the difference of length of strings is more than 1
then we return false because we know that the strings are more than 1 away from each other.
otherwise we compare the characters. If the characters are different we increment the total shifts by 1
then we move the longer string by 1 character if the length of both strings is different.
If length of both strings are same then we increment move each string by 1 character
"""

def one_away(string1, string2):
    len_str1 = len(string1)
    len_str2 = len(string2)
    
    if abs(len_str1 - len_str2)>1:
        return False
    
    
    diff = 0 #total number of differences
    i = 0
    j = 0
    while(i<len_str1) and (j<len_str2):
        if string1[i] != string2[j]:
            if diff == 1:
                return False
            
            if len_str1>len_str2:
                i+=1
            elif len_str1<len_str2:
                j+=1
            else:
                i+=1
                j+=1
            
            diff+=1
        
        else:
            i+=1
            j+=1
        
    if i<len_str1 or j<len_str2:
        diff+=1
    
    return diff<=1


print(one_away("Pale","Bale"))
print(one_away("Pale","Bali"))        