'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''

myDict={'id':'11203094','name':'Mohan','salary':'55555.55','email':'mohan.chinnaiah@gmail.com' ,'fn':'Mohan'};


print(myDict)

for key in myDict:
    print(key,'    ',myDict[key])
    
    
    
'''Filtering a dictionary'''    
filter_string="Mohan";    
filtered_dict = {k:v for k,v in myDict.items() if filter_string in v}

print(filtered_dict)


abc=(10,20,30)

n1,n2,n3=abc
print(n1)