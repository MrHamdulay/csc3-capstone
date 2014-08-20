#Shaylan Lalloo
#LLLSHA008
#finds unique strings in a list


#stores unique numbers
unique = []

cur = input('Enter strings (end with DONE):\n')
#reads input

while cur != 'DONE':
    #if input is already seen, does nothing
    if cur in unique:
        pass
    else:
        #otherwise throws into unique list
        unique.append(cur)
    #reads next input
    cur = input()

#prints list
print()
print('Unique list:')

print('\n'.join(unique))
