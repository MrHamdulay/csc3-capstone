"""Question 2 of Assignment 9: Reformats a text file to a specified line length without splitting words
SWNREI001
2014/05/11"""

def outformatsingle(line, width):
    """Splits newlineless line into width number of character or less segments"""
    out = ""
    remainder = len(line)
    while remainder > width:
        remainder -= width
        part = line[:width]
        if line[width] != " ":
            while part[-1] != " ":
                part = part[:-1]
        remainder += (width - len(part))
        out += part.lstrip() + "\n"
        line = line[len(line) - remainder:]
    out += line # add remainder
    return out

def outformat(line, width):
    """Formats string line to lines of specified width"""
    lines = line.split("\n")
    ans = ""
    for i in lines:
        ans += outformatsingle(i, width) + "\n\n"
    return ans

def singleString(lines):
    """Turns a list of strings into a single string"""
    ans = ""
    for i in lines:
        if i == '' or i == '\n':
            ans += '\n'
        elif i.endswith("\n"):
            ans += i[:-1] + " " # remove trailing newline
        else:
            ans += i + " "
    return ans

def main():
    """Main function of program"""
    infilename = input("Enter the input filename:\n")
    outfilename = input("Enter the output filename:\n")
    linewidth = eval(input("Enter the line width:\n"))
    # read lines from input file into a list variable
    infile = open(infilename, "r")
    lines = infile.readlines()
    infile.close()
    # convert into single string
    lineString = singleString(lines)
    # split at maximum of 'linewidth' characters without breaking up words
    newlines = outformat(lineString, linewidth)
    # write to output file
    out = open(outfilename, "w")
    print(newlines, file=out)

if __name__ == "__main__":
    main()