# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 01:45:17 2018

@author: Rishabh Sharma
"""

"""
Write an algorithm that if an element in an MxN matrix is 0, its entire row and
column are set to 0

"""

"""
This is one of the most trickey questions I have encountered as it is difficult
to solve it in just 1 pass but I have got a fair idea as to how to do it

We will keep the track to see if first row and column are zero or not. then we 
can use first row and column to set the desired row and columns to zeros
"""


def zero_mat(mat):
    
    first_row_zero = False
    first_col_zero = False
    
    for i in range(len(mat)):
        if mat[i][0] == 0:
            first_col_zero = True
            break
    
    for i in range(len(mat[0])):
        if mat[0][i] == 0:
            first_row_zero = True
            break
    
    
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[i][j]==0:
                mat[i][0]=0
                mat[0][j]=0
        
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            if mat[1][0] == 0 or mat[0][j]==0:
                mat[i][j] = 0
    
    if first_col_zero:
        for i in range(len(mat)):
            mat[i][0] = 0
    
    if first_row_zero:
        for i in range(len(mat[0])):
            mat[0][i] = 0
            
    return mat



print(zero_mat([ [1,0,1],
                [1,1,1],
                [1,1,0] ]))
    
    

print(zero_mat([ [1,0,1],
                [1,1,1] ]))
    
    
    