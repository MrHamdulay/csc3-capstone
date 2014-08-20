# program to print out list of strings without duplicates
# mllgad001
# 27 April 2014

strings = input("Enter strings (end with DONE):\n") # prompt user to enter list of strings

string_list = []
while strings != 'DONE': # when user enters 'DONE', add all strings to empty list
    string_list.append(strings)
    strings = input("")
    
list_ = [] 
for i in string_list: # create a new list without the duplicates
    if not i in list_:
        list_.append(i)
print()
print("Unique list:")
for i in list_: # print all string in the list without the duplicates
    print(i)