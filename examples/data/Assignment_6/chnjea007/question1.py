# assignment 6 question 1
print("Enter strings (end with DONE):")

name = ""
names = []
while name != "DONE":
    name = input()
    names.append(name)

max = 1
for i in range(len(names)):
    if len(names[i]) > max:
        max = len(names[i])
        
print("\nRight-aligned list:")

for i in range(len(names) - 1):
    print(" " * (max - len(names[i])), end = "")
    print(names[i])