word="none"
list1=[]
print("Enter strings (end with DONE):")
while word!="DONE":
    word=input()
    list1.append(word)

print()
print("Unique list:")
        

if list1[0]!="DONE":
    list1=list1[0:-1]
    
    list2=[]
    
    for i in range(len(list1)):
        if list1[i] not in list1[0:i]:
            list2.append(list1[i])
    
    for i in list2:
        print(i)