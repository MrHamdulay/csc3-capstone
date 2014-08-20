"""program to allign mnumerous input from user
yasha longstaff
24 april 2014"""

string = input('Enter strings (end with DONE):\n')
max_len = 0
string_list = []
while string != "DONE":
    if len(string) > max_len:
        max_len = len(string)
    string_list.append(string)
    string = input()


print ('\nRight-aligned list:')
for item in string_list:
    print(str.format("{0:>{1}}", item,max_len))
    

    