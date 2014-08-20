#this program determines which student requires to see a student advisor
#Hebert TEMA- TMXTHA006
#10 MAY 2014


def average(array):
    """calculate the average of the scores on a given list"""
    sum_values=sum(array)
    mean=sum_values/len(array)
    return mean

def std_deviation(array, mean):
    """calulate the standard deviation of the scores when given a list and an average"""
    sqrd_sum=0
    for i in array:
        sqrd_sum+= (i-mean)**2
    varience= sqrd_sum/len(array)
    std_dev=(varience)**0.5         #squareroot of varience
    return std_dev

#get input from the user
file_name=input("Enter the marks filename:\n")


#file processing
f=open(file_name, "r")
data=f.readlines()
f.close()

#data processing
details=[]
for line in data:
    temp=line[:-1].split(",")
    temp[-1]=eval(temp[-1])
    details.append(temp)
values=[]
for i in details:
    values.append(i[-1])
#calculatre the average and the standard deviation
average=average(values)
std_dev=round(std_deviation(values, average), 2)

#less than 1 standard deviation from the mean
line=average-std_dev

#return the output
print("The average is:", "{0:0^5}".format(round(average,2)))
print("The std deviation is:", std_dev)

students=[]
for i in details:
    if i[-1]<line:
        students.append(i[0])
if students:
    print("List of students who need to see an advisor:")
    for j in students:
        print(j)

