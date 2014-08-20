"""Program to reformat a text file
Jaren Hendricks
15 May 2014"""
        
#Gets file names and width
file_name = input('Enter the input filename:\n')
outfileName = input('Enter the output filename\n')
width = eval(input("Enter the line width\n"))

# open the files
inFile = open(file_name,'r')
outFile = open(outfileName, 'w')
string = inFile.read()
char_count = 0
line = []

""" Gets length of word & characters and saves each word to a list
which is less than the inputed width"""

for word in string.split(): # saves each word to a list
    if char_count + len(word) + 1 <= width: # 
        line.append(word)
        char_count+= len(word)+1
    else:
        print (" ".join(line), file = outFile) # prints a space between each word in the list/ saves to output files
        line = [word] # saves words to an array
        char_count = len(word)

# saves the last line to the output file 
for i in line:
    print(i, file = outFile, end=' ')

#closes files
inFile.close()
outFile.close()

# ouputs the file
out = open(outfileName,'r')
data = out.read()
print(data)

# closes file
out.close()
