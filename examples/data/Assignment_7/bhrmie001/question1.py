# Miengha Behardien
# Assignment 7
# 26 April 2014

def strings():                                  #get strings from user
    list_of_strings=[]
    print("Enter strings (end with DONE):")
    string=input()
    while string!="DONE":                       #not add to list_of_strings if DONE
        list_of_strings.append(string)          #add input to lis_of_strings
        while string:
            string=input()
            if string=="DONE":
                break
            list_of_strings.append(string)
    return list_of_strings

def unique_string():                        #create unique strings from old list
    new_strings=[]
    old_list=strings()
    for word in old_list:
        if word not in new_strings:         #adds words to new list not including repeats
            new_strings.append(word)
    print("\nUnique list:")
    for new_word in new_strings:
        print(new_word)                     #prints out each unque string

unique_string()