"""making a list of names
Yonela Ford
30 April 2014"""



def list():
    #CREATE A LIST OF STRINGS
    strings=[]
    command=input("Enter strings (end with DONE):\n")
    while command !="DONE":
        strings.append(command)
        command=input("")
    print()
    print("Unique list:")
    #make a new list of unique string
    new_strings=[]
    #check if list has repeated string
    for i in strings:
        if not i in new_strings:
            new_strings.append(i)
    for i in new_strings:
        #print each unique string
        print (i)
        
list()
