
#Sandisha Budhal
#16/05/2014
#Program to reformat a text file so that all lines are at most a given length

def reading(f_name):
    #read lines in the file, remove new l escape sequences and return all contents as a list
    new_lis = [] #creating an empty list
    
    file = open(f_name,"r") #opening the file to read from it 
    lines = file.readlines() #creating a list that stores all the lines from the file
    file.close()#closing the file
    
    for l in lines:
        new_lis.append(l.replace('\n','')) #appending the list
    return new_lis

def setting(L,W):
    s = ''
    tmp_list = [''] #creating a new list
    
    a = 0
    
    for l in L:
        if len(l) > 1:
            wrds = l.split(' ') #splitting on the basis of an empty space
            
            for wrd in wrds:
                if (len(tmp_list[a])+len(wrd)) <= W :
                    tmp_list[a] += wrd+" "
                    
                elif wrd == 'a':
                    tmp_list[a]=tmp_list[a]+ wrd
                    
                else:
                    tmp_list.append(wrd+" ") #appending the list
                    a=a+1
        else:
            tmp_list.append('\n') #appending the list
            a=a+1
            
    return tmp_list  #returning the list

def writing(f_name,lines):
    #write contents of outList to output file
    f = open(f_name,'w') #opening the file
    for l in lines:
        print(l,file=f) #prints each line into file
    f.close()   #closing the file 

def file_n():  #function to ask the user to input the input filename, output filename and line width
    in_filename = input("Enter the input filename:\n")
    
    out_filename = input("Enter the output filename:\n")
    
    line_width = eval(input("Enter the line width:\n"))
    
    lines = reading(in_filename)
    
    lines = setting(lines,line_width)
    
    writing(out_filename,lines)

file_n() #calling the function