
#Siphesihle Cele
#16 May 2014
#Assignment 9

#statements to get user inputs and line width
#get data and read it from the file.
#then, recreate the data read into the form that id desired.
#lastly, print the recreated file.
import textwrap

                                              
file_1=input("Enter the input filename:\n")
file_last=input("Enter the output filename:\n")
lines_width=eval(input("Enter the line width:\n"))

inputfile=open(file_1,"r")         
s_words= inputfile.read()
inputfile.close()


s_words_list=textwrap.wrap(s_words, lines_width) 

outputfile=open(file_last,"w") 
for z in s_words_list:
    print(z, file=outputfile)
outputfile.close()           