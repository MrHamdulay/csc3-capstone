"""Program to reformat text (line width)
Pankaj Munbodh
10 May 2014"""

#Get inputs from user
input_file=input("Enter the input filename:\n")
output_file=input("Enter the output filename:\n")
line_width=eval(input("Enter the line width:\n"))

f_i=open(input_file,'r')
f_o=open(output_file,'w')

#Create list of lines
liste=f_i.readlines()

i=0
for i in range(len(liste)):            #strip list elements of newline character
    liste[i]=liste[i][:-1]
    
newline_list=[]                       #gives the indices where newlines were found
for i in range(len(liste)):
    if liste[i]=='':
        newline_list.append(i)

#If there are newlines in file (there are paragraphs), go through 'liste' in chunks where newlines were found i.e. divide list into chunks and work through each paragraph    
if len(newline_list)!=0:
    for i in range(len(newline_list)+1):
        piece_list=[]
        
        if i!=0 and i!=len(newline_list):              # to avoid indexerror    (what follows is code for after 1st paragraph has been read and before last paragraph has been read)
            for j in range(newline_list[i-1]+1,newline_list[i]):
                piece_list.append(liste[j])
            long_string=' '.join(piece_list)
                
            index1=0
            up=1
            while up==True:
                try:
                    if long_string[index1+line_width] !=' ':       #  read string in sequences of line_width and check so that words are not chopped halfway through
                        get_str=long_string[index1:index1+line_width]
                        index2=get_str.rfind(' ')+index1
                        print(long_string[index1:index2],file=f_o)
                        index1=index2+1
                    else:                                      #if word would not be chopped, execute this 'else' statement (otherwise 'if' above is executed)
                        print(long_string[index1:index1+line_width],file=f_o)
                        index1=index1+line_width+1
                except:
                    print(long_string[index1:],file=f_o)        #to print last line of particular paragraph. 'up' variable used to terminate while loop because end of paragraph has been reached.
                    up=''
            print("\n",end='',file=f_o)              #print a newline before processing next paragraph
                
                    
                    
        else:
            if i ==0:                 #To print reformatted first paragraph. Structure of code is same as above except indices are adjusted to avoid off-by-one and index errors.
                for j in range(newline_list[i]):
                    piece_list.append(liste[j])
                long_string=' '.join(piece_list)
                            
                index1=0
                up=1
                while up==True:
                    try:
                        if long_string[index1+line_width] !=' ':
                            get_str=long_string[index1:index1+line_width]
                            index2=get_str.rfind(' ')+index1
                            print(long_string[index1:index2],file=f_o)
                            index1=index2+1
                        else:
                            print(long_string[index1:index1+line_width],file=f_o)
                            index1=index1+line_width+1
                    except:
                        print(long_string[index1:],file=f_o)
                        up=''
                print("\n",end='',file=f_o)
                            
                        
                                     
                
            elif i==len(newline_list):                 #To print reformatted last paragraph. Structure of code is same as above except indices have been adjusted to avoid errors.
                for j in range(newline_list[i-1],len(liste)):
                    piece_list.append(liste[j])
                long_string=' '.join(piece_list)
                                        
                index1=1
                up=1
                while up==True:
                    try:
                        if long_string[index1+line_width] !=' ':
                            get_str=long_string[index1:index1+line_width]
                            index2=get_str.rfind(' ')+index1
                            print(long_string[index1:index2],file=f_o)
                            index1=index2+1
                        else:
                            print(long_string[index1:index1+line_width],file=f_o)
                            index1=index1+line_width+1
                    except:
                        print(long_string[index1:],file=f_o)
                        up=''
                f_i.close()
                f_o.close()

else:                 #If file is not in paragraphs(contains no blank lines):   structure of code is same as above except the string can be taken as a whole and processed. It needs not be broken into paragraphs as above before processing.
    long_string=' '.join(liste)
    
    index1=0
    up=1
    while up==True:
        try:
            if long_string[index1+line_width] !=' ':
                get_str=long_string[index1:index1+line_width]
                index2=get_str.rfind(' ')+index1
                print(long_string[index1:index2],file=f_o)
                index1=index2+1
            else:
                print(long_string[index1:index1+line_width],file=f_o)
                index1=index1+line_width
        except:
            print(long_string[index1:],file=f_o)
            up=''
    
    f_i.close()
    f_o.close()    
