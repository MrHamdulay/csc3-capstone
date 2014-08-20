'''program to print out histogram after taking in marks as input
Thabiso Beau
24 April 2014
Assignment 6: #question4.py'''

def main():
     #bevele vir die variables wat die punte gaan tel
    first = 0
    second_upper = 0
    second_lower = 0
    third = 0
    fail = 0
    
    #ass. statement vir die mens wat die program gaan gebruik
    mark = input('Enter a space-separated list of marks: \n')
    mark = mark.split()
    
    #maak 'n for loop wat deur die punte gaan sif __ onthou vir Michelle se program oor Boolean-goeters om die DP te tel
    for i in mark:
        if eval(i) >=75: #as dit nou 'n First Class is
            first +=1
        elif 70<= eval(i): #as dit nou 'n Tweede Hoer
            second_upper +=1
        elif 60<= eval(i): #as dit nou 'n 2- is
            second_lower +=1
        elif 50<= eval(i): #as dit nou 'n 3 is
            third +=1
        else: #as die mens nou gedruip het
            fail +=1
    #gaan nou alles print        
    print('1 |', 'X'*first, sep='')
    print('2+|', 'X'*second_upper, sep='')
    print('2-|', 'X'*second_lower, sep='')
    print('3 |', 'X'*third, sep='')
    print('F |', 'X'*fail, sep='')
main()