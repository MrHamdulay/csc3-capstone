"""Program to print out histogram
Thiloshni Moodley
22 April 2014"""

marks = input("Enter a space-separated list of marks:\n")
marks_list= marks.split(' ')

histo= [0,0,0,0,0] #Initial list

#counting and adding to count
for i in marks_list:
    if eval(i)>=75:
        histo[0]+=1
    if eval(i)>=70 and eval(i)<75:
        histo[1]+=1
    if eval(i)>=60 and eval(i) <70:
        histo[2]+=1
    if eval(i)>=50 and eval(i) <60:
        histo[3]+=1
    if eval(i) <50:
        histo[4]+=1

#Output
one = "1 |"
two_plus = "2+|"
two_minus = "2-|"
three = "3 |"
fail = "F |"
print(one + histo[0] *"X")
print(two_plus + histo[1] *"X")
print(two_minus + histo[2] *"X")
print(three + histo[3] *"X")
print(fail + histo[4] *"X")
