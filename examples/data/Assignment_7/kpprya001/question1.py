words = input("Enter strings (end with DONE):\n")
wordsArray=[]
removedDuplicates=[]
count = 0
while words != "DONE":
    wordsArray.append(words)
    words=input("")

for word in wordsArray:
    if not word in removedDuplicates:
        removedDuplicates.append(word)
        count += 1
print()        
print("Unique list:")
for i in range (count):
    print(removedDuplicates[i])

        
        
