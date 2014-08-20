fileName1 = input("Enter the input filename:\n")
#fileName2 = input("Enter the output filename:\n")
#width = input("Enter the line width:\n")
listLines = []
listWords = []
count = 0

file1 = open(fileName1,"r")
line1 = file1.readlines()
file1.close()
words = []
for lines in line1:
    listLines.append(lines)

for strings in range(len(listLines)):
    x = (listLines[strings])
    words.append (x.split(" "))
    print (words)

for i in range(len(words)):
    for j in range (len(words[i])):
        count += len(words[j])
        print(count)        
        

