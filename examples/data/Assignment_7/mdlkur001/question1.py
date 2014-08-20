"""Kureshlen Moodley
MDLKUR001
3 May 2014"""
#programme to print entered list without repitions

#create blank list for words to be entered into

entries=[]
entry=input("Enter strings (end with DONE):\n")
while entry !="DONE":
    entries.append(entry)
    entry=input()
    
#create second blank list where words will only be stored once
    
strings=[]
for i in entries:
    if i not in strings:
        strings.append(i)
    else:
        pass
    
#print list    

print("\nUnique list:")
for i in strings:
    print(i)       