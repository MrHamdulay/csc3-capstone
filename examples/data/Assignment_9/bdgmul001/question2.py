''' fit text into width supplied by user to a specific file
by : badugela mulisa
16 may 2014'''
import textwrap
def reform():
    # user inputs
    inputfile=input("Enter the input filename:\n")           
    output=input("Enter the output filename:\n")
    width=eval(input("Enter the line width:\n"))
    
    # use the files assigned    
    file=open(inputfile,"r")
    lines=file.read()
    file.close()    
    outfile=open(output,"w")
    # wrap the text to applied width
    print(textwrap.fill(lines,width), file=outfile,end='')
    outfile.close()
    
    
reform()