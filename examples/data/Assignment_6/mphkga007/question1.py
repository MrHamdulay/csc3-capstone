""" program that enters a list of people and right align them
kenneth mphele
2014\04\20"""


# creates a list of strings as long as the user doesnt input "DONE" keeps adding the strings to the list
strings=input("Enter strings (end with DONE):\n")
if strings!="DONE":
        
    list_string=[]
    while not strings=="DONE":
        list_string.append(strings)
        strings=input("")
        
    
    
    #checks the longest string in the list   
    length_list=[]
    for i in list_string:
        length=len(i)
        length_list.append(length)
    maximum=max(length_list)

    print("\nRight-aligned list:")
    #right aligns with the longest string
    for i in list_string:
        gap=maximum-len(i)
    
        print(" "*gap+i)
        
else:
    print("\nRight-aligned list:")
    
    




    
    
    #print(i)
    
#maximum=max(list_string)
#print(maximum)
    