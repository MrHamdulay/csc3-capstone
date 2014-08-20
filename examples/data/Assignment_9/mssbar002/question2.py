"""a program to reformat a text file so that all lines are at most a given length
Barnett Msiska
13 May 2014"""

def main():
    #request user input
    inputFile = input("Enter the input filename:\n")
    outputFile = input("Enter the output filename:\n")
    width = eval(input("Enter the line width:\n"))
    #open inputfile for reading
    f = open(inputFile, "r")
    lines = f.readlines()
    #truncate lines to given length and append to cumulative array
    formatted = []
    carriedString = ""
    for i in range(len(lines)):
        currentString = carriedString + lines[i]
        if i > 0 and lines[i] == "\n":
            formatted.append("\n")
            continue
        while currentString != "\n":               
            if len(currentString) >= width:
                if currentString[width-1] != " " or currentString[width-1] != "\n" :
                    count = 0
                    for j in range(width,0,-1):
                        if currentString[j] != " ":
                            count += 1
                        else:
                            break
                    
                formatted.append(currentString[:width-count])
                currentString = currentString[width-count+1:]
                
            else:
                carriedString = currentString[:-1] + " "
                if i == len(lines)-1:
                    formatted.append(carriedString)
                currentString = "\n"
    #write output to file
    f = open(outputFile, "w")
    for k in formatted:
        print(k, file=f)
        
    
main()