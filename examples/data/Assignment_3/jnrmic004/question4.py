def main():
    start = int(input("Enter the starting point N:\n"))
    end = int(input("Enter the ending point M:\n"))
    num = start
    lst = []
    while (num+1)!=end:
        if start==end:break
        num +=1
        snum = str(num)
        
        pal  = ""
        for i in range(len(snum)-1,-1,-1):
            pal += snum[i]
        
        
        x = num - 1   
        if snum == pal:
            a = True
            
            while True:
                if x==1: break
                elif x == 0:
                    a=False
                    break
                elif num%x==0: 
                    a = False
                    break
                
                else: 
                    x -= 1
                    continue
                
            if a==True: lst.append(num)
            else: continue
            
        else: continue
    
    print("The palindromic primes are:")
    for i in lst:
        print(i)
        
main()        