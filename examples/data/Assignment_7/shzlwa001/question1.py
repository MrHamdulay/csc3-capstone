# program for removing duplicate strings after "first encounter"
# Lwazi Shezi
# 1 May 2014

print('Enter strings (end with DONE):')

# initialise variables to be used 
new_string = ''
string_list = []

while new_string != 'DONE' :
    new_string = input()
    # add the new string in the list containing the strings, only if it has not been encountered before
    if new_string != 'DONE' and new_string not in string_list:
        string_list.append(new_string)
        
print()
print('Unique list:')

for i in string_list:
    print(i)
        