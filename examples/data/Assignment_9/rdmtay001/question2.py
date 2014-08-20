# Tayla Radmore
# 12 May 2014
# formatting information
from textwrap import fill


infile_name=input("Enter the input filename:\n")
outfile_name=input("Enter the output filename:\n")
line_width=eval(input("Enter the line width: \n"))


infile = open (infile_name, "r")  
information = infile.read ()
words=information.split(" ")

infile.close ()  
outfile = open (outfile_name, "w") 

x=fill(information,line_width)
print(x,file = outfile)
      
      
outfile.close ()
