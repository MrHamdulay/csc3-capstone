"""Right aliging program
alexander whiting
23 april 2014"""

names = []
name = ""
print("Enter strings (end with DONE):")
while name != "DONE":
    name=input()
    names.append(name)
del names[len(names)-1] #removes done from the list
maxlen=0
for i in names: #finds the longest name
    if len(i)>maxlen:
        maxlen=len(i)
print()
print("Right-aligned list:")
for i in names:
    print(" "*(maxlen-len(i)),i,sep="")#adds spaces to the name to right align
    
    
    