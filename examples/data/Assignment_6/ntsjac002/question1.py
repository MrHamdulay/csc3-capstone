'''A program that get a list of names from the user and print out the list right-aligned with the longest string
Jacob Ntesang
4 April 2014'''

#Get the list from the user and until they enter enter "DONE",keep the names coming
Names = input ("Enter strings (end with DONE):\n\n")
Names_str = []
while Names != "DONE":
    Names_str.append (Names)#Add names to the empty list till the user types DONE
    Names = input("")
   
else:
    print("Right-aligned list:")
    Max=0
    for i in Names_str:
        if Max < len(i):
            Max = len(i)
            
    for j in Names_str:
        
        print(" "*(Max-len(j))+j)
        
        
        
        