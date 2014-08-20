'''Program to create a 'unique' list
30 April 2013
Luke Barker'''
strings = input('Enter strings (end with DONE):\n')    #get strings
list_strings = []
while strings != 'DONE':      #terminate with DONE
    if strings not in list_strings:
        list_strings.append(strings)
    strings = input()
print()
print('Unique list:')
for i in list_strings:  #print each value of the list
    print(i)


        