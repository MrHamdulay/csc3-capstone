def ndom_to_decimal(a):
    a = str(a)
    result = 0
    for i in range(len(a)):
        value = 6**i * int(a[-i-1])
        result += value
    return result
    
def decimal_to_ndom(a):
    if a == 0:
        return "0"
    result = ""
    while(a != 0):
        digit = a % 6
        result = str(digit) + result
        a = a // 6
    return result
    
def ndom_add(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    added = a + b
    added = decimal_to_ndom(added)
    return added

def ndom_multiply(a, b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    added = a * b
    added = decimal_to_ndom(added)
    return added

if __name__ == "__main__":
    assert ndom_to_decimal("0") == 0
    assert ndom_to_decimal("1") == 1
    assert ndom_to_decimal("2212") == 512
    assert decimal_to_ndom(0) == "0", decimal_to_ndom(0)
    assert decimal_to_ndom(1) == "1", decimal_to_ndom(1)
    assert decimal_to_ndom(6) == "10", decimal_to_ndom(6)
    assert decimal_to_ndom(512) == "2212", decimal_to_ndom(512)
    assert ndom_add(10, 14) == "24", ndom_add(10, 14)
    assert ndom_multiply(10, 14) == "140", ndom_multiply(10, 14)
