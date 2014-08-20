#Gillian Wachira
#15/05/2014
#reformatting a text file

infile=input("Enter the input filename:\n")
outfile=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
line=0

#open and read the file then close it

f=open(infile, "r")
lines=f.readlines()
f.close

for i in range(len(lines)-1):
    lines[i]=lines[i][:-1]
x=[] #create empty list
 
for i in range(len(lines)):
    if lines[i]=="":
        x.append(["\n\n"]) #create a paragraph if space
    else:
        x.append(lines[i].split(" "))
#open and overwrite in the outfile considering the width

f=open(outfile,"w")
for i in range(len(x)):
    for j in range(len(x[i])):
        if line==0:
            line=len(x[i][j])+1
            print(x[i][j],end=" ",file=f)
        elif x[i][j]=="\n\n":
            line=0
            print(x[i][j],sep="",end=" ",file=f)
        elif len(x[i][j])+line>width:
            line=len(x[i][j])+1
            print("\n",x[i][j],sep="",end=" ",file=f)
        else:
            if len(x[i][j])+line<=width:
                line+=len(x[i][j])+1
                print(x[i][j],end=" ",file=f)
            else:
                print(x[i][j],end="",file=f)
f.close()
                   
                 
                   