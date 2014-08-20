'''program to print a list of strings without duplicates
nasreen hoosain
30 april 2014'''

#get input from user
string_list = []
print('Enter strings (end with DONE):')
string = input()
while string != 'DONE':
    string_list.append(string)
    string = input()
#reverse list and delete repeated words
reverse_list = string_list[::-1]
for word in reverse_list:
    while reverse_list.count(word) != 1: #if word occurs more than once, delete repetitions
        reverse_list.remove(word)
new_list = reverse_list[::-1] #reverse list again
#print unique list
print()
print('Unique list:')
for word in new_list:
    print(word)


        
    