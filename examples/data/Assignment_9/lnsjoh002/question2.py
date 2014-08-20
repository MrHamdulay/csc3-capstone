"""Program to reformat a text file so that all lines are at most a given length
JP Lanser
10 May 2014"""
#Prompt user for filename
file_to_reformat = input('Enter the input filename:\n')
f = open(file_to_reformat, 'r')

file =f.read()

f.close()

#Prompt user for name of the new file
new_name = input('Enter the output filename:\n')
#Prompt user for the width they want
width = eval(input("Enter the line width:\n"))

#New paragraphs are indicated by '\n\n', split into a list according to this
list_of_paragraphs = file.split('\n\n')

#Now split the paragraphs into separate words

list_of_words=[]
for i in list_of_paragraphs:
  
    x=i.split(" ")
   
    list_of_words.append(x)
    
    
#Get rid of any '\n' that may be within words or at the beginning of words

for i in range(len(list_of_words)):
    j=0 
        
    for k in (list_of_words[i]):
        if '\n' in k:
            temp_list = k.split('\n')  #split where '\n' appears
            
            list_of_words[i].remove(k) #remove the whole string
            
            y=j
            
            for x in temp_list:
                list_of_words[i].insert(y,x) #add the two words (which are now separate strings) to the list of words
                y+=1
                
                
            
            
        j+=1
            
                    
              
            
            
        
        
f = open(new_name,'w')   #Open the new file to write to it             
                
#Now I have a 2D list, with the different paragraphs each in a different list:
#The paragraphs are also separated into lists of words


#Now print to the new file
for i in range(len(list_of_words)):
    characters_in_line =0  #This keeps track of the number of characters already in the line, so that a new line can be started when required
    if i!=0: #This is just so that an empty line is not printed the first time (at the top)
        print(file=f)
    
    for j in (list_of_words[i]): #Loop through the paragraphs first
        
        characters_in_line+= len(j)
        
        if characters_in_line <= width: #If the line will exceed the width, start a new line. If it doesn't, keep printing on that line,.
            print(j, end=" ", file=f)
            characters_in_line+=1
            
        else: 
            print(file=f)
            print(j, end=" ", file=f)
            characters_in_line = len(j) +1
    print(file =f)
            
f.close() 
        
        
        


    





    
    











  
