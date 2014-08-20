"""histogram of representation of the marks according to the mark categories at UCT
Yamkela Venfolo
24 April 2012 """

xString=input("Enter a space-separated list of marks:\n")
#Split the string by spaces to obtain data
ArraysMarks=xString.split(" ")
#Define our dictionary according to the categories
dictionary={'F':0,'3':0,'2-':0,'2+':0,'1':0}
#Populate our dictionary using the diffent categories using for loop

for i in range(len(ArraysMarks)):
    integer=eval(ArraysMarks[i])  
    if(integer < 50 ):
        dictionary['F']=dictionary['F']+1
    elif 50 <= integer < 60:
        dictionary['3']=dictionary['3']+1
    elif 60 <= integer < 70:
        dictionary['2-']=dictionary['2-']+1
    elif 70<= integer < 75:
        dictionary['2+']=dictionary['2+']+1
    elif integer >= 75:
        dictionary['1']=dictionary['1']+1

print("1 |",dictionary['1']*"X",sep="")
print("2+|",dictionary['2+']*"X",sep="")
print("2-|",dictionary["2-"]*"X",sep="")
print("3 |",dictionary["3"]*"X",sep="")
print("F |",dictionary['F']*"X",sep="")
