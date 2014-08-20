"""program to reformat a text file so that all lines are at most a given length.
John Odetokun
11 May 2014"""

fname = input("Enter the input filename:\n")
f = open(fname , "r")
inpt = ""
lines = f.readlines()
#print(lines)
for q in lines:
    if q != "\n":
        inpt += q.replace("\n", " ")
    else:
        inpt += q + q
f.close()
words = inpt.split(" ")
arr = ""
nfname = input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))
count = width
for i in words:
    if "\n\n" in i:
        arr += i + " "
        count = width - (len(i)-1)
    elif len(i) <= count:
        wrd = i
        arr += wrd
        count -= len(wrd)
        if count >= 1:
            arr += " "
            count -= 1
    else:
        arr += "\n" + i + " "
        count = width - len(i) -1
        

nfile = (open(nfname, "w"))
print(arr, file = nfile)
nfile.close()