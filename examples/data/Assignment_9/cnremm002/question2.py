"""Rewidth paragraph
Emmanuel Conradie
16 May 2014"""

input_file =input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#open the inputfile for reading
inputfile=open(input_file,"r")

#open the outfile for overwriting
outputfile=open(output_file,"w")

#process each line of the inputfile
lines = inputfile.readlines()         
inputfile.close()
count=-1 

#removing the \n character and splitiing the line into words
for line in lines:
    if line!='\n' :
        line=line.replace('\n','')     
        line=line.split(' ')           
        for word in line:
            count+=len(word)+1         
            if count <= width:
                print(word,file=outputfile,end=' ')
            else:
                print(file=outputfile)
                print(word,file=outputfile,end=' ')
                count=len(word)
    
#provides for printing it into separate paragraphs
    else:
        line=line                     
        print(file=outputfile) 
        print(file=outputfile)
        count=-1
outputfile.close()