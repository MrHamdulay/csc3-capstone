import textwrap
#Get I/P
f_input= input("Enter the input filename:\n")
f_output= input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
#Open file
f = open(f_input, "r")
f1 = open(f_output, "w")
#Read file
read = f.read()
value = """Your program should store a single row of the triangle and calculate each subsequent row by adding a value to the values 
immediately above it and to its left.  The values on each line must be space-separated."""

# Wrap this text.
list = textwrap.wrap(read, width)

# Print each line.
for element in list:
    print(element, file = f1 )
f.close()
f1.close()