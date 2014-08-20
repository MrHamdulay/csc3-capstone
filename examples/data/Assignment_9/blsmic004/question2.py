# program to reformat a text file so that all lines are at most a given length
# Michele Balestra  BLSMIC004
# 16 ay 2014

source = input("Enter the input filename:\n")
dest = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

inf = open(source,"r")
lines = inf.read().split()
inf.close()

# uses a variable as an incrementer and when variable exceeds width, prints on new line
incr = 0
outf = open(dest,"w")
for i in range(len(lines)):
    if incr + len(lines[i]) > width:
        print('\n' + lines[i], file=outf, end=' ')
        incr = 0 
    else:
        print(lines[i], file=outf, end=' ')
    incr = incr + 1 + len(lines[i])
outf.close()