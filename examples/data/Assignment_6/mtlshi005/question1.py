#Shivaan Motilal
#20/04/2014


print("Enter strings (end with DONE):")  #Tells user what sentinel is
list=[]
string=""
while string!="DONE":
    string=input()                       #User inputs a list of string
    list.append(string)                  #Each string added to accumulator list
    
print()

print("Right-aligned list:")


MAX=0

for s in list:
    L=len(s)
    if L>MAX:
        MAX=len(s)
#print(MAX)
    #print( "{0:>len(s)}".format(s))
    #if s=="DONE":
       # break
       
for s in list:
    if s=="DONE":
            break    
    print(" "*(MAX-len(s)),s,sep="")
    
    
    
