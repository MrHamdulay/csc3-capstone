
__author__ = 'George de Kock'
""" Program to reformat a text file so that all lines are at most a given length.
2014-05-12"""


inputfilename = input("Enter the input filename:\n")
outputfilename = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(inputfilename, "r")
data = f.read() #Read the whole file into one line
f.close()

lines = [] #Create a empty list to store the new textfile's lines
data = data.replace("\n\n","n3l!n3")
data = data.replace("\n"," ")       #Removes all the newlines except when a new paragraph is needed.
data = data.replace("n3l!n3","\n\n")

count = 0
nextstr = ""
while data != "" or nextstr != "":
    lines.append(nextstr)
    nextstr = ""
    while True:
        if data == "":
            break
        elif data.find(" ") != -1:
            nextstr = data[0:(data.find(" ")+1)] #nextstr is the next word that must be added to the lines
            data = data[data.find(" ")+1:]
        else:
            nextstr = data
            data = ""

        stop = len(nextstr)
        if nextstr[-1] == " ":
            stop -= 1

        if "\n\n" in nextstr:       #Make a blank item in the list to serve as a empty line before a new manual paragraph
            first = nextstr[0:nextstr.find("\n\n")]
            lines[count] = lines[count] + first
            count +=2
            lines.append("")
            last = nextstr[nextstr.find("\n\n")+2:]
            lines.append(last)

        elif (len(lines[count]) + stop) <= width: #Add the nextstr to the current line if it won't be too long afterwards
            lines[count] = lines[count] + nextstr
            nextstr = ""
        else:
             break
    count += 1

f = open(outputfilename,"w")
for a in lines:
    print(a, file=f) #Print the lines array to the new textfile
    print(a)
f.close()