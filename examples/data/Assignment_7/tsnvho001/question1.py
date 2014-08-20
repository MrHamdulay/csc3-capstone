"""Program to print out entered strings in the same order but without duplications
Tsanwani Vhonani
29 April 2014"""

def strings():
    list_strings=[]
    enter_string=input("Enter strings (end with DONE):\n")
    if enter_string != "DONE":
        list_strings.append(enter_string)
    while enter_string!="DONE":
        enter_string=input("")
        if enter_string != "DONE":
            if not enter_string in list_strings:
                list_strings.append(enter_string)
    print()
    print("Unique list:")   
    for a in list_strings:
        print(a)
strings()
        
    
    