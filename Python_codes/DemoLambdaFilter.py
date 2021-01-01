'''
Created on 22-Jun-2017

@author: mohan.chinnaiah

Program to filter out only the even items from a list using filter() and 
lambda functions
The function filter(function, list) offers an elegant way to filter out all the 
elements of a list, for which the function function returns True. 
'''
my_list= [1, 5, 4, 6, 8, 11, 3, 12]
even_list= list(filter(lambda x: (x%2 == 0) , my_list))
print(even_list)