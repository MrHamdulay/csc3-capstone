#MSRGRA002
#Grant Meeser	
#15/05/2014

inputFile=input('Enter the input filename:\n')
outputFile=input('Enter the output filename:\n')
words = []
rowLength = 0
output=''
length=int(input('Enter the line width:\n'))

f = open(inputFile,"r")
lines = f.readlines()
f.close()

for line in lines:
	if line!='\n':
		line=line.replace('\n','')
	else: line+='\n'
	words+= line.split(" ")

output=words[0]
rowLength=len(words[0])

i=1
while i <(len(words)):
	if words[i]=='\n\n': 
		rowLength=0
		output+=words[i]
		i+=1
		if i==len(words):break
		rowLength=len(words[i])
		output+=words[i]
		i+=1
	if i==len(words):break

	if (rowLength+len(words[i]+' '))<=length:
		output+=' '+words[i]
		rowLength+=len(words[i]+' ')
	else:
		output+='\n'+words[i]
		rowLength=len(words[i])
	i+=1
f = open(outputFile,"w")
print(output, file=f)
