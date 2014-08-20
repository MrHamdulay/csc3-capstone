'''#maisha ivha 
14 may 2014
a  program to reformat a text file so that all lines are at most a given length without breaking words'''


#importing shortcut to wrap text to a given width
import textwrap
def txt():
   
   
    
        
        filename=input("Enter the input filename:\n")   #input file from user         
        file=open(filename,"r")                         #opening the input file
        
        lines=file.read()                               #reading the file
        file.close()                                    
        output=input("Enter the output filename:\n")    #the name of the output file
        outfile=open(output,"w")                        #overwritng to the output file as a way of storing our reformed text
        
        
        #requesting the width from the user      
        width=eval(input("Enter the line width:\n"))
        #print(lines)
        #for i in range(len(lines)):
            
        print (textwrap.fill(lines,width), file=outfile, end=" ") # printing out the reformated text to our output file
        outfile.close()
        
txt()