# Course: CS1068
# Laboratory: Assignment 2
# Date of creation: 2020/12/20
# Author: Amit Somnath Sambrekar
# Number: 120220153
# Description: Write a function find repeats(fname) that detects repeated words in a text file. When a
#repeated word is found your function should print a message that contains the line number
#and the repeated word.

#main function to find repeated words.
def find_repeats(fname):
    file = open(file_name, "rrr")
    lines = file.readlines()
    num_char = 0
    for k in range(len(lines)):
        num_char += len(lines[k].split())
        if num_char >= fname:
            return k + 1
    
#Open and Read the file from the file location.
    file_name = "F:\\Programming in Python\\Sample.txt"
    text_file = open(file_name, "r")
    repeated_words = []
    text = text_file.read()
    j = text.split()

#Checking for punctuations and special characters
    for i in range(len(j)-1):
        c = j[i+1]
        MARKS = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for p in MARKS:
            c = c.replace(p, "")
        if j[i].lower() == c.lower():
            repeated_words.append((i+1, j[i])) 

    text_file.close ()


#Repeated words and output format
    for i in range(len(repeated_words)):
        fname = find_repeats(repeated_words[i][0])
        print("Line number- {},Repeated word - {}".format(fname, repeated_words[i][1]))

    #Closing the file.
    text_file.close ()