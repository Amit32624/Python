'''
Created on 12-Jun-2017

@author: mohan.chinnaiah
'''

from datetime import date

def calculate_age(bday):
    today = date.today()
    return today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))


print('Enter a date in YYYY-MM-DD format');
date_entry = input();
year, month, day = map(int, date_entry.split('-')) # Added the relevant comment


bday=date(year,month,day);
print(bday)
age=calculate_age(bday);
print("Your Age",age)