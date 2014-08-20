"""histogram
kennedy muranda
25/4/2014"""

first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0



first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0  
    
mark = input("Enter a space-separated list of marks:\n")
marks = mark.split(" ")
    
for grade in marks:
    if eval(grade)<50:
        fail+= 1
    elif 50<= eval(grade)<60:
        third+= 1
    elif 60<= eval(grade)<70:
        lower_second+= 1
    elif 70<= eval(grade)<75:
        upper_second+= 1
    elif eval(grade)>=75:
        first+= 1
            
print("1 |"+first*"X")
print("2+|"+upper_second*"X") 
print("2-|"+lower_second*"X") 
print("3 |"+third*"X") 
print("F |"+fail*"X") 
            
                        

