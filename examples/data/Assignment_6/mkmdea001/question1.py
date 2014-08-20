#prog to enter a lost and the format it so that its on the right hand side 

def list():
    #get user input 
    x = input('Enter strings (end with DONE):\n')
    print()
#create empty     
    list=[]
    #initial value for count 
    number_of_inputs=0
    #get the max length of the input
    max = len(x)
    
 #if input id not DONE then and the input to the list 
    while x !='DONE':
        list.append(x)
        x=input("")
        number_of_inputs+=1
        # if input length is greater the initial max then 
        if len(x) > max:
            max = len(x)
    print('Right-aligned list:')
    
                  
    #loop over the inputs and each time calculate the number of spaces, then print output
    for i in range(number_of_inputs):
        spaces = max-len(list[i])
        print(' '*spaces+list[i])
        
list()
    
    
        
        
    
    #print(list,sep='')
    #print('DONE')
    
    
        