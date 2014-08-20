#Program to output a list of strings without duplicates
#Kayla Hendricks
#28 April 2014

def unique_list():
    #create empty list to store strings
    str_list=[]
    string = input("Enter strings (end with DONE):\n")
    while string!="DONE":
        #add strings to list
        str_list.append(string)
        string = input()
    print()
        
    print("Unique list:")
    
    #create a second list to store strings less duplicates
    sec_list = []
    for i in str_list:
        if i in sec_list:
            continue
        else:
            sec_list.append(i)
    
    #print each word in second list        
    for i in sec_list:
        print(i)
    
unique_list()