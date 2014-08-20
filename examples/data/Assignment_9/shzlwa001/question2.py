# Program for formatting lines in a text file to some other file with specified format
# Lwazi Shezi
# 16 May 2014

# Get all the inputs
input_filename = input('Enter the input filename:\n')
output_filename = input('Enter the output filename:\n')

# Store the input file content in a list
input_file = open(input_filename,'r')
input_file = input_file.read()
#input_file.close()
input_file = input_file.split()

width = eval(input('Enter the line width:\n'))

output_lines = []

# Now store all the lines from the input file to some output file, with each line equal to the specified width.
while len(input_file) > 0 :
    line = ''
    for word in input_file :
        counter = 0
        while counter < width :
            if len(word) <= (width - len(line)) :
                if line != '' :
                    if len(word) < (width - len(line+ ' ')) :
                        line += ' ' + word
                        counter += len(word)
                        input_file = input_file[1:]  
                    else : break
                else:
                    line += word
                    counter += len(word)
                    input_file = input_file[1:]
                break
                
            else :
                break
            
        if len(word) > (width - len(line)) :
            break
                
    output_lines.append(line)

# Take the lines from the output lines list to some output file
output_lines = '\n'.join(output_lines) 
output = open(output_filename,'w')   
print(output_lines,file = output)
output.close()