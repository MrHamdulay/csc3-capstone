"""reformats text file so all lines are at most a specified length
Jonathan Nathan 
10 may 2014"""

from textwrap import fill

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))

def reformat(line_width):
    lis = ''
    paragraph_array = []
    final_array =[]
    
    f = open(input_file, 'r') 
    for line in f:
        lis += line
    f.close() 
    
    number_paragraphs = lis.count('\n\n')
    
    for i in range (number_paragraphs + 1):
        paragraph_array.append(lis[:lis.find('\n\n') ])
        lis = lis[lis.find('\n\n') + 1 : ]
        
    for i in range (len(paragraph_array)):
        if paragraph_array[i][0] == '\n':
            paragraph_array[i] = paragraph_array[i][1:]        
        
    
    for paragraph in paragraph_array:
        final_array.append(fill(paragraph, line_width))
    

    
    h = open(output_file, 'w')
    for item in final_array:
        print(item + '\n', file = h)
    h.close()
    

reformat(line_width)