'''This program reformat a text file so that all lines are at most a given length
Nxumalo Goodman
16 May 2014'''

#prompt the user to enter the input filename
infile = input('Enter the input filename:\n')         
#prompt the user to enter the output filename
outfile = input('Enter the output filename:\n')      
#prompt the user to enter the width of the lines
width = eval(input('Enter the line width:\n')) 

#open and reads the input filename.
f=open(infile,'r')
#open and writes to the output filename.
outfile = open(outfile,'w')
lines = f.readlines()

f.close()
statement = ''
for i in range(len(lines)):
    if lines[i][0].islower() and i > 0 or lines[i][0] ==  '(':
        lines[i] = ' '+lines[i]
    
    if len(lines[i]) > 1:
        lines[i] = lines[i][:-1]

    statement += lines[i]


#calculate lastpoint
def lastpoint(statement):
    backward=statement[width::-1]
    if '\n' in backward:
        lastpoint = width - backward.find('\n')
    else:
        lastpoint = width - backward.find(' ')
    return lastpoint

def newlines(statement):
    
    if len(statement) < width:
        print(statement)
        print(statement,file=outfile)
        
    else:
        stop= lastpoint(statement)
        print(statement[:stop+1],stop='\n')
        print(statement[:stop+1],stop='\n',file=outfile)
        newlines(statement[stop+1:])

newlines(statement)
outfile.close()