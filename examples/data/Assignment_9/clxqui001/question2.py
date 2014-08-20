"""this program reads a text fits each line suck that the length of the lines is less than equal to
a given input
quincy cele
17 may 2014"""

#chose file and create new file in which the new text with set paragraphs can enter

infile=input("Enter input filename:\n")
outfile=input("Enter output filename:\n")
width=eval(input("Enter the line width:\n"))
text=open(infile,"r")
text1=open(outfile,"w")
paragraph=text.read()
text.close()

#create a list of words seperated by a empty spaced line
lines=paragraph.split("\n\n")

#import textwrap to call a function that would align the paragraph in a specific width 
import textwrap
#create te paragraphs and add them in the newly created file
for words in lines:
    newword=words.replace("\n"," ")
    string=textwrap.wrap(newword,width)
    for i in string:
        print(i,file=text1)
    print(file=text1)
text1.close()