"""program to print unique list
nasonkwe hampwaye
2014/04/30"""
def unique_list():
    #get strings
    strings=[]
    strings_input=input("Enter strings (end with DONE):\n")
    while strings_input!="DONE":
        strings.append(strings_input)
        strings_input=input("")
    print()
    print("Unique list:")
    #checking for unique string   
    new_strings=[]    
    for i in range(len(strings)):
        if strings[i] in new_strings:
            continue
        else:
            new_strings.append(strings[i])
    #since len is less than len of old list         
    for j in new_strings:       
        print(j)        
        
    
unique_list()    