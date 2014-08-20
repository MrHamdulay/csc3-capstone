'''A program to reformat a text file so that all lines are at most a given length. Do not break up words. Write the formatted text to a new text file
Jacob Ntesang
15 May 2014'''

'''marks = input("Enter the sentence:\n")
f = open("input.txt","w")
while marks != "":
    f.write(marks + "\n")
    marks = input()
f.close()'''
file = input("Enter the input filename:\n")
output = input("Enter the output filename:\n")
size = eval(input("Enter the width:\n"))
f = open(file,"r")
line = f.readlines()
f.close()
#write in to the file
S = open(output,"w")
File = " "
for i in line:
    i = i# get rid of new lines characters
    File += i
File = File.split()#make an array by spliting ,to get a position of each word not lettter

F = ""#empty string to add editted lines at a specified width to it
for i in File:
    if len(F) + len(i) > size:# if the size of the empty string of a fixed width is full while trying to add another word,now write to a fle
        print(F, file = S)
        if i[-1] == ".":
            F = i + "  "# if there is a full stop,add two empty space,to cover the permanent space
        else:
            F = i + " "
    else:
        F += i + " "
print(F, file = S)
S.close()
S = open(output,"r")
for line in S:
    print(line, end = "")#Print out the file to the screen
S.close()
    
    

      
