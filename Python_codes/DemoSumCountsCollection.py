'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''

import collections
num = [2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(num).values()))
