'''Dumisani Ngwenza
NGWDUM005
29/04/2014
Assignment 7 Question 1'''

#creating empty list
list_of_strings = []
strings = input ('Enter strings (end with DONE):\n')

#populating list_of_strings
while strings != 'DONE':
    list_of_strings.append(strings)
    strings = input ()

#eliminating duplicate strings
string_list = []
for i in list_of_strings:
    if i not in string_list:
        string_list.append(i)

#printing out strings
print ()
print ('Unique list:')
for i in string_list:
    print (i)

#print (string_list)