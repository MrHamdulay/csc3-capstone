"""program where the user can enter a list of strings and these strings are 
   then printed in the same order but without duplicates.
   Bridgette Lefatsa
   LFTNTO002
   29 April 2014"""

#Get string list from user
strings=[]
x=input("\nEnter strings (end with DONE):\n")
if x=="DONE":
    print("\nUnique list:\n")
else:
    while x !="DONE":
        strings.append(x)
        x=input("")
    
    #Unique list
    unique_list=[]
    for x in strings:
        if x not in unique_list:
            unique_list.append(x)

    print("\nUnique list:")
    for x in unique_list:
        print(x)