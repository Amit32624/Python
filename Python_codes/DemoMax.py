'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''


print("Enter three numbers");
n1=int(input());
n2=int(input());
n3=int(input());


if (n1 > n2 and  n1 > n3):
    print("N1 is Bigger");
else:
    if(n2 > n3):
        print("N2 is Bigger");
    else:
        print("N3 is Bigger")
     
