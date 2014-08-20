infile = input ("Enter the input filename:\n")
outfile = input ("Enter the output filename:\n")
maxwidth = eval (input ("Enter the line width:\n"))
#filename = "para2.txt"
#maxwidth = 40

f = open (infile, "r")
data = f.readlines ()
f.close ()

for l in range (len (data)):
   data[l] = data[l][:-1]
   
position = 0
while position < len(data)-1:
   if data[position] != "" and data[position+1] != "":
      while len (data[position])>0 and data[position][:-1] == " ":
         data[position] = data[position][:-1]
      while len (data[position+1])>0 and data[position+1][0] == " ":
         data[position+1] = data[position+1][1:]
      data[position] = data[position] + " " + data[position+1]
      del data[position+1]
   else:
      position = position + 1

g = open (outfile, "w")

for l in data:
   words = l.split (" ")
   linelength = 0
   for w in words:
      if linelength == 0:
         linelength += len (w)
         print (w,end="",file=g)
      elif linelength + 1 + len (w) <= maxwidth:
         linelength += 1 + len (w)
         print (" " + w,end="",file=g)
      else:
         print (file=g)
         linelength = len (w)
         print (w,end="",file=g)
   print (file=g)
g.close()