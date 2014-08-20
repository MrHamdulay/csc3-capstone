from collections import OrderedDict

words=[]
x = input("Enter strings (end with DONE):\n")
while x!= "DONE":
        if x != "DONE":
                words.append(x)
                x = input("")

print()
print("Unique list:")

newwords = list(OrderedDict.fromkeys(words))

for newword in newwords:
        print (newword)


#the
#old
#man
#and
#the
#sea
#DONE