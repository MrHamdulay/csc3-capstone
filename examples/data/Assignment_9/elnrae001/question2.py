'''Program to reformat a text file so that all lines are at most a given length
Author:Raees Eland
Date:10 May 2014'''

inputfile=input('Enter the input filename:\n')
outputfile=input('Enter the output filename:\n')
line_width=eval(input('Enter the line width:\n'))


infile=open(inputfile,'r')
lines=infile.read()
infile.close()


lines=lines.split('\n\n')   # creates a list with paragraphs 
output=open(outputfile,'w')
for i in lines:
    i=i.replace('\n',' ')
    i=i.split(' ') # creates a list of words
    count=-1 # to start counting from position 0
    for word in i:
        count+=len(word)+1 # +1 to include the spaces
        if count <= line_width:
            print(word,file=output,end=' ')
        else:
            print(file=output)
            print(word,file=output,end=' ')
            count=len(word)
    print(file=output)  # if text is in paragraphs 
    print(file=output)
output.close()



    
    

    