def reformat():
    input_f = input('Enter the input filename:\n')
    output_f = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    
    f = open(input_f, 'r')
    line = f.readline()
    f.close()
    
    for i in range(len(line)):
        variant = width
        if width < len(line):
            if line[variant] == ' ':
                line[variant] == '\n'
            else:
                return line[variant - 1]

reformat()