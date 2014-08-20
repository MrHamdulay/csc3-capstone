'''a program to output a histogram from a given list of marks.
Sfiso Mthembu
23/04/2014'''

#initially assign all categories to zero

fail= 0
third = 0
lower_second = 0
upper_second = 0
first = 0

#ask for the marks
x=input('Enter a space-separated list of marks:\n')

#convert thex input to a list
x=x.split(' ')

#create a new list where th input will be stored as integers
marks=[]

for i in x:
    #add the input to new list , now as integers
    marks.append(eval(i))
    
    #categorize
    if eval(i) < 50:
        fail+=1
    elif 50 <= eval(i) <60:
        third +=1
    elif 60 <= eval(i) < 70:
        lower_second+=1
    elif 70 <= eval(i) < 75:
        upper_second+=1
    elif eval(i) >= 75:
        first +=1
            
#Now print desired output
print("1 |" ,first*"X",sep='')
print("2+|" ,upper_second*"X",sep='')
print("2-|" ,lower_second*"X",sep='')
print("3 |" ,third*"X",sep='')
print("F |" ,fail*"X",sep='')