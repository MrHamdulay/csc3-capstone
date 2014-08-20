#Khyati Jinerdeb
#Assignment 8
#Date Submitted:09/05/2014
#program to count the number of pairs of repeated characters in a string

def countpairs(string,x):
    if len(string)==0 or len(string)==1:# to check if string has one letter or none
        return print("Number of pairs:",x)

    elif string[0]==string[1]:
        x+=1
        return countpairs(string[2:],x)# checks for pairs in every two charaters
    else:
        return countpairs(string[2:],x)#moves to the next two charaters
string=input("Enter a message:\n")
countpairs(string,0)




