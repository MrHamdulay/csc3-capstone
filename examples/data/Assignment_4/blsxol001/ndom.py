def ndom_to_decimal(num):
    num = str(num)
    value = 0
    for i in range (len(num)):
        value += int(num[-(i+1)])*6**i
        return value
def decimal_to_ndom(n):
    """Convert a positive number 10 to its digit representation in base 6."""
    digits = [] 
    while n>0:
        digits.insert(0, n % 6)
        n  = n // 6
        n -=1 
    return digits  
decimal_to_ndom(2)