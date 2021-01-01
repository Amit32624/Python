'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''# illustrates how tuple works in python
# Mohan

#Create Tuple

names=("Amar","Brian","Chandru","Dharma","Evan","Ferrari","Gowri")

#Print Whole Tuple @ once
print(names)
print(len(names))


#Iterate and Print
for name in names:
    print(name)


#concatenate

names+=("Harini","Ilahi","John")

print(names)
print(len(names))

#Membership
print("gowri" in names)
print("Mangala" in names)

#indexing, slicing

print("Second Name :",names[2])
print("Second from last :",names[-2])

print(names[1:4])
print(names[:4])
print(names[4:])

#delet a tuple
del names
print(names)


