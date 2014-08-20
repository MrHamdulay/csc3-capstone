"""Dumisani Ngwenza
NGWDUM005
07/05/2014
Assignment 8 Question 2"""

#require input from user
string = input('Enter a message:\n')

def main(string):
    if string == '':
        return 0
    if len(string)==1:
        return 0    
    if len(string)>2 and string[0] == string[1] and string[1] == string[2]:
        return 1 + main(string[2:])    
    if string[0] == string[1]:
        return 1 + main(string[1:])
    if string[0] != string[1]:
        return 0 + main(string[1:])

y = main(string)    
print('Number of pairs:', y)
