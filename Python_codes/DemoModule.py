'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''
import sys
#sys.path.append("C:\Training\EclipseWS\Python\Python3Days\Day_1")
print(sys.path)
from utilities import checkPrime, square as sq


if(checkPrime(13)):
    print("It's Prime")
else:
    print("It's NOT Prime")
    
  
print(sq(100));   