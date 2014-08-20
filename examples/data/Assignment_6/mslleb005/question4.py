x=input("Enter a space-separated list of marks:\n").split()
count=0
b=0
a=0
g=0
d=0

first_grade=""
second_grade=""
third_grade=""
fourth_grade=""
fifth_grade=""

for mark in x:
    
    mark=int(mark)
    if mark >= 75:
        count=count+1
        first_grade=count * "X"
           

    if 70<= mark < 75:
            b=b+1
            second_grade=b * "X"
            
            
            
    if 60 <= mark < 70:
            a=a+1
            third_grade=a * "X"
                       
            
    if 50 <= mark < 60:
            g= g + 1
            fourth_grade=g * "X"
             
   
    if mark < 50:
        d = d+1
        fifth_grade= d* "X"
print("1","|" + first_grade) 
print("2+"+"|"+second_grade)
print("2-"+"|"+third_grade)
print("3","|"+fourth_grade) 
print("F","|"+fifth_grade)