# Question 2
# Richard van Gysen
# 14 April 2014
# import textwrap
import textwrap
# get commands
to = input("Enter the input filename:\n")
where = input("Enter the output filename:\n")
width1 = eval(input("Enter the line width:\n"))
# open and read input file
f = open(to, 'r')
edit = f.readlines()
# rid the input file of \n
with open(to, 'r') as f:
        edit = [line.strip("\n") for line in f]
f.close()
# edit the string to rid of commas, spaces and brackets
string = str(edit).strip("[]")
string = string.strip("''")
string = string.replace("', '" , "")
# make to required width
last = textwrap.wrap(string , width = width1)
# output
output = open(where, "w")
with open(where , "w") as output:
        for item in last:
                output.write("%s\n" % item)
output.close()
                        
