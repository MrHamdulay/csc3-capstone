#Sheldon Kisten
#histogram of marks
#23 April 2014

score= input("Enter a space-separated list of marks:\n")

score_list= score.split(' ') #split string in list

class1= [0,0,0,0,0] #place holder values

for i in score_list: #search list to determine category
    if eval(i)>=75:
        class1[0]+=1
    if 70<=eval(i)<75:
        class1[1]+=1
    if 60<= eval(i) <70:
        class1[2]+=1
    if 50<= eval(i) <60:
        class1[3]+=1
    if eval(i) <50:
        class1[4]+=1
        
#create histogram
print("1 |"+class1[0] *"X")
print("2+|"+ class1[1] * "X")
print("2-|"+ class1[2] * "X")
print("3 |"+class1[3] * "X")
print("F |"+ class1[4] * "X")
            
        
    