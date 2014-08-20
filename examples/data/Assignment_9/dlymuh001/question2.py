"""program to reformat a text file so that all lines are at most a given length. Do not break up words. Write the formatted text to a new text file.
Muhammad Nabeel Dulymamode
11/05/2014"""

infilename = input("Enter the input filename:\n")
outfilename = input("Enter the output filename:\n")
width = int(input("Enter the line width:\n"))

infile = open(infilename,"r")
lines = infile.readlines()
s = " "
paras = s.join(lines)
infile.close()
outfile = open(outfilename,"w")
outline = ""

n = len(paras)
start = 0
end = 0    
while end <= n:
    if end >= n:
        print(outline, file = outfile)
        break
    elif end - start < width:
        if paras[end] != "\n":
            outline += paras[end]
        else:
            if end < n-1:
                if paras[end+1] == "\n":
                    outline += "\n"
                    end += 1
        end += 1
    else:
        while paras[end] != " ":
            end -= 1
            outline = outline[0:end-start+1]
        print(outline, file = outfile)
        outline = ""
        end += 1
        start = end
outfile.close()