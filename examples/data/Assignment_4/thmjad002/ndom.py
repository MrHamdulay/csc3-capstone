"""2 April 2014
Jadon Thomson
Assignment 4, Question 2"""

def ndom_to_decimal(num):
    num2 = str(num)
    num2 = num2[::-1]
    answer = 0
    for i in range(1,len(num2)+1):
        a = num2[(i-1)]
        a = eval(a)
        answer += a*(6**(i-1))
    return answer
        
def decimal_to_ndom(num):
    answer = ''
    variable = num
    while variable > 0:
        remainder = variable % 6
        variable = variable//6
        answer += str(remainder)
    answer = answer[::-1]
    return answer
    
def ndom_add(a,b):
    new_a = ndom_to_decimal(a)
    new_b = ndom_to_decimal(b)
    dec_ans = new_a + new_b
    answer = decimal_to_ndom(dec_ans)
    return answer

def ndom_multiply(a,b):
    new_a = ndom_to_decimal(a)
    new_b = ndom_to_decimal(b)
    dec_ans = new_a * new_b
    answer = decimal_to_ndom(dec_ans)
    return answer    
    
        
    
    
    
