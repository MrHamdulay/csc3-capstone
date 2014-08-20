"""Assignment 6 Question 4
Outputs a histogram represntation of a list of marks
Shaheen Karodia
KRDSHA003
2014-04-20"""


dict={"1":0, "2+":0 , "2-":0 , "3":0 , "F":0} #intiliase dicitonary with different grade levels and setting th value of all keys to zero
x=(input("Enter a space-separated list of marks:\n")).split() #Make input a list of strings

for i in x: #interate through list of strings
    j=eval(i) #convert string into a number
    
#Check actual mark against possible grade, then increment the value of the corresponding key
    if j < 50:
        dict["F"]+=1
    elif j < 60:
        dict["3"]+=1
    elif j < 70:
        dict["2-"]+=1
    elif j <75:
        dict["2+"]+=1
    else:
        dict["1"]+=1
 
 
#print output       
print("1 |", dict["1"]*"X",sep="")
print("2+|", dict["2+"]*"X",sep="") 
print("2-|", dict["2-"]*"X",sep="") 
print("3 |", dict["3"]*"X",sep="")
print("F |", dict["F"]*"X",sep="")
    
 
