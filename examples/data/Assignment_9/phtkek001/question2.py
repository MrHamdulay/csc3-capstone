"""Kekolo Phetla
phtkek001
Assignment 9 question 2
output formatting"""

infile = input('Enter the input filename:\n')
outfile = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n'))

f = open(infile,'r')
outfile = open(outfile, 'w')
line = f.readlines()
f.close()

#adding words to a new empty string
lines = ''
for i in line:
    words = i.split(' ')
    for word in words:
        if word == words[-1]:
            lines = lines+word
        else:
            lines = lines+word+' '
            
#finding the endpoint of each line in the output  
def end(lines):
    reverse=lines[width::-1]
    if '\n' in reverse:
        end = width - reverse.find('\n')
    else:
        end = width-reverse.find(' ')
    return end

#printing out the paragraph per line
def print_par(lines):
    if len(lines)<width:
        print(lines)
        print(lines, file=outfile)
    else:
        line_end = end(lines)
        print(lines[:line_end+1], end='\n')
        print(lines[:line_end+1], end='\n', file=outfile)
        print_par(lines[line_end+1:])
        
print_par(lines)
outfile.close
   

  


    