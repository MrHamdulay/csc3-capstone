# program to print out strings inputted by user without duplicates
# khadeejah omar
# 29 april 2014

string = input("Enter strings (end with DONE): \n")

# create list of strings inputted by user
string_list = []
while string != "DONE" :
    string_list.append(string)
    string = input("")

# create list of the inputted strings without its duplicates
unique_string_list = []
for string in string_list :
    if string not in unique_string_list :
        unique_string_list.append(string)

# print the list of unique strings
print("\nUnique list:")
for string in unique_string_list :
    print(string)