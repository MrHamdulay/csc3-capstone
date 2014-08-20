#Tendani Netshitenzhe
#question1
#16May2014

#Ask the user for the input and output filenames and the line width
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#Read from the input filename given
f = open(input_file, "r")
lines = f.read()

#Close the input file
f.close()

#Create the output file from the given name
output= open(output_file, "w")

#Close the output file
output.close()

#Open the output file for appending
output_t = open(output_file, "a")

#Get the length of the lines
length = len(lines)

#Get rid of newline characters that dont form the paragraphs
find = lines.find(".\n")
if find  == -1:
    lines = lines.replace("\n", " ")
else:
    a = lines[:find+1].replace("\n", " ")
    find2 = lines[find+3:].find(".\n")
    y = find+3+find2+1
    b = lines[find+3:y+1].replace("\n", " ")
    find3 =lines[y+1:].find(".\n")
    x = y+2+find3+1
    c = lines[y+1:x].replace("\n", " ")
    find4 = lines[x+1:].find(".\n")
    r = x+2+find4+1
    d = lines[x+1:r].replace("\n", " ")
    e = lines[r+1:].replace("\n", " ")
    f = (b+c).replace("\n", " ")
    lines = a + "\n\n" + f +"\n\n" + d +"\n\n" +e
    
#Get the number of times for the loop
position = length//width

#Initialize the starting index value
start = 0

#Check if length of the lines is less than/or bigger than the width
if length <= width:
    output_t.write(lines)
else: #If the length of the lines is bigger than the assigned width
    for k in range(position):       
        if lines[start] == " ": #Checks if any of the starting indices are " "
            start +=1
        interval = start+width  #Creates an interval for the lines to wrap          
        if lines[interval-1] == " ": #Checks to see if the last interval is a character 
            output_t.write(lines[start:interval-1]+"\n")
            start = interval
        else: #If the last interval is a character
            index = lines.rfind(" ", start, interval-1)
            if lines[index-1]==" ":
                output_t.write(lines[start:index-1]+"\n")
            else:
                output_t.write(lines[start:index]+"\n")
            start = index
            
    if lines[start] == " ":
        start+=1
    interval = start+width
    output_t.write(lines[start:interval]+"\n")
    output_t.write(lines[interval:]+"\n")#Writes the last line 

#Closes the appended file
output_t.close()