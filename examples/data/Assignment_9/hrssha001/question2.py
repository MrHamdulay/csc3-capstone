infile= input("Enter the input filename:\n")
outfile= input("Enter the output filename:\n")
width = eval(input("Enter the line width:\n"))

#Shane Horsley
#Program to write to a file from a previous file with a certain line width
#13 May 2014
file1= open(infile, "r") #open file
readfile = file1.read() #read the whole file in to a single string
file1.close() #NB
list1=[] #eventually list of each word in a file
line="" #to check whether new line must be put in
temp = readfile.split(' ') #remove "" character if there are 2 spaces after a sentence.
for i in range(len(temp)-1):
       if temp[i]=='':
              temp[i+1]=' '+temp[i+1]
              del temp[i]
#print(temp) #tracing
for i in temp:
       if "\n" in i:
              y=i.split("\n")
              for j in y:
                     list1.append(j)
                     #print(y)
       else:
              list1.append(i)
              line+=i+" "
#print(list1) #tracing
a=[] #new list to include "" if there should be a new paragraph
b='' #empty string
flag = False #i added a flag
for i in list1:
       if i=='': #this is what was in the list when there was a new paragraph
              a.append(i)
              flag = True #forces program starts new line
              b+=i+' ' 

       elif (len(b)+len(i))-1<width and not flag: #skips this end of paragraph. (because line isn't wide enough, but still a new line has to start)
              a.append(i)
              b+=i+' '
       else:
              a.append(" ")
              a.append(i)
              b=i+" "
              flag = False #continue as per usual
string=""
for i in a:
       if i==" ":
              string+="\n" #new line
       elif i=='':
              string+='\n' #new paragraph
       else:
              string+=i + " "

file2 = open(outfile, "w")
#print(string) #tracing
print(string, file=file2) #write the string with adjusted line width to file2
file2.close() #NB