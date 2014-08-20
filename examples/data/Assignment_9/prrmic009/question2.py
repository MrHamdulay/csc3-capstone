"""program to format text in an input text document to an input line length,
and then re-write the altered text to a new text document of input name
Mick Perring
16 May 2014"""

file = input("Enter the input filename:\n")  # user inputs filename of text document to be changed (input)
new_file = input("Enter the output filename:\n") # user inputs name of output file to be created or overwritten
line_width = eval(input("Enter the line width:\n")) # user inputs line width that they wish text document to be altered to

f = open(file, "r")  # program opens document, records data, and closes document
lines = f.readlines()
f.close()

for i in range(len(lines)-1): # replaces trailing cariage returns with spaces at the end of string lines
    lines[i] = lines[i][:-1]
    lines[i] = lines[i] + " "

single_str = "".join(lines) # joins strings in original list into one long string
single_list = single_str.split(" ") # splits long string into list of individual word strings
single_list.append(" "*100) # adds a string of 100 spaces to end of list (exagerated string deleted later)

new_line = ""
new_list = []

for i in range(len(single_list)-1): # adds single strings from list to form new strings of input lenghth, stopping when
    new_line = new_line + single_list[i] + " "  # following single string with cause new string to exceed length
    if (len(new_line) + len(single_list[i+1])) >= line_width:
        new_list.append(new_line)  # adds new strings of input length to new list
        new_line = ""
        
for i in range(len(new_list)):  # removes trailing space from all strings in new list
    new_list[i] = new_list[i][:-1]
    
fn = open(new_file, "w")  # opens new text document of input name

for i in new_list:  # adds strings in new list to new text document
    print(i, file=fn)
    
fn.close()  # closes new text document