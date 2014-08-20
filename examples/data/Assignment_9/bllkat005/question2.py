"""BLLKAT005
Kate Bell
12 May 2014
Assignment 9 Q2"""

inputfile = input("Enter the input filename:\n")
outputfile = input("Enter the output filename:\n")
linewidth = eval(input("Enter the line width:\n"))

f = open (inputfile,"r")
text = f.read()
f.close()

#remove new lines, except where there are two in a row, which indicates paragraph separation
text = text.replace("\n\n","~~~")
text = text.replace("\n"," ")
text = text.replace("~~~"," \n\n")

words = text.split(" ")

line = "" 
f = open(outputfile, "w")
for word in words:
    # if word is first word of a new paragraph, it's length doesn't include the "\n"
    if word.startswith("\n"):
        print(line,file=f)
        line=""
        if (len(word[1:])+len(line[1:])) <= linewidth:
                line += word[1:] + " " 
    # if it's the first line of a new paragraph, the line length doesn't include the "\n"    
    elif line.startswith("\n"):
        if (len(word)+len(line[1:])) <= linewidth:
            if not word.startswith("\n"): 
                line += word + " "
        else:
            print (line[:-1], file = f)
            line = word + " "            
    #if adding the word to the line won't make the line too long, add it     
    elif (len(word)+len(line)) <= linewidth:
        if not word.startswith("\n"): 
            line += word + " "
    # if line's as long as it can be, print it to the file    
    else: 
        if not word.startswith("\n"):
            print (line[:-1], file = f)
            line = word + " "
print(line,file=f)
f.close()

