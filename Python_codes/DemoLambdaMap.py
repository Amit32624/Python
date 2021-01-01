'''
Created on 22-Jun-2017

@author: mohan.chinnaiah

map(func, seq) The first argument func is the name of a function and the 
second a sequence (e.g. a list) seq. map() applies the function func to all 
the elements of the sequence seq. It returns a new list with the elements 
changed by func
'''
my_list= [1, 5, 4, 6, 8, 11, 3, 12]
new_list= list(map(lambda x: x ** 2 , my_list))
print(new_list)
