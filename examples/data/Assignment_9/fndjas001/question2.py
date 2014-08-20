"""A program that makes all the lines in a file a certain length
Jason Findlay
13/05/2014"""

infilename=input("Enter the input filename:\n")
outfilename=input("Enter the output filename:\n")
line=input("Enter the line width:\n")

f=open(infilename,"r")
words=f.readlines()
f.close()

for i in range(len(words)):
    words[i]=words[i][:-1]

words2=words[0]
if len(words)>1:
    for i in words[1:]:
        if i =="":
            words2+="\n\n"
        else:
            words2+=" "+i

words2=words2.split(" ")
for i in range(len(words2)-1):
    words2[i]=words2[i]+" "

f=open(outfilename,"w")
newline=""
for i in words2:
    if i =="":
        print("",file=f)
    if len(newline)+len(i)<=int(line):
        newline+=i
    else:
        print(newline,file=f)   
        newline=i

if newline!="":
    print(newline,file=f)
f.close()
