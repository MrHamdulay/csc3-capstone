def encrypter(ip,op,n):
    if n<len(ip):
        sw=ord(ip[n])
        a=sw+1
        if sw==122:
            a=97
        elif sw<96:
            a=sw
        pop=chr(a)
        return encrypter(ip,op+pop,n+1)
    else:
        return op
def main():
    ip=input("Enter a message:\n")
    op=''
    n=0
    print("Encrypted message:\n",encrypter(ip,op,n),sep='')
    
main()