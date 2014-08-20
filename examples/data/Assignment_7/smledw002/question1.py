#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 27 April 2014
#Function       : removes duplicates from a given list
#Title          : Question1

user_input = input("Enter strings (end with DONE):\n")
unique_list = []

while user_input != "DONE":
    #prevents duplicates from being added to unique_list
    if not user_input in unique_list:
        unique_list.append(user_input)
    user_input = input("")

print("\nUnique list:")
#prints each item individually
for i in unique_list:
    print(i)