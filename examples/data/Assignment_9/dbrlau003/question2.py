#Lauren de Bruyn
#Reformat a text file so that all lines are at most a given length
#10 May 2014

import textwrap

#prompt user for input and output file names and the width of the lines
txt_input= input("Enter the input filename: \n")
txt_output= input("Enter the output filename: \n")
linewidth= eval(input("Enter the line width: \n"))

#open input file, read the input file lines, close input file
f = open (txt_input, "r")
lines=f.readlines()
f.close ()

#create one string of text in input file
#longline=''
#    if line[-1]=="\n":
#        line=line[:-1]+" "
#        longline=longline+line
#   else:
#       longline=longline+line
newlines= " ".join(lines)

#seperate long string into strings on given width        
final = textwrap.wrap(newlines, linewidth)

#print strings of correct width to output file
g= open(txt_output, "w")
for i in final:
    print(i, file=g)
g.close()

