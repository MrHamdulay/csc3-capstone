#Assignment 7, Question 1
#Avreyna Kistensamy
#27 April 2014

words = []

strings = input("Enter strings (end with DONE):\n")
while strings != "DONE":
    words.append(strings)
    strings = input("")
    
unique = []
for word in words:
    if not word in unique:
        unique.append(word)
        
print("\nUnique list:")
for word in unique:
    print(word)
    