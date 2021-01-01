'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''
import math

def evenOrOdd(n):
    if n%2==0:
        return True;
    else:
        return False;


def checkPrime(n):
    for i in range(2,n):
        if(n % i ==0 ):
            return False

    return True;

def square(n):
    return n*n;



def squareRoot(n):
    return math.sqrt(n);