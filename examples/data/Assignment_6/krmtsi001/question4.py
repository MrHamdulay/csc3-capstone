marks=input("Enter a space-separated list of marks:\n").split() #is is to make what the user has inputted into a list for manipulation
first_class=0
upper_second=0    #line 2 to 5 making each grade a category
lower_second=0
third_class=0
fail=0

for grade in marks:
    if eval(grade)<50:       #looping through the mark so that they can be put into their respective grades
        fail+=1
    elif eval(grade) < 60:
        third_class+=1
    elif eval(grade)< 70:
        lower_second+=1
    elif eval(grade)<75:
        upper_second+=1
    else:
        first_class+=1
print("1 |"+"X"*first_class)
print("2+|"+"X"*upper_second)     #displaying the grades with each mark grouped in a histogram 
print("2-|"+"X"*lower_second)
print("3 |"+"X"*third_class)
print("F |"+"X"*fail) 