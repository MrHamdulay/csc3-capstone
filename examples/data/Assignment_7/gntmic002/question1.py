#Assignment 7.1
#Michael Gant
#27/04/2014

#Remove string duplicates

lNames = []
sInput = ""

sInput = input("Enter strings (end with DONE):\n")
while sInput != "DONE":
    if not sInput in lNames:
        lNames.append(sInput)
    sInput = input("")
    
print("\nUnique list:")
for i in lNames:
    print(i)
    