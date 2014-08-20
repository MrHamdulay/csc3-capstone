'''program form histogram of marks
nicole henning
due: 25 april 2014'''

#ask for marks
marks_str = input("Enter a space-separated list of marks:\n")
marks_list = marks_str.split(" ") #to make string into a list of the marks

#make marks into integers
marks_list = [int(i) for i in marks_list]

#count number per catagory
count_f=0
count_3=0
count_l2=0
count_u2=0
count_1=0

for i in marks_list:
   
    if i<50:
        count_f+=1 #if found in catagory, count goes up by 1
    if 50<=i<60:
        count_3+=1
    if 60<=i<70:
        count_l2+=1
    if 70<=i<75:
        count_u2+=1
    if 75<=i:
        count_1+=1
    

#print X in cat row for number to make histogram
print ("1 |", "X"*count_1, sep="")
print ("2+|", "X"*count_u2, sep="")
print ("2-|", "X"*count_l2, sep="")
print ("3 |", "X"*count_3, sep="")
print ("F |", "X"*count_f, sep="")