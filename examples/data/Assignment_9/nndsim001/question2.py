#This Python program reformats a text file so that all lines are at most a given length. 
#Do not break up words. Write the formatted text to a new text file.

#Treat each set of consecutive non-empty lines as a paragraph - join such lines together with a single space if necessary.

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 11 May 2014

# Ask user for input file name
inputname = input("Enter the marks filename:\n")
# Ask user for output file name
outname = input("Enter the output filename:\n")
# Ask for desired width
width = eval(input("Enter the line width:\n"))

f = open(inputname,"r") # Open the file
content = f.readlines() # Store the contents of the file in a list
f.close() # Close the file

words = []
usewords = []

# Separate the words at the spaces
for i in range(len(content)):
    for j in range(len(content[i])):
        words.append(content[i].split(" "))
        break

# Create a 1-d lists with the words instead of a list of lists
for k in range(len(words)):
    for l in range(len(words[k])):        
        if words[k][l] == '\n': # Look for paragraphs
            usewords.append('/*-+')
        else:
            usewords.append(words[k][l])
        #if words[k][l].find('\n') == -1: 
            #usewords.append(words[k][l])
        #else: # Remove new line character at the end of a string
            #usewords.append(words[k][l][:words[k][l].find('\n')])

# Remove \n at the end of the strings if it has any
for l in range(len(usewords)):
    usewords[l] = usewords[l].rstrip('\n')
    

out = open(outname,"w") # Open the output file

# This part prints the text from the input file to output file
# by printing exactly 40 characers per line

space = width # Available printing space
for m in range(len(usewords)):     
    if len(usewords[m]) > space: # Print new line if printing space is insufficient
            print("\n",end='',file=out)
            print(len(usewords[m]),space,usewords[m],"-->: wont fit here, new line")
            space = width    
    
    if usewords[m] == '/*-+': # Print new paragraph
            print("**************new paragraph***************")
            print("\n\n",end='',file=out) 
            space = width 
    
    if len(usewords[m]) <= space and usewords[m] != '/*-+': # Print the word
        print(len(usewords[m]),space,usewords[m])
        print("{0}".format(usewords[m]),end='',file=out)        
        space -= (len(usewords[m])) # Track available printing space
        if space != 0: # Print a space after each word
            print(" ",end='',file=out)
            space -= 1 # Track available printing space

out.close() # Close the file after printing

#Sample File (input.txt):

#Your program should store a single row of the triangle and calculate each subsequent row by adding a value to the values 
#immediately above it and to its left.  The values on each line must be space-separated.

#Sample File (output.txt):

#Your program should store a single row
#of the triangle and calculate each
#subsequent row by adding a value to the
#values immediately above it and to its
#left.  The values on each line must be
#space-separated.

#Sample console I/O:
#Enter the input filename:
#input.txt
#Enter the output filename:
#output.txt
#Enter the line width:
#40