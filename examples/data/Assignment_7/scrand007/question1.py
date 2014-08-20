words = []
printedwords = []

print ("Enter strings (end with DONE):")

while True:
    word = input("")
    if word == "DONE":
        break 
    words.append(word)      
    
print ("")
print ("Unique list:")
for i in range(len(words)):
    if words[i] not in printedwords:
        print (words[i])
        printedwords.append(words[i])