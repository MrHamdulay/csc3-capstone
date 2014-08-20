#program to print a list of strings right aligned with the longest string
#F.J.Chigwaza
#22 April 2014

def words():
    
    word=input('Enter strings (end with DONE):\n')
    w=[]
#precondition for while loop    
    while word!='DONE':
        w.append(word)
        word=input('')
#initialising the length of the word input   
    length =0
#setting the maximum length for the words    
    for i in(w):
        if len(i) > length:
            length = len(i)
            
    
#output of the strings aligned to the right    
    print('\nRight-aligned list:')
    for j in (w):
        gap=length-len(j)
        print(' '*gap,(j),sep='')
   
words()        
    
        

        
        
   
    
    