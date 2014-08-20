#Phumelele Ndimande
#Assignment 6

#get marks
marks = input("Enter a space-separated list of marks:\n")

#split marks
mark=marks.split()

fail = 0
third=0
lower_second=0
upper_second=0
first=0

#count results and add to appropriate group
for i in mark:
    if int(i)<50:
        fail+=1
    elif 50<=int(i)<60:
        third+=1
    elif 60<= int(i) <70:
        lower_second+=1
    elif 70<= int(i) <75:
        upper_second+=1
    elif int(i)>=75:
        first+=1
        
#print histogram        
print("1 |" + 'X'*first)
print("2+|" + 'X' * upper_second)
print("2-|" + 'X'* lower_second)
print("3 |" + 'X' * third)
print("F |" + 'X' * fail)

        

        