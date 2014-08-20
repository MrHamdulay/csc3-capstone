# Assignment 7
# Question 1: Program to print input without duplicates
# Frans van Hoek
# 30 April 2014

def main():
    alist = []
    print ("Enter strings (end with DONE):")
    
    while True:
        ans = input('')
        
        if ans in alist:
            continue
        
        elif ans == 'DONE':
            break
        
        else:
            alist.append(ans)
            
    print("\nUnique list:")    
    for i in alist:
        print(i)
            
if __name__ == '__main__': main()