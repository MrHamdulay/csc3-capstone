"""list of string then print them out without repeating the same one twice
kenneth mphele
27/04/2014"""
def list_of_strings():
    strings=[]
    string2=[]
    #enter a list of strings as long as the user hasnt entered DONE
    enter=input("Enter strings (end with DONE):\n")
    while enter!="DONE":
        strings.append(enter)
        enter=input("")
    #check if a string appears only once in a list
    for i in strings:
        if i in string2: continue
        string2.append(i)
    #print the list
    print("\nUnique list:")
    for list in string2:
        print(list)
    
    
    
list_of_strings()