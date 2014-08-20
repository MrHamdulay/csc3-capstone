# Program to format text files
# Hendrik Joosten
# 16/05/2014

import textwrap

filename_in = input("Enter the input filename:\n")
filename_out = input("Enter the output filename:\n")
line_width = int(input("Enter the line width:\n"))

lines = []
f = open(filename_in,"r")
lines = f.readlines()
f.close()

s = ""
for i in range(len(lines)) :
     if lines[i] == "\n":
          lines[i] = ":: "
     s = s + lines[i].replace("\n"," ")
l = textwrap.wrap(s,line_width)
s = ""
for j in range(len(l)):
     s = s + l[j] + "\n"
s.replace("::","\n\n")

f = open(filename_out,"w")
print(s,file=f)
f.close()