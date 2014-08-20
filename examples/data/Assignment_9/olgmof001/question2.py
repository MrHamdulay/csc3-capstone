"""Tofunmi Olagoke
OLGMOF001
Programme that formats"""
inputf = input("Enter the input filename:\n")
outputf = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(inputfile, "r")
content = f.read()
f.close()


lst= content.split(' ') 
para =''
countline = 0 


for x in lst:
    #if line is smaller than required length its will write the whole line
    countline += len(x)
    if width > countline:
        para = para + x + ' '
        countline = countline+1 
        
        
    else:
    #if line is longer than required length its will write the excess on a new line
        countline = 0
        para = para + x + ' '
        countline = len(x) + 1
        para = para + '\n'
  
f = open(outputf, "w")
print(para, file = f)
f.close()