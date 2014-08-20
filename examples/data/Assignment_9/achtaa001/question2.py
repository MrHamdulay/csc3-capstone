#Taahirah Achmat
#function for paragraphs
def tay(f1 ,f2 ,width):
        #read the file as one string
    f=open(f1,'r')    
    l = f.read()
    f.close()
           #open file to overwrite it
    b=open( f2 , 'w')
          
    
    #get all paragraphs
    paragraph = l.split('\n\n')

    
    
    p=0
    while p<len(paragraph):
        l = paragraph[p].split(" ")
        l=' '.join(l)
        
        l=l.replace('\n',' ')
        l = l.split(' ')
        i=0
        j=0
       
        while i< len(l):
            while j<=width:
               
                if i>=len(l):break
                
                
                
                if l[i]==" ":
                    i+=1
                        
            
                if len(l[i])<= width-j:
                    print(l[i], file=b, end=" ")
                    j+=(len(l[i])+1)
                    i+=1
                else:
                    print('\n',l[i] , file=b , end=" ",sep='')
                    j=(len(l[i])+1)
                    i+=1
                
                
                if j>=width:
                    j=0
                    print(file=b)
        #start new paragraph
        print('\n',file=b)
        p+=1 
                     
    b.close()
#get input and use the function
f1 = input("Enter the input filename:\n")
f2 = input("Enter the output filename:\n")
width =eval(input("Enter the line width:\n"))    
tay(f1 ,f2,width)