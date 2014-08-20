""" Skhulile Thenjwayo
Assignment 9 question2
12/05/2014"""

ifilename = input("Enter the input filename:\n")
ofilename= input("Enter the output filename:\n")
f = open(ifilename,"r")
lines = f.read()
f.close()
lines = lines.replace("\n","")
x = open (ofilename, "a")
x.close ()   
width = eval(input("Enter the line width:\n"))
i=0
while i <= len(lines):
    if i==width:
        while lines[i]!=" " and i>=0:
            i-=1
            if len(lines)<i:
                break
        x = open (ofilename, "a")
        print (lines[0:i], file=x)
        x.close ()        
        lines = lines[i+1:]
        i=0
    i+=1    
        