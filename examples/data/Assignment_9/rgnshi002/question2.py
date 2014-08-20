#Shivam Ragoonaden RGNSHI002
#Program to reformat the structure of a given textfile
#10 May 2014

fileinput = input("Enter the input filename:\n")

fileoutput = input("Enter the output filename:\n")

width = eval(input("Enter the line width:\n"))

f = open (fileinput,"r")   

lines = f.read() #Get all the lines in one string value
        
import textwrap

wrapped = textwrap.wrap(lines, width)   #Wrap the text according to the given width

fo = open(fileoutput,"w")  #Output file

for line in wrapped:
    print(line, file = fo)  #Print in the new file

f.close()
 
fo.close()  #Close output file