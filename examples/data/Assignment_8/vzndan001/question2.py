"""Recursion: counting repeated character pairs
danica van der zandt
9 may 2014"""


counter=0
def count_characters(s):
    global counter 
    
    if len(s)<=1:
        print("Number of pairs:", counter) 
    elif s[0]==s[1]:
        counter=counter+1
        return counter and count_characters(s[2:])
    
    else:
        return count_characters(s[1:])
      
    

s=input("Enter a message:\n")
count_characters(s)