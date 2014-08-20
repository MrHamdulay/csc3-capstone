"""question 1
clare walker
27 april2014"""

words=[]    # initiate array
print("Enter strings (end with DONE):")

while True:
    word=input("")
    if word == "DONE":
        break
    elif word not in words: #check for duplicate
        words.append(word) #add if not duplicate
        
print()        
print("Unique list:")
for word in words:
    print(word)