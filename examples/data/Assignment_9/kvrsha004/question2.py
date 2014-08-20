""" Q2 of Assignment 9: Reformatting a text file according to given line width
Shaheel Kooverjee - KVRSHA004
16 May 2014 """

ifile = input("Enter the input filename:\n")
ofile = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

inputfile = open(ifile, "r") #input file in read mode
inf = inputfile.readlines() #strings of each line of input file

for line in range(len(inf)):
    if len(inf[line]) >= 2:
        inf[line] = inf[line][:-1] + " " #remove "new line" from end of line
    else:
        inf[line] += "\n" #paragraph separation case
        
infjoined = "".join(inf) #join strings of input file

lessthanwidth = False
outputfile = open(ofile, "w") #output file in write mode
outputlines = [] #array for newly formatted lines


while lessthanwidth == False: #loop runs while length of joined string is longer than given width
    
    if "\n\n" in infjoined[0:width]: #in the case of paragraph separation
        newline = infjoined[0:(infjoined.index("\n\n"))] + "\n"
        infjoined = infjoined[(infjoined.index("\n\n")+2):]
        
    elif len(infjoined) <= width: #for last line of output (when length of line is shorter than given width)
        lessthanwidth = True
        newline = infjoined
        
    else: #check end of line for incomplete words
        character = infjoined[width]
        tempwidth = width
        while character != " ": #loop only broken when space occurs
            tempwidth -= 1
            character = infjoined[tempwidth]
        newline = infjoined[0:tempwidth] #next output line
        infjoined = infjoined[(tempwidth+1):] #shorten line that is not yet in list of ouput lines
        
    outputlines.append(newline) #add new line to list of new output lines
    
inputfile.close()

for i in outputlines:
    print(i, file = outputfile) #write each new line to output file

outputfile.close()