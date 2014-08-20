"""Program to reformat text files
Thiloshni Moodley
16 May 2014"""

in_file= input("Enter the input filename:\n")
f = open(in_file,"r") #open input file and read
out_file = input("Enter the output filename:\n")
o = open(out_file,"w") # open output file and overwrite
words=f.read()

position=0
count=-1

width = eval(input("Enter the line width:\n")) #prompt user for input
for i in range(len(words)):
    if(i==len(words)-1):  #case 1
            lists=[] #create an empty list
            lists.append(words[count+1]) #append to the list
            for j in range(count+2,i):
                if(words[j]!='\n'): #If its not the character of new line
                    lists.append(words[j]) #append to list
                else:
                    lists.append(" ") # else append an empty string
            lists.append(words[i])      
            for j in lists:
                print(j,end='',file=o)
                
    elif(words[i]=="\n" and words[i+1]=="\n"): #In the case where it is new line character, case 2
        lists=[] # create new empty string
        lists.append(words[count+1])
        for j in range(count+2,i):
            if(words[j]!='\n'):
                lists.append(words[j])
            else:
                lists.append(" ")
        lists.append(words[i])
        for j in lists:
            print(j,end='',file=o)
        print("",file=o)        
        
        count=i+1     
    
    elif(i==count+width and words[i+1]==" "): #case 3
        lists=[] #create new empty list
        lists.append(words[count+1]) #append to list
        for j in range(count+2,i):
            if(words[j]!='\n'):
                lists.append(words[j])
            else:
                lists.append(" ")
        lists.append(words[i])
        for j in lists:
            print(j,end='',file=o)
        print("",file=o)        
        
        count=i+1
    
    elif(i==count+width and words[i+1]!=" "):  #case 4   
        for j in range(i,count,-1):
            if(words[j]==" " or words[j]=="\n"):
                posit=j
                break
        lists=[] #create new list
        lists.append(words[count+1]) #append to list
        for j in range(count+2,posit-1):
            if(words[j]!='\n'):
                lists.append(words[j])
            else:
                lists.append(" ")
        lists.append(words[posit-1])        
        for j in lists:
            print(j,end='',file=o)
        print("",file=o)
        count=position
        
#close both files
f.close() 
o.close()
