"""Format Lines
B.Player
11/05/2014"""
import textwrap

#Variables
inName=input("Enter the input filename:\n")
outName=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

paras=[]
i=0
inFile=open(inName,'r')
data=inFile.read()
inFile.close()
paras=data.split("\n\n")

outFile=open(outName,'w')
for para in paras:
   text=textwrap.wrap(para,width)
   for line in text:
      print(line,file=outFile)
   print("",file=outFile)
outFile.close()
