'''Write a program to reformat a text file so that all lines are at most a given length. 
Do not break up words. Write the formatted text to a new text file.
Sinead Urisohn
14 May 2014
'''
#Get input and output file names and length of desired lines
filenameInput=input("Enter the input filename:\n")
filenameOutput=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

#open input file and read content to string
fIn=open(filenameInput,"r")
s=fIn.read()
#close input file
fIn.close()
#split string of input file at new lines
l=s.split("\n")
#set counter to 0 to keep track of line length
counter=0
#set empty list to append lines of changed width to
write=[]

#loop through length of list
for i in range(len(l)):
    #get each word in list by spliting at space
    word=l[i].split(" ")
    #loop through each word
    for letters in range(len(word)):
        #if word only consists of one item that is an empty space
        if len(word)==1 and word[letters]=='':
            #append new paragraph and set counter to 0
            write.append("\n\n")
            counter=0
        else:
            #else if the length of word and counter is smaller and equal to width
            if (len(word[letters])+counter)<=width:
                #increment counter and add length of word
                counter+=len(word[letters])
                #if adding a space (length 1) to counter is still smaller and equalt to width
                if counter+1<=width:
                    #append word and a space to write list and increment counter by 1 
                    #to account for the space added
                    write.append(word[letters]+" ")
                    counter+=1
                #otherwise just add word with no space
                else:
                    write.append(word[letters])            
            #if there is in empty string(length 0) in word list this means that it is a space
            #so check if adding a space( of length 1) is smaller and equal to width
            elif len(word[letters])==0 and (1+counter)<=width:
                #add space and increment counter by 1
                write.append(" ")
                counter+=1
            else:
                #set counter to 0 and start a new line
                counter=0
                write.append("\n"+word[letters]+" ")
                #add length of word and space to counter
                counter+=len(word[letters])+1
            
#open/create output file and overwrite its content
fOut = open (filenameOutput, "w")
#write content in write list to output file
for item in write:
    print(item,file=fOut,end="")
#close output file
fOut.close()