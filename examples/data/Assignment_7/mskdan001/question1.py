#danson masuka
#program to remove epeated words
#1 may 2014

#input for the list and all
names = []
nme = input("Enter strings (end with DONE):\n")
while nme != 'DONE':
        names.append(nme)
        nme = input("")

#check for repeated words in list and add to ANOTHER NEW LIST WITOUT REPEATED WORDS
unrep = []
for word in names:
        if not word in unrep:
                unrep.append(word)
print ()
print ("Unique list:")
#loop to print out the list
for new_list in unrep:
        print (new_list)