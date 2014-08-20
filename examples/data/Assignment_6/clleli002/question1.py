"""list of strings printed out right-aligned with the longest string
Elizabeth Cilliers
19/04/2014"""


def listOfstr():
    
    #create list
    list_of_strings=[]
    
    # get a list of names
    string = input ("Enter strings (end with DONE):\n")
    # as long as user has not typed done
    while string != "DONE":
        # store name in array
        list_of_strings.append (string)
        # get next name
        string = input ("") 
    
     #determine the length of the longest string in the list of strings
    maximum=0       
    for string in list_of_strings:
        if string=="DONE": 
            break
        if len(string)>maximum: #if length of string is greater than current value for maximum then make this value the new maximum.
            maximum=len(string)
        
    
    print()
    print ("Right-aligned list:") # print out the list of strings right-aligned with the longest string.
    
    for string in list_of_strings:

        space=" "*(maximum-len(string))
        print (space,string,sep="")    
        
listOfstr()
    