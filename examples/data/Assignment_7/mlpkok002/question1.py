strings=[] #create empty list
string=input("Enter strings (end with DONE):\n") #prompt for strings


if string!="DONE": #if user does not enter DONE first:
    while string!="DONE":
        strings.append(string)#fill list with strings until user enters DONE
        string=input("") #allows user to keep entering strings until user types DONE     
   
    print("")    
    print("Unique list:")
    unique_list=[] #create empty list
    for i in strings: #loop over strings:
        if i in unique_list:
            continue  #if string already in unique_list, do not add it again!
        unique_list.append(i) #fill empty list with strings
        print(i) #print the strings, with none of them appearing more than once (line 12-13)
        
        

else:   #if user enters DONE first     
    print("")
    print("Unique list:")
    print("")
    
    
    