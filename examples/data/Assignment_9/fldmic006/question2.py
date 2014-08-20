#code to extract lines from a specific file and write them in a new format to a new file
#michael field
#11 may 2014

infile = input("Enter the input filename:\n")
#infile = "input.txt"
lines = []
words = []

f = open (infile, "r")
#extract lines from the input file
for line in f:
        lines.append(line)
f.close()
        
#make the input into a single string
string = ""
for line in lines:
        string += line
    
#get the file to write to
outfile = input("Enter the output filename:\n")
#outfile = "output.txt"
width = input("Enter the line width:\n")
#width = 40
fl = open (outfile, "w")


#print the output
def printout(count, orcnt):
        count += eval(width)  #next set of specific characters
        
        if count<=len(string):
                #if in the middle of the word move the printing cursor back til it reaches the beginning of the word
                while string[count] != " ":
                        count -= 1
                else:
                        print(string[orcnt:count], file = fl)
                        orcnt = count + 1
                        printout(count, orcnt)
        else:
                print(string[orcnt:], file = fl)
                fl.close()




if __name__ == "__main__":
        count = 0
        orcount = 0
        printout(count, orcount)