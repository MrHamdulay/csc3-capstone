string = input("Enter a message:\n")
count = 0
listi = []

def pairs(string,count):
    
    
    if len(string) == 0 or len(string)==1:
    
        print("Number of pairs:",count)
        #print(listi)
        
    elif len(string) > 1:
        
        if string[0] == string[1]:
        
            count = count + 1
            #listi.append(string[0])
        
        pairs(string[2:],count)
    
pairs(string,count)

