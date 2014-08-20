#A program to histogram marks of classes
#Thabang Bhili
#2014/04/25


list=[]

#Filling list of marks
marks=input('Enter a space-separated list of marks:\n')
list=marks.split(' ')

#Changing strings to numbers in the list
for i in range(len(list)):
    list[i]=eval(list[i])

first=0
upsec=0
lowsec=0
third=0
fail=0

#Iterating through list and testing each item. One of the variables above then augmented accordingly
for i in list:
    
    if i>=75:
        first+=1
    elif 70<=i<75:
        upsec+=1
    elif 60<=i<70:
        lowsec+=1
    elif 50<=i<60:
        third+=1
    elif i<50:
        fail+=1
        
#Printing histogram        
print("1 |"+(first*'X'))
print("2+|"+(upsec*'X'))
print("2-|"+(lowsec*'X'))
print("3 |"+(third*'X'))
print("F |"+(fail*'X'))
