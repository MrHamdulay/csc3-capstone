"""Keegan Naidoo
NDXKEE009
20 April 2014"""

i=0

list=[]                 #Creating empty list

strings=""              #Assigning string variable to store names temporarily. Making it empty so first itteration will run

max=0                   #Assigning max variable to 0 this will store the maximum length of a string to allign Names

strings=input("Enter strings (end with DONE): \n")  #Input names, type "DONE" to quit/stop

counter=0

while(strings!="DONE"): #Loop that runs until "DONE" is entered
    
    if counter==0:
        strings=strings
        
    else:
            
        strings=input("")
        
    counter+=1
    
    list.append(strings)                                 #Adds names to list
    
    i+=1    #Increases list index by 1
    
print()

for k in range(len(list)-1):      #Loop to find max length to allign names
    
    x=len(list[k])                #current length
    
    if max>x:     #If max> current length store 1st length else store 2nd length. Itterates and compares all lengths.
        
        max=max
        
    else:
        
        max=(len(list[k]))
        
#print(max)
        
print("Right-aligned list:")

for j in range(len(list)-1):          #Prints list right-alligned to the longest name 
    print(list[j].rjust(max))

    