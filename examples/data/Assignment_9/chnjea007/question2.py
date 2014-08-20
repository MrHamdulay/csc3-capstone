def edit(text, lw, ntext = ""):
    if len(text) < lw + 1:
        return ntext + text
    for i in range(lw, -1, -1):
        if text[i] == " ":
            ntext += text[:i] + "\n"
            return edit(text[i + 1:], lw, ntext)
    else:
        ntext += text[:lw + 1] + "\n"
        return edit(text[lw+1:], lw, ntext)
fni = input("Enter the input filename:\n")
fno = input("Enter the output filename:\n")
lw = eval(input("Enter the line width:\n"))
fi = open(fni, "r")
fo = open(fno, "w")
otext = ""

index = lw
for line in fi:
    otext += line.rstrip("\n") + " "
print(edit(otext, lw), file = fo)

fi.close()
fo.close()