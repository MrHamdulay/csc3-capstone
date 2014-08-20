#input
newstring = ""
liststrings = []
print("Enter strings (end with DONE):")
while newstring != "DONE" :
    newstring = input()
    liststrings.append(newstring)

#find longest
longest = liststrings[0]
for i in range(1,len(liststrings)-1):
    if len(liststrings[i]) >= len(longest):
        longest = liststrings[i]
print(" ")
print("Right-aligned list:")
for j in range(len(liststrings)-1):
    print(" "*(len(longest)-len(liststrings[j])) + liststrings[j])