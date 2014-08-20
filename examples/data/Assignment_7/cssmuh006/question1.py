"""Removing duplicate words from a list of strings
M HAAROON CASSIEN, CSSMUH006"""

words=[]
inpt=""
print("Enter strings (end with DONE):")
while(inpt!="DONE"):
    inpt=input()#get input
    added=False
    for i in range(len(words)):
        if inpt==words[i]:#check if word is in list
            added=True
            
    if not added and inpt!="DONE":# if it is not add it in
        words.append(inpt)       
        
print("\nUnique list:")
for i in range(len(words)):#print outut
    print(words[i])    