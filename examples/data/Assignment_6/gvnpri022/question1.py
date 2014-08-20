"""question 1-assignment 6- display string right-aligned
GVNPRI022
23 April 2014"""

name=[]#initialise array

nameVar=input(("Enter strings (end with DONE):\n\n"))
x=0
while(nameVar!="DONE"):#end loop when 'DONE' entered
    name.append(nameVar)
    nameVar=(input()) #input list of names
    x=x+1   


print("Right-aligned list:")
if(len(name)>0):
    maxLen= len(name[0])
    for i in range(len(name)):
        length= len(name[i])
        if(length>maxLen):
            maxLen=length #finding longest string


    for j in range(len(name)):
    
    
        print( (name[j].rjust(maxLen,' '))) #right aligning with longest string
    
    
    
    
   
    

    
