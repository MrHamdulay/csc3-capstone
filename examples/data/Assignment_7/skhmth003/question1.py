#Module that collects a set of strings from a user and prints out a unique list of the provided strings
#Gordon Skhosana
#2/05/2014

def Get_strings():
    """Function that get strings from user"""
    global string_list
    string_list=[]
    next_string=""
    first_string=input("Enter strings (end with DONE):\n")
    if first_string!="DONE":
        string_list.append(first_string)
        while next_string!="DONE":
            next_string=input("")
            if next_string!="DONE":
                string_list.append(next_string)
    else: string_list=[" "]
def Unique_list():
    """Function that generates unique list"""
    Get_strings()
    print()
    string_lookup=''
    if string_list!=[" "]:
        for i in string_list:
            if i in string_lookup:
                continue
            else: string_lookup+=i+" "
        unique_list=string_lookup.split()
        print("Unique list:")
        for i in unique_list:
            print(i)
    else:
        print("Unique list:")
        print(" ")
Unique_list()