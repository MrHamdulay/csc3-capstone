def line_maker(string, length):
    if len(string) > length:
        line = string[0:length]
        if line[-1] != " " and string[len(line)] != " ":
            while line[-1] != " ":
                line = delete_till_space(line)
            line = line[:-1]
            return line, string[len(line) + 1:]  
        else:
            if line[-1] != " ":
                return line, string[len(line) + 1:]
            else:
                return line[:-1], string[len(line):]
    else:
        line = string
        return line, ""
            
def delete_till_space(string):
    if string[-1] == " ":
        return string
    else:
        return delete_till_space(string[:-1])
    
def paragraph_printer(paragraph_list, length, name):
    outfile = open(name, 'w')
    for paragraph in paragraph_list:
        while paragraph > "":
            line, paragraph = line_maker(paragraph, length)
            print(line, file = outfile)
        print('\n', end = '', file = outfile)
            
def main():
    # getting inputted variables
    name_infile = input('Enter the input filename:\n')
    name_outfile = input('Enter the output filename:\n')
    line_length = eval(input('Enter the line width:\n'))
    
    # reading text from input
    infile = open(name_infile, "r")
    in_text = infile.read()
    infile.close()
    
    # splitting text into list of paragraphs
    paragraph_list = in_text.split('\n\n')
    for i in range(len(paragraph_list)):
        paragraph_list[i] = paragraph_list[i].replace('\n', ' ')
    
    # printing reformatted paragraphs to output
    paragraph_printer(paragraph_list, line_length, name_outfile)
   
    
if __name__ == '__main__':
    main()