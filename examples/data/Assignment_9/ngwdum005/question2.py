'''Dumisani Ngwenza
NGWDUM005
10/05/2014
Assignment 9 Question 2'''

#require input from user
#infile = input ('Enter the input filename:\n')
#outfile = input ('Enter the out filename:\n')
length = int (input('Enter the line width:\n'))

f = open ("input.txt", "r")

line = f.readline()
other_file = open("output.txt", "w")
#formats the text file and prints it into a new text file
while line!='':
    line = line[:-1]
    if len(line) < length:
        first = line
        line = f.readline()
    elif line[length] !=' ' and line[length-1]!=' ' and line[length-2]!=' ' and line[length-3]!=' ' and line[length-4]!= ' ' and line[length-5] != ' ' and line[length-6] == ' ':
        first = line[:length-6]
        line = line[length-6:] + f.readline()
    elif line[length] !=' ' and line[length-1]!=' ' and line[length-2]!=' ' and line[length-3]!=' ' and line[length-4]!= ' ' and line[length-5] == ' ':
        first = line[:length-5]
        line = line[length-5:] + f.readline()
    elif line[length]!= ' ' and line[length-1]!=' ' and line[length-2]!=' ' and line[length-3]!=' ' and line[length-4]== ' ':
        first = line[:length-4]
        line = line[length-4:] + f.readline()   
    elif line[length] !=' ' and line[length-1]!=' ' and line[length-2]!= ' ' and line[length-3] == ' ':
        first = line[:length -3]
        line = line[length-3:] + f.readline()
    elif line[length] != ' ' and line[length-1]!=' ' and line[length-2] == ' ':
        first = line[:length-2]
        line = line[length-2:] +  f.readline()    
    elif line[length]!=' ' and line[length-1] == ' ':
        first = line[:length-1]
        line = line[length-1:] +  f.readline()
    elif line[length] == ' ':
        first = line[:length]
        line = line[length:] +  f.readline()
        
    print (first, file=other_file)
f.close()
other_file.close()

#removes the newline characters at the end of the sentence
other_file = open("output.txt", "r")
line = other_file.readlines()
other_file.close()
for i in range(len(line)):
    line[i] = line[i][:-1]   
    
#removes the preceding spaces of a sentence
for i in range(len(line)):
    if line[i][0] == ' ':
        line[i] = line [i][1:]

#re-writes the text file without the preceding spaces        
other_file = open("output.txt", "w")
for i in range(len(line)):
    print (line[i], file=other_file)
other_file.close()