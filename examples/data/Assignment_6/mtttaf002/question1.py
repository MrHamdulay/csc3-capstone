"""produce right aligned list of names
tafara mtutu
20 apr 2014"""


names = []
count = 0
aligned = []
sort = ""

#ask user for names
print("Enter strings (end with DONE):")
name = input()
while name.lower() != "done":
    if count < len(name):
        count = len(name)
    names.append(name)
    name = input()
    
#make length of equal to the length of longest string
for i in names:
    sort = " "*(count-len(i)) + i
    aligned.append(sort)
print()
print("Right-aligned list:")
for j in aligned:
    print(j)
