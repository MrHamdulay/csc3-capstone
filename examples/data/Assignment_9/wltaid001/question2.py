"""Aiden Walton
Assignment 9 - question 2"""
filename=input("Enter the input filename:\n")
output=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
file=open(filename,"r")
file_orig=file.read()
file.close()

#file_orig=file_orig.replace("\n"," ")
filelist=file_orig.split("\n\n")

for s in range(len(filelist)):
    filelist[s]=filelist[s].replace("\n"," ")
    filelist[s]=filelist[s].split(" ")
newfile=[""]
x=0
for i in range(len(filelist)):
    for word in filelist[i]:
        if len(newfile[x])+len(word)>width:
            newfile.append("")
            x+=1
        newfile[x]+=(word+" ")
    newfile.append("")
    newfile.append("")
    x+=2
    
#for s in range(len(newfile)):
   #newfile[s]=newfile[s][:-1]
#new_s="\n".join(newfile)
new=open(output,"w")
for s in newfile:
    print(s,file=new)
new.close()
    
        

            
        
