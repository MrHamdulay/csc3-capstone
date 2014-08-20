#Assignment 8,Question 2
#Avreyna Kistensamy
#3 May 2014

def pairs(check):
    num_of_p = 0
    if len(check) < 2:
        return 0
    elif check[0] == check[1]:
            return 1 + pairs(check[2:])
    else:
        return pairs(check[1:])
    
x = input("Enter a message:\n")
check = x
print("Number of pairs:",pairs(check))    