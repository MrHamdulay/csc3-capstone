"""question 4
clare walker
19 april 2014"""
#get marks
mark_string = input("Enter a space-separated list of marks:\n")
mark_string=mark_string.split(' ')
#convert to list

marks=[]
for i in range(len(mark_string)):
    marks.append(str(mark_string[i]))
 
#get 'y coords' of histogram
fail = 0
third = 0 
lower_sec = 0
upper_sec = 0
first = 0
m=""
for mark in marks:
    m = eval(mark)
    if m < 50:
        fail+=1
    elif m<60:
        third+=1
    elif m<70:
        lower_sec+=1
    elif m<75:
        upper_sec+=1
    else:
        first+=1
#print histogram

print("1 |"+"X"*first)
print("2+|"+"X"*upper_sec)
print("2-|"+"X"*lower_sec)
print("3 |"+"X"*third)
print("F |"+"X"*fail)
    
    