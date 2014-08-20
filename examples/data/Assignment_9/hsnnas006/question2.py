'''program to reformat text file
nasreen hoosain
11/05/14'''

#function to remove newline characters from file and keep paragraph form
def para_split(file_list):
    splt = lines.split('\n\n') #splits on basis of paragraphs
    paragraph = []
    for i in range(len(splt)):
        par = splt[i]
        par = par.replace('\n', ' ') #replace newlines with spaces
        paragraph.append(par)    
    #para_string = '\n\n'.join(paragraph) #rejoins paragraph without newlines in between
    return paragraph
    
#function to format string in given width
def form_str(s, w):
    if len(s) <= w:
        return s
    else:
        sw = w #string width = width
        while s[sw] != ' ': #while character in postion sw != space, move position 1 back
            sw -= 1
        return s[:sw] + '\n' + form_str(s[sw+1:], w) #return function from sw

if __name__ == '__main__':
    
    inputfilename = input('Enter the input filename:\n')
    outputfilename = input('Enter the output filename:\n')
    width = eval(input('Enter the line width:\n'))
    
    #open file, readlines and close
    inputfile = open(inputfilename, 'r')
    lines = inputfile.read()
    inputfile.close()    
    
    #print to outputfile and close
    paragraph = para_split(lines)
    f = open(outputfilename, 'w')
    for line_str in paragraph:
        print(form_str(line_str, width), file = f, end = '\n\n')
    f.close()