'''Program to reformat a text file to a reduced line width   
Simangaliso Mlangeni
16 May 2014
assignment9, question2'''

#Prompt user to enter the file name
f = open(input("Enter the input filename:\n"),"r")
#save lines in file as a list
lines = f.readlines()
f.close()#close off the file


NewFile = input("Enter the output filename:\n")  
LineWidth = eval(input("Enter the line width:\n"))
#create counter variable to make lines dont exceed width
lenWords = 0
#Create variable to append words to
NewT = ""

#iterate through list containing strings
for line in lines:
    if line == "\n":
        NewT += "\n\n"
        lenWords = 0
    else:#go over each character in the line
        words = line[:-1].split(" ")#split words
        for word in words:
            lenWords += len(word)
            if lenWords > LineWidth:
                NewT += "\n" + word + " "
                lenWords = len(word) + 1
            elif lenWords == LineWidth:
                NewT += word + "\n"
                lenWords = 0
            else:
                NewT += word + " "
                lenWords += 1
    

#write out the output file an the new file with reduced line width            
New = open(NewFile,"w")  
New.write(NewT)
New.close()