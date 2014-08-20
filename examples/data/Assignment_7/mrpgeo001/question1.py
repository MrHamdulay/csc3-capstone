"""Program to print unrepeated lists of words
Geoff Murphy
MRPGEO001
27 April 2014"""

strings = input("Enter strings (end with DONE):\n")

words = []

while strings != 'DONE':  #Continues until the sentinel word 'DONE' is entered
    if strings == 'DONE':
        break
    elif strings in words:   #Does nothing if the new word is already in the list
        pass
    else:
        words.append(strings)    #Adds the word to the list if it is not already in the list
        
    strings = input('')


print('')    
print('Unique list:')
for i in words:                #Prints out the list of words
    print(i)