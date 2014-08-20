"""emile mclennan
6/5/14
A8 Q2"""



def count_pairs(w,count):
    n=0
    if n >= len(w)-1:
        return count
    elif w[n] == w[n+1]:
        return count_pairs(w[n+2:],count+1)
    else:
        return count_pairs(w[(n+1):],count)
    
word= input("Enter a message:\n")
count=0
print("Number of pairs:",count_pairs(word,count))
