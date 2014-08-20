# program for Manipulating textfiles
# Anthony Jacob
# 12 May 2014

import textwrap

f = input("Enter the input filename: \n")
O = input("Enter the output filename: \n")
width = eval(input("Enter the line width: \n"))

if width<0:
    print("Invalid width")
else:
    innerf = open(f,"r")
    outterf = open(O,"w")
    txt = innerf.read()
    
    
    print (textwrap.fill(txt,width), file=outterf)
    innerf.close()
    outterf.close()