"""Remove duplicates from a string
Telisha Ramlall
27 April 2014"""

words = []

#Input words
word = input("Enter strings (end with DONE):\n")
while word.lower() != "done":
    if not word in words: #check if word exsists in list
        words.append(word) #if word does not exist in list, append to list
    word = input()
    
#Output list with unique words
print("\nUnique list:")
for word in words:
    print(word)
    