"""program to enter list of strings and print strings in order but without duplicates
vicky stark
28 april"""

#create an empty string
list_=[] 

#get user to enter input
words=input("Enter strings (end with DONE):\n")

#loop through words and append words to list (until reaches 'DONE')
while words != 'DONE':
    list_.append(words)
    words=input('')
    
#print heading
print()
print("Unique list:")
    
#loop through list and print words (but no duplicates)
list_of_printed='' #create a list so that if words is in list it won't reprint 

for words in list_:
    if words not in list_of_printed:
        print(words)
        list_of_printed+=words
        