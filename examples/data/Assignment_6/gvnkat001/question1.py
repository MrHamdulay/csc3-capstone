
text=[]
strings=input("Enter strings (end with DONE):\n")

#compiling list of
while strings != "DONE":
    text.append(strings)
    strings=input("")
    
y=0    
#create list of how long each string in the list 
if len(text)>0:
    characters=[]    
    for j in range(len(text)):
        characters.append(len(text[j]))
    y+=max(characters)


#assign the value of the longest string to y


print()
print("Right-aligned list:")
    
#print strings alligned to the right with the longest string as the width
for i in range(len(text)):
    print(text[i].rjust(y))

