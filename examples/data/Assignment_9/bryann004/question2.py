"""reformat text file to have lines of a given length
anna borysova
2014-05-12"""


infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = int(input("Enter the line width:\n"))

new_lines = []
infile = open(infile)
original = infile.read()
infile.close()

# split into paragraphs
original = original.split("\n\n")
for i in range(len(original)):
    # fuse lines
    original[i] = original[i].replace("\n", " ")
        

def reformat(string, width):
    """puts line breaks every certain number of characters"""
    
    if len(string) <= width:
        return string
    # if character after supposed break is space, cut 
    if string[width] == " ":
        return string[:width] + "\n" + reformat(string[width + 1:], width)
    i = -1  
    cut = string[width-1:0:-1]
    
    # cut at next word break
    for ch in cut:
        i += 1
        if ch == " ":
            return string[:width - i]+"\n" + reformat(string[width - i:], width)

# print to file
outfile = open(outfile, 'w')
for paragraph in original:
    print(reformat(paragraph, width) + "\n", file=outfile)
outfile.close()