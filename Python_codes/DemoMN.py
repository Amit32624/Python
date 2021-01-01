'''
Created on 04-Dec-2018

@author: mohan.chinnaiah
'''


def addDigits(n):
    s=0
    while n > 0:
        rem = n % 10
        s=s+rem
        n=int(n/10)
        
    return s    
        
        
print('Enter an integer')
n=int(input())        
 
while n > 9:        
    n=addDigits(n) 
    
    
if(n==1):    
    print("It's a magic Number")    
else:
    print("It's not a magic Number")         
 
 
 