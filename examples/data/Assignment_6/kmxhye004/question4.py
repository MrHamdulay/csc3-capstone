#Helin Kim
#Question 4 
#Comsci Assignment 



#get the user to input the list of marks 

mark = input("Enter a space-separated list of marks: \n")

#split the numbers so they are a list
mark = mark.split()

  
fail = 0
third = 0
lower_second = 0 
upper_second = 0
top = 0


for i in range(len(mark)):
    mark[i] = eval(mark[i])


for i in mark:
    if i < 50:
        fail += 1
    elif 50 <= i < 60:   
        third += 1
    elif 60 <= i < 70:
        lower_second += 1 
    elif 70 <= i < 75:
        upper_second += 1
    else:
        top += 1
   
print ("1 ", "|", "X"*top, sep="")
print ("2+", "|", "X"*upper_second, sep="")
print ("2-", "|", "X"*lower_second, sep="")
print ("3 ", "|", "X"*third, sep="")
print ("F ", "|", "X"*fail, sep="")