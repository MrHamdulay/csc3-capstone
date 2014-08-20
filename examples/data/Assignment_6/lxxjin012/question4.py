# a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks
#Jenny Luo
#25 April 2014

fail=0
third=0
lowersecond=0
uppersecond=0
first=0

#add elements into the list
marklist=[]
mark=input("Enter a space-separated list of marks:\n")
mark=mark.split()
for i in mark:
    marklist.append(eval(i))

#count the number of marks corresponding to each mark category  
for i in marklist:
    if i < 50:
        fail+=1
    elif 50 <=i and i <60:
        third+=1
    elif 60<=i and i <70:
        lowersecond+=1
    elif 70 <=i and i< 75:
        uppersecond+=1
    else:
        first+=1
        
#print the histogram
print("1 |"+"X"*first)  
print("2+|"+"X"*uppersecond)
print("2-|"+"X"*lowersecond)
print("3 |"+"X"*third)
print("F |"+"X"*fail)
