'''program to align names to the right
Norman Pilusa 
April 2014'''

def align():
    #collection of names
    data=[] 
    names=input('Enter strings (end with DONE):\n')
    
    #addition of names to 'database'
    while True:
        
        if names=='DONE': #termination of program
            break
        else: 
            data.append(names)
            names=input()
    print()
    print('Right-aligned list:')
    
    #find longest name
    longest=0
    for name in data: 
        if len(name)>longest:
            longest=len(name)
    
    #align name to right      
    for name in data: 
        print(name.rjust(longest))            
align()