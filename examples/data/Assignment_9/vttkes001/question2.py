"""Format textfile to number of words set by user
Keshin Vittee
14 May 2014"""

iname = input("Enter the input filename:\n")
oname = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open(iname, "r")
line = f.read() 
f.close()

lines = [] 
line = line.replace("\n\n","n3l!n3")
line = line.replace("\n"," ")       #Removes all the newlines except when a new paragraph is needed.
line = line.replace("n3l!n3","\n\n")

count = 0
s = ""
while line != "" or s != "":
    lines.append(s)
    s = ""
    while True:
        if line == "":
            break
        elif line.find(" ") != -1:
            s = line[0:(line.find(" ")+1)] #s is the next word that must be added to the lines
            line = line[line.find(" ")+1:]
        else:
            s = line
            line = ""

        stop = len(s)
        if s[-1] == " ":
            stop -= 1

        if "\n\n" in s:       #Make a blank item in the list to serve as a empty line before a new manual paragraph
            first = s[0:s.find("\n\n")]
            lines[count] = lines[count] + first
            count +=2
            lines.append("")
            last = s[s.find("\n\n")+2:]
            lines.append(last)

        elif (len(lines[count]) + stop) <= width: #Add the s to the current line if it won't be too long afterwards
            lines[count] = lines[count] + s
            s = ""
        else:
             break
    count += 1

f = open(oname,"w")
for a in lines:
    print(a, file=f) #Print the lines array to the new textfile
    print(a)
f.close()