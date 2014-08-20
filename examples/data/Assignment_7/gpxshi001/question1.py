#GPXSHI001
#2nd MAY2014
#Ass 7
#q1
def newlist():
    
    x= [] #creates empty list
    y= ("")
    repeats= []
    print("Enter strings (end with DONE):")
    
    while y!= "DONE":
        y= input("")
        
        if y!= ("DONE"):
            x.append(y)
         
        for i in x:   
            
            if i not in repeats:            
                repeats.append(i)
    print()            
    print("Unique list:")            
    for i in repeats:
        print(i)
                
    
newlist()