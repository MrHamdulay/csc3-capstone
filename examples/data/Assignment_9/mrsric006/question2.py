filename = input("Enter the input filename:\n")
outputname = input("Enter the output filename:\n")
width = input("Enter the line width:\n")

f = open (filename,"r")
stringa = f.read()
f.close()
count = 0
lista = []
space_locate = 0
start_locate = 0

outfile = open (outputname,"w")
for i in range(len(stringa)-1): #note - len now -2 to avoid index issues with removing the double space
  if stringa[i] == "\n":
    if stringa[i+1] == "\n":
      stringa = stringa[0:i]+stringa[i+1:]
    else:
      stringa = stringa[0:i]+stringa[i+1:]
  if stringa[i] == " ":
    space_locate = i
    if stringa[i+1] == " ":
      stringa = stringa[0:i+1]+stringa[i+2:]
  if (i+1) % eval(width) == 0:
    print(stringa[start_locate: space_locate],file=outfile)
    start_locate = space_locate+1
  if i == len(stringa)-2:
    print(stringa[start_locate:],file=outfile)
outfile.close() 
