"""recursive program to find the number of repeated characters in a string
Rofhiwa Liphauphau
5 May 2014"""

message=input("Enter a message:\n")
def pairs(m):
    count=0
    if len(m)==1:
        return count
    else:
        if m[0]==m[1] :
            count=1
            if len(m)>2:
                return count + pairs(m[2:])
            else:
                return count
        else:
            return pairs(m[1:])

print("Number of pairs:",pairs(message))
    


