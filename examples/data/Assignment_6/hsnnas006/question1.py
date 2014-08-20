'''program to print out right-aligned list of strings
by nasreen
27/04/14'''

string_list = []

#user enters list of strings
print('Enter strings (end with DONE):')
string = ''
while string != 'DONE':
    string = input()
    string_list.append(string)
string_list = string_list[:-1] #removes 'DONE' string from end of list

#find alignment length
max_word = ''
for word in string_list:
    if len(word) > len(max_word):
        max_word = word
alignment = len(max_word)
#align list
al = "{0:>"+str(alignment)+"}"
#print list
print()
print('Right-aligned list:')
for word in string_list:
    print(al.format(word))