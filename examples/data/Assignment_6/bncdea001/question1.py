#Program to print an indefinite list of strings-right aligned
#Dean Bunce
#21 April 2014

def main():
    #Create empty list
    list_strings=[]
    #Get strings
    strings=input("Enter strings (end with DONE): \n \n")
    
    #Add strings to list while the user is inputting
    while strings!="DONE":
        list_strings.append(strings)
        strings=input("")
    
    #Find the longest string    
    longest=0
    for strings in list_strings:
        if len(strings)>longest:
            longest=len(strings)
                
            
    print("Right-aligned list:")
    #Print each string
    for string in list_strings:
        print("{0:>{1}}".format(string,longest))   
    

main()