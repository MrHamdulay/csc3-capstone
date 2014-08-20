"""assignment 7
shannon clacey
1 may 2014"""

def string():
    string = input("Enter strings (end with DONE): \n")
    list1 = [] #this list is put in place to check for any duplicates
    list2 = [] #this list checks to find the first occurence of the word within the list
    while string != "DONE":
        if string not in list1: #if the given string as not yet been mentioned
            list1.append(string)
        else: #if the given string has already been mentioned
            list2.append(string)
        string = input() #continually getting input from user without reprinting input statement
    print()
    print("Unique list:") #printing the output required by the question
    for i in list1:
        print(i)
string()                          