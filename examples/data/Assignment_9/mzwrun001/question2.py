"""Program to change the width of a paragraph
Runako Muzwidzwa
13/05/2014"""
input_=input("Enter the input filename:\n")
output=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))
f=open(input_,"r")
lines=f.readlines()
f.close
for i in range (len (lines)):
    lines[i] = lines[i][:-1]
new_list=[]
for line in (lines):
    words=line.split(",")
    new_list.append(words)
g=open(output,"w")
to_print=""
length=0
for word in range(len(new_list)):
    if length<(width-3):
        nxt=new_list[word]
        to_print+=nxt+" "
        length+=len(to_print)
    else:
        to_print+=",\n"

for wrd in to_print:
    print(wrd,file=output)
    



g.close