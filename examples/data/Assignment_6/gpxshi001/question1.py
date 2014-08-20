#GPXSHI001
#ASS 6
#CREATING LIST AND FORMATTING RIGHT
#Q1

def shift_right():
    
    long=""
    x= [] #creates empty list
    
    y= ("")
    print("Enter strings (end with DONE):")
    
    while y!= "DONE":
        y= input("")
        
        if y!= ("DONE"):
            x.append(y)
         
    for i in range (len(x)):
        if (len(x[i]))>len(long):
            long=x[i]
    
    for_format= '{:>' + str(len(long)) + '}'
    
    print ("\nRight-aligned list:")
    
    for j in range (len(x)):                  #lenth starts from 1. need to make same as index. subtract1.
        print(for_format.format(x[j]))
        
        
shift_right()