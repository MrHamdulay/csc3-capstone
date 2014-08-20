""" program to reformat a text file so that all lines are at most a given length
Dean Gracey
11 May 2014"""



inputfile = input("Enter the input filename:\n")
f = open(inputfile,"r")
filelist = f.readlines()
f.close()

outputfile = input("Enter the output filename:\n")
linewidth = eval(input("Enter the line width:\n"))

doublespace = False
file2line = ""
for line in filelist:
    file2line = file2line + line
    
if ("  " in file2line):
    doublespace=True


#put whole file in one line
file1line = ""
for line in filelist:
    file1line = file1line + " " + line[:-1]

file1line = file1line[1:] + line[-1]  #takes away the space in the begining and puts the last character back



words = file1line.split(" ")


#format the message
spaceleft = linewidth
message = ""



for word in words:
    if message == "":
        message = word
        spaceleft = spaceleft-len(word)
    else:    
        
        if (word=="") and doublespace==False:
            message = message + "\n\n"
            spaceleft = linewidth - len(word)
            continue
        elif (word=="") and doublespace==True:
            message = message + " "
            spaceleft = linewidth - len(word) -1       
        elif(message[len(message)-2:len(message)]=="\n\n"):
            message = message + word
            spaceleft = spaceleft - len(word)

        elif(spaceleft>len(word)):
            message = message + " " + word
            spaceleft = spaceleft - len(word) -1
            
        elif(spaceleft<=len(word)):
            message = message + "\n" + word   
            spaceleft=linewidth - len(word)
          
f = open(outputfile,"w")
print(message,file=f)     
f.close()    
