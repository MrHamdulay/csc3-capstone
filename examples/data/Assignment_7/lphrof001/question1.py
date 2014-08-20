#prompt user to enter inputs
#place the inputs into a list
words=[]
x=input("Enter strings (end with DONE):\n")
while x!="DONE":
    words.append(x)
    x=input("")
    if x=="DONE":
        break

print()
print("Unique list:")
#create a list where nothing is repeated
second=[]
for i in words:
    if not i in second:
        second.append(i)
    else:
        continue

for j in second:
    print(j)