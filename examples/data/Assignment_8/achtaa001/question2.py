#Taahirah Achmat
count=0

def pair(p):
    global count
    if len(p)<=1:
        print(count)
    elif p[0]==p[1]:
        count = count+1
        return pair(p[2:])
    else:
        return pair(p[2:])

p = input("Enter a message:\n") #Users input
print("Number of pairs: ",end ="")
pair(p)