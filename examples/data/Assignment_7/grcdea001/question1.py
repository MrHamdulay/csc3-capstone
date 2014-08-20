"""Program to print out a list of strings without duplicates, assignment 7 question 1
Dean Gracey
27 April 2014"""

word=input("Enter strings (end with DONE):\n")
words = []

while word!= "DONE":
    if not word in words:
            words.append(word)    
    word = input("")
    
print("\nUnique list:")        
for i in words:
    print(i)