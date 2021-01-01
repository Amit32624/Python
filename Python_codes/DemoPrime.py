'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''

def checkPrime(n):
    for i in range(2,n):
        if(n % i ==0 ):
            return 0

    return 1

print("Enter an integer")
n=int(input())

check=checkPrime(n)

if(check==0):
    print(n ,'is Not Prime')
else:
    print(n ,'is Prime')
