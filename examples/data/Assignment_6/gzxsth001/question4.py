"""A programme to take a list of marks and outputs a histogram
Andile Sthabiso Gazu
april 2014"""
#create a dictionary
fail=0
third=0
lower_second=0
upper_second=0
first=0
marks=input("Enter a space-separated list of marks:\n")
List_of_marks=marks.split(" ")
for i in List_of_marks:#grouping the marks
    if int(i)<50:
        fail+=1
    elif 50<=int(i)<60: 
        third+=1
    elif 60<=int(i)<70:
        lower_second+=1
    elif 70<=int(i)<75:
        upper_second+=1
    elif int(i)>=75:
        first+=1
        
#to return histogram
x=first
y=upper_second
k=lower_second
l=third
m=fail


print("1 |",'X'*x,sep='')
print("2+|",'X'*y,sep='')
print("2-|","X"*k,sep='')
print("3 |","X"*l,sep="")
print("F |",'X'*m,sep='')
