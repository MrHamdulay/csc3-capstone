def histogram():
    
    marks=input("Enter a space-separated list of marks:\n") #prompt for string of marks
    mark_list=marks.split(" ") #convert string of marks into list
    
    for i in range(1):  
        print("1 |",end="") #mark category,print once
        for marks in mark_list:
            if marks>= "75" or marks=="100": #iterate over marks and print "X" a certain number of times depeding on how many 'marks' meet criteria; the marks are in the form of strings, so need to say "75", "100" etc, instead of 75, 100, etc. 
                print("X",end="")   
    print()
    
    #REPEAT STEPS FOR ALL CATEGORIES OF MARKS:
    for i in range(1):
        print("2+|",end="")
        for marks in mark_list:
            if "70"<=marks<"75":
                print("X",end="")
    print()
    
    for i in range(1):
        print("2-|",end="")
        for marks in mark_list:
            if "60"<=marks<"70":
                print('X',end="")
    print()
    
    for i in range(1):
        print("3 |",end="")
        for marks in mark_list:
            if "50"<=marks<"60":
                print("X",end="")
    print()
    
    for i in range(1):
        print("F |",end="")
        for marks in mark_list:
            if marks<"50" and marks !="100":
                print("X",end="")
                
histogram()
            
            
        
