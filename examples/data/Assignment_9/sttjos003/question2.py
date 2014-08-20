#Programme to make a paragraph
#Joe Sutton
#11 May 2014

inputfilename=input("Enter the input filename:\n")
outputfilename=input("Enter the output filename:\n")
linewidth=eval(input("Enter the line width:\n"))

f = open(inputfilename, "r")
totalfile=f.readlines()
f.close()
totalfiles=""
for line in totalfile:
    if line[:-1]=="":
        totalfiles+=line
    else:
        totalfiles+=line[:-1]+" "

totalfiles=totalfiles.split("\n")
f = open(outputfilename, "w")

for paragraph in totalfiles:
    
    listofwords=paragraph.split(" ")
    counter=0
    newline=""
    for word in listofwords:
        if counter+len(word)<linewidth:
            newline+=(word+" ")
            counter+=len(word)+1
        elif counter+len(word)==linewidth:
            print(newline+word, file=f)
            newline=""
            counter=0
        else:
            print(newline[:-1], file=f)
            newline=word+" "
            counter=len(word)+1

    if newline:
        print(newline[:-1], file=f)
    print("", file=f)

f.close()
        