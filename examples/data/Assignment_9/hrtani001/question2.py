#Aniq Hartle
#12/05/2014
#print output file from input file with a user selected width

inFile = input("Enter the input filename:\n")          #file name input from user

f = open (inFile, "r")                                 #open file, create array from lines, close file
lines = f.read()
f.close ()

outFile = input("Enter the output filename:\n")        #store name of output file
width = eval(input("Enter the line width:\n"))         #store width as entered by user

lines = lines.replace("  "," @ ")                      #add flags for surprise double spaces and new lines
lines = lines.replace("\n"," ")

f = open(outFile,"w")                                  #open file

words = lines.split(" ")                               #split file into array of words

for word in words:                                     #based on flags, edit the array
    if "@" in word:
        wrdInd = words.index("@")
        words[wrdInd]="  "
        
characters = 0
for i in range(0,len(words)):                          #go through array adding length of word to characters until it reaches the width then move to new line
    if words[i]=="  ":
        print(" ",end="",file=f)
    elif words[i]=="":
        print("\n",file=f)
        characters = 0
    else:
        if characters+len(words[i])<=width:
            print(words[i]," ",sep="",end="",file=f)
            characters+=len(words[i])+1
        else:
            print("\n",words[i]," ",sep="",end="",file=f)
            characters = len(words[i])+1
f.close()                                              #close file