"""removes duplicates from list and prints out new list
mishka latib
01 may 2014"""

#user enters list of inputs

p=input("Enter strings (end with DONE):\n")

a=0
words=[p]

if p!="DONE":
    while a!='DONE':
        a=input("")
        words.append(a)

#checks for duplicates and deletes them

new = words[0:(len(words)-1)]
w=[]

q=a
while new!=[]:
    if new[0] not in w:
        w.append(new[0])
    if new[0] in w:
        del new[0]
        
#makes new list

print("")
print("Unique list:")

for i in w:
        print(i)
