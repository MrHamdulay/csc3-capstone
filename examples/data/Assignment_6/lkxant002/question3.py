word="none"
list1=[]
party_name=[]
done_check=0

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
while word!="DONE":
    word=input()
    list1.append(word)
    
if list1[0]=="DONE":
    done_check=1
    
list1=list1[0:-1]
list1.sort()

for i in range(len(list1)):
    if (list1[i] in list1[0:i])==False:
        party_name.append(list1[i])

print()
print("Vote counts:")
        
if done_check==0:
         
    votes=[]
    for i in party_name:
        
        print(i," "*(11-len(i)),"- ",list1.count(i),sep="")
    
    
    