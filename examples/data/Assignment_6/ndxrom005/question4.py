
scores= input("Enter a space-separated list of marks:\n")

scores_list= scores.split(' ') #split string in list

class1= [0,0,0,0,0] #place holder values

for j in scores_list: #search list to determine category
    if eval(j)>=75:
        class1[0]+=1
    if 70<=eval(j)<75:
        class1[1]+=1
    if 60<= eval(j) <70:
        class1[2]+=1
    if 50<= eval(j) <60:
        class1[3]+=1
    if eval(j) <50:
        class1[4]+=1
        
#create histogram
print("1 |"+class1[0] *"X")
print("2+|"+ class1[1] * "X")
print("2-|"+ class1[2] * "X")
print("3 |"+class1[3] * "X")
print("F |"+ class1[4] * "X")
            
        
    