# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:35:54 2018

@author: Rishabh Sharma
"""

#URLify: To replace the spaces in the string with %20



def URLify(string,replace_str):
    return replace_str.join(string.split())

print(URLify("Jhon Smith","%20"))
        