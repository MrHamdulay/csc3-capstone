"""program to reformat a text file
   kevin kumasamba
   14 may 2014"""

#in_filename="input.txt"
#out_filename="output.txt"
#width=40
in_filename=input("Enter the input filename:\n")
out_filename=input("Enter the output filename:\n")
width=eval(input("Enter the line width:\n"))

# save the file as a list
# count the number of characters in each word of the list
# for each word, count a space
# have a counter that counts the number of characters

f=open(in_filename, "r")
string=f.readlines()
f.close()

new_string=[]
for item in string:
    if "\n" in item:
        new_string.append(item[:-1])
    else:
        new_string.append(item)

count=0
g=open(out_filename, "w")
for sentence in new_string:
    spl_sen=sentence.split(" ")
    for word in spl_sen:
        if count+len(word)<=width:
            print(word, end=" ", file=g)
            count+=len(word)
            count+=1
        else:
            count=0          
            print("", file=g)
            print(word, end=" ", file=g)
            count+=len(word)
            count+=1        
g.close()

g=open(out_filename, "r")
final=g.readlines()
g.close()

x=[]
for line in final:
    if "\n" in line:
        x.append(line[:-2])
    elif line[-1]==" ":
        x.append(line[:-1])
    else:
        x.append(line)

g=open(out_filename, "w")
for i in x:
    print(i, file=g)
g.close()