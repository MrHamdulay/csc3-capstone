def text_wrap():   
    
    f_input = input("Enter the input filename:\n")
    f_output = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))         
    
    f = open(f_input, "r")
    lines = f.readlines()
    f.close()
    
    
    for i in range(len(lines)-1):          # Removes all the \n
        if len(lines[i]) >= 2:
            if lines[i][-1] == "\n" and lines[i][-2] != ".":     
                lines[i] = lines[i][:-1]
        if lines[i][-1] == "\n" and lines[i+1][0].islower():
            lines[i] = lines[i][:-1]
       
    lines_string = ""
    for j in range(len(lines)):
        if lines[j][-1] == "\n" and len(lines[j]) == 0 or j > 0 and lines[j-1][-1] == "\n" :
            lines_string += lines[j]
        elif j == 0:
            lines_string += lines[j]
        else:
            lines_string += " " + lines[j]
    
    print_lines = []
    while len(lines_string) > 0:

        if len(lines_string) > width:
            for i in range(width):
                if lines_string[width-i] == " ":
                    count = width - i
                    break
            if "\n" in lines_string[:count]:
                for j in range(count):
                    if lines_string[width-j] == "\n":
                        count = width - j
                        break  
        else:
            count = len(lines_string)
        print_lines.append(lines_string[:count])
        if len(lines_string) - count == 0:
            lines_string = ""
        else:
            lines_string = lines_string[count + 1:]     
    f_out = open(f_output, "w")
    for i in range(len(print_lines)):
        print(print_lines[i], file = f_out, sep = "")
    f_out.close()

text_wrap()