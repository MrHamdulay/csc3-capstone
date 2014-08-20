#RusselJhamba
#03/05/2014

listofnames= []
a= []
NameList=input("Enter strings (end with DONE):\n")
x= [NameList]
while NameList!="DONE":
    x=x+listofnames
    NameList=input("")
    listofnames=[NameList]
for i in range(len(x)):
    if x[i] not in a:
        a.append(x[i])
    
print("\nUnique list:")
for g in a:
    print(g)
    
    
