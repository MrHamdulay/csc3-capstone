'''program to determine the students who need to see student adivisor
Wandile Khowa
11-05-2014
'''
def manipulation(a):
    file = open(a, "r") #opens the file for reading
    whole_file = file.readlines()   #creates a variable containing the contents of file as list of strings   
    new_list_marks = [] #creates an empty list to hold the marks of students
    new_list_names = [] #creates an empty list to hold the names of students
    for h in whole_file:
        u = h.split(",")
        new_list_names.append(u[0]) #adds the names of students to the list as in the order they appear in the file
    for i in whole_file:
        x = i.split(",")
        new_list_marks.append(eval(x[1]))   #adds the marks of students as in the order they appear in the file
    file.close()
    c = len(new_list_marks)
    sum_a = 0
    for j in new_list_marks:
        sum_a+=j    #works out the sum of the marks
    average = sum_a/c   #computes the mean of the marks
    sum_s = 0
    for k in new_list_marks:
        sum_s += (k-average)**2
    standard_dev = (sum_s/c)**(0.5) #works out the standard deviation of the marks
    print("The average is:", "%.2f" % average)
    print("The std deviation is:", "%.2f" % standard_dev)
    count = 0
    statement = False
    for l in new_list_marks:
        if l < average-standard_dev and statement == False :    #makes sure that the line that reads 'List of students...' is printed only once
            print("List of students who need to see an advisor:")
            print(new_list_names[count])
            count+=1
            statement = True
        elif l < average-standard_dev:
            print(new_list_names[count])
            count+=1
        else:
            count+=1
        
def main():
    ques = input("Enter the marks filename: \n")
    manipulation(ques)
    
if __name__=='__main__':
    main()