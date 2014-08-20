def decimal_to_ndom(num):
    if num == 0:
        return 0
    ans = ""
    while num > 0:
        ans = str(num%6) + ans
        num /= 6
    return ans

def ndom_to_decimal(num):
    if num == 0:
        return 0
    num = str(num)
    ans = int(num[0])
    for i in num[1:]:
        ans *= 6
        ans += int(i)
    return ans

if __name__ == '__main__':
    a = decimal_to_ndom(78)
    b = ndom_to_decimal(a)
    

    
    
    