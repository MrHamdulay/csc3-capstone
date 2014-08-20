"""using a file to get marks and make a list of students who need to see an advisor
Roger Cox 
14 May 2014 """


import math # so i can use sqrt
def ave_stdev (count,sum_marks): # veriables that i will change and starts at zero
    marks=[] 
    filename=input("Enter the marks filename:\n")
    f=open(filename,"r")
    for line in f :
        name_word=line.split(",") #splits the name from the mark
        marks.append(eval(name_word[1]))
        #add the mark to marks
        count+=1   # the number of people in the test
        sum_marks +=eval(name_word[1]) # total marks
        
    f.close()    
    # works out the average and prints it
    average=sum_marks/count 
    av_format="The average is: {average:0.2f}"
    print(av_format.format(average=average))
    
    
    sd_sum_mrks=0   
    for mark in marks : # goes through the marks array and gives me the total marks to culculate standard deviation
        sd_sum_mrks+=((mark-average)**2)
    # culculates and prints standard deviation    
    sd=math.sqrt(sd_sum_mrks/count)
    sd_format="The std deviation is: {sd:0.2f}" 
    print(sd_format.format(sd=sd))
    # checks if student needs to see advisor
    allowed_deviation= sd+1
    f=open(filename,"r")
    num_of_students=0
    for line in f :
        line_array=line.split(",")
        deviation=(eval(line_array[1])-average)
        
        if(deviation<-allowed_deviation):
            if num_of_students ==0 :
                print("List of students who need to see an advisor:")
                print(line_array[0])
                num_of_students+=1
            else :
                print(line_array[0])
                
                
    f.close()
ave_stdev (0,0)     
