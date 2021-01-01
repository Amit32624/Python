'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''

set1={1,2,3,4,5,6,7}
set2={4,5,6,7,8,9,10}

print(set1);
print(set2);



print(set1.union(set2));
print(set1.intersection(set2));

print(set1.difference(set2));
print(set2.difference(set1));

engineers   = {'John', 'Jane', 'Jack', 'Janice'}
programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
managers    = {'Jane', 'Jack', 'Susan', 'Zack'}

'''union'''
employees=engineers | programmers | managers   
print(employees)

'''intersection'''
eng_man=engineers & managers
print(eng_man)