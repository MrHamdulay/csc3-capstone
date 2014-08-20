"""program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks
Elizabeth Cilliers
22 April 2014"""

def marks():
    
    Inputmarks=input("Enter a space-separated list of marks:\n")
    list_marks = Inputmarks.split ()
    
    
    
    cat={"F":0,"3":0,"2-":0,"2+":0,"1":0} #create dictionary/catalogue of grades
    for mark in list_marks:
        
        mark=eval(mark)
        
        if mark<50:
            cat["F"]+=1 #if mark is lower than 50% add 1 to F category
        
        elif mark<60:
            cat["3"]+=1
        
        elif mark<70:
            cat["2-"]+=1
        
        elif mark<75:
            cat["2+"]+=1
        
        else:
            cat["1"]+=1
        
    print("1 |","X"*cat["1"],sep="")  #print out value stored for each category 
    print("2+|","X"*cat["2+"],sep="")
    print("2-|","X"*cat["2-"],sep="")
    print("3 |","X"*cat["3"],sep="")
    print("F |","X"*cat["F"],sep="")
      
   
marks()