# Unique list entry
# James Behr
# 2014-04-30

def listinput():
    strings = []
    print('Enter strings (end with DONE):')
    while True:
        add = input()
        if add == 'DONE':
            break
        strings.append(add)    
    return strings

strings = listinput()
# Use a set to filter non-unique values
unique = list(set(strings))
# Sort according to the orginal list
unique.sort(key = lambda k: strings.index(k))
print()
print('Unique list:')
for item in unique:
    print(item)