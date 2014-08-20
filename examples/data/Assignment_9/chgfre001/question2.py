#program to reformat a text file making all lines at most of a given length
#FJChigwaza
#16 may 2014

import textwrap

txt=''

f_input=input('Enter the input filename:\n')

f=open(f_input,'r')
line=f.readlines()
f.close()

f_output=input('Enter the output filename:\n')
for i in line:
    #line=line.split()
    #line.remove('\n')
    txt+=i
#print(txt)
width=eval(input('Enter the line width:\n'))
    
    
formatt=textwrap.wrap(txt,width)

o=open(f_output,'w')
for i in formatt:
    #print(txt)
    print(i,file=o)
o.close()


