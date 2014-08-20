"""bar chart printout based on given marks
Duldey Mutero
24/4/14"""

list1=[] 
f=0              #empty variales for plotting graph with
three=0          #empty variales for plotting graph with
twominus=0       #empty variales for plotting graph with
twoplus=0        #empty variales for plotting graph with
one=0            #empty variales for plotting graph with
a=input("Enter a space-separated list of marks:\n") 
list1=a.split() #split the list of numbers entered by user
for i in list1: #run thru the whole list 1 item after another
    d=eval(i)   #our list has been split as a string. Evaluating helps to check e class of e mark
    if d<50:        #evaluating for fail
        f+=1
    elif 50<= d <60:    #evaluating for 3rd grade
        three+=1
    elif 60<= d <70:        #evaluating for 2nd lower class
        twominus+=1
    elif 70<= d<75:     #evaluating for 2nd upper class
        twoplus+=1
    elif d >=75:     #evaluating distinc
        one+=1
print("1 |","X"*one,sep="")     #Printing out the bar chat
print("2+|","X"*twoplus,sep="")
print("2-|","X"*twominus,sep="")
print("3 |","X"*three,sep="")
print("F |","X"*f,sep="")