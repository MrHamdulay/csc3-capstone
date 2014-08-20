#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014/04/16
#Function       : prints out right-aligned list the user has entered.
#Title          : Question1

user_input = input("Enter strings (end with DONE):\n")
the_users_list = []
#Gets input from the user till a DONE user input == Done
while user_input != "DONE":
    the_users_list.append(user_input)
    user_input = input("")
    
print()

print("Right-aligned list:")

#Determines the length of the longest string


for i in the_users_list:
    #Determines the length of the longest string in the list
    longest_length = len(max(the_users_list, key=len))

    print("{0:>{1}}".format(i, longest_length))


