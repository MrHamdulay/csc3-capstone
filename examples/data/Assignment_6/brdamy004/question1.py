# Assignment 6 question 1
# Amy Brodie
# 22/04/2014

strings = input("Enter strings (end with DONE):\n")
count = 0
string_list = []

# input strings and append them to a list
while strings != "DONE":
    string_list.append(strings)
    strings = input()
    count += 1

print()
print("Right-aligned list:")

if string_list:    
    # find length of longest word 
    max = len(string_list[0])
    for i in range(count):
        if max < len(string_list[i]):
            max = len(string_list[i])

    # format and print items in list
    for i in range(count):
        print("{0:>{width}}".format(string_list[i], width = max))