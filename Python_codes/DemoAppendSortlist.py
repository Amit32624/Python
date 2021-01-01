
aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)

print("Final List : ",aList)
list = ['larry', 'curly', 'moe']
list.append('shemp')  ## append elem at end
list.insert(0, 'xxx')  ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))  ## 2

ritem=list.remove('curly')  ## search and remove that element
list.pop(1)  ## removes and returns 'larry'
print("ri",ritem)
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

#!/usr/bin/python

# sorting.py

print('numbers')
n = [3, 4, 7, 1, 2, 8, 9, 5, 6]
print(n[0])
print(n[-1])

print(n[1:-1])


