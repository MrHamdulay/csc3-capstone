"""Assignment 6 question 4
shannon clacey
23 april 2014"""
def uct_marks():
    marks = input("Enter a space-separated list of marks: \n") #get marks from user
    list_marks = marks.split(" ") #create list from marks
    add_f = 0 #where to start for the the sum of marks within the given categories. The character after the the underscore represents the category
    add_3 =0
    add_2lower = 0
    add_2upper = 0
    add_1 = 0    
    for i in list_marks: #creating for loop within the list of marks
        x = eval(i) #eval i so that it is numerical
        if 0<= x< 50:
            add_f += 1 #counting the number of marks in the list within each of the given categories
        elif 50 <= x <60:
            add_3 +=1
        elif 60 <= x <70:
            add_2lower += 1
        elif 70 <= x <75:
            add_2upper += 1
        elif 75 <= x <=100:
            add_1 += 1
    print("1 |", "X"*add_1, sep='') #creat histogram 
    print("2+|", "X"*add_2upper, sep='')
    print("2-|", "X"*add_2lower, sep='')
    print("3 |", "X"*add_3, sep='')
    print("F |", "X"*add_f, sep='')
uct_marks()
        
        