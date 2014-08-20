#-------------------------------------------------------------------------------
# Name:        queston2
# Purpose:
# Author:      Lungelo
# Created:     10/05/2014
# Copyright:   (c) Lungelo 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

inputfile=input("Enter the input filename:\n")
outputfile=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

f=open(inputfile,'r')
outputfile=open(outputfile,'w')
lines=f.readlines()

f.close()
paragraph=""
for i in range(len(lines)):
    if lines[i][0].islower() and i>0 or lines[i][0]=='(':
        lines[i]=' '+lines[i]
    #if lines[i]=='\n':
    #    lines[i]*=2
    if len(lines[i])>1:
        lines[i]=lines[i][:-1]

    paragraph+=lines[i]


#calculate endpoint
def endpoint(paragraph):
    reves=paragraph[width::-1]
    if '\n' in reves:
        endpoint=width-reves.find('\n')
    else:
        endpoint=width-reves.find(" ")
    return endpoint

def print_line(paragraph):
    if len(paragraph)<width:
        print(paragraph)
        print(paragraph,file=outputfile)
    else:
        end= endpoint(paragraph)
        print(paragraph[:end+1],end='\n')
        print(paragraph[:end+1],end='\n',file=outputfile)
        print_line(paragraph[end+1:])

print_line(paragraph)

outputfile.close()