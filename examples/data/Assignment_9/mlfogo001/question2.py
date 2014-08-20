"""Program to justify text.
Ogone Molefe 
16 May 2014"""


#define function to line paragraphs to certin length
def hello(file1 ,file2 ,width):
    #read the file as one string
    f=open(file1,'r')    
    lines = f.read()
    f.close()
    #open file to write over it
    s=open( file2 , 'w')
    #print(lines)
    
    #get all paragraphs
    par = lines.split('\n\n')

    
    
    p=0
    #print(paragrahs)
    #run through each paragraph
    while p<len(par):
        lines = par[p].split(" ")
        lines=' '.join(lines)
        
        lines=lines.replace('\n',' ')
        lines = lines.split(' ')
        #lines.replace('\n',' ')
        #print(lines)
        i=0
        j=0
        #print the given length to each line.
        while i< len(lines):
            while j<=width:
                #start new line when length is met
                if i>=len(lines):break
                
                
                
                if lines[i]==" ":
                    i+=1
                        
            
                if len(lines[i])<= width-j:
                    print(lines[i], file=s, end=" ")
                    #print(lines[i])
                    j+=(len(lines[i])+1)
                    i+=1
                else:
                    #print(file=s)
                    print('\n',lines[i] , file=s , end=" ",sep='')
                    
                    j=(len(lines[i])+1)
                    i+=1
                
                
                if j>=width:
                    j=0
                    print(file=s)
        #start new paragraph
        print('\n',file=s)
        p+=1 
                     
    s.close()
#get inout and call the function
file1 = input("Enter the input filename:\n")
file2 = input("Enter the output filename:\n")
width =eval(input("Enter the line width:\n"))    
hello(file1 ,file2,width)