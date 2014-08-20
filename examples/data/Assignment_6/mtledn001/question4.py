'''The marks shown in a histogram
Ednecia Matlapeng 
20 April 2014'''
#Get the marks
marks = input('Enter a space-separated list of marks:\n')
#Put the into a list
markList = marks.split(' ')
#Convert them into numbers
for i in range(len(markList)):
    markList[i]= eval(markList[i])
#print(markList) Ok it works
#
#Categorising the marks
fail,passed, lower, upper, a,=0,0,0,0,0
for mark in markList:
    if mark<50:
        fail+=1
    elif mark<60:
        passed+=1
    elif mark <70:
        lower+=1
    elif mark<75:
        upper+=1
    else:
        a+=1
#Ok well that was that
#Now we face the display
print('1 |','X'*a,'\n2+|','X'*upper,'\n2-|','X'*lower,'\n3 |','X'*passed,'\nF |','X'*fail,sep='')
            
    
        

