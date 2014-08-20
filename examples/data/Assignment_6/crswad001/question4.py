'''Wade Cresswell Question 4'''
listm  = input("Enter a space-separated list of marks:\n")
l = listm.split(' ') # creating a list of all the marks
oness=''
twos=''
twom=''
threem=''
f=''

for i in l:
    if eval(i) >=75: #classifying each by mark, and adding an x onto the accumulator variable for that mark if it is in the range
        oness+='X'
    elif eval(i) >= 70:
        twos+='X'
    elif eval(i) >= 60:
        twom+='X'
    elif eval(i) >=50:        
        threem+='X'
    else: 
        f+='X'

print('1 |',oness,sep='')
print('2+|',twos,sep='')
print('2-|',twom,sep='')
print('3 |',threem,sep='')
print('F |',f,sep='') # printing the results

    
