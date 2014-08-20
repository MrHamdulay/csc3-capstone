"""Program to store list of strings and output it right-aligned with the longest string
Pankaj Munbodh
20 April 2014"""
#Create list of strings
str_list=[]
get_string = input("Enter strings (end with DONE):\n")
if get_string !='DONE':
    str_list.append(get_string)


#sentinel loop keeps asking for input until user enters'DONE'
    while (get_string=='DONE')==False:
        get_string = input("")
        if get_string!='DONE':
            str_list.append(get_string)

#Width of character of maximum length is found 
    width=max(len(word) for word in str_list)

    print()
    print("Right-aligned list:")

#List is iterated through and each character is printed right-justified in field width of maximum with found earlier
    for word in str_list:
        print(word.rjust(width))
#output for exception
else:
    print()    
    print("Right-aligned list:") # if-else statement to cater for exception if user types in "DONE" right at start