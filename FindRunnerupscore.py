#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:37:47 2022

@author: root
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    Fmax=-100
    Smax=-100
   
    if n>=2:
         
        for i in range(n):
            if arr[i]>Fmax:
                Smax=Fmax
                Fmax=arr[i]
                
            
            elif (arr[i]>Smax)and(arr[i]!=Fmax):
                Smax=arr[i]
            
    print(Smax)