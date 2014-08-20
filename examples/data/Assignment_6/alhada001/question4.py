marksEntered = input("Enter a space-separated list of marks:\n") #User enters list of marks
indmark = marksEntered.split(" ") #List is split on spaces into individual marks
NumberofMarks = [] #Array declared
for i in range(len(indmark)):#For loop that goes as many times as there are  individual marks
        
        #If the marks falls under tha catecogry it is written to the array
        if int(indmark[i]) < 50:
            NumberofMarks.append(50)
        elif int(indmark[i]) < 60:
            NumberofMarks.append(60)    
        elif int(indmark[i]) < 70:
            NumberofMarks.append(70)    
        elif int(indmark[i]) < 75:
            NumberofMarks.append(75)
        elif int(indmark[i]) <= 100:
            NumberofMarks.append(100)
#Classifications are mad with regard to the marks
Fail = NumberofMarks.count(50)
First = NumberofMarks.count(100)
Second1 = NumberofMarks.count(75)
Second2 = NumberofMarks.count(70)
Third = NumberofMarks.count(60)

#The outcome is printed in terms of the marks

print("1 |"+"X"*First)
print("2+|"+"X"*Second1)
print("2-|"+"X"*Second2)
print("3 |"+"X"*Third)
print("F |"+"X"*Fail)



