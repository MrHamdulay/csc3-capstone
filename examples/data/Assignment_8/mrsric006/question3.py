"""Encrypting program
Richard Marais
11/05/14"""

def Encrypt(index,inpstring,output):
    if index == len(inpstring):       #base case to print at the end
        print("Encrypted message:\n",output,sep='')    
    elif inpstring[index] in 'abcdefghijklmnopqrstuvwxy':     #checks if it's in the lowercase alphabet (could use ord values alternatively
        output += chr(ord(inpstring[index])+1)       #encrypts and runs for the next index value
        Encrypt(index+1,inpstring,output)        
    elif inpstring[index] == 'z':               #for the z case moves back 25 ord values to get to a
        output+= chr(ord(inpstring[index])-25)
        Encrypt(index+1,inpstring,output)
    else: 
        output+=inpstring[index]                 #if not in lowercase alph, just add to output as is
        Encrypt(index+1,inpstring,output)

string = input("Enter a message:\n")
Encrypt(0,string,'')