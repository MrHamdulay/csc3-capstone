#question2
#author: justin valsecchi
#date:19 may 2014

#opening txt file for opening
input_filename = input("Enter the input filname:\n")
open_filename = open(input_filename,"r")
output_file = input("Enter the output filename:\n")
Outfile = open(output_file,"w")
linewidth = int(input("Enter the line width:\n"))

list=[]

for i in open_filename:
    word=i
    list.append(word)

list2=[]
for j in list:
    if j =="\n": #checking for escape functions
        enter = "\n\n" #doubling escape function
    else:
        enter = j
    list2.append(enter) #creating a list of 'new lines'   
list3=[]
for k in list2:
    newline= k[:len(k)-1]
    list3.append(newline)   

rewrite=""    
for z in list3:
    if rewrite=="":
        rewrite = z
    else:
        rewrite=rewrite+" "+z 
   
listpace = rewrite.split(" ")


count = 0
list2=[]
for t in listpace: #reformating the file
    if t =="\n":
        t = "\n\n"
        list1=t
        list2.append(list1)
        count = 0 #counting the number of newlines
    else:
        count=count + len(t) #using the number of newlines, to format paragraphs and indentations
        if count<=linewidth:
            list1=t+" " #adding a space to the end of everyone last word
            list2.append(list1)
            count = count+1
        else:
            list1="\n"+t+" "
            count=len(t) + 1
            list2.append(list1)
  
        
Outfile.writelines(list2)        
open_filename.close()
Outfile.close()