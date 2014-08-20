#Right-aligned strings
#Devaksha Pillay
#21 April 2014

maximum = 0

#Enter multiple inputs
name = input ("Enter strings (end with DONE):\n")
name_list = []
while name != "DONE":
    name_list.append(name)
    name = input ()
    
if name == "DONE":
    #Print free line
    print()
    
    print("Right-aligned list:")
    
    #work out item of maximum length
    for i in range (len(name_list)):
        if len(name_list[i]) >= maximum:
            maximum = len(name_list[i])
            
    for i in range (len(name_list)):
        #number of spaces must be equal to the difference between the length of the name entered and the length of the maximum name
        spaces = (maximum) - (len(name_list[i]))
        #print out each value in the list after it is aligned to the right
        print (spaces*" ",name_list[i], sep = "")