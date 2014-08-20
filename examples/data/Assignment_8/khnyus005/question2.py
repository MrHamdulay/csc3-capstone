'''
Created on 06 May 2014
Repeated pairs counting with recursion
@author: Yusuf Khan
KHNYUS005
'''
def rep_count(message):
    if message[-1::]=='':
        return 0#if string empty, stop recursion
    if message[-1]==message[-2:-1:]:#compares last two chars
        message = message[0:-2:1]#remove last char from string
        return (1+rep_count(message))#add repetition to count
    else:
        message = message[0:-1:1]#if no adjacent repeated letters
        return (0+rep_count(message))#remove last letter and add zero to count
    

message = input("Enter a message:\n")#input
print ("Number of pairs:",rep_count(message))#output