'''Program to right_align a list of strings
Raeesa Behardien
BHRRAE003
Assignment 6
Question 1'''

#Create empty string
stringlist = []
insertstring = input("Enter strings (end with DONE):\n")

#create while function
    
while insertstring != "DONE":
    stringlist.append(insertstring) #to add another string
    insertstring = input("") #enter more input until done

if len(stringlist)>0:
    width = max(len(string) for string in stringlist)
    RightAlign = ">{}".format(width)

#print right alignment
    print("")
    print("Right-aligned list:")
    for string in stringlist:
        print (format(string, RightAlign))
else:
    print("")    
    print("Right-aligned list:")









    