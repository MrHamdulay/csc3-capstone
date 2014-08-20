#Author: NLXALE001
#Date: 13 May 2014
#Assignment 9

filein = input("Enter the input filename:\n")
fileout = input("Enter the output filename:\n")
f = open(filein, "r")
doc = ""
#put document into one string deleting \n as you go
for line in f:
    doc += line[:-1]
    doc += " "
f.close()

enter = eval(input("Enter the line width:\n"))

#put all woprds into one list
words = doc.split(" ")
count = 0
line = ""
f = open(fileout, "w")

#write lines to output file
for word in words:
    if count >= enter:#at end of line
        print (line, file=f) 
        line = word
        count = len(word)
    elif count < enter:#add word to line
        if (enter-count)>len(word):#space to add a whole word
            if count == 0:#beginning of new sentence
                count = len(word)
                line = word 
            else:
                count += len(word) +1 #+1 for the space
                line += " "
                line += word
        else:#not enough space to add new word
            print (line, file=f)
            line = word
            count = len(word)
print (line, file=f)
f.close()
            
    

