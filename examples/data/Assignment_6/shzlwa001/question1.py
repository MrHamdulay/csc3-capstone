# Program for formatting strings
# Lwazi Shezi
# 25 April 2014

print('Enter strings (end with DONE):')

# Initialise variables
list_strings = []
new_string = ""

# Get strings
while new_string != 'DONE':
    new_string = input("")
    list_strings.append(new_string)
print()
    
maximum = list_strings[0]

# find the maximum length string
for i in range(0,len(list_strings)):
    if len(list_strings[i-1]) and len(list_strings[i]) > len(list_strings[i-1]):
        maximum = list_strings[i]
        
    else: continue

# the maximum-length string would be wrong if it occurs as the first inputted string, this is to account for that case
if len(list_strings[0]) >= len(maximum):
    maximum = list_strings[0]

# output the strings right-aligned with the maximum length string
print('Right-aligned list:')
for i in list_strings[:len(list_strings)-1]:
    max_length = len(maximum)
    x = '{0:>'+str(max_length)+'}'
    print(x.format(i))