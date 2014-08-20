"""Pragramme to right align a given list of names
Dumisani J Nyathi
24-04-2014"""

def right_align():
    x=input("Enter strings (end with DONE):\n")#this will prompt user to enter the names
    y = [x]#creating the list and x inside to account for the first name given as it is out of loop
    
    while x != 'DONE':#loop will iterate as long as input given is not DONE
        if x!='DONE':
            x=input("")
            y.append(x)#adding input to the end of the list
        
       
    length=0
    for j in y:
        if len(j)>length:
            length=len(j)#to create spaces to cause text to right-align
            
    print("\nRight-aligned list:")
    
    for i in y:
        if i =='DONE':
            continue#to ensure DONE is not in the final list
        else:
            print(" "*(length-len(i))+i)
            
right_align()