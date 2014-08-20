enter = input ("Enter strings (end with DONE):\n")
words = []
newlist=[]
count = 0
while enter != "DONE":
    words.append (enter)
    enter = input("")
    for i in words:
        if not i in newlist:
            newlist.append(i)
            count = count + 1
print()
print("Unique list:")
for i in range (count):
    print (newlist[i])
    
        