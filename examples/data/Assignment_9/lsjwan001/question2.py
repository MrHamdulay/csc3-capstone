# Program reformats a text file, all lines are at most given length
# Wandile Lesejane
# 14 May 2014

#open file
file=input("Enter the input filename:\n")
f=open(file,"r")
lines=f.readlines()
f.close()

file2=input("Enter the output filename:\n")
length=eval(input("Enter the line width:\n"))

count=0
for i in range(len(lines)):
    lines[i]=lines[i][:-1]

line=(" ").join(lines)
line=line.split()
#change paragragh format
para=""
for i in range(len(line)):
    if count<length and count+len(line[i])<length:
        para+=line[i]+" "
        count+=len(line[i])+1
    elif count+len(line[i])==length:
        para+=line[i]+"\n"
        count=0
    elif count+len(line[i])>length:
        para+="\n"+line[i]+" "
        count=len(line[i])+1
#print the new paragragh in the output file    
f2=open(file2,"w")
print(para,file=f2) 
f2.close