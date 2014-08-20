"""Assignment 9, question2, question2.py
10 May 2014 
by Jonathan Ovadia"""
import math
def main():
    file_name = input("Enter the input filename:\n")
    output_file = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    format_file(file_name,output_file,width)


def format_file(file_name,output_file,width):
    #open text file
    f = open(file_name,"r")
    lines = []
    new_lines = []
    remainder = []
    count = 0 
    #read in text file and strinp return charachters 
    for i in f:
        if i != "":
            i = i.rstrip('\r\n')
        lines.append(i)
    current_line = ""
    while len(remainder) > 0 or len(lines) > count:
        #add next line for manipulation
        try:
            line = lines[count]
        except IndexError:
            line = ""
            next_line =[]
        if len(remainder) > 0 :
            current_line  = " ".join(remainder[::-1]) + " "+ line
        else:
            current_line  =  line
        remainder=[]
        while len(current_line)> width:
            current_line = current_line.split(" ")
            remainder.append(str(current_line[-1]))
            current_line = current_line[0:-1]
            current_line = " ".join(current_line)
        else:
            new_lines.append(current_line + "\r\n")
        count +=1
    f.close()
    f = open (output_file,"w+")
    for i in new_lines:
        f.write(i)
    f.close()
if __name__ =="__main__": main()

