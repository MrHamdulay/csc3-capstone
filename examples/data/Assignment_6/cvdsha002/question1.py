"""Shahrain Coovadia 
24 April 2014
CVDSHA002"""

start=[]      #empty string
list=input("Enter strings (end with DONE):\n")         #ask for strings
while list!= 'DONE':                      
    start.append(list)                #add list to string that is empty
    list=input("")    #empty string
    n_string=0 
    for i in start:               #loop through strings
        if len(i)>n_string:            
            n_string=len(i)
print(" ")            
print("Right-aligned list:")
 
for words in start:
    print(' '*(n_string-len(words)), words, sep='')   #print