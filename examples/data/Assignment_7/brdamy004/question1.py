# Assignment 7 question 1
# Amy Brodie
# 29/04/2014


words = input("Enter strings (end with DONE):\n")
string_list = []
unique_list = []


# Add strings to list
while words != "DONE":
    string_list.append(words)
    words = input()

# check for duplicate strings and create a unique list
for i in range(len(string_list)):
    if not(unique_list):
        unique_list.append(string_list[i])
    else:
        if not(string_list[i] in unique_list):
            unique_list.append(string_list[i])

# print out unique list
print()
print("Unique list:")
if unique_list:
    for i in range(len(unique_list)):
        print(unique_list[i])