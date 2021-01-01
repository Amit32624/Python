'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''


text="Hello everyone , Good Morning";

print(text);
print(len(text))
print(text[0])
print(text[-1])
print(text[0:4])
print(text[:-1])
print(text[1:])
print(text[:5])

for word in text.split(' '):
    print(word)

for ch in text:
    print(ch)


str1=str("Hello");
str2=str("Hello");

if str1==str2:
    print("Equals")
else:
    print("Nope")
    
if(text.find("hello",5)):
    print('Hello found')
else:
    print('Not Found')

names=["Mohan","Venkat","Rahul","Chetak","Aman"];


print(names)
names.sort(reverse=True)
print(names)