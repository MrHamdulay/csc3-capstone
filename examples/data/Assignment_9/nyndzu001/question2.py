"""Dzunisani Nyoni
12 May 2014
A program to print formated text files"""


def main():
        
        textfile=input("Enter the input filename:\n")
        output_file=input("Enter the output filename:\n")
        line_width = eval(input("Enter the line width:\n"))
        counter=0   #Initialization of a variable to count the width
        
        f=open(textfile, "r") #Reads the textfile
        
        lines=f.read()# Read all the text in the file to a variable lines
        
        f.close() #Closes the textfile
        
        textlist=lines.split() #creates a list of the words in the old textfile
        
        new_file=open(output_file, "w") #opens and overwrites the output text file
        
        for i in range(len(textlist)):#Iterates through the list
                
                counter+=len(textlist[i])+1 #Add the width to the counter
               
                if counter<line_width:
                        print(textlist[i],end=' ', file=new_file)
                        
                else:
                        print('\n', end='',file=new_file)
                        print(textlist[i],end=' ',file=new_file)
                        counter= len(textlist[i])
        new_file.close() #closes the output textfile

if __name__=='__main__':
        main()