# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 01:28:21 2018

@author: Rishabh Sharma
"""

# given an image represented by NxN matrix. Rotate the matrix by 90 degrees
#Can you do this rotation inplace

"""
The approach is to rotate the outer most part of the matrix first and then keep
on moving to the inner part of the matrix
"""


def rotate(mat,N):
    
    
    for i in range(0,int(N/2)):
        
        for j in range(i,N-i-1):
            
            temp = mat[i][j]
            
            mat[i][j] = mat[j][N-1-i]
            
            mat[j][N-1-i] = mat[N-1-i][N-1-j]
            
            mat[N-1-i][N-1-j] = mat[N-1-j][i]
            
            mat[N-1-j][i] = temp
            
    return mat

print(rotate([ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ],4))