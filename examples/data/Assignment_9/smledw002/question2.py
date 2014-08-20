#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014/05/15
#Function       : Format an input text file to a given width
#Title          : Question2

in_filename = input("Enter the input filename:\n")
out_filename = input("Enter the output filename:\n")
line_width = int(input("Enter the line width:\n"))
in_file = open(in_filename)
text = in_file.readlines()
in_file.close()
#creates a list where paragraphs will be stored
paragraphs = [[]]

for line in text:
    #removes new line characters
    line = line.replace("\n", "")
    #checks if its the end of a paragph
    if line != "":
        words = line.split(" ")
        #adds a to the paragrph if its not the end of A PARAGRAPH
        paragraphs[-1] += words
    else:
        #STARTS A NEW PARAGRPH
        paragraphs.append([])
out_file = open(out_filename, "w")
line = ''
lines = []


for paragraph in paragraphs:
    #stores lines of a given width
    for word in paragraph:
        #checks the length
        if len(line) + len(word) <= line_width:
            #puts the word at the end of the line
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
            #adds any left over words
    if len(line) >= 1:
        lines.append(line)

    for i in lines:
        print(i, file=out_file)
    out_file.write('\n')
    line = ''
    lines = []
out_file.close()
