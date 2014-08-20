#Joy Arendse-Gorvalla
x=input("Enter strings (end with DONE):\n") #asking for input
if x=="DONE":
    g=[] #if input is DONE you dont add anothing to the list
else:
    g=[x]
    l=len(x) #l is the length of the input x
    y=""

    while y!="DONE":#loop keeps going until "DONE" is entered
        y=input() #input without reasking question
        g.append(y) #adds the input y to the list g
        L2=len(y)
        if L2>l:
            l=L2 #the larger L2 will become the new l
            
    g.remove("DONE") #removes DONE from the list so that it wont print in the right-aligned list
    
print() #prints a blank line
print("Right-aligned list:")
for i in g:
    print(i.rjust(l)) #right aligns every name in the list g with the lenght of l




