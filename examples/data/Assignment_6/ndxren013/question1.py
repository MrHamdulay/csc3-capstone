#Reneshan Naidoo
#Right Justified

def main ():
    
    x = []
    count = 0
    x.append(input("Enter strings (end with DONE):\n"))
    #reads input
    while x[count] != "DONE":
        count += 1
        x.append(input())

    long = len(x[0])
    for i in range (1,count,1):
        temp = len(x[i])
        if (temp > long):
            long = temp
    #finds longest string
    print()
    print('Right-aligned list:')
    for i in range (count):
        print(" " * (long - len(x[i])) +  x[i])
    #outputs according to longest length
    
main()
