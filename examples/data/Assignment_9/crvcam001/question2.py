# question2.py
# program to reformat a text file so that all lines are at most a given length without breaking up words
# camilla craven
# 13 may 2014


# prompting user for file names and preferred line width
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))


# open file and read lines
f = open(input_file, "r")
lines = f.read()
f.close()


List = lines.split(" ") # split words in list
row = 0 # setting row's character count to 0
paragraph = ""

# add each word's length to word count
for word in List:
    row += len(word)
    # if count is smaller than max row width, add word and space to that line
    if row < width:
        paragraph = paragraph + word + " "
        row += 1 # taking spaces into account
    # if count is bigger than max row width, add word and space to new line and set count to 0 again
    else:
        paragraph = paragraph + "\n"
        row = 0
        paragraph = paragraph + word + " "
        row = len(word) + 1
    
    
# write to output file
f = open(output_file, "w")
print(paragraph, file = f)
f.close ()