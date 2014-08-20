#Asil Motala
#MTLASI002
#Assignment 6
#Question 4

marks=input("Enter a space-separated list of marks:\n")     #get input from user

marks_list=marks.split(" ")                                 #separate input into list

first=""                                                    #initialize variables
second_plus=""                                              #initialize variables
second_minus=""                                             #initialize variables
third=""                                                    #initialize variables
fail=""                                                     #initialize variables

for i in marks_list:                                        #loop through marks
    m=eval(i)
    if m>=75:
        first+="X"                                          #create bar 1
    elif m>=70:
        second_plus+="X"                                    #create bar 2+
    elif m>=60:
        second_minus+="X"                                   #create bar 2-
    elif m>=50:
        third+="X"                                          #create bar 3
    else:
        fail+="X"                                           #create bar F

print("1 |"+first)                                          #print histogram
print("2+|"+second_plus)                                    #print histogram
print("2-|"+second_minus)                                   #print histogram
print("3 |"+third)                                          #print histogram
print("F |"+fail)                                           #print histogram