"""read a file and reformat lines to a new length, then save in a new file
Tim Hardie
16 May 2014"""

if __name__ == "__main__":
    file_in = input ("Enter the input filename:\n")
    file_out = input ("Enter the output filename:\n")
    width = input ("Enter the line width:\n")
    
    f_in = open (file_in, 'r')
    lines = f_in.readlines()
    f_in.close()
    
    f_out = (file_out, 'w')
    print (lines, file = f_out)
    f_out.close