"""aligning a list of strings
Jacqueline Blomendahl
23/04/2014"""

#asking user for input and creating parameters
strings=input("Enter strings (end with DONE):\n")
l=[]
l.append(strings)
max_length=len(strings)
counter=0
#asking for more values until DONE is typed in
while strings != "DONE":
    strings=input()
    l.append(strings)
    counter+=1
    #finding the lenght of the longest string
    if len(strings) >= max_length:
        max_length= len(strings)
#printing
print()
print("Right-aligned list:")        
for i in range(counter):
    
    y=l[i]
    print(y.rjust(max_length))

