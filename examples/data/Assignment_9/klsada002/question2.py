"""KLSADA002
Assignment 9 Q2
2014-05-13"""
import textwrap

inputname = input('Enter the input filename:\n')
outputname = input('Enter the output filename:\n')
linewidth = eval(input('Enter the line width:\n'))

read = open(inputname, "r")
s = read.read()
read.close()
i=0
"""while True:
    if len(lines[i]) > linewidth:
        for j in range(len(lines[i]),1,-1):
            if lines[i][j-1:j] == ' ' and j-1 <= linewidth:
                s=lines[i][j:]
                lines[i] = lines[i][:j-1]
                if s == '\n':
                    s=s
                elif s[len(s)-1:len(s)]=='\n':
                    s = s[:len(s)-1]
                if i == (len(lines)-1):
                    lines.append(s)
                else:
                    lines[i+1] = s + ' '+lines[i+1]
                break
    else:
        break
    i+=1"""
t=''
y=[]
write = open(outputname, "w")
lines = s.split('\n\n')
for i in range (len(lines)):
    y=(textwrap.wrap(lines[i],width=linewidth))
    lines[i]=''
    for j in y:
        lines[i]+= j
        lines[i]+='\n'
for i in range (len(lines)):
    t+=lines[i]
    t+='\n'
t=t[:(len(t)-2)]
print(t,file = write)
write.close()
