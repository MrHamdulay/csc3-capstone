#Program to determine students outside standard deviation of mean
#Tyrone Arnold
#12 April 2014


import math
def see_tutor():
    file = input("Enter the marks filename:\n")
    f = open(file , "r")
    mark_list = f.readlines()
    number_list = [] 
    f.close()
    
    for i in range(len(mark_list)):
        mark_list[i] = mark_list[i].strip("\n").split(",")
    
    for j in range(len(mark_list)):
        number_list.append(mark_list[j][1])
    
    for j in range(len(number_list)):
        number_list[j] = eval(number_list[j])
    
    mean = sum(number_list) / float(len(number_list))

    dev = []
    
    for x in number_list:
        dev.append((x-mean)**2)
    
    standard_dev = math.sqrt(sum(dev)/(len(dev)))
    
    checker = mean - standard_dev
    tutor_list = []
    for num in range(len(number_list)):
        if checker > number_list[num]:
            tutor_list.append((mark_list[num][0])) 
        else:
            continue
                     
    print("The average is: " , "%0.2f"%mean, sep="")
    print("The std deviation is: " , "%0.2f"%standard_dev , sep="")
    
    if standard_dev >0:
        print("List of students who need to see an advisor:")
        for name in range(len(tutor_list)):
            print(tutor_list[name], end="\n")
    else:
        pass
see_tutor()