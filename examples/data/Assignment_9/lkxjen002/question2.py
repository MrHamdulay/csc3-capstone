#A program to reformat a text file so that all lines are at most a given length
#Created by:Jenna Lake
#Date: 13 may 2014

#get info from user
input_filename=input("Enter the input filename:\n")
output_filename=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

#Open files
f_in=open(input_filename, "r")
f_out=open(output_filename, "w")

word1=[]
new_lines=[]
remcount=0
replaced_words=[]

#split lines which end on "\n"
for i in f_in:
    word=i
    word1.append(word)

#replace newline character with double newlinecharacter    
for seg in word1:
    if seg=="\n":
        enter="\n\n"
    else:
        enter=seg

more_words=[]
more_words.append(enter)
more_words2=[]

#remove one of the newline characters
for k in more_words:
    new_line=k[:-1]
    more_words2.append(new_line)
    
words_join=""
count=0
counter=[]

#add spaces so all one extended line
for l in more_words2:
    if words_join=="":
        words_join=l
    else:
        words_join=words_join + " " + l 
separate=words_join.split(" ")

#
for n in separate:
    if n=="\n":
        one_nl="\n\n"
        counter.append(one_nl)
        count=0    # if there has been a newline, the counter needs to restart
    else:
        count= count + len(n)
        if count<=width:
            one_nl=n + " "
            counter.append(one_nl)
            count=count+1
        else:
            one_nl="\n" + n + " "
            count=len(n)+1
            counter.append(one_nl)
        
    
f_out.writelines(counter)
#f_in.close
#f_out.close()
        
