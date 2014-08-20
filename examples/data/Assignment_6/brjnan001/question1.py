"""Assignment 6 Q1 right aligning a list
Nandani Birjanund
22/04/14"""

array=[] #creates and empty array 

name=input("Enter strings (end with DONE):\n") #User enters names into array

if name=="DONE": #DONE when list is over
    print("")
    print("Right-aligned list:")
else:
    while name!="DONE": 
        array.append(name) #adds to array
        name=input() #lets user input strings to array

#stores length of names in a different array called array_2

    array_2=[] #new array

    arraylength=len(array) #array length to het longest string to align rest

    for i in range (arraylength): #loop for length
    
        namelength=len(array[i])
        
        array_2.append(namelength) #adding to array_2
    
    array_2.sort()
    end=len(array_2)
#set width equal to maximum length
    max_width=array_2[end-1]
#output right alligned list using format
    print("")
    print("Right-aligned list:")

    for j in range (arraylength):
    
        space=max_width-(len(array[j])) #prints aligned list
        print(" "*space,array[j],sep="")