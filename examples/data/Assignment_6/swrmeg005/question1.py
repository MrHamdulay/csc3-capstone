#A program that allows a user to enter a string of strings followed by the sentinel "DONE" and then prints it out right-aligned with the longest string
#Megan Swartz
#24 April 2014

def list_strings():
    
    #we want the user to enter a list of strings, ended with done 
    #We need to accumulate the strings into a list and initialize an empty list
    
    list_1 = []
    string = input("Enter strings (end with DONE):\n")
    
    while string != "DONE":
        list_1.append(string)
        string = input("")
    
    #find the maximum length and set original length equal to 0
    maxlength = 0
    for i in list_1:
        if len(i) > maxlength:
            maxlength = len(i)
    
    #print out a right-aligned list with the longest string
    print("\nRight-aligned list:")
    for i in list_1:
        print(i.rjust(maxlength))

list_strings()