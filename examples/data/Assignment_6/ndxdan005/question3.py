import collections
heading="Independent Electoral Commission"
print(heading)
print("-"*len(heading))
print("Enter the names of parties (terminated by DONE):\n")
listed=[]
c=input()
while c != "DONE":
    listed.append(c)
    c=input()
counter={}
for element in listed:
    if not element in counter:
        counter[element]=1
    else:
        counter[element]+=1
print("Vote counts:")
final=sorted(counter)
for i in range(len(final)):
    for element in counter:
        if element==final[i]:
            print(str(element) + " "*(10-len(element)) + "- " + str(counter[element]))
        else:
            continue

        