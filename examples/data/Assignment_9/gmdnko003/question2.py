'''program to reformat text fine so that each line is at most a given length without breaking up words
nkosi gumede
13 may 2014'''

import sys
sys.setrecursionlimit(100000)

x=input("Enter the input filename:\n")
y=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

#input.txt
f=open(x,"r")
lines= f.readlines()
f.close()

#Remove '\n' from <lines> array
for i in range(len(lines)):
    lines[i]= lines[i][:-1]
    if lines[i]=="":
        del lines[i]

text=lines[0]
#Call function to add '\n' after " " for len(lines)<40
listed=[]
for i in text:
    listed.append(i)

def string_text(start,width): #to slice string of length- width, replacing ' ' with '\n'
    if width<len(listed):
        if listed[width-1]!=" ":
            if width<=len(listed):
                string_text(start,width-1)  
        elif listed[width-1]==" ":
            listed[width-1]='\n'
            if width+40<=len(listed):
                string_text(width,width+40)        
                
string_text(0,width)

new_string="".join(listed)
#problem: width+40<=len(listed)
f= open(y,"w")
print(new_string, file=f)
f.close()

f= open(y,"r")
data=f.readlines()
f.close()