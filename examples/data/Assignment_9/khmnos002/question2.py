"""program to reformat text file to lines of equal length
Nosipho Khumalo
10 May 2014"""

def reformat():
    #initiating variables
    words = []
    input_file = input("Enter the input filename: \n")
    out_file = input("Enter the output filename: \n")
    width = eval(input("Enter the line width: \n"))
    
    # open and load the data from the file
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()
    
    # chop off the trailing carriage returns
    for i in range (len (lines)):
        lines[i] = lines[i][:-1] 
    
    #formatting text file
    for i in range(len(lines)):
        split_line = lines[i].split(" ")
        words += split_line


    #write to output file
    out = open(out_file, "w")
    line = ""
    for i in range(len(words)):
        if (len(line) + len(words[i])) < width:
            line += words[i] + " "
        else:
            print(line, file = out)
            line = words[i] + " "
    
    #printing what is left in line    
    print(line, file = out)
    out.close()
    
    f = open(out_file, "r")
    for line in f:
        print(line, end = "")
    f.close()
    
reformat()
    
    