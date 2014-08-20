"""Program to draw histogram from a list of marks
Leandra Govender
23 April 2014"""

marks= input("Enter a space-separated list of marks:\n")                       #ask user for list of marks

mark_list= marks.split(' ')                                   

classes= [0,0,0,0,0]

for i in mark_list:
    if eval(i)>=75:
        classes[0]+=1
    if 70<=eval(i)<75:
        classes[1]+=1
    if 60<= eval(i) <70:
        classes[2]+=1
    if 50<= eval(i) <60:
        classes[3]+=1
    if eval(i) <50:
        classes[4]+=1
        

print("1 |"+classes[0] *"X")                        #draw the histogram
print("2+|"+ classes[1] * "X")
print("2-|"+ classes[2] * "X")
print("3 |"+classes[3] * "X")
print("F |"+ classes[4] * "X")
            
        
    