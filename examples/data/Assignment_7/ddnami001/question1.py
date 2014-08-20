#Amitha Doodnath
#DDNAMI001
#30/04/2014
#Programme to remove repitition from input strings in an array

words=[]
word=input("Enter strings (end with DONE):\n")

while word != "DONE":
    if not word in words:
        words.append(word)
    word=input()

print()
print("Unique list:")

for i in range (len(words)):
    print(words[i])