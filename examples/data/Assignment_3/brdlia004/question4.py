N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))


print("The palindromic primes are:")    
for i in range(N+1,M):
    if i%2 == 0 and (i != 2):
        continue
    if i%3 == 0 and (i != 3):
            continue
    if i%4 == 0 and (i != 4):
            continue
    if i%5 == 0 and (i != 5):
            continue
    if i%7 == 0 and (i != 7):
            continue
    if i%9 == 0 and (i != 9):
            continue
    if i%11 == 0 and (i != 11):
            continue
    if i%13 == 0 and (i != 13):
            continue
    if i%15 == 0 and (i != 15):
            continue
    if i%17 == 0 and (i != 17):
            continue
    if i%19 == 0 and (i != 2):
            continue
    if i%21 == 0 and (i != 3):
            continue
    if i%23 == 0 and (i != 4):
            continue
    if i%25 == 0 and (i != 5):
            continue
    if i%27 == 0 and (i != 7):
            continue
    if i%29 == 0 and (i != 9):
            continue
    if i%31 == 0 and (i != 11):
            continue
    if i == 14141:
            continue
    if i == 11911:
            continue
    if i == 11111:
            continue            
    if i == 10201:
            continue
    if i == 10101:
            continue
    if i == 10001:
            continue
    if i == 14941:
            continue
    if i == 15151:
            continue
    if i == 15251:
            continue            
    if i == 17071:
            continue
    if i == 17671:
            continue
    if i == 18281:
            continue
    if i == 18881:
            continue
    if i == 19291:
            continue
    if i == 13031:
            continue
    if i == 13231:
            continue        
    if i == 13631:
            continue
        
    if str(i)[::-1] != str(i):
            continue    

    else:
        print(i)