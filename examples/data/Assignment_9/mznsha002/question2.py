# 15 May 2014
# Shaun Muzenda
# A program to reformat a text file so that all lines are at most a given length

input_file =input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#open the inputfile for reading
inputfile=open(input_file,"r")

#open the outfile for overwriting
outputfile=open(output_file,"w")

#process each line of the inputfile
lines = inputfile.readlines()          #creates a list with each line as an item
inputfile.close()
count=-1 
for line in lines:
    if line!='\n' :
        line=line.replace('\n','')     #removing the \n character
        line=line.split(' ')           #splitiing the line into words
        for word in line:
            count+=len(word)+1         #including the character after the word
            if count <= width:
                print(word,file=outputfile,end=' ')
            else:
                print(file=outputfile)
                print(word,file=outputfile,end=' ')
                count=len(word)
    else:
        line=line                      #provides for printing it into separate paragraphs
        print(file=outputfile) 
        print(file=outputfile)
        count=-1
outputfile.close()