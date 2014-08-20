#Dhriven Hamlall

def marks():
    
    marks=(input("Enter a space-separated list of marks:\n"))
    return marks

def lists():
    
    count=[0,0,0,0,0] # creating empty blocks for array
    list_Of_Marks=marks().split(" ")
    length_Of_Marks=len(list_Of_Marks)
    
    for i in range(length_Of_Marks):
        
        list_Of_Marks[i]=int(list_Of_Marks[i])
        
        if(list_Of_Marks[i]<50): #standard : given by question
            count[0]+=1
            
        elif(50<=list_Of_Marks[i]<60):
            count[1]+=1
            
        elif(60<=list_Of_Marks[i]<70):
            count[2]+=1
            
        elif(70<=list_Of_Marks[i]<75):
            count[3]+=1
            
        elif(75<=list_Of_Marks[i]<=100):
            count[4]+=1 
    
    return count

def histogram():
    
    marks=lists()
    
    symbols=["1 |","2+|","2-|","3 |","F |"]
    
    for i in range(5):
        
        x=marks[(len(marks)-1)-i] # works out number of X to multiply by
        print(symbols[i]+"X"*x) 
        
histogram()