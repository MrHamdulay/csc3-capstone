'''program to reformat a text file so that all lines are at most a given length
Patrick Boroughs
10 May 2014'''

#user input
inputName = input("Enter the input filename:\n")
outputName = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#open readable input and writable output files
inputF = open(inputName,'r')
outputF = open(outputName, 'w')

#read lines into array
lines=inputF.readlines()

#delete \n from end of lines, keep paragraph seperation
for i in range(len(lines)):
    if len(lines[i])>=2:
        lines[i] = lines[i][:-1]+' '
    else:
        lines[i] = lines[i]+'\n'

#join into a single string        
line = ''.join(lines)

#create array for output
newlines = []

#flag to test if line is finished
moreline = True

while moreline:
    
    #paragraph seperation case  
    if '\n\n' in line[:width]:
        newline = line[:line.index('\n\n')]+'\n'
        line = line[line.index('\n\n')+2:]
        
    #last line of output
    elif len(line)<=width:
        moreline = False
        newline = line
        
    else:
        char = line[width]
        tempwidth = width
        
        #only break when there's a space
        while char!=' ':
            tempwidth-=1
        
            char = line[tempwidth]
        
        #create next output line
        newline = line[:tempwidth]
            
        
        #shorten line that hasn't been but into output array yet
        line = line[tempwidth+1:]
    
    #add to output array    
    newlines.append(newline)

#output printing
for line in newlines:
    print(line,file=outputF)

#close files   
inputF.close()
outputF.close()