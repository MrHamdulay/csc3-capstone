# reformats a text file so that all lines are at most a given length
# Conor O'Sullivan
# 10/05/2014


#main function: prompts user for input and output file name and line width
def main():
       infile = input("Enter the input filename:\n")
       outfile = input("Enter the output filename:\n")
       width = eval(input("Enter the line width:\n")) 
       
       readfile = open(infile, "r")
       writefile = open(outfile, "w")

       readlines = readfile.read()
       #Check how many spaces after a the full stop
       spaces = 0
       pos_fs = readlines.find(".")
       if readlines[pos_fs+1: pos_fs+3] == "  ":
              spaces = 1
       else:
              spaces = 0   
       
       #split by paragraphs
       readlines = readlines.split("\n\n")
       #split sentence into words and print formated length to output file
       line = ""
       for para in readlines:
              words = para.split()
              
              for word in words:
                     if word[-1] == ".":
                            word = word + " "*spaces
                            
                     if len(line + " " + word) <= width:

                            line += (word + " ")
                     
                     elif len(line + word) == width:
                            line += word 
                            
                     else:
                            print(line, file=writefile)
                            line = word + " "
              print(line, file=writefile)
              print(line)
              line = ""
              print("",file=writefile)
              
              

       
       readfile.close()
       writefile.close()
       readlines2 = open(outfile, "r")
       readlines2 = readlines2.read()
       print(readlines2)
       
main()