#List of Strings
#29/04/2014
#Sydney Simpson

#Find unqiue words
def unique(lst):
    words=[]
    position=[]
    for i in (lst):
        words.append(i)
        position.append(lst[i])
    #print (words)
    #print(position)
    
    print("Unique list:")
    for j in range (len(words)):
        num=0
        for p in position:
            if p==j:
                #print (j)
                print (words[num])
            num+=1
        
#Enter List
lst={}
n=0
choice=""
print("Enter strings (end with DONE):\n")
while choice!="DONE":
    choice=input()
    if choice not in lst and choice!="DONE":
        lst[choice]=n
        n+=1
unique(lst)

