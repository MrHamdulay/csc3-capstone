# Kate Bell
# BLLKAT005
# 28 April 2014 

# Create array and populate with words entered by user if word not already in array
wordlist = []
word = input("Enter strings (end with DONE):\n")
while not word == "DONE":
    if not word in wordlist:
            wordlist.append(word)  
    word = input("")
    
# Print out array    
print("\nUnique list:")
for word in wordlist:
    print (word)