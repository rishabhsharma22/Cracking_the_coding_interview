# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:03:43 2018

@author: Rishabh Sharma
"""

# Write an algorithm to find if a string has all unique characters



'''
The idea is to make a set of elements that we have seen and then to verify that every element that we see is a new 
element. Time Complexity is O(n) and Space Complexity is O(n)
'''
def is_unique(string):
    seen = set()
    
    for elem in string:
        if elem in seen:
            return "not_unique"
        else:
            seen.add(elem)
    return "unique"


'''
To find the unique elements without using a new data structure.
Time Complexity: O(nLogn)
Space Complexity: O(1)
'''
def unique_or_not(string):
    string = sorted(string)
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            return "not unique"
    return "unique"


print(is_unique("hello"))
print(is_unique("helo"))
print(unique_or_not("hello"))
print(unique_or_not("helo"))


