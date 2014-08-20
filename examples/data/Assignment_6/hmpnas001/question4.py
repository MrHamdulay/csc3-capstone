"""program to show histogram of results
nasonkwe hampwaye
2014-04-24"""
#getting marks
marks_input=input("Enter a space-separated list of marks:\n")
marks=marks_input.split(" ")
count1=[]
count2up=[]
count2low=[]
count3=[]
countF=[]
#categorizing
for i in marks:
    i=eval(i)
    if i>=75:
        count1.append(i)
      
    elif i>=70:
        count2up.append(i)
    elif i>=60:
        count2low.append(i)
    elif i>=50:
        count3.append(i)
    else:
        countF.append(i)
        
# output
print("1 |","X"*len(count1),sep='')
print("2+|","X"*len(count2up),sep='')
print("2-|","X"*len(count2low),sep='')
print("3 |","X"*len(count3),sep='')
print("F |","X"*len(countF),sep='')
        
        
