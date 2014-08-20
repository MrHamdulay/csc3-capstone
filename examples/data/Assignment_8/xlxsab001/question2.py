

def counting(text, c, n):
    if len(text) <= c:        
        return n
    if text[c-1] == text[c]: 
        n += 1                 
        c += 2
    else:
        c += 1                      
    return counting(text, c, n)

x = input("Enter a message:\n")
y = counting(x, 1, 0)
print("Number of pairs:", y)