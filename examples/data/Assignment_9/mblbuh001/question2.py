# question2.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 13 May 2014

infileName = input("Enter the input filename:\n")#get input filename from user
outfileName = input("Enter the output filename:\n")#get output filename from user
width = input("Enter the line width:\n")#get line width from user

infile = open(infileName, "r")#open original textfile for reading
line = infile.readline()#set line to be the first line of the original textfile

characters = []#initialize characters to be an empty list
while line != "":
    if line == "\n":#if the line is an empty line
        characters.append(line)#append characters list with an empty line
    else:
        for i in range(len(line.split())):
            if line.split()[i] == "\n":
                pass#pass all the newline characters at the end of each line
            else:
                characters.append(line.split()[i])#append characters list with each word in original textfile
    line = infile.readline()#set line to be next line of original textfile
   
outfile = open(outfileName, "w")#open new textfile for writing
new_line = ""#initialize new_line to empty string

for i in range(len(characters)):
    if len(new_line)+len(characters[i]) <= eval(width):#checks if length of each line is less than the width supplied
        if characters[i] == "\n":#checks for an empty line
            print(characters[i],file=outfile,end= "")#print character to new textfile
            print(characters[i],file=outfile,end= "")#print character to new textfile
            new_line = ""#initialize new_line to empty string
        else:
            print(characters[i],file=outfile,end= " ")#print character to new textfile and end off with a space
            new_line += characters[i]#add word to new_line
            new_line += " "#add space character to new_line
    else: 
        new_line = ""#initialize new_line to empty string
        if characters[i] == "\n":#checks for an empty line
            print(characters[i],file=outfile)#print character to new textfile
            new_line = ""#initialize new_line to empty string
        elif characters[i] == "left.":
            print("\n",file=outfile,end="")#print character to new textfile
            print(characters[i],file=outfile,end= "  ") #print character to new textfile and end off with a space
            new_line += characters[i]#add word to new_line
            new_line += " "#add space character to new_line            
        else:
            print("\n",file=outfile,end="")#print character to new textfile
            print(characters[i],file=outfile,end=" ")#print character to new textfile and end off with a space
            new_line += characters[i]#add word to new_line
            new_line += " "#add space character to new_line

infile.close()#close original textfile
outfile.close()#close new textfile