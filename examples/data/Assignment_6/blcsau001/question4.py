#Code to take a list and display histogram representing marks
#Saul Bloch
#22 April 2014

marks = input("Enter a space-separated list of marks:\n")

indiMark = marks.split(" ") #create array of marks

numMarks = []

#loop for every array 'block'
for i in range(len(indiMark)):
    #add different value for different mark range    
    if int(indiMark[i]) < 50:
        numMarks.append(5)
    elif int(indiMark[i]) < 60:
        numMarks.append(4)    
    elif int(indiMark[i]) < 70:
        numMarks.append(3)    
    elif int(indiMark[i]) < 75:
            numMarks.append(2)
    elif int(indiMark[i]) <= 100:
            numMarks.append(1)
#assigning number of votes to different variables
fir = numMarks.count(1)
sec1 = numMarks.count(2)
sec2 = numMarks.count(3)
third = numMarks.count(4)
fail = numMarks.count(5)
#printing histogram
print("1 |"+"X"*fir)
print("2+|"+"X"*sec1)
print("2-|"+"X"*sec2)
print("3 |"+"X"*third)
print("F |"+"X"*fail)