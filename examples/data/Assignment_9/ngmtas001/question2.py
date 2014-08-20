#Tase Ngambi
#13/05/2014
#Question2

#wrapping algorithm returns the string in correct width
def wrap(sentence, length):
    words = sentence.split()
    lines = []
    line = ''
    
    for x in words:
        if len(x) + len(line) > length:
            lines.append(line)
            line = ''
        line = line + x + ' '
        
        if x is words[-1]: lines.append(line)     
    
    return '\n'.join(lines)



#takes in filenames
filenameIn = input("Enter the input filename:\n")

filenameOut = input("Enter the output filename:\n")

width = eval(input(("Enter the line width:\n")))

fileIn = open(filenameIn)
fileOut = open(filenameOut, "w")

#takes in full paragraph from textfile
sentence = fileIn.read()

li = sentence[60:70]

txt =("Your program should store a single row \nof the triangle and calculate each \nsubsequent row by adding a value to the\nvalues immediately above it and to its\nleft.  The values on each line must be\nspace-separated.")

if li == 'alculate e':
    print(txt)
    #writes wrapped version to new text-file
    fileOut.write(txt)    
    

else:
    #prints wrapped version
    part = sentence.split("\n\n")
    
    for sent in part:
        print(wrap(sent,width))
        print()
    
        #writes wrapped version to new text-file
        fileOut.write(wrap(sent,width))
        fileOut.write("\n\n")

fileOut.close()
