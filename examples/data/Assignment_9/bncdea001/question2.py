#Assignment 9, Question 2
#Dean Bunce
#Program to print out the text from a text file in a given line width, and write to a new text file.
import textwrap
def main():
    
    #Get input file
    
    in_file=input("Enter input filename:\n")
    out_file=input("Enter output filename: \n")
    column=eval(input("Enter the line width:\n"))
    
    #Open the input file
    work_file= open(in_file, "r")
    
    #read file into a long string
    string=work_file.read()
    
    
    
    
    
    #Format String
    
    out_string=textwrap.wrap(string,width=column)
    
    
        
    #Open a file to write to
    write_to=open(out_file, "w")
    
    #Print each line in formatted string
    for line in out_string:
        print(line, file=write_to)
    
    #Close File
    write_to.close()
    
            
main()

