def ndom_to_decimal(a):
    y = str(a)
    answer = int(y[0]) * 6
    for i in range(len(y) - 2):
        answer += eval(y[i + 1])
        answer = 6 * answer
    answer += eval(y[len(y) - 1])
    return answer    
    
def decimal_to_ndom(a):
    answer_string = "" 
    while a / 6 > 0.15:
        if a > 1:
            answer_string += str(a % 6) 
        elif a == 1:
            answer_string += "1"
        a = a//6
    answer_string = answer_string[::-1]
    answer = eval(answer_string)
    return answer
    
def ndom_add(a, b):
    prelim_answer = ndom_to_decimal(a + b)
    answer = decimal_to_ndom(prelim_answer)
    return answer

def ndom_multiply(a, b):
    prelim_answer = ndom_to_decimal(a) * ndom_to_decimal(b)
    answer = decimal_to_ndom(prelim_answer)
    return answer