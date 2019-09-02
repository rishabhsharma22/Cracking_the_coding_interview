#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:56:33 2019

@author: rishabh
"""

def createStack():
    stack = []
    return stack

def is_Stack_Empty(stack):
    return len(stack) == 0

def push_elem(stack,elem):
    stack.append(elem)
    
def top(stack):
    len_stack = len(stack)
    return stack[len_stack-1]

def pop_elem(stack):
    if (is_Stack_Empty(stack)):
        exit(1)
    return stack.pop()

def print_stack(stack):
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=" ")
    print()

def sortStack(stack):
    temp = createStack()
    while(is_Stack_Empty(stack) == False):
        tmp = top(stack)
        pop_elem(stack)
    
        while(is_Stack_Empty(temp) ==False and int(top(temp))>int(tmp)):
            push_elem(stack,top(temp))
            pop_elem(temp)
        
        push_elem(temp,tmp)
    
    return temp


stack = createStack() 
push_elem( stack, str(34) ) 
push_elem( stack, str(3) ) 
push_elem( stack, str(31) ) 
push_elem( stack, str(98) ) 
push_elem( stack, str(92) ) 
push_elem( stack, str(23) ) 
  
print("Sorted numbers are: ") 
sortedst = sortStack ( stack ) 
print_stack(sortedst) 