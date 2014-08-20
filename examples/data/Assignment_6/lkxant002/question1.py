word="none"
list1=[]
print("Enter strings (end with DONE):")
while word!="DONE":
    word=input()
    list1.append(word)

print()
print("Right-aligned list:")
        

if list1[0]!="DONE":
    list1=list1[0:-1]
    
    lengths=[]
    for i in range(len(list1)):
        lengths.append(len(list1[i]))
                       
    max1=max(lengths)
        
    for i in list1:
            print((max1-len(i))*" ",i,sep="")
