'''Programjme for printing vertical list of names 
Siphesihle Zwane 
20/04/14'''
empty=[] #empty array
new=""
print("Enter strings (end with DONE):") #insructions to user
#while new!= "Done": 
while True:
    new=input("")
    if new =="DONE":
        print()
        break
    empty.append(new) #changing the list
#empty.remove("Done")
long=max(empty, key=len)#finding the length of the longest string
long=len(long)
print("Right-aligned list:")
for i in range(len(empty)):
    draw=empty[i]
    print(draw.rjust(long)) #googled r adjust function :)

    

