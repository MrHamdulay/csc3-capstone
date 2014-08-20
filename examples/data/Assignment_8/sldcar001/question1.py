def strpal(ip,pal,n):
    if ip==pal:
        return ip
    elif len(ip)==1:
        return ip
    elif n>=0:
        return strpal(ip,pal+ip[n],n-1)
    else:
        return ''
def main():
    ip=input("Enter a string:\n")
    n=len(ip)-1
    pal=''
    a=strpal(ip,pal,n)
    if a==ip:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
main()