#Program to print out a right-aligned list with the longest string
#Kayla Hendricks
#23 April 2014

def list_of_strings():
    #start with an empty list
    the_list = []
    string=input("Enter strings (end with DONE):\n")
    while string != "DONE":
        #add user's input to list
        the_list.append(string)
        string = input()
    print("\nRight-aligned list:")
    length = 0
    for i in the_list:
        #storing longest length as variable "length"
        if len(i)>length:
            length=len(i)
    for i in the_list:
        #printing out right-aligned list with length of longest string
        right_list = i.rjust(length)
        print(right_list)

list_of_strings()
        