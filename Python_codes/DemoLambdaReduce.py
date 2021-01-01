from functools import reduce
'''
Created on 22-Jun-2017

@author: mohan.chinnaiah

The function reduce(func, seq) continually applies the function func() to the 
sequence seq. It returns a single value. 

'''

tot=reduce(lambda x,y: x+y, [47,11,42,13])
print(tot)


nlist=[1,3,5,7,11,13,17,23,29]
product=reduce(lambda x,y: x*y, nlist)
print(product)


