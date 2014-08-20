# a program to count the number of pairs
# xola Bilose
# 09/05/2014
global count
count = 0   
def count_pairs(s):
    global count
    
    if len(s)<=1:
        return count
    else:
        if s[0] == s[1]:
            count += 1
            return count_pairs(s[2::])
        else:
            return count_pairs(s[1::])
count = 0
message = input("Enter a message:\n")
print("Number of pairs:",count_pairs(message))

        