def pair(ip,a,n):
    if n>=0:
        if a+1<len(ip):
            if ip[a]==ip[a+1]:
                if a+2!=len(ip):
                    return 1 + pair(ip,a+2,n-1)
                else:
                    return 1+pair(ip,a+1,n-1)
            else:
                return 0+pair(ip,a+1,n-1)
            
        else:
            return 0
    else:
        return 0
    
        
def main():
    ip=input("Enter a message:\n")
    n=len(ip)-2
    a=0
    print("Number of pairs:",pair(ip,a,n))
    
main()