"""
Histogram
"""
mark_input = input("Enter a space-separated list of marks:\n")
mark = mark_input.split() #marks split by space
mark_list = [] #empty list

first=0 
second_upper=0
second_lower=0
third=0
fail=0

for i in range (len(mark)):
    mark[i] = eval(mark[i]) #mark converted into integer 
    mark_list.append(mark[i]) #appended to mark list
    
for j in mark: #mark intervals 
    if ( 0 <= j < 50):
        fail+=1
    elif (j< 60):
        third+=1
    elif (j < 70):
        second_lower+=1
    elif (j < 75):
        second_upper+=1
    else:
        first+=1
        
print("1 |","X"*first,sep='')
print("2+|","X"*second_upper,sep='')
print("2-|","X"*second_lower,sep='')
print("3 |","X"*third,sep='')
print("F |","X"*fail,sep='')
        