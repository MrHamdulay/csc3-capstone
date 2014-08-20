"""Program to print out a histogram of a list of marks
John Odetokun ODTJOH001
20 April 2014"""
#recieving marks into variable
marks = input("Enter a space-separated list of marks:\n").split(" ")
#creating dictionary
markDict = {'1 |': '','2+|':'', '2-|':'', '3 |':'', 'F |':''}
#adding 'X's to dictionary for marks in certain categories
for i in range(len(marks)):
    if eval(marks[i]) < 50:
        markDict['F |'] += 'X'
    elif eval(marks[i]) >= 50 and eval(marks[i]) <60:
        markDict['3 |'] += 'X'
    elif eval(marks[i]) >= 60 and eval(marks[i]) <70:
        markDict['2-|'] += 'X'
    elif eval(marks[i]) >= 70 and eval(marks[i]) <75:
        markDict['2+|'] += 'X'
    elif eval(marks[i]) >= 75:
        markDict['1 |'] += 'X'
#print histogram
for i in sorted(markDict):
    print(i , markDict[i], sep ="")
        
        