"""Assignment 9
Question 2
Barry Su
15 May 2014
Program to reformat a text file so that all lines are at most a given length"""

#get name of file 
infile = input("Enter the input filename:\n")
outf = input("Enter the output filename:\n")

#open file in reading mode and get entire file into a list of strings, then close
inf = open(infile, "r")
outf = open(outf, "w")

width = int(input("Enter the line width:\n"))

#create a list for the lines in the infile
wordlst=[]
for i in inf:
    wordlst.append(i)
    
#create list to change "\n" into "\n\n"
wordlst2=[]
for i in wordlst:
    if i =="\n":
        i = "\n\n"
    wordlst2.append(i)   

#create another list and remove the"\n"    
wordlst3=[]
for i in wordlst2:
    newline= i.rstrip("\n")
    wordlst3.append(newline) 

#put it all into one long string          
text=""    
for i in wordlst3:
    if text=="":
        text = i
    else:
        text=text+" "+i      
wordlst4 = text.split(" ")

count = 0
lst=[]
for t in wordlst4:
    if t =="\n":
        t = "\n\n"
        list1=t
        lst.append(list1)
        count = 0
    else:
        count=count + len(t)
        if count<=width:
            list1=t+" "
            lst.append(list1)
            count = count+1
        else:
            list1="\n"+t+" "
            count=len(t) + 1
            lst.append(list1)
  
        
outf.writelines(lst)        
inf.close()
outf.close()