#Recursion
#MTHKHI001
#Assignment 8
#question 4

import sys
sys.setrecursionlimit(20100)
""" program uses recursion to find all the palindromic primes between two integers supplied as inputs"""

def prime_tester(number,position,counter):
    if counter == 3:
        #print("false" + str(number))
        return False
    
    if position == number + 1:
        #print(("true" + str(number)))
        return True
    
    else:
        
        #print(str(number%position))
        if number%position != 0:
            return prime_tester(number,(position+1),counter)
        
        
        if number%position == 0:
            return prime_tester(number,(position+1),(counter+1))


def palindromic_checker(number,length,position):
    #print(number,str(length),str(position))
    if position == length:
        return True
    
    else:
        if number[position] == number[-(position+1)]:
            return palindromic_checker(number,length,(position+1))
        
        else:
            return False



def test_numbers(start,end,position1):
    if position1 == end:
        flag = True
        return flag # end the repitition of outer loop
    
    else:
        indiv_pos = 1
        counter1 = 0
        check = prime_tester(position1, indiv_pos, counter1)
        #print(check)
        
        if check == False:
            return test_numbers(start,end,position1 + 1)
        
        if check == True:
            number = str(position1)
            length = len(number)
            position = 0
            
            palindromic_check = palindromic_checker(number,length,position)
            
            if palindromic_check == True:
                if position1 != 1:
                    print (position1)
            
            return test_numbers(start,end,position1 + 1)




start = eval(input("Enter the starting point N:\n"))
        
end = eval(input("Enter the ending point M:\n"))#Start and endpoints are included so will need to increase end point by 1

end = end + 1
position = start

print("The palindromic primes are:")
flag = test_numbers(start,end,position)


