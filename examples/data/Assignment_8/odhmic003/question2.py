"""Michael Odhiambo
ODHMIC003
Assignment 8_Question 2
Program to count number of pairs in string"""
string= input("Enter a message:\n")#Prompt user for input
array=[]
"""Scan through string and append the value "1" to an array every time a pair is found"""
def chr_pairs(string):
    if len(string)>=2:
        if string[0]==string[1]:
            a=1
            array.append(a)
            chr_pairs(string[2:])
        else:
            chr_pairs(string[1:])

chr_pairs(string) 
count= len(array)#Find length of array i.e count number of pairs found
print("Number of pairs:",count)

