""""Assignment 9 Question  2 
Adam Edelberg"""
import textwrap


inname = input('Enter the input filename:\n')
outname = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n'))

#read from file

filein = open(inname, "r")
s = filein.read()
filein.close()



#writing to file
fileout = open(outname, "w")

string=''
line=[]
#split on new lines
lines = s.split('\n\n')
for i in range (len(lines)):
    line=(textwrap.wrap(lines[i],width=width))
    lines[i]=''
    for j in line:
        lines[i]+= j
        lines[i]+='\n'
for i in range (len(lines)):
    string+=lines[i]
    string+='\n'
string=string[:(len(string)-2)]
print(string,file = fileout)



fileout.close()
