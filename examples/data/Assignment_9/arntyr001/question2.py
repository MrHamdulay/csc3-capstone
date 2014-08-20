#Program to split a line into another after x characters
#Tyrone Arnold
# 13 April 2014

import textwrap
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))


f = open( input_file , 'r')

to_edit = f.readlines()



with open( input_file , 'r') as f:
        to_edit = [line.strip("\n") for line in f]

f.close()


edit_string = str(to_edit).strip("[]")
edit_string = edit_string.strip("''")
edit_string = edit_string.replace("', '" , "")



final = textwrap.wrap(edit_string , width = line_width)

output = open(output_file , "w")

with open(output_file , "w") as output:
        for item in final:
                output.write("%s\n" % item)
output.close()
                        
