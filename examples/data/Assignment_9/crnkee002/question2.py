"""A9Q2 - Paragraph Editor
11/05/2014
CRNKEE002"""

import textwrap

def main():
    infile = input('Enter the input filename:\n')
    outfile = input('Enter the output filename:\n')
    width = eval(input('Enter the line width:\n'))
    para = read_file(infile)
    newlines = format_paragraph(para, width)
    write_file(outfile, newlines)
    
def read_file(file):
    f = open(file, 'r')
    newpara = []
    para = f.readlines()
    f.close
    if len(para) == 1:
        f.close
        return para        
    else:
        #remove trailing characters
        for i in range(len(para)-1):
            para[i] = para[i][:-1]
            string = ''
        #combine lines
        for i in range(len(para)):
            if para[i] == '':
                pass
            else:
                if para[i][len(para[i])-1] != ' ':
                    string += para[i] + ' '
                else:
                    string += para[i]
                if i != len(para)-1:
                    if para[i+1] == '':
                        print(string)
                        newpara.append(string)
                        string = ''
        newpara.append(string)
    print(newpara)
    return newpara

def format_paragraph(paragraph, spacing):
    newlines = []
    for i in range(len(paragraph)):
        newlines.append(textwrap.wrap(paragraph[i], spacing))
    return newlines

def write_file(file, lines):
    f = open(file, 'w')
    for i in range(len(lines)):
        for x in range(len(lines[i])):
            if lines[i][x] == '':
                print('', file = f)
            else:
                print(lines[i][x], file = f)
        print('', file = f)
    f.close()   
                      
if __name__ == '__main__':
    main()