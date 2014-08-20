"""reformat a text file so that all lines are at most a given length
Barak setton
11/05/2014"""

#--------- getting info from user ------------
file = input("Enter the input filename:\n")
outfile = input("Enter the output filename: \n")
width = eval(input("Enter the line width:\n"))
#---------------------------------------------

f = open(file,"r")
lstring =""
v=0
line = f.readlines()
if line[len(line)-1][-1:]=="\n":
    line[len(line)-1] = line[len(line)-1][:-1]
    
    

for i in range(len(line)):
    if line[i]=="\n":
        line[i]="\n"   
    elif i == len(line)-1:
        line[i] = line[i]
    else:
        line[i] =line[i][:-1]+" "
    


lstring ="".join(line)
f.close()
space=0
count =0
start =0
ri = open(outfile,"w")

for char in lstring:
    count +=1
    if char ==" ":
        space = count
        
    if char=="\n":
        print(lstring[start:space-1], file =ri)
        print("",file =ri)
        char = lstring[start:start+1]    
        start =space+1
    elif count > width +start:
        print(lstring[start:space-1], file =ri)
        start = space
        char = lstring[start:start+1]
        
print(lstring[start:count],end="", file =ri)
ri.close()
