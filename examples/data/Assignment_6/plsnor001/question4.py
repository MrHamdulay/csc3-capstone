'''program to plot histogram of marks
Norman Pilusa 
April 2014'''

def histogram():
    marks=input('Enter a space-separated list of marks:\n')
    marks=marks.split(' ')
    first=0
    upper=0
    lower=0
    third=0
    fail=0
    for mark in marks:
        if eval(mark)<50:
            fail+=1
        elif 50<=eval(mark)<60:
            third+=1
        elif 60<=eval(mark)<70:
            lower+=1
        elif 70<=eval(mark)<75:
            upper+=1
        elif 75<=eval(mark):
            first+=1
            
    print('1 |'+'X'*first
          ,'\n2+|'+'X'*upper
          ,'\n2-|'+'X'*lower
          ,'\n3 |'+'X'*third
          ,'\nF |'+'X'*fail)
    
    
    
    
    
histogram()