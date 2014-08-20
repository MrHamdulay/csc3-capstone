def ndom_to_decimal(a):
    string_length = str(a)
    string_of_a = str(a)
    result=0
    if len(string_length) == 1:
        result = a
        return result
    if len(string_length) == 2:
        result = (eval(string_of_a[0])*6) + (eval(string_of_a[1]))
        return result
    if len(string_length) == 3:
        result = (eval(string_of_a[0])*36) + (eval(string_of_a[1])*6) + (eval(string_of_a[2]))
        return result

def decimal_to_ndom(a):
    n= a//36
    if (0 <= a <= 5):
        result = a
        return result
    if (6 <= a <= 35):
        result = str(a//6) + str(a%6)
        return eval(result)
    else:
        result = str(a//36) + str((a-(n*36))//6) + str(a%6)
        return eval(result)

def ndom_add(a,b):
    result=0
    adec=ndom_to_decimal(a)
    bdec=ndom_to_decimal(b)
    answer_decimal= adec + bdec
    result = decimal_to_ndom(answer_decimal)
    return result

def ndom_multiply(a,b):
    result=0
    adec=ndom_to_decimal(a)
    bdec=ndom_to_decimal(b)
    answer_decimal= adec * bdec
    result = decimal_to_ndom(answer_decimal)
    return result    