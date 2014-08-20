"""Program to edit a text file and produce sentences of fixed length
by Tinashe Choga
17/05/2014"""
import textwrap 
input_file=input("Enter the input filename:\n") 
output_file=input("Enter the output filename:\n")
wide=eval(input("Enter the line width:\n"))
file = open(input_file, "r") # reading from the file
string=file.read() # reading all the lines into a  variable
file.close()

text= textwrap.wrap(string,width=wide)
file2=open (output_file, "w") # creating the file and writing to it
for sentence in text:
   print(sentence, file=file2)
file2.close()