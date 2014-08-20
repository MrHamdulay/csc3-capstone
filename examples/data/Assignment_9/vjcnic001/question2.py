import textwrap

input_file = input("Enter the input filename:\n")
f = open(input_file,"r")
output = input("Enter the output filename:\n")
t = open(output,"w")
wid = input("Enter the line width:\n")
count = 0 
lst = []
x = f.read()
w = []
lst = x.split("\n\n")

for a in lst:
	w.append(str.replace(a, "\n", " "))

lst = []
	
for a in w:
	if a != "":
		lst.append(a)
		
for a in lst:
	a
	
d = textwrap.wrap(a,width=wid)
for e in d:
	t.readlines(e)
	
f.close()
t.close()
	