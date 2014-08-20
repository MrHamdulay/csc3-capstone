"""Program to reformat text file
Sithasibanzi Kondleka
16 May 2014"""

mainfile = input("Enter the input filename:\n")
newfile = input("Enter the output filename:\n")
linewidth = input("Enter the line width:\n")
width = eval(linewidth) #change into number

f = open(mainfile, "r")
process = f.readlines() #processing the file
f.close()
print(process)
f = open(newfile, "w")
count = 0 #counter of spaces used
line = []
for i in process:
    x = i.replace("\n","") #removing newline character
    x = x.split(" ")
    for j in x:
        line.append(j)
     #separating according to spaces

count = 0
print(line)
for word in line:
    if count+len(word)<= width:
        print(word, end=" ", file=f) #writing to Output file
        count+=len(word)+1 #count spaces already used
    else:
        print('\n' + word, end=" ", file=f) #writing to Output file
        count = len(word)+1

f.close()