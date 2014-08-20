'''Jason Pietersen'''
names= input('Enter strings (end with DONE):\n')
string_list= []

while (names != 'DONE'):
    if not names in string_list:
        string_list.append(names)

    names= input()
print('\nUnique list:')
for i in string_list:
    print(i)