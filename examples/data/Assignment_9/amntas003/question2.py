#AMNTAS003  #Tashfia Amin   #Due Date: 16 May 2014
#Question 2: Assignment 9   #Reformatting files to specified length per line

import textwrap 

#Create variables for input of details used in the program
initial = input("Enter the input filename:\n")
output = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

# open the input file closing file
f = open (initial, "r")
text = f.read()
f.close()

#Split text into paragraphs before
if text.count("\n\n") > 0:
    para = text.split("\n\n")

#Wrap the text with textwrap module so that each line has a specified width    
if text.count("\n\n") > 0:
    text = []
    for x in para: 
        sentence = textwrap.wrap(x,width) 
        text += sentence
        text += " "                                     #Add a space between paragraphs
else:
    text = textwrap.wrap(text,width)

#Write the changes made onto a new file
new = open(output, "w")
for i in text: 
    print(i, file = new)
new.close()