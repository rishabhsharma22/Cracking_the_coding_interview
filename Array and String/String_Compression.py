# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 00:12:50 2018

@author: Rishabh Sharma
"""

# String Compression: To compress a given string using the character followed by the number of occuance of that character. Assume character to be uppercase and lowercase alphabets


"""
We will check the consicutive characters. If the consecutive characters are same
we will increase the occurance of character else we will print the character with 
its occurance that has been obtained.
"""

def str_compression(string):
    
    
    count = 1
    ans = ""
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            count+=1
        else:
            ans += string[i]+str(count)
            
            count = 1
    ans += string[i]+str(count)
    
    return ans


print(str_compression("aaabb"))
print(str_compression("abbbb"))
print(str_compression("aaabbbbssZZZ"))