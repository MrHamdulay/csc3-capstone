#Ashton Singh

wList = []


word = input("Enter strings (end with DONE):\n")
while word.lower() != "done":
    if not word in wList: 
        wList.append(word) 
    word = input()
    

print("\nUnique list:")
for word in wList:
    print(word)
    