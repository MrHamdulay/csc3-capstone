"""program that rewrites list of words right-aligned"""

names= []

name=input('Enter strings (end with DONE):\n')


while True:
    if name == "DONE":
        break
    names.append(name+"\n")
    name=input()
    
    
longest = 0
if len(names) != 0:
    longest = max(map(len, names))

print()
print("Right-aligned list:")

for i in range (len(names)):
    print(names[i].rjust(longest), end ="")
