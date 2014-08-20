"""Cherise Dube 
14 May 2014
Program to reformat a text file so that all lines are at most a given length."""
import sys
sys.setrecursionlimit (60000)

filename_in=input("Enter the input filename:\n")
filename_out=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

f=open(filename_in,"r")
s=f.read()
f.close()

s=s.replace("\n"," ")
    
def strings(s):
    if len(s)>width:
        if s[width]==" ":
            return strings(s[:width])+ "+"+strings(s[width+1:])
        elif s[width].isalpha():
            for i in range(width):
                if s[width-1-i] !=" ":
                    continue
                else:
                    a=width-1-i
                    break
            return strings(s[0:a]) + "+"+strings(s[a:])
        
    else:
        return s
    
strings=strings(s).split("+")


f=open(filename_out,"w")
for i in strings:
    if i[0]==" ":
        print(i[1:],file=f)
        
    else:
        print(i,file=f)
f.close()


