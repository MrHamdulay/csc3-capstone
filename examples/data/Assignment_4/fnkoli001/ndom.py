#Converting ndom (base 6) numbers to decimals and muliplying and adding ndom numbers
#Written by: Oliver Funk
#Completed on: 31/03/14

def ndom_to_decimal(a):
    no_str = str(a)
    cnt = 0
    dec = 0
    for i in no_str:
        dec += eval(i) * 6 ** (len(no_str) - 1 - cnt)
        cnt += 1
    return dec


def decimal_to_ndom(a):
    quotient = a
    rem = ""
    while quotient != 0:
        rem += str(quotient % 6)
        quotient //= 6
    ndom = eval(rem[::-1])
    return ndom


def ndom_add(a, b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    added = dec_a + dec_b
    return decimal_to_ndom(added)


def ndom_multiply(a, b):
    dec_a = ndom_to_decimal(a)
    dec_b = ndom_to_decimal(b)
    multi = dec_a * dec_b
    return decimal_to_ndom(multi)