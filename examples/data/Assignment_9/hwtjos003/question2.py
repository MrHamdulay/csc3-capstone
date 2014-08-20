"""line format
Joshua Hewitson
2/5/2014"""

mylist = []
# lines is a list for reading in the lines of the text file
lines = []
string = ""

file_input = input("Enter the input filename:\n")
file_output = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))
word_count = 0
out_string = ""

#read in from the input file
f = open(file_input , "r")
lines = f.readlines()
f.close()

#make a list (mylist) of all the words
for line in lines:
    # for case of new paragraph:
    if line == "\n":
        mylist.append("\n")
    elif line[-1] == "\n":
        mylist += line[:-1].split()
    else:
        mylist += line.split()

#create output string:
for i in mylist:
    word_count += len(i) +1
    if i == "\n":
        out_string += i + "\n"
        word_count = 0;
    elif word_count < line_width +1:
        out_string += i + " "
    else:
        out_string += "\n" + i + " "
        word_count = len(i) +1;
        
#write to the output file
f = open(file_output, "w")
f.write(out_string)
f.close()

