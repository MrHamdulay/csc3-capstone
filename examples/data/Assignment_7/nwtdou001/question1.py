'''question1.py
douglas newton
30 april 2014'''

# array to store strings from the user
strings = []

# map to store strings from user (keys) and whether each was printed (values)
string_printed = {}

# get strings from user until they type 'DONE'
input_string = input ('Enter strings (end with DONE):\n')
while input_string!='DONE':
    strings.append(input_string)
    string_printed[input_string] = False
    input_string = input('')

# print each string in order of list occurence, if not printed already
print ('\nUnique list:')
for string in strings:
    if not string_printed[string]:
        print(string)
        string_printed[string] = True