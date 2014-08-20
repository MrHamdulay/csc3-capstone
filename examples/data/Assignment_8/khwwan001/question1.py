def recursive(a, x, b):
    if x >= round(x/2):
        if len(a[b]) == len(a[x]):
            if a[b][0] == a[x][(len(a[x])-1)]:
                new_list.append(1)
                recursive(a, x-1, b+1)
            else:
                new_list.append(-1)
                recursive(a, x-1, b+1)
        else:
            new_list.append(-1)
            recursive(a, x-1, b+1)
       
    if -1 not in new_list:
        return True
    else:
        return False


def main():
    s = input("Enter a string: \n")
    s_new = s.split()
    x = len(s_new)-1
    global new_list
    new_list = []
    if recursive(s_new, x, 0) == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
    
if __name__=='__main__':
    main()

    
    
        
    
    
    
    
    
