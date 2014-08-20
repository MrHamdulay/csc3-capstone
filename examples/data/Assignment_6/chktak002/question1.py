x=input("Enter strings (end with DONE):\n")
count=0
names=[]
maximum =len(x)
while x !="DONE":# sentinal
    names.append(x) #adds items to the list
    x=input()
    count+=1

    if len(x)>maximum:
        maximum = len(x) #gets max for spacing ofr right alignment
print()   
print("Right-aligned list:")
for j in range(count):
    space=maximum-len(names[j]) #calculates the spacing 
    print(space*" "+names[j])






