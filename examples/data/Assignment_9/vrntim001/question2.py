''' format files to length
Tim Mostert
13.05.14'''

infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
width = input("Enter the line width:\n")

outputlist = []
f = open(infile,"r")
text = f.read()
f.close

paragraphs = text.split("\n\n")
workable_paragraphs = []
final_paragraphs = []


for sentences in paragraphs:
    sentences = sentences.replace("\n"," ")
    workable_paragraphs.append(sentences)
for string in workable_paragraphs:
    newlines = []
    newline = ''    
    count = 0
    eachword = string.split(" ")
    for i in eachword:
        count += 1
        if len(newline+(i+" ")) <= eval(width)+1:
            newline += (i+" ")
            if count == len(eachword):
                newlines.append(newline[:-1])
        else:
            newlines.append(newline[:-1])
            newline = ""
            newline += (i+" ")
            if count == len(eachword):
                newlines.append(newline)
    final_paragraphs.append(newlines)     

f = open(outfile, "w")
for i in final_paragraphs:
    for line in i:
        print(line, file = f)
    print(file = f)    
f.close()        