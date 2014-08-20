#takunda chikondo
#a progrmme to reformat text from a file and wi=rite it into a new text file 
import textwrap

filename = input("Enter the input filename:\n")
output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
sentence = ""

f = open(filename,"r")
lines = f.readlines()
f.close

for i in lines:
    sentence= sentence + i

line = textwrap.wrap( sentence , width) #wraps text of a given width

newfile = open(output,"w") # print every iteration of the wrapped text on a new line
for i in line:
    print( i ,file = newfile)
newfile.close()

    

