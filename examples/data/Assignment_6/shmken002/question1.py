"""right aligned list from given string list
ringo shima 
23/04/14"""

def list_names():
    x = [] #initiate empty string
    
    y = ""
    list_names = print ("Enter strings (end with DONE):") #prompt for input of names
    
    while list_names != "DONE": #definebreak point
        
        list_names = input() #keep asking for input
        x.append(list_names) #add new names to list
    

        if len(list_names) > len(y):
            y = list_names
    x.remove("DONE")
    
    print()
    print("Right-aligned list:")
    
    
    formStr = "{0:>{1}}"
    for i in x:
        
        print (formStr.format(i, len(y)))
        
    
list_names()


    
    
    
    


    