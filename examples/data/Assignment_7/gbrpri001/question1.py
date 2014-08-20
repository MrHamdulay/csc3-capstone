"""PRIYANKA GOBERDHAN
STRINGS WITHOUT DUPLICATES
1/05/2014"""

print("Enter strings (end with DONE):\n")
names_list=[]
a=""

while(a!="DONE"):
    a=input()
    names_list.append(a)
names_list.remove("DONE")

words = []

for word in range (len(names_list)):
    if (names_list.index(names_list[word])==word):
        words.append(names_list[word])  

print("Unique list:")
for i in range(len(words)):
    print(words[i])