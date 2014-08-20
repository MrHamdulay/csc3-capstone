#VHRJOC001
#assignment 9
#formatting text

# variables
file=input("Enter the input filename:\n")
editfile=input("Enter the output filename:\n")
length=eval(input("Enter the line width:\n"))
count=0

#making the file
f=open(file,"r")
lines=f.readlines()
f.close()
temp=[]

for i in range(len(lines)):
    lines[i]=lines[i][:-1]
    if lines[i]=="":
        temp.append("\n\n")
    else:
        temp.append(lines[i].split(" "))

#overwriting new file
nf=open(editfile,"w")

for i in range(len(temp)):  
    for j in range(len(temp[i])):
        if temp[i][j]=='\n':
            count=0
            print(temp[i][j],sep='',end='',file=nf)
        elif len(temp[i][j])+count>length:
            print('\n',temp[i][j],sep='',end=' ',file=nf)
            count=len(temp[i][j])+1
        else:
            if len(temp[i][j])+count<=length:
                count+=len(temp[i][j])+1
                print(temp[i][j],end=' ',file=nf)
            else:
                print(temp[i][j],end='',file=nf)
                
                
nf.close()                