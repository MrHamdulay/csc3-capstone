#Assignment 9
#Question 2

input_file = input("Enter the input filname:\n")
infile = open(input_file,"r")
output_file = input("Enter the output filename:\n")
outfile = open(output_file,"w")
width = int(input("Enter the line width:\n"))

#Create list of each line ending in \n
list_words1=[]

for i in infile:
    list_words1.append(i)
#print(list_words1)   

#Replace line with only newline with 2 new lines
list_words2=[]

for i in list_words1:
    if i =="\n":
        new = "\n\n"
    else:
        new = i
    list_words2.append(new)    
#print(list_words2)

#Get rid of \n from each line
list_words3=[]
for i in list_words2:
    newline= i[:len(i)-1]
    list_words3.append(newline)   #words3 = minus the "\n" (only 1)
#print(list_words3)    
       
total_words=""    
for i in list_words3:
    if total_words=="":
        total_words = i
    else:
        total_words=total_words+" "+i #TW makes it all one long line
#print(total_words)        
wordSpace = total_words.split(" ")
#print(wordSpace)

count = 0
list_count=[]
for i in wordSpace:
    if i =="\n":
        i = "\n\n"
        list1=i
        list_count.append(list1)
        count = 0
    else:
        count=count + len(i)
        if count<=width:
            list1=i+" "
            list_count.append(list1)
            count = count+1
        else:
            list1="\n"+i+" "
            count=len(i) + 1
            list_count.append(list1)
  
        
outfile.writelines(list_count)        
infile.close()
outfile.close()