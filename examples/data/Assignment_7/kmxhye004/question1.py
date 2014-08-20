strings = input("Enter strings (end with DONE):\n")#input
#creating a list
list=[]
#creating a list removing duplicates
unique=[]
counter = 0
while(strings!="DONE"):
    list.append(strings) 
    strings = input("")
    #adding the strings
      
    #checking if there are duplicates
    for i in list:
            if (i not in unique):
                unique.append(i) 
                counter+=1
     
else:
    print()
    
    print("Unique list:")
    for i in range(counter): #minus 1 to exclude it printing the DONE
        print(unique[i])
    
        