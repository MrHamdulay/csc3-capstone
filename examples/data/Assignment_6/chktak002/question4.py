x =input("Enter a space-separated list of marks:\n")

st=0
upper_second=0
lower_second=0
third=0
fail=0
marks=[] #create an empty list
for num in x.split(): # splits the input seperated by spaces into seperate indexes in the list
    num=eval(num)
    marks.append(num) #adds marks to the list

for i in range(len(marks)): 
    
    if  marks[i] >= 75: # categorizes data into the categories
        st+=1
    
    elif 70 <= marks[i]< 75:
        upper_second+=1
    
    elif 60<= marks[i] < 70:
        lower_second+=1
    
    elif 50 <=marks[i]< 60:
        third+=1
    
    else:
        if marks[i]<50:
            
            fail+=1
        

print("1 |"+ "X"*st)       #prints the number of x's corresponding to the frequency of the marks 
print("2+|"+ "X"*upper_second)
print("2-|"+ "X"*lower_second)
print("3 |"+ "X"*third)
print("F |"+ "X"*fail)

