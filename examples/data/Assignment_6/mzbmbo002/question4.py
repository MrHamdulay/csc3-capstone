#Mbongeni Mazibuko
#MZBMBO002
#Assignment 6

def histogram():
    '''function takes in a list of marks and outputs a histogram representation of the marks according to the mark categories at UCT'''
    marks= input('Enter a space-separated list of marks:\n')
    marks= marks.split(' ')
    x=['','','','','']
    for i in range(len(marks)):
        if eval(marks[i])>=75:
            x[0]+='X'
        elif 70<=eval(marks[i])<75:
            x[1]+='X'
        elif 60<=eval(marks[i])<70:
            x[2]+='X'
        elif 50<=eval(marks[i])<60:
            x[3]+='X'
        elif eval(marks[i])<50:
            x[4]+='X'
    print('''1 |'''+x[0]+'''
2+|'''+x[1]+'''
2-|'''+x[2]+'''
3 |'''+x[3]+'''
F |'''+x[4])
    
if __name__=='__main__':
    histogram()