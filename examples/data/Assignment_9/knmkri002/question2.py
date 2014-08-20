""" program to format a text file so that all lines are a most a given length
Kristin Kinmont
9 may 2014"""

# get input file
input_name = input("Enter the input filename:\n")
# get output file name
output_name = input("Enter the output filename:\n")
# get line width
width = eval(input("Enter the line width:\n"))

# open input file and convert contents to a string
F = open(input_name, "r")
FILE = F.readlines()
F.close()

# remove "\n" from the end of each line and convert line to a series of strings
for i in range(len(FILE)):
    FILE[i] = FILE[i][:-1]
    FILE[i] = FILE[i].split(" ")

# adjust line widths and save to output file   
count = 0 # keeps track of the length of each line   
k = open(output_name, "w")
for line in FILE:
    if line == [""]: # indicates theres a new paragraph
        print("\n", file = k)
        count = 0
        continue
    for i in range(len(line)):
        if width - len(line[i]) - count >= 0: # test to see if by adding a new word the length of the line will still be <= width
            print( line[i], end = " " , file = k)
            count += (len(line[i]) +1)            
        else:
            print( "\n" + line[i], end = " " , file = k)
            count = (len(line[i]) +1)         
  
k.close()




    
    
