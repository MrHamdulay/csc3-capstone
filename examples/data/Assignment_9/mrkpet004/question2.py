""" program to reformat a text file so that all lines are at most a given length without breaking up words
peter m muriuki
26/5/14"""

#open and load the data from the file
Infilename=input("Enter the marks filename:\n") ##"input.txt"
file=open (Infilename, "r")
lines=file.readlines ()
file.close()
l=[] # initialise list to be used later
m="" #initialise empty string to be used later

# get output file name and line width
Outfilename=input("Enter the output filename:\n") ##"output.txt"
w=eval(input("Enter the line width:\n"))

# create and open outputfile and get lines from input file
f=open (Outfilename,"w")
count=0
for char in range(len(lines)):
   l+=lines[char].split(" ") # add lines into initialised list
   count+=(len(lines[char]))
##print(l)   
##print(count)
# check over items in list and format them if they occur at end of line in inputfile
for i in range(len(l)):
   #if l[i]!="\n":
   if "\n" in l[i]:
      l[i]=l[i].replace("\n","")     
   else:
      continue

##print(l)
# iterate over the words and print out formatted lines according to specified w into outputfile
width=0
for i in range(len(l)):
   width+=len(l[i])
  # if it's a new paragraph in inputfile,print a new paragraph in output file and subsequent words
   if l[i]=="\n":
      width=0
      l[i].replace("\n","")
      m+="\n"+l[i]+" "
      width+=len(l[i])+1      
   if l[i]==" ": # extra space between words in input file is removed
      l[i].replace(" ","")
  ## l[i]=l[i]+" "
   if width <= w: 
      width+=1
      m+=(l[i]+" ")
   # when the length of line in reaches the maximum,subsequent words are printed to a new line
   elif width > w:
      width=0
      m+="\n"+l[i]+" "
      width+=len(l[i])+1
print(m,file=f)
f.close ()