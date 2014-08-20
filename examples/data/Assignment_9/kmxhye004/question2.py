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
    if j =="\n":
        help = "\n\n"
    else:
        help = j
    list2.append(help)   
list3=[]
for k in list2:
    newline= k[:len(k)-1]
    list3.append(newline)   

TW=""    
for z in list3:
    if TW=="":
        TW = z
    else:
        TW=TW+" "+z 
   
listpace = TW.split(" ")


count = 0
list2=[]
for t in listpace:
    if t =="\n":
        t = "\n\n"
        list1=t
        list2.append(list1)
        count = 0
    else:
        count=count + len(t)
        if count<=linewidth:
            list1=t+" "
            list2.append(list1)
            count = count+1
        else:
            list1="\n"+t+" "
            count=len(t) + 1
            list2.append(list1)
  
        
Outfile.writelines(list2)        
open_filename.close()
Outfile.close()