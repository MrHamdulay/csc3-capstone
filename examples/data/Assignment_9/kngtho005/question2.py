# question2.py
# program to reformat a text file so that all lines are at most a 
# a given length without breaking up words.
# Thomas Konigkramer
# 11 May 2014
  
def text_wrapper():   
    
    f_input = input("Enter the input filename:\n")
    f_output = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))         
    
    # opening input file, reading into lines of string and closing again
    f = open(f_input, "r")
    lines = f.readlines()
    f.close()
    
    # removing all the "\n"
    # however, if "\n" succeeds ".", indicates end of paragraph, thus keep that "\n"
    # and if the letter following the "\n" is a lowercase letter, then it is not a new paragraph
    for i in range(len(lines)-1):
        if len(lines[i]) >= 2:
            if lines[i][-1] == "\n" and lines[i][-2] != ".":     
                lines[i] = lines[i][:-1]
        if lines[i][-1] == "\n" and lines[i+1][0].islower():
            lines[i] = lines[i][:-1]
    
    # creating one long string    
    lines_string = ""
    for j in range(len(lines)):
        if lines[j][-1] == "\n" and len(lines[j]) == 0 or j > 0 and lines[j-1][-1] == "\n" :
            lines_string += lines[j]
        elif j == 0:
            lines_string += lines[j]
        else:
            lines_string += " " + lines[j]
    
    # creating list of what the new file should contain
    print_lines = []
    while len(lines_string) > 0:

        if len(lines_string) > width:
            # checks that a word isn't cut: finds closest space to specified width
            for i in range(width):
                if lines_string[width-i] == " ":
                    count = width - i
                    break
            # checks if line contains "\n". Must then separate, because paragraph
            if "\n" in lines_string[:count]:
                for j in range(count):
                    if lines_string[width-j] == "\n":
                        count = width - j
                        break
        # can't have a line of the specified width if the line isn't even that long        
        else:
            count = len(lines_string)
    
        # appends line to list
        print_lines.append(lines_string[:count])
      
        # shortens length of string according to length of string appended to list
        if len(lines_string) - count == 0:
            lines_string = ""
        else:
            lines_string = lines_string[count + 1:]
    
       
    f_out = open(f_output, "w")
    for i in range(len(print_lines)):
        # checks and removes space at the beginning of each paragraph as result of editing
        print(print_lines[i], file = f_out, sep = "")
    f_out.close()

text_wrapper()