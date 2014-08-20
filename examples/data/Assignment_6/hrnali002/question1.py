"""A program that prints out a list right aligned
Alison Hoernle
HRNALI002
20 April 2014"""

# get list until 'DONE'
list = []
strings = input("Enter strings (end with DONE):\n")

while strings != 'DONE':
    list.append(strings)
    strings = input('')

print()
print("Right-aligned list:")

if list == []:
    print('')

else:
    # determine length of longest string in list
    length = len(list[0])
    for string in list:
        length_next = len(string) # determines length of the next word in the string
        
        # if this word is longer than previous word, make this the new length
        if length_next > length:
            length = length_next
            
    # right align list with longest length word
    for string in list:
        print(string.rjust(length))