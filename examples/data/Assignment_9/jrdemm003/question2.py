"""ASSIGNMENT 9, QUESTION 2- print out a text in given width rows
EMMA JORDI
10 MAY 2014"""




 
 

infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
file = ""
for line in open(infile, "r"):
    file = file+" "+line
print(file)
lines = []
lines = file.split()
        
    
    
#get the whole file
#split the words of the file
#while characters <width, add the word to the line

g = open (outfile, "w")    
total = 0
width = eval(input("Enter the line width:\n"))

for word in lines:
    total = total + len(word) + 1
    
    if total <= width:
        print(word," ", sep="", end="", file=g)
         
    else:#else start a new line
        print("\n", word+" ", sep="", end="", file=g) 
        total=len(word)
g.close()
