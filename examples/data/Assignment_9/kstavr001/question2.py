#Assignmnet 9,Question 2
#Avreyna Kistensamy
#11 May 2014

import textwrap
old_file = input("Enter the input filename:\n")
new_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

f = open (old_file,"r")
sentences = f.readlines()
f.close

#Removing newline after each sentence
for i in range(len(sentences)-1):
    if sentences[i] != '\n': #Keep paragraphs seperate
        sentences[i] = sentences[i][:-1]
print(sentences)
#Creating list of paragraphs
paragraph = ""                     
chapter = []
for i in range(len(sentences)):                
    if sentences[i] != '\n':
        paragraph += sentences[i] + " "
    elif sentences[i] == '\n':
        paragraph += sentences[i] +" "
        chapter.append(paragraph)
        paragraph = ""
    if i == (len(sentences)-1):
        chapter.append(paragraph)


#Creating new formated file
output = open(new_file, "w")
for i in range(len(chapter)):
        x = textwrap.wrap(chapter[i],width) 
        for j in x:
            print(j,file=output)
        print(file=output)
output.close()
        



