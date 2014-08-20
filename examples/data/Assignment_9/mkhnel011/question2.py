"""a program that formats a given text file so that only the desired number of words appear per line
nelisile mkhwebane
13 May 2014"""

"""get the filenames from the user"""
filename = input("Enter the input filename:\n")
output_filename= input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

"""get the lines from the input file"""
f = open (filename, "r")
lines = f.readlines()
f.close()
tracker = 0
"""cutting off the "\n" at the end off each line"""
for i in range(len(lines)):
    lines[i]= lines[i][:-1]
    
"""joining the strings into one paragraph/string and space-seperated"""
text = (" ").join(lines)
text = text.split()
"""wrapping the text"""
words = ""
for i in range(len(text)):
    if tracker < width and tracker + len(text[i]) < width:
        """you add onto what should be printed"""
        words+=text[i]+" "
        tracker+= len(text[i])+1
    elif tracker +len(text[i]) == width:
        """ if the len of the line together with the extra words are longer than required len"""
        words += text[i] + "\n"
        tracker = 0
    elif tracker + len(text[i])>width:
        """when the words exceed the the required length"""
        words += "\n" + text[i]+ " "
        tracker = len(text[i]) +1

"""open the file you want to print in"""
output = open(output_filename, "w")
""" print new lines in the file"""
print(words, file=output)
output.close()
 