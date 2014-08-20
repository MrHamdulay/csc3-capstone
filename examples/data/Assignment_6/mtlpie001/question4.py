#Piet motalaota
marks = input("Enter a space-separated list of marks:\n")

marks_list = marks.split(" ")
Fail=[]
third=[]
lower_2nd=[]
upper_2nd=[]
first=[]

for i in range(len(marks_list)):
    
    if eval(marks_list[i])>=75:
        first.append(marks_list[i])

     
    elif 70<= eval(marks_list[i]) <75:
        upper_2nd.append(marks_list[i])

    
    elif 60<= eval(marks_list[i]):
        lower_2nd.append(marks_list[i])

    
    elif 50<=eval(marks_list[i])<60:
        third.append(marks_list[i])
    
    elif eval(marks_list[i])<50:
        Fail.append(marks_list[i])
print("1 |"+"X"*len(first))        
print("2+|"+"X"*len(upper_2nd))        
print("2-|"+"X"*len(lower_2nd))        
print("3 |"+"X"*len(third))        
print("F |"+"X"*len(Fail))
