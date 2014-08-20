"""reformat a text file so all lines are at most a given length
Lauren Denny
11 May 2014"""

i_file=input("Enter the input filename:\n") #get input filename
o_file=input("Enter the output filename:\n") #get output filename
width=eval(input("Enter the line width:\n")) #get integer value for line width

f=open(i_file,"r")
lines=f.readlines() #store all lines in input file as a list of strings called lines
f.close()

for i in range(len(lines)):
    lines[i]=lines[i][:-1] #get rid of "\n"'s for each line

#put everything in 1 paragraph in 1 string with joined lines separated by a single space if necessary
new_lines=[]
for i in range(len(lines)):
    if i==0:
        new_lines.append(lines[i]) #put first line as first element in new_lines
    else:
        if lines[i]!="" and new_lines[-1]!="": #if neither of the last element in new_lines and first ith element in lines are empty lines
            if lines[i-1][-1]==" ": #if the line before the ith line in lines ends in a single space, add line[i] to the last string in new_lines
                new_lines[-1]+=(lines[i])
            else:
                new_lines[-1]+=(" "+lines[i]) #otherwise, if lines[i-1] doesn't end in a space, join line[i] to the last string in new_lines with a single space        
        else:
            new_lines.append(lines[i]) #otherwise, if either of the two are empty lines, add line[i] as the new last element of new_lines


#write to output file
g=open(o_file,"w")

for line in new_lines:
    start=0
    end=width
    while end<=len(line):       
        while line[end]!=" ": #if the portion of the line to printed is a not a " ", i.e. is in the middle of of word, make the end 1 character shorter until the end of the line is at the end of a word
            end-=1         
        print(line[start:end],file=g) #print the line going form the start index to the end-1 index (don't print the " " at the end of the segment) to the output file 
        start=end+1 #the next letter to be printed is the one after the " "
        end+=(width+1) #end width places after start
    print(line[start:],file=g) #if the line is shorter than the desired width, print the line as it is
    
g.close()