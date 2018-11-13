# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:56:16 2018

@author: Rishabh Sharma
"""

#Palindrome Permutation
'''
Given a string we need to return true if the string has a permutation that
is also a palindrome else we will return False.
'''

"""
The idea is that in a palidrome we will have even occurance of all the 
character and at max we will have one odd occurance of any character
"""


def is_plain_perm(string):
    char_count = {}
    
    for elem in string:
        if elem in char_count:
            char_count[elem] += 1
        else:
            char_count[elem] = 1
    
    odd_count = 0        
    for key, value in char_count.items():
        if value%2 != 0 and odd_count == 0:
            odd_count += 1
        elif value%2 != 0 and odd_count != 0:
            return False
    return True

