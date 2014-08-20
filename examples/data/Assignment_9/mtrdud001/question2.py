"""text wrapping given a number to wrap upon
Dudley Mutero
15/5/14"""


a=input("Enter the input filename\n")
d=input("Enter the output filename:\n")
b=eval(input("Enter the line width:\n"))
bb=b
f=open(a,"r")
g=open(d,"w")
for i in f:
    list1=[]
    list1=i.split(" ")
    print(list1)
    
    tempvar=("\n") in list1
    temp3=len(list1)
    if temp3>1 and list1[-1]!= "\n":
        temp4=list1[-1]
        temp5=temp4[0:-1]
        del list1[-1]
        list1.append(temp5)
    if tempvar == True and temp3 > 1:
        list1.remove("\n")
    #temp3=list1[0]
    if list1[0]=="\n":
        print("\n",file=g,end="")
        b=bb
       
    else:
        k=0
        for j in list1:                 #error when looking for empty line
           # temp1=list1.find ("\n")
           # if temp1 != -1:              #remove the new line printing
             #   j=j[0:temp1]
            
           # k=0
            c=len(j)
            if c <= (b-k):               #boundary value problem
                b-=(c)
                k+=1
                print(j,file=g,end=" ")
            else:
                print("\n"+j,file=g,end=" ")
                b=bb-c
                k=1
                
              
            
f.close()        
g.close()
two=open("2.txt.","r")
q1=two.readlines()
two.close()
print(q1)