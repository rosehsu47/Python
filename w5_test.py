#!/usr/bin/env python
#-*-coding: utf-8-*-
def isPrime(N):
    a=1
    for x in range(2,N,1):
        if N%x==0:
            a=0
    return a

        
sum=0
for y in range (2,1000,1):  
    if isPrime(y)==1:
        sum+=y
print sum


