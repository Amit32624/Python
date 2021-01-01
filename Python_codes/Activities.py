'''
Created on 04-Apr-2018

@author: mohan.chinnaiah
'''

print("Enter an Integer")
n=int(input())
'''
if(n%2==0):
    print("n is even")
else:
    print("n is odd")
    
  '''  
#prime or not
i=2
for i in range(2,n):
    print("i = ",i)
    if(n%i==0):
        print("i = ",i)
        print("N is not Prime")
        break;
    
if(i==n-1):
    print("N is Prime")
    
print("Another integer")    
m=input()    
print(len(m))      


for name in dir(__builtins__):
    print(name)
    
    print("Hello"+str(3))
    