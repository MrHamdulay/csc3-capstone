# Michaela Heale
# Assignment 6 Question 1
# Right-Aligned Array

# allows for user input
opt = input("Enter strings (end with DONE):\n")
names = []
c = 0

while not opt == "DONE":
    names.append(opt)
    opt = input()
    c+= 1
  
# finds the longest word's length
long = 0
for z in range (0,c):
    place = len(names[z])
    if (place>long):
        long = place

print("\nRight-aligned list:")
for q in range (0,c):
    lng = len(names[q])
    space = long - lng 
    print((" "*space),names[q],sep="")
